import os
import uuid
from typing import Dict

import stripe
from fastapi import APIRouter, Depends, Form, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

import core.wording as wording
from core.database import get_db
from core.models import AuditSubmission
from core.pdf import generate_pdf
from core.scoring import AuditEngine
from core.ui import templates

router = APIRouter()


# --- RaaS SCHEMA ---
class AuditSubmissionSchema(BaseModel):
    business_name: str
    email: EmailStr
    answers: Dict[str, str]


# --- WEB ENDPOINT (The UI Form) ---
@router.post("/submit", response_class=HTMLResponse, name="submit")
async def web_submit(
    request: Request,
    business_name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    form_data = await request.form()
    answers = {k: v for k, v in form_data.items() if k.startswith("q")}

    # 1. Run the Scoring Engine
    engine = AuditEngine(answers)
    results = engine.compute()

    # 2. Generate persistent ID
    submission_id = str(uuid.uuid4())[:16]

    # 3. Save to PostgreSQL
    db_entry = AuditSubmission(
        id=submission_id,
        business_name=business_name,
        email=email,
        score=results["assessment"],
        risk_level=results["risk_level"],
        failed_items=results["failed"],
        is_paid=False,
    )
    db.add(db_entry)
    db.commit()

    # Pull IBAN from environment(.env)
    iban_value = os.getenv("IBAN", "CHxx xxxx xxxx xxxx xxxx x")

    # 4. Render UI
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "submission_id": submission_id,
            "business_name": business_name,
            "submission": results,
            "level": results.get("risk_level"),
            "RESULT": {**wording.RESULT, "risk_levels": wording.RISK_LEVELS},
            "PRODUCT": wording.PRODUCT,
            "IBAN": iban_value,  # Use the variable from os.getenv
            "DISCLAIMERS": wording.DISCLAIMERS,
        },
    )


# --- REPORT / PDF ENDPOINT ---
@router.get("/report/{submission_id}", name="report")
async def view_report(submission_id: str, db: Session = Depends(get_db)):
    """Fetches the audit from DB to verify it exists before showing preview."""
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    if not audit:
        raise HTTPException(status_code=404, detail="Audit nicht gefunden.")

    # Create a clean slug for the filename
    # Removes spaces and special characters from the business name
    safe_business_name = "".join(x for x in audit.business_name if x.isalnum())
    date_str = audit.created_at.strftime("%Y-%m-%d")

    # Use a simple, professional filename
    filename = f"Bericht_{safe_business_name}_{date_str}.pdf"

    # Generate the PDF in memory
    pdf_buffer = generate_pdf(
        template_name="report_pdf.html",
        audit_record=audit,
        company_name=os.getenv("COMPANY_NAME", "MedSecure Schweiz"),
        iban=os.getenv("IBAN", ""),
    )

    # Return as a PDF response
    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        headers={
            # Using 'inline' allows it to open in the browser,
            # but 'filename' specifies what it will be called when saved.
            "Content-Disposition": f'inline; filename="{filename}"'
        },
    )


# --- INVOICE / PDF ENDPOINT ---
@router.get("/invoice/{submission_id}", name="invoice")
async def view_invoice(submission_id: str, db: Session = Depends(get_db)):
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    if not audit or not audit.is_paid:
        raise HTTPException(
            status_code=403, detail="Rechnung nur nach Zahlung verfügbar."
        )

    pdf_buffer = generate_pdf(
        template_name="invoice_pdf.html",
        audit_record=audit,
        company_name=os.getenv("COMPANY_NAME", "MedSecure Schweiz"),
        iban=os.getenv("IBAN", ""),
    )

    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=Rechnung_{submission_id}.pdf"
        },
    )


# --- PAYMENT ---
@router.get("/pay/{submission_id}", name="pay")
async def pay(request: Request, submission_id: str, db: Session = Depends(get_db)):
    """Fetches real email/data from DB for Stripe Checkout."""
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    if not audit:
        raise HTTPException(status_code=404, detail="Audit nicht gefunden.")

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=audit.email,  # Professional touch: pre-fill email
            line_items=[
                {
                    "price_data": {
                        "currency": "chf",
                        "unit_amount": 4900,
                        "product_data": {
                            "name": f"IT-Sicherheitsbericht: {audit.business_name}"
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            metadata={"submission_id": submission_id},
            success_url=str(
                request.url_for("payment_success", submission_id=submission_id)
            ),
            cancel_url=str(request.url_for("submit")),
        )
        return RedirectResponse(url=checkout_session.url, status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- PAYMENT SUCCESS ---
@router.get("/payment/success/{submission_id}", name="payment_success")
async def payment_success(request: Request, submission_id: str):
    return templates.TemplateResponse(
        "payment_success.html", {"request": request, "submission_id": submission_id}
    )


# --- STRIPE WEBHOOK ---
@router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, "whsec_..."  # Your Webhook Secret
        )
    except Exception:
        return {"status": "invalid payload"}, 400

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        sid = session["metadata"]["submission_id"]

        # TRIGGER BACKGROUND TASK HERE:
        # 1. Update DB to 'paid'
        # 2. Generate PDF with WeasyPrint
        # 3. Send Email
        print(f"Payment confirmed for {sid}")

    return {"status": "success"}
