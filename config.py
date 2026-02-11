import os

ENV = os.getenv("ENV", "development")
# ENV = os.getenv("ENV", "production")

COMPANY_NAME = os.getenv("COMPANY_NAME", "MedSecure Schweiz")
IBAN = os.getenv("IBAN", "")

EMAIL_FROM = os.getenv("EMAIL_FROM")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

DATA_DIR = "data"
SUBMISSIONS_DIR = os.path.join(DATA_DIR, "submissions")
PDF_DIR = os.path.join(DATA_DIR, "pdfs")
LOG_FILE = os.path.join("logs", "submissions.log")

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
STRIPE_PRICE_CHF = int(os.getenv("STRIPE_PRICE_CHF", "5000"))
