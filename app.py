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

from scoring import QUESTIONS, compute_score

app = Flask(__name__)
app.config.from_prefixed_env()  # load from .env if using python-dotenv

DATA_DIR = "data"
LOG_FILE = os.path.join("logs", "submissions.log")
os.makedirs(os.path.join(DATA_DIR, "submissions"), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, "pdfs"), exist_ok=True)
os.makedirs("logs", exist_ok=True)


def save_submission(sub):
    # append to a log file as a simple flat store for MVP
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(sub, ensure_ascii=False) + "\n")


def generate_pdf(submission_id):
    """Generate and store PDF for a given submission_id"""

    # Load submission as usual
    submission_path = os.path.join(DATA_DIR, "submissions", f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return None

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    # Prepare context
    utc_dt = datetime.fromisoformat(submission["created_at"])
    zurich_dt = utc_dt.astimezone(ZoneInfo("Europe/Zurich"))
    submission["created_at_human"] = zurich_dt.strftime("%d.%m.%Y %H:%M") + " (CH)"

    # Render HTML
    html = render_template(
        "report_pdf.html",
        submission=submission,
        company=os.getenv("COMPANY_NAME", "SwissSecurityCheck"),
    )

    # Save PDF
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    pdf_filename = f"{submission_id}_{timestamp}.pdf"
    pdf_path = os.path.join(DATA_DIR, "pdfs", pdf_filename)

    HTML(string=html).write_pdf(pdf_path)
    return pdf_path


def send_report_email(to_email, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Ihr Cybersecurity-Bericht"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email
    msg.set_content(
        "Vielen Dank! Im Anhang finden Sie Ihren persönlichen Bericht als PDF."
    )
    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )
    with smtplib.SMTP_SSL(
        os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT", "465"))
    ) as server:
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.send_message(msg)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audit")
def audit():
    return render_template("audit.html", questions=QUESTIONS)


@app.route("/submit", methods=["POST"])
def submit():

    business_name = request.form.get("business_name", "").strip()
    email = request.form.get("email", "").strip()
    answers = {}
    na_count = 0
    # Unique ID (short but safe)
    submission_id = hashlib.sha256(
        f"{business_name}{email}{datetime.now(timezone.utc).isoformat()}{uuid.uuid4()}".encode(
            "utf-8"
        )
    ).hexdigest()[:16]

    for q in QUESTIONS:
        answers[q["id"]] = request.form.get(q["id"], "na")
        na_count = sum(1 for a in answers.values() if a == "na")
    result = compute_score(answers)

    submission = {
        "id": submission_id,
        "business_name": business_name,
        "email": email,
        "answers": answers,
        "score": result["score"],
        "failed": result["failed"],
        "na_count": na_count,
        "paid": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    save_submission(submission)

    # Persistence: save last submission to a temp json file for manual PDF creation.
    submission_path = os.path.join(DATA_DIR, "submissions", f"{submission_id}.json")
    with open(submission_path, "w", encoding="utf-8") as f:
        json.dump(submission, f, ensure_ascii=False, indent=2)
    return render_template(
        "result.html",
        submission=submission,
        submission_id=submission_id,
        IBAN=os.getenv("IBAN", "CHxxx..."),
    )


@app.route("/admin/generate_pdf/<submission_id>")
def admin_generate_pdf(submission_id):
    pdf_path = generate_pdf(submission_id)
    if not pdf_path:
        return "Submission not found", 404
    return f"PDF generated: {pdf_path}"


@app.route("/pdf/<submission_id>")
def pdf(submission_id):
    submission_path = os.path.join(DATA_DIR, "submissions", f"{submission_id}.json")
    if not os.path.exists(submission_path):
        return "Not found", 404

    with open(submission_path, "r", encoding="utf-8") as f:
        submission = json.load(f)

    utc_dt = datetime.fromisoformat(submission["created_at"])
    zurich_dt = utc_dt.astimezone(ZoneInfo("Europe/Zurich"))
    submission["created_at_human"] = zurich_dt.strftime("%d.%m.%Y %H:%M") + " (CH)"

    html = render_template(
        "report_pdf.html",
        submission=submission,
        company=os.getenv("COMPANY_NAME", "SwissSecurityCheck"),
    )

    pdf_bytes = HTML(string=html).write_pdf()

    filename = f"{submission['business_name']} - Cybersecurity-Bericht.pdf"

    return Response(
        pdf_bytes,
        mimetype="application/pdf",
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
