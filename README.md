# MedSecure-Check Schweiz 🇨🇭

**Automated Cyber-Security Assessment & Reporting for Swiss Medical Practices.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Framework](https://img.shields.io/badge/FastAPI-0.115.0-black.svg)
![Stripe](https://img.shields.io/badge/Payments-Stripe-6772e5.svg)
![Security](https://img.shields.io/badge/Compliance-nDSG__Ready-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Product Vision

MedSecure-Check is a professional Micro-SaaS designed to bridge the gap between technical security audits and formal compliance for Swiss medical clinics (dentists, physiotherapists, chiropractors). It automates the generation of actionable PDF reports specifically aligned with the Swiss **nDSG** (Federal Act on Data Protection) and **NCSC** standards.

### Why this project stands out:

- **Domain Specific**: Tailored for Healthcare providers with strict data privacy requirements.
- **Zero-Touch Automation**: 100% automated flow from user input to Stripe payment and immediate PDF delivery.
- **Swiss-Native UX**: Multi-dialect support (**de-CH, fr-CH, it-CH**) with CHF currency and Swiss-standard date formatting.

## 🏗️ Technical Architecture

The application follows **Clean Architecture** principles, ensuring core business logic remains independent of the web framework.

- **Logic Engine (`scoring.py`)**: A decoupled, Object-Oriented engine that identifies vulnerabilities, calculates pillar-based maturity scores, and handles "Inconclusive" states for incomplete assessments.
- **Dynamic Data Reconciliation**: A PostgreSQL backend tracks audit history and payment status, allowing for reliable asynchronous reconciliation via Stripe Webhooks and direct API verification.
- **Intelligent PDF Orchestration**: A custom-built engine using **WeasyPrint** and advanced CSS Paged Media rules. It features dynamic pagination logic (using `page-break-inside: avoid`) to prevent orphaned text and logically group legal disclaimers.
- **Single Source of Truth (`wording.py`)**: A centralized localization system. A single change updates the Web UI, PDF reports, and database-stored JSON findings across all three languages.

## 🛠️ Tech Stack

| Layer          | Technology                                                |
| :------------- | :-------------------------------------------------------- |
| **Backend**    | Python 3.12, **FastAPI**                                  |
| **Database**   | **PostgreSQL** (SQLAlchemy ORM) with JSONB for audit logs |
| **PDF Engine** | WeasyPrint 68.0, Jinja2, HTML5/CSS3 (Paged Media)         |
| **Payments**   | Stripe API 14.3+ (Checkout & Webhooks)                    |
| **Frontend**   | Pico.css (Semantic HTML & Minimalist UI)                  |
| **DevOps**     | Pydantic (Data validation), Dotenv (Secret masking)       |

## 🚀 Advanced Features

- **Dynamic Pagination Engine**: Solved complex PDF layout issues using CSS Paged Media rules. The engine automatically ensures methodology sections and legal disclaimers stay grouped, moving them to a 3rd page only when necessary to maintain professional readability.
- **Localized JSON Schema**: The database stores assessment results, pillar scores, and failed items as JSON objects, preserving the linguistic context and specific standards (e.g., DSG Art. 8 or NCSC 5.1.1) used during the audit.
- **Transaction Integrity**: Dual-layer verification (Webhook + Direct Session Check) ensures reports are only generated and persistent data is updated after a successful Stripe transaction.

## 📂 Project Structure

- `api/v1/endpoints.py`: Web routing, Stripe orchestration, and report delivery.
- `core/scoring.py`: Core risk-assessment logic and confidence algorithms.
- `core/wording.py`: SSOT (Single Source of Truth) for de-CH, fr-CH, and it-CH.
- `core/models.py`: Database schema for persistent audit and payment tracking.
- `core/pdf.py`: Enhanced PDF generation logic and layout management.
- `templates/`: Localized Jinja2 templates for UI, Reports, and Invoices.

---

## 🛠️ Getting Started & Local Development

### 1. Prerequisites

Ensure you have Python 3.12+ installed locally. If you run the application outside of Docker, you must install the system layout engines required by WeasyPrint 68+:

- **macOS**: `brew install pango libffi`
- **Ubuntu/Debian**: `sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 shared-mime-info`
- **Windows**: Follow the official WeasyPrint installation guide to install the GTK+ libraries.

### 2. Installation & Setup

Clone the repository and install the Python dependencies inside a clean virtual environment:

```bash
# Clone the repository
git clone [https://github.com/your-username/medsecure-check.git](https://github.com/your-username/medsecure-check.git)
cd medsecure-check

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the root directory and populate your runtime variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/medsecure_db
STRIPE_SECRET_KEY=sk_test_your_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
STRIPE_PRICE_CHF=8900
COMPANY_NAME="MedSecure Schweiz"
```

### 4. Running the Application

Run the local development Uvicorn server to launch the platform:

```bash
uvicorn main:app --reload
```

The application will be accessible locally at `http://127.0.0.1:8000`.

---

_Disclaimer: This tool provides guidance based on Swiss technical standards. It does not replace professional legal or IT forensic advice._
