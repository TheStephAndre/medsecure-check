import smtplib
from email.message import EmailMessage

from sqlalchemy.orm import Session

from core.config import Config
from core.models import AuditSubmission
from core.pdf import generate_pdf
from core.wording import get_lexicon


def send_audit_results_email(submission_id: str, db: Session):
    # Fetch data
    audit = (
        db.query(AuditSubmission).filter(AuditSubmission.id == submission_id).first()
    )
    if not audit:
        return

    lang = audit.lang or "fr-CH"
    lex = get_lexicon(lang)

    # Generate PDF Attachments in memory
    report_pdf = generate_pdf("report_pdf.html", audit, lex, lang, Config.COMPANY_NAME)
    invoice_pdf = generate_pdf(
        "invoice_pdf.html", audit, lex, lang, Config.COMPANY_NAME
    )

    # Build Email
    msg = EmailMessage()
    msg["Subject"] = f"{lex['EMAIL']['subject']} - {Config.COMPANY_NAME}"
    msg["From"] = Config.EMAIL_FROM
    msg["To"] = audit.email
    msg.set_content(lex["EMAIL"]["body"])  # Add this key to your lexicon

    # Attach Files
    msg.add_attachment(
        report_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=f"Rapport_{audit.business_name}.pdf",
    )
    msg.add_attachment(
        invoice_pdf.getvalue(),
        maintype="application",
        subtype="pdf",
        filename=f"Facture_{audit.business_name}.pdf",
    )

    # Send via SMTP
    try:
        with smtplib.SMTP_SSL(Config.SMTP_HOST, Config.SMTP_PORT) as server:
            server.login(Config.SMTP_USER, Config.SMTP_PASS)
            server.send_message(msg)
        print(f"Email successfully sent to {audit.email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
