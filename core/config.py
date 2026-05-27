"""
MedSecure Schweiz Configuration Management.
Handles environment variables and directory mapping.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Project Root (parent of core/ is the true root-level of the project)
BASE_DIR = Path(__file__).resolve().parent.parent

# Target the .env file at the project root
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Database Configuration
DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://localhost/medsecure_db")

# Business Information
COMPANY_NAME: str = os.getenv("COMPANY_NAME", "MedSecure")
IBAN: str = os.getenv("IBAN", "")

# Email & Mail Server Configurations
EMAIL_FROM: str = os.getenv("EMAIL_FROM", "info@medsecure-check.ch")
SMTP_HOST: str = os.getenv("SMTP_HOST", "localhost")
try:
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "465"))
    if SMTP_PORT <= 0:
        SMTP_PORT = 465
except ValueError:
    SMTP_PORT = 465

SMTP_USER: str = os.getenv("SMTP_USER", "")
SMTP_PASS: str = os.getenv("SMTP_PASS", "")

# Stripe Gateway Credentials
STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
try:
    STRIPE_PRICE_CHF: int = int(os.getenv("STRIPE_PRICE_CHF", "4900"))
except ValueError:
    STRIPE_PRICE_CHF = 4900
