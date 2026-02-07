# app.py
import hashlib
import json
import os
import smtplib
import uuid
from datetime import datetime, timezone
from email.message import EmailMessage
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from flask import Flask, Response, render_template, request
from weasyprint import HTML

import config
from scoring import QUESTIONS, compute_assessment
from wording import (
    AUDIT,
    DISCLAIMERS,
    LANDING,
    PAYMENT,
    PRODUCT,
    REPORT,
    REPORT_PDF,
    RESULT,
    RISK_LEVELS,
    SCOPE,
)

# Load the content of the .env file before launch Flask.
load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

os.makedirs(config.SUBMISSIONS_DIR, exist_ok=True)
os.makedirs(config.PDF_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)


# List of events for the submissions. Save in logs/submissions.log.
# - logs/submissions.log => Immutable history of what happened.
def log_event(event, submission):
    record = {
        "event": event,
        "event_at": datetime.now(timezone.utc).isoformat(),
        "submission_id": submission["id"],
        "data": submission,  # submission_id.json
    }

    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# A submission has ONE current state(save in data/submission),
# but MANY events(save in logs).
# - data/submissions/<id>.json => Latest known state.
def save_submission(submission):
    path = os.path.join(config.SUBMISSIONS_DIR, f"{submission['id']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(submission, f, ensure_ascii=False, indent=2)


# It prevents the "forgot to save" bugs for important cases:
# - paid.
# - future payment_* fields
# - email_sent_at.
# - email_error.
# Not use it for initial submission creation or pure read operations.
def update_submission(submission, **changes):
    for key in changes:
        if key not in submission:
            # A warning if it writes a field that did not previously exist.
            app.logger.warning(f"New field added: {key}")
    submission.update(changes)
    save_submission(submission)


def generate_submission_id(business, email):
    raw = f"{business}|{email}|{datetime.now(timezone.utc)}|{uuid.uuid4()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def generate_report_pdf(submission_id):
    submission_path = os.path.join(config.SUBMISSIONS_DIR, f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return None

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    # HARD SAFETY GUARD
    if submission.get("report_filename"):
        app.logger.warning(
            f"Report already exists for {submission_id}, refusing regeneration"
        )
        return None

    try:

        utc = datetime.fromisoformat(submission["created_at"])
        ch = utc.astimezone(ZoneInfo("Europe/Zurich"))
        submission["created_at_human"] = ch.strftime("%d.%m.%Y %H:%M (CH)")

        html = render_template(
            "report_pdf.html",
            submission=submission,
            company=config.COMPANY_NAME,
        )

        # Report name.
        filename = f"report_{submission_id}_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"
        pdf_path = os.path.join(config.PDF_DIR, filename)

        HTML(string=html).write_pdf(pdf_path)

        return {
            "path": pdf_path,
            "filename": filename,
        }

    except Exception:
        app.logger.exception("generate_report_pdf failed")
        return None


def generate_report_pdf_force(submission_id):
    submission_path = os.path.join(config.SUBMISSIONS_DIR, f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return None

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    try:

        utc = datetime.fromisoformat(submission["created_at"])
        ch = utc.astimezone(ZoneInfo("Europe/Zurich"))
        submission["created_at_human"] = ch.strftime("%d.%m.%Y %H:%M (CH)")

        html = render_template(
            "report_pdf.html",
            submission=submission,
            company=config.COMPANY_NAME,
        )

        # Report name.
        filename = f"report_{submission_id}_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"
        pdf_path = os.path.join(config.PDF_DIR, filename)

        HTML(string=html).write_pdf(pdf_path)

        return {
            "path": pdf_path,
            "filename": filename,
        }

    except Exception:
        app.logger.exception("generate_report_pdf failed")
        return None


def generate_invoice_number(submission_id):
    date_part = datetime.now().strftime("%Y%m")
    return f"MS-{date_part}-{submission_id[:6].upper()}"


def generate_invoice_pdf(submission_id):
    submission_path = os.path.join(config.SUBMISSIONS_DIR, f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return None

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    # HARD SAFETY GUARD (missing today)
    if submission.get("invoice_filename"):
        app.logger.warning(
            f"Invoice already exists for {submission_id}, refusing regeneration"
        )
        return None

    try:
        with open(submission_path, "r", encoding="utf-8") as f:
            submission = json.load(f)

        utc = datetime.fromisoformat(submission["created_at"])
        ch = utc.astimezone(ZoneInfo("Europe/Zurich"))
        submission["created_at_human"] = ch.strftime("%d.%m.%Y")

        html = render_template(
            "invoice_pdf.html",
            submission=submission,
            company=config.COMPANY_NAME,
            IBAN=config.IBAN,
        )

        # Invoice name.
        filename = (
            f"invoice_{submission_id}_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"
        )
        pdf_path = os.path.join(config.PDF_DIR, filename)

        HTML(string=html).write_pdf(pdf_path)

        return {
            "path": pdf_path,
            "filename": filename,
        }

    except Exception:
        app.logger.exception("generate_invoice_pdf failed")
        return None


# Read-only PDF function
def get_report_pdf_path(submission_id):
    submission_path = os.path.join(config.SUBMISSIONS_DIR, f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return None

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    filename = submission.get("report_filename")
    if not filename:
        return None

    path = os.path.join(config.PDF_DIR, filename)
    return path if os.path.exists(path) else None


def smtp_config_is_valid():
    return all(
        [
            config.SMTP_HOST,
            config.SMTP_PORT,
            config.SMTP_USER,
            config.SMTP_PASS,
            config.EMAIL_FROM,
        ]
    )


def send_report_and_invoice_email(to_email, report_path, invoice_path, submission):
    msg = EmailMessage()
    msg["Subject"] = (
        f"Ihre MedSecure-Einordnung - Rechnung {submission['invoice_number']}"
    )
    msg["From"] = config.EMAIL_FROM
    msg["To"] = to_email

    msg.set_content(
        f"""Guten Tag

Vielen Dank für die Nutzung von MedSecure.

Im Anhang finden Sie:
- Ihren IT-Sicherheitsbericht
- die zugehörige Rechnung ({submission['invoice_number']})

Freundliche Grüsse
{config.COMPANY_NAME}
"""
    )

    for path in [report_path, invoice_path]:
        with open(path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename=os.path.basename(path),
            )

    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as s:
        s.login(config.SMTP_USER, config.SMTP_PASS)
        s.send_message(msg)


# Use the sentences from "wording.py" to have a Swiss medical tone.
@app.context_processor
def inject_wording():
    return {
        "PRODUCT": PRODUCT,
        "LANDING": LANDING,
        "AUDIT": AUDIT,
        "RISK_LEVELS": RISK_LEVELS,
        "RESULT": RESULT,
        "REPORT": REPORT,
        "REPORT_PDF": REPORT_PDF,
        "DISCLAIMERS": DISCLAIMERS,
        "PAYMENT": PAYMENT,
        "SCOPE": SCOPE,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audit")
def audit():
    return render_template("audit.html", questions=QUESTIONS)


@app.route("/submit", methods=["POST"])
def submit():

    business = request.form.get("business_name", "").strip()
    email = request.form.get("email", "").strip()

    answers = {}
    na_count = 0
    for q in QUESTIONS:
        answers[q["id"]] = request.form.get(q["id"], "na")
    na_count = sum(1 for a in answers.values() if a == "na")

    result = compute_assessment(answers)
    submission_id = generate_submission_id(business, email)
    invoice_number = generate_invoice_number(submission_id)

    submission = {
        "id": submission_id,
        "invoice_number": invoice_number,
        "business_name": business,
        "email": email,
        "answers": answers,
        "assessment": result["assessment"],
        "risk_level": result["risk_level"],
        "failed": result["failed"],
        "na_count": na_count,
        "paid": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    # Submission is saved even if email fails.
    # Email failure:
    #  - does not crash the request.
    #  - is recorded for later inspection.
    # "email_sent_at" means what it says.

    # Save the submission before sending the email.
    save_submission(submission)
    # Save the event of the submission before sending email.
    log_event("submission_created", submission)

    # Documents generation (one time only)
    # data/submissions/<id>.json is the authority.
    report_pdf = generate_report_pdf(submission_id)
    invoice_pdf = generate_invoice_pdf(submission_id)

    # Add the report and invoice file name to submission(dict)
    if report_pdf:
        update_submission(
            submission,
            report_filename=report_pdf["filename"],
        )

    if invoice_pdf:
        update_submission(
            submission,
            invoice_filename=invoice_pdf["filename"],
        )

    # Log documents generation events.
    if report_pdf:
        log_event(
            "report_generated",
            {
                **submission,
                "report_filename": report_pdf["filename"],
            },
        )

    if invoice_pdf:
        log_event(
            "invoice_generated",
            {
                **submission,
                "invoice_filename": invoice_pdf["filename"],
            },
        )

    # The email is sent in production, not in development.
    if smtp_config_is_valid() and report_pdf and invoice_pdf:
        if config.ENV == "production":
            try:
                send_report_and_invoice_email(
                    submission["email"],
                    report_pdf["path"],
                    invoice_pdf["path"],
                    submission,
                )

                update_submission(
                    submission,
                    email_sent_at=datetime.now(timezone.utc).isoformat(),
                )
                log_event("email_sent", submission)

            except Exception:
                app.logger.exception("Email sending failed")
                update_submission(submission, email_error="smtp_failed")
                log_event("email_failed", submission)

        else:

            update_submission(
                submission, email_error="email_disabled_or_not_configured"
            )
            log_event("email_skipped_dev", submission)

    return render_template(
        "result.html",
        submission=submission,
        submission_id=submission_id,
        IBAN=config.IBAN,
    )


@app.route("/admin/generate_pdf/<submission_id>")
def admin_generate_pdf(submission_id):
    pdf = generate_report_pdf_force(submission_id)
    submission = load_submission(submission_id)

    if not pdf:
        return "Submission not found", 404

    update_submission(
        submission,
        report_filename=pdf["filename"],
    )

    log_event(
        "report_regenerated",
        {
            "id": submission_id,
            "previous_report": submission.get("report_filename"),
            "new_report": pdf["filename"],
        },
    )

    return f"PDF regenerated: {pdf['filename']}"


@app.route("/pdf/<submission_id>")
def serve_pdf(submission_id):
    path = get_report_pdf_path(submission_id)
    if not path:
        return "PDF not available", 404

    with open(path, "rb") as f:
        return Response(
            f.read(),
            mimetype="application/pdf",
            headers={
                "Content-Disposition": f"inline; filename={os.path.basename(path)}"
            },
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
