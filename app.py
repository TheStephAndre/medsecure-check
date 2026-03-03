"""
Main Flask Application for MedSecure Schweiz.
Features: Automated Audit, Stripe Integration, PDF Generation & SMTP Delivery.
"""

import os
import hashlib
import json
import uuid
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage
from zoneinfo import ZoneInfo

import stripe
from flask import Flask, Response, abort, redirect, render_template, request, url_for
from weasyprint import HTML
from dotenv import load_dotenv

import config
from scoring import QUESTIONS, AuditEngine
from wording import * # Loads Swiss-German strings

# Load environment & app configuration
load_dotenv()
app = Flask(__name__)
app.config.from_prefixed_env()
stripe.api_key = config.STRIPE_SECRET_KEY

# Ensure required directory structure
for path in [config.SUBMISSIONS_DIR, config.PDF_DIR, "logs"]:
    os.makedirs(path, exist_ok=True)

# --- CORE UTILITIES ---

def log_event(event_type, data, submission_id=None):
    """Immutable event logger for audit trails."""
    record = {
        "event": event_type,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "submission_id": submission_id,
        "data": data,
    }
    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def save_submission(submission):
    """Persists the current state of a submission to disk."""
    path = os.path.join(config.SUBMISSIONS_DIR, f"{submission['id']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(submission, f, ensure_ascii=False, indent=2)

def update_submission(submission, **kwargs):
    """Updates and saves a submission atomically."""
    submission.update(kwargs)
    save_submission(submission)

def load_submission(sid):
    path = os.path.join(config.SUBMISSIONS_DIR, f"{sid}.json")
    if not os.path.exists(path): return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# --- PDF & EMAIL LOGIC ---

def generate_documents(sid, force=False):
    """Handles PDF generation for reports and invoices."""
    sub = load_submission(sid)
    if not sub: return None
    
    try:
        # Timezone conversion for Swiss compliance
        ch_time = datetime.fromisoformat(sub["created_at"]).astimezone(ZoneInfo("Europe/Zurich"))
        sub["created_at_human"] = ch_time.strftime("%d.%m.%Y %H:%M")

        # Render & Save Report
        html_report = render_template("report_pdf.html", submission=sub, company=config.COMPANY_NAME)
        rep_name = f"report_{sid}_{datetime.now().strftime('%Y%m%d')}.pdf"
        rep_path = os.path.join(config.PDF_DIR, rep_name)
        HTML(string=html_report).write_pdf(rep_path)

        # Render & Save Invoice
        html_inv = render_template("invoice_pdf.html", submission=sub, company=config.COMPANY_NAME, IBAN=config.IBAN)
        inv_name = f"invoice_{sid}_{datetime.now().strftime('%Y%m%d')}.pdf"
        inv_path = os.path.join(config.PDF_DIR, inv_name)
        HTML(string=html_inv).write_pdf(inv_path)

        return {"report": rep_name, "invoice": inv_name, "r_path": rep_path, "i_path": inv_path}
    except Exception as e:
        app.logger.error(f"Doc gen failed: {e}")
        return None

# --- ROUTES ---

@app.context_processor
def inject_ui_text():
    """Injects Swiss-German wording into all templates."""
    return {
        "PRODUCT": PRODUCT, "LANDING": LANDING, "AUDIT": AUDIT,
        "RISK_LEVELS": RISK_LEVELS, "RESULT": RESULT, "REPORT": REPORT
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/audit")
def audit():
    return render_template("audit.html", questions=QUESTIONS)

@app.route("/submit", methods=["POST"])
def submit():
    """Handles audit form submission and orchestrates background tasks."""
    business = request.form.get("business_name", "Unbekannt").strip()
    email = request.form.get("email", "").strip()
    
    # 1. Calculation
    engine = AuditEngine(request.form.to_dict())
    results = engine.compute()
    
    # 2. Create Submission
    sid = hashlib.sha256(f"{business}{email}{uuid.uuid4()}".encode()).hexdigest()[:16]
    submission = {
        "id": sid,
        "business_name": business,
        "email": email,
        "assessment": results["assessment"],
        "risk_level": results["risk_level"],
        "failed": results["failed"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "payment_status": "unpaid",
        "invoice_number": f"MS-{datetime.now().strftime('%Y%m')}-{sid[:4].upper()}"
    }
    
    save_submission(submission)
    log_event("submission_created", {"email": email}, sid)

    # 3. Doc Generation Flow
    docs = generate_documents(sid)
    if docs:
        update_submission(submission, 
                          report_filename=docs["report"], 
                          invoice_filename=docs["invoice"])
        log_event("documents_ready", docs, sid)

    return redirect(url_for("result", submission_id=sid))

@app.route("/result/<submission_id>")
def result(submission_id):
    sub = load_submission(submission_id)
    if not sub: abort(404)
    return render_template("result.html", submission=sub, submission_id=submission_id)

@app.route("/pay/<submission_id>")
def pay(submission_id):
    sub = load_submission(submission_id)
    if not sub: abort(404)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "chf",
                "unit_amount": config.STRIPE_PRICE_CHF,
                "product_data": {"name": "Cyber Risk Kurzbewertung"},
            },
            "quantity": 1,
        }],
        mode="payment",
        metadata={"submission_id": submission_id},
        success_url=url_for("payment_success", submission_id=submission_id, _external=True),
        cancel_url=url_for("index", _external=True),
    )
    return redirect(session.url)

@app.route("/payment/success/<submission_id>")
def payment_success(submission_id):
    sub = load_submission(submission_id)
    if sub and sub.get("payment_status") == "paid":
        return render_template("payment_success.html", submission=sub)
    return redirect(url_for("result", submission_id=submission_id))

@app.route("/stripe/webhook", methods=["POST"])
def stripe_webhook():
    """Truth source for payment confirmation via Stripe Webhooks."""
    payload = request.data
    sig = request.headers.get("Stripe-Signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig, config.STRIPE_WEBHOOK_SECRET)
    except: return "Invalid", 400

    if event["type"] == "checkout.session.completed":
        sid = event["data"]["object"]["metadata"]["submission_id"]
        sub = load_submission(sid)
        if sub:
            update_submission(sub, payment_status="paid", paid_at=datetime.now(timezone.utc).isoformat())
            log_event("payment_confirmed", {"sid": sid}, sid)
            
    return "", 200

if __name__ == "__main__":
    app.run(debug=config.ENV == "development")
