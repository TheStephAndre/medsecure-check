import uuid
from typing import Dict

import stripe
from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

import core.wording as wording

# Professional Import Path from our new /core folder
from core.scoring import QUESTIONS, AuditEngine
from core.ui import templates

router = APIRouter()


# --- RaaS SCHEMA ---
class AuditSubmission(BaseModel):
    business_name: str
    email: EmailStr
    answers: Dict[str, str]


# --- API ENDPOINT (The RaaS Product) ---
@router.post("/assess")
async def api_assess(submission: AuditSubmission):
    """The core engine accessible via JSON for third-party integration."""
    engine = AuditEngine(submission.answers)
    results = engine.compute()
    return {
        "status": "success",
        "submission_id": str(uuid.uuid4())[:8],
        "results": results,
    }


# --- REPORT / PDF ENDPOINT ---
@router.get("/report/{submission_id}", name="report")
async def view_report(request: Request, submission_id: str):
    """
    Placeholder for viewing/downloading the PDF report.
    In the future, this will return the actual PDF file.
    """
    return HTMLResponse(
        content=f"<h1>Bericht Vorschau für ID: {submission_id}</h1><p>PDF-Generierung wird hier implementiert.</p>"
    )


# --- PAYMENT PLACEHOLDER ---
@router.get("/pay/{submission_id}", response_class=HTMLResponse, name="pay_page")
async def pay_page(request: Request, submission_id: str):
    """Placeholder for the payment/checkout page."""
    return templates.TemplateResponse(
        "payment.html",
        {
            "request": request,
            "submission_id": submission_id,
            "PAYMENT": wording.PAYMENT,
        },
    )


# --- WEB ENDPOINT (The UI Form) ---
@router.post("/submit", response_class=HTMLResponse, name="submit")
async def web_submit(
    request: Request, business_name: str = Form(...), email: str = Form(...)
):
    form_data = await request.form()
    answers = {k: v for k, v in form_data.items() if k.startswith("q")}

    engine = AuditEngine(answers)
    results = engine.compute()

    # Create a unique ID (Replacing your hashlib logic for simplicity)
    submission_id = str(uuid.uuid4())[:16]

    # TODO: Save to PostgreSQL here (instead of json.dump)
    # For now, we pass it to the result page
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
            "DISCLAIMERS": wording.DISCLAIMERS,
        },
    )


@router.get("/pay/{submission_id}", name="pay")
async def pay(request: Request, submission_id: str):
    """Refactored Stripe Checkout from your Flask app."""
    try:
        # Note: In production, fetch the business_name/email from DB using submission_id
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "chf",
                        "unit_amount": 4900,  # 49.00 CHF
                        "product_data": {
                            "name": "MedSecure-Check IT-Sicherheitsbericht"
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            metadata={"submission_id": submission_id},
            # url_for in FastAPI requires the Request object
            success_url=str(
                request.url_for("payment_success", submission_id=submission_id)
            ),
            cancel_url=str(request.url_for("submit")),
        )
        return RedirectResponse(url=checkout_session.url, status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/payment/success/{submission_id}", name="payment_success")
async def payment_success(request: Request, submission_id: str):
    return templates.TemplateResponse(
        "payment_success.html", {"request": request, "submission_id": submission_id}
    )


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
