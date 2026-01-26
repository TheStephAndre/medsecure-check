# app.py
import hashlib
import json
import os
import smtplib
import uuid
from datetime import datetime, timezone
from email.message import EmailMessage
from zoneinfo import ZoneInfo

from flask import Flask, Response, render_template, request
from weasyprint import HTML

import config
from scoring import QUESTIONS, compute_score

app = Flask(__name__)
app.config.from_prefixed_env()

os.makedirs(config.SUBMISSIONS_DIR, exist_ok=True)
os.makedirs(config.PDF_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)


def save_submission(sub):
    # append to a log file as a simple flat store for MVP
    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(sub, ensure_ascii=False) + "\n")

    path = os.path.join(config.SUBMISSIONS_DIR, f"{sub['id']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sub, f, ensure_ascii=False, indent=2)


def generate_submission_id(business, email):
    raw = f"{business}|{email}|{datetime.now(timezone.utc)}|{uuid.uuid4()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def generate_pdf(submission_id):
    submission_path = os.path.join(config.SUBMISSIONS_DIR, f"{submission_id}.json")

    if not os.path.exists(submission_path):
        return None

    try:
        with open(submission_path, "r", encoding="utf-8") as f:
            submission = json.load(f)

        utc = datetime.fromisoformat(submission["created_at"])
        ch = utc.astimezone(ZoneInfo("Europe/Zurich"))
        submission["created_at_human"] = ch.strftime("%d.%m.%Y %H:%M (CH)")

        html = render_template(
            "report_pdf.html",
            submission=submission,
            company=config.COMPANY_NAME,
        )

        filename = f"{submission_id}_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"
        pdf_path = os.path.join(config.PDF_DIR, filename)

        HTML(string=html).write_pdf(pdf_path)
        return pdf_path

    except Exception:
        app.logger.exception("generate_pdf failed")
        return None


def send_report_email(to_email, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Ihr MedSecure-Bericht"
    msg["From"] = config.EMAIL_FROM
    msg["To"] = email
    msg.set_content(
        "Vielen Dank für Ihr Vertrauen.\n\n"
        "Im Anhang finden Sie Ihren persönlichen Datensicherheits-Bericht."
    )

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )

    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as s:
        s.login(config.SMTP_USER, config.SMTP_PASS)
        s.send_message(msg)


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

    result = compute_score(answers)
    submission_id = generate_submission_id(business, email)

    submission = {
        "id": submission_id,
        "business_name": business,
        "email": email,
        "answers": answers,
        "score": result["score"],
        "failed": result["failed"],
        "na_count": na_count,
        "paid": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    save_submission(submission)

    return render_template(
        "result.html",
        submission=submission,
        submission_id=submission_id,
        IBAN=config.IBAN,
    )


@app.route("/admin/generate_pdf/<submission_id>")
def admin_generate_pdf(submission_id):
    pdf_path = generate_pdf(submission_id)
    if not pdf_path:
        return "Submission not found", 404
    return f"PDF generated: {pdf_path}"


@app.route("/pdf/<submission_id>")
def pdf(submission_id):
    try:
        pdf_path = generate_pdf(submission_id)
        if not pdf_path:
            return "Submission not found", 404

        with open(pdf_path, "rb") as f:
            return Response(
                f.read(),
                mimetype="application/pdf",
                headers={
                    "Content-Disposition": (
                        f"inline; filename={os.path.basename(pdf_path)}"
                    )
                },
            )

    except Exception as e:
        app.logger.exception("PDF generation failed")
        return f"PDF generation error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
