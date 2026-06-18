import uuid
from typing import Dict

import stripe
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    Form,
    Header,
    HTTPException,
    Query,
    Request,
    Response,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

import core.wording as wording
from core import config
from core.database import SessionLocal, get_db
from core.email import send_audit_results_email
from core.models import AuditSubmission
from core.pdf import generate_pdf
from core.scoring import AuditEngine
from core.ui import templates

router = APIRouter()

# Global context security configuration initialization
stripe.api_key = config.STRIPE_SECRET_KEY


# --- RaaS SCHEMA ---
class AuditSubmissionSchema(BaseModel):
    business_name: str
    email: EmailStr
    answers: Dict[str, str]


# --- Get Lexicon for a specific language ---
def get_localized_lexicon(lang: str = "fr-CH") -> dict:
    """Returns the dictionary for the requested language, fallback to French."""
    return wording.LEXICON.get(lang, wording.LEXICON["fr-CH"])


# --- WEB ENDPOINT (The UI Form) ---
@router.post("/submit", response_class=HTMLResponse, name="submit")
async def web_submit(
    request: Request,
    business_name: str = Form(...),
    email: str = Form(...),
    # Capture language form a hidden form field
    lang: str = Form("fr-CH"),
    db: Session = Depends(get_db),
):
    form_data = await request.form()
    form_dict = dict(form_data)

    # Force build an invariant, comprehensive 10-key answer dictionary,
    # If the browser or network miss a key/value because of a bug,
    # while the audit strictly requires 10 questions from q1 to q10,
    # this loop is going to build that dictionary layout manually,
    # by replacing the value of the key missing by 'na'.
    answers = {}
    for i in range(1, 11):
        q_key = f"q{i}"
        answers[q_key] = form_dict.get(q_key, "na")

    # Run the Scoring Engine
    engine = AuditEngine(answers, lang=lang)
    results = engine.compute()

    # Generate persistent ID
    submission_id = str(uuid.uuid4())[:16]

    # Save to PostgreSQL
    db_entry = AuditSubmission(
        id=submission_id,
        business_name=business_name,
        email=email,
        lang=lang,  # language
        score=results["assessment"],
        risk_level=results["risk_level"],
        failed_items=results["failed"],
        pillar_scores=results["pillar_scores"],
        is_paid=False,
    )
    db.add(db_entry)
    db.commit()

    # Get the specific wording
    lex = get_localized_lexicon(lang)

    # Render UI
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "current_lang": lang,
            "request": request,
            "submission_id": submission_id,
            "business_name": business_name,
            "submission": results,
            "level": results.get("risk_level"),
            # Use the local lexicon instead of wording.RESULT
            "RESULT": {**lex["RESULT"], "risk_levels": lex["RISK_LEVELS"]},
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
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

    # Refresh to get the latest status from the Webhook
    db.refresh(audit)

    # The Gatekeeper Logic if it is not paid
    if audit.is_paid is not True:
        # Redirect to the pay route if they haven't paid yet
        return RedirectResponse(url=f"/api/v1/pay/{submission_id}")

    # Use the language stored in the DB for the PDF
    lang = str(audit.lang) if audit.lang is not None else "fr-CH"
    lex = get_localized_lexicon(lang)  # Returns the full DE/FR/IT dict

    # Create a clean business_name to string for alnum check)
    # Removes spaces and special characters from the business name
    biz_name = str(audit.business_name).replace(".", "").replace(" ", "_")
    safe_business_name = "".join(x for x in biz_name if x.isalnum() or x == "_")

    # Construct the localized filename
    # Result example: Rapport_MedSecure_Clinic_Bern_2026-04-24.pdf
    report_prefix = lex["REPORT_PDF"]["filename_prefix"]
    date_str = audit.created_at.strftime("%Y-%m-%d")

    # Use a simple, professional filename for report
    filename = f"{report_prefix}_MedSecure_{safe_business_name}_{date_str}.pdf"

    # Generate the PDF in memory
    pdf_buffer = generate_pdf(
        template_name="report_pdf.html",
        audit_record=audit,
        # Pass the whole localized lexicon to the PDF generator(core/pdf.py)
        lexicon=lex,
        lang=lang,
        company_name=config.COMPANY_NAME,
        # Passing the filename to the template context
        display_filename=filename,
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


# --- PAYMENT ---
@router.get("/pay/{submission_id}", name="pay")
async def pay(request: Request, submission_id: str, db: Session = Depends(get_db)):
    """Fetches real email/data from DB for Stripe Checkout."""
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    if not audit:
        raise HTTPException(status_code=404, detail="Audit nicht gefunden.")

    # Define 'lex' here so it is not undefined
    lang = str(audit.lang) if audit.lang is not None else "fr-CH"
    lex = get_localized_lexicon(lang)

    try:
        # request.url_for can return NoneType, cast to str()
        success_url = f"{str(request.url_for('payment_success', submission_id=submission_id))}?lang={lang}"
        cancel_url = str(request.url_for("submit"))

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=str(audit.email),  # Professional touch: pre-fill email
            # Add client_reference_id so the Webhook knows which audit to update
            client_reference_id=submission_id,
            line_items=[
                {
                    "price_data": {
                        "currency": "chf",
                        "unit_amount": config.STRIPE_PRICE_CHF,
                        "product_data": {
                            # Localized Stripe product name
                            "name": f"{lex['PRODUCT']['report_name']}: {audit.business_name}"
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return RedirectResponse(
            url=str(checkout_session.url) if checkout_session.url else "/",
            status_code=303,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- PAYMENT SUCCESS ---
@router.get("/payment/success/{submission_id}", name="payment_success")
async def payment_success(
    request: Request, submission_id: str, db: Session = Depends(get_db)
):
    # Fetch the record to get the saved language
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    # Default to fr-CH if not found, but use the record's lang if available
    lang = audit.lang if audit else "fr-CH"
    lex = get_localized_lexicon(str(lang))

    return templates.TemplateResponse(
        request=request,
        name="payment_success.html",
        context={
            "request": request,
            "submission_id": submission_id,
            "current_lang": lang,
            "PRODUCT": lex["PRODUCT"],
            "SUCCESS": lex["SUCCESS"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )


# --- LEGAL COMPLIANCE & PRIVACY ---


@router.get("/privacy", response_class=HTMLResponse, name="privacy")
async def get_privacy_page(
    request: Request, lang: str = Query("fr-CH", regex="^(de-CH|fr-CH|it-CH)$")
):
    """
    Renders the Swiss FADP / revDSG compliant privacy policy page.
    Accepts URL dialect query parameters (?lang=de, ?lang=fr, ?lang=it).
    """
    lex = get_localized_lexicon(lang)
    return templates.TemplateResponse(
        request=request,
        name="privacy.html",
        context={
            "request": request,
            "current_lang": lang,
            "config": wording.LEGAL_CONFIG,
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )


@router.get("/terms", response_class=HTMLResponse, name="terms")
async def get_terms_page(
    request: Request, lang: str = Query("fr-CH", regex="^(de-CH|fr-CH|it-CH)$")
):
    """
    Renders the General Terms and Conditions (AGB / CGV / CGA) page with core disclaimers.
    """
    lex = get_localized_lexicon(lang)
    return templates.TemplateResponse(
        request=request,
        name="terms.html",
        context={
            "request": request,
            "current_lang": lang,  # Unified variable name
            "config": wording.LEGAL_CONFIG,
            "PRODUCT": lex["PRODUCT"],
            "DISCLAIMERS": lex["DISCLAIMERS"],
        },
    )


# --- STRIPE WEBHOOK ---


@router.post("/webhook/stripe")
async def stripe_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    stripe_signature: str = Header(None),
    db: Session = Depends(get_db),
):
    payload = await request.body()

    try:
        # Verify the event integrity
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, config.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.SignatureVerificationError:
        # Invalid signature
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle the specific event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        # This ID must be passed when you create the Checkout Session initially
        audit_id = session.client_reference_id

        if audit_id:
            #  Update the PostgreSQL record
            audit = (
                db.query(AuditSubmission).filter(AuditSubmission.id == audit_id).first()
            )
            if audit:
                setattr(audit, "is_paid", True)
                db.commit()
                print(f"Payment confirmed for Audit: {audit_id}")
                # --- ASYNCHRONOUS BACKGROUND THREAD OFFSITE ---
                # Pushes the processing down to the application's task manager in FastAPI
                # instead of blocking the execution thread while dealing with network connectivity loops(Stripe and SMTP server).
                background_tasks.add_task(
                    send_audit_results_email, audit_id, SessionLocal
                )
            else:
                print(f"Webhook received for unknown Audit ID: {audit_id}")

    # Response to Stripe to confirm payment receipt and close the connection.
    # Fast execution, completely secure against Stripe's 10-second timeout.
    return {"status": "success"}


# --- INVOICE / PDF ENDPOINT ---
@router.get("/invoice/{submission_id}", name="invoice")
async def view_invoice(submission_id: str, db: Session = Depends(get_db)):
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )

    if not audit or audit.is_paid is not True:
        raise HTTPException(
            status_code=403, detail="Invoice available only after payment."
        )

    # Fetch localized wording
    lang = getattr(audit, "lang", "fr-CH")
    lex = get_localized_lexicon(lang)

    # Construct the localized filename
    inv_lex = lex["INVOICE"]
    # Create the dynamic filename here
    # Use only the first 8 chars of ID for a cleaner look
    short_id = str(submission_id)[:8]
    # Use a simple, professional filename for invoice
    filename = f"{inv_lex['filename_prefix']}_MedSecure_{short_id}.pdf"

    pdf_buffer = generate_pdf(
        template_name="invoice_pdf.html",
        audit_record=audit,
        lexicon=lex,
        lang=lang,
        company_name=config.COMPANY_NAME,
        # Passing the filename to the template context
        display_filename=filename,
    )

    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        # Use 'inline' so it opens in browser, but 'filename'
        # tells the browser what to call it when the user clicks 'Save'.
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )
