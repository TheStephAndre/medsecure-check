import os
import smtplib
from email.message import EmailMessage

from sqlalchemy.orm import Session

from core.models import AuditSubmission
from core.pdf import generate_pdf
from core.wording import get_lexicon


def send_audit_results_email(submission_id: str, db: Session):
    # Fetch data safely
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )
    if not audit:
        print(f"Email error: Submission {submission_id} not found.")
        return

    # Extract and strictly type-cast variables to satisfy Pylance
    lang = str(audit.lang) if audit.lang is not None else "fr-CH"
    business_name = (
        str(audit.business_name) if audit.business_name is not None else "Cabinet"
    )
    recipient_email = str(audit.email) if audit.email is not None else ""

    if not recipient_email:
        print(f"Email error: No email address bound to submission {submission_id}.")
        return

    lex = get_lexicon(lang)
    company_name = os.getenv("COMPANY_NAME", "MedSecure")

    # Generate PDF Attachments in memory (with safe string passing)
    report_pdf = generate_pdf("report_pdf.html", audit, lex, lang, company_name)
    invoice_pdf = generate_pdf("invoice_pdf.html", audit, lex, lang, company_name)

    # Build Email using the newly isolated EMAIL mapping dictionary
    msg = EmailMessage()
    msg["Subject"] = lex["EMAIL"]["subject"]
    msg["From"] = os.getenv("EMAIL_FROM", "info@medsecure-check.ch")
    msg["To"] = recipient_email
    msg.set_content(lex["EMAIL"]["body"])

    # Clean the business name for a professional attachment filename
    biz_name_clean = business_name.replace(".", "").replace(" ", "_")
    safe_business_name = "".join(x for x in biz_name_clean if x.isalnum() or x == "_")

    #  Attach Files
    msg.add_attachment(
        report_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=f"Rapport_MedSecure_{safe_business_name}.pdf",
    )
    msg.add_attachment(
        invoice_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=f"Quittance_MedSecure_{safe_business_name}.pdf",
    )

    #  Send via SMTP securely using environment configs
    smtp_host = os.getenv("SMTP_HOST", "localhost")
    try:
        smtp_port = int(os.getenv("SMTP_PORT", "465"))
    except ValueError:
        smtp_port = 465

    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")

    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email via SMTP {smtp_host}: {e}")
