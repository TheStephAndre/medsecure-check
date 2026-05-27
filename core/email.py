import smtplib
from contextlib import contextmanager
from email.message import EmailMessage

from core import config
from core.models import AuditSubmission
from core.pdf import generate_pdf
from core.wording import get_lexicon


def send_audit_results_email(submission_id: str, db_factory):
    # Fetch data safely
    # Create an independent context-managed session
    # handles open/close routines safely off the main request thread
    with contextmanager(db_factory)() as db:
        audit = (
            db.query(AuditSubmission)
            .filter(AuditSubmission.id == submission_id)
            .first()
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

    # Clean the business name for a professional attachment filename
    biz_name_clean = business_name.replace(".", "").replace(" ", "_")
    safe_business_name = "".join(x for x in biz_name_clean if x.isalnum() or x == "_")

    # Extract creation date string (e.g., 2026-05-26)
    date_str = audit.created_at.strftime("%Y-%m-%d")

    # --- DYNAMIC FILENAMES (Matched to endpoints.py) ---
    report_prefix = lex["REPORT_PDF"]["filename_prefix"]
    report_filename = f"{report_prefix}_MedSecure_{safe_business_name}_{date_str}.pdf"

    inv_lex = lex["INVOICE"]
    short_id = str(submission_id)[:8]
    invoice_filename = f"{inv_lex['filename_prefix']}_MedSecure_{short_id}.pdf"

    # Generate PDF Attachments in memory using explicit keyword arguments
    report_pdf = generate_pdf(
        template_name="report_pdf.html",
        audit_record=audit,
        lexicon=lex,
        company_name=config.COMPANY_NAME,
        lang=lang,
        display_filename=report_filename,
    )
    invoice_pdf = generate_pdf(
        template_name="invoice_pdf.html",
        audit_record=audit,
        lexicon=lex,
        company_name=config.COMPANY_NAME,
        lang=lang,
        display_filename=invoice_filename,
    )

    # Build Email using the newly isolated EMAIL mapping dictionary
    msg = EmailMessage()
    msg["Subject"] = lex["EMAIL"]["subject"]
    msg["From"] = config.EMAIL_FROM
    msg["To"] = recipient_email
    msg.set_content(lex["EMAIL"]["body"])

    #  Attach Files
    msg.add_attachment(
        report_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=report_filename,
    )
    msg.add_attachment(
        invoice_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=invoice_filename,
    )

    try:
        # LOCAL DEV ENVIRONMENT: Use normal unencrypted SMTP connection for testing tool pipelines (e.g., Mailpit)
        if config.SMTP_PORT == 1025:
            with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT) as server:
                if config.SMTP_USER and config.SMTP_PASS:
                    server.login(config.SMTP_USER, config.SMTP_PASS)
                server.send_message(msg)

        # PRODUCTION ENVIRONMENT: Enforce implicit structural SSL encryption for Infomaniak stacks
        else:
            with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as server:
                if config.SMTP_USER and config.SMTP_PASS:
                    server.login(config.SMTP_USER, config.SMTP_PASS)
                server.send_message(msg)

        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email via SMTP {config.SMTP_HOST}: {e}")
