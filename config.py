"""
MedSecure Schweiz Configuration Management.
Handles environment variables and directory mapping.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent


class Config:
    """Application configuration encapsulated in a class for Flask compatibility."""

    # Environment & Branding
    ENV = os.getenv("ENV", "development")
    COMPANY_NAME = os.getenv("COMPANY_NAME", "MedSecure")
    IBAN = os.getenv("IBAN", "")

    # Mail Server - (SMTP)
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

    # Stripe Integration
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    STRIPE_PRICE_CHF = int(os.getenv("STRIPE_PRICE_CHF", "5000"))  # Amount in cents
