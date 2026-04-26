# MedSecure-Check Schweiz 🇨🇭

**Automated Cyber-Security Assessment & Reporting for Swiss Medical Practices.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Framework](https://img.shields.io/badge/FastAPI-0.115.0-black.svg)
![Stripe](https://img.shields.io/badge/Payments-Stripe-6772e5.svg)
![Security](https://img.shields.io/badge/Compliance-nDSG_Ready-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Product Vision

MedSecure-Check is a professional Micro-SaaS prototype designed to solve "compliance anxiety" for small Swiss medical clinics (dentists, physiotherapists, chiropractors). It automates the gap between a security audit and a formal, actionable PDF report, specifically aligned with the technical expectations of the Swiss **nDSG** (Federal Act on Data Protection).

### Why this project stands out:

- **Domain Specific**: Built for a high-stakes niche (Healthcare) with strict data privacy requirements.
- **Zero-Touch Automation**: 100% automated flow from user input to Stripe payment and PDF delivery.
- **Swiss-Native UX**: Built for the Swiss market with CHF currency, Swiss date formats (DD.MM.YYYY), and full **trilingual support** (de-CH, fr-CH, it-CH).

## 🏗️ Technical Architecture

The application follows **Clean Architecture** principles, ensuring that business logic remains independent of the web framework.

- **Logic Engine (`scoring.py`)**: A decoupled, Object-Oriented engine that identifies vulnerabilities and applies a _Confidence Penalty_ algorithm (adjusting scores based on "N/A" answer frequency).
- **Single Source of Truth (`wording.py`)**: A centralized localization system managing three languages. A single change here updates the Web UI, PDF reports, and Invoices across all linguistic regions simultaneously.
- **Document Orchestration**: Server-side PDF generation using **WeasyPrint** with custom CSS optimized for A4 print standards, featuring dynamic metadata injection for professional document naming.
- **Secure Payment Flow**: Integration with **Stripe Checkout** utilizing **Webhooks** and direct API verification to prevent race conditions during payment state management.

## 🛠️ Tech Stack

| Layer          | Technology                                                 |
| :------------- | :--------------------------------------------------------- |
| **Backend**    | Python 3.12, **FastAPI**                                   |
| **Server**     | Uvicorn / Gunicorn (optimized worker/thread configuration) |
| **Database**   | PostgreSQL (SQLAlchemy ORM)                                |
| **PDF Engine** | WeasyPrint 68.0, Jinja2, HTML5/CSS3                        |
| **Payments**   | Stripe API 14.3+                                           |
| **Frontend**   | Pico.css (Semantic HTML & Minimalist UI)                   |
| **DevOps**     | Pydantic (Data validation), Dotenv (Secret masking)        |

## 📂 Project Structure

- `api/v1/endpoints.py`: Web routing, Stripe orchestration, and PDF delivery.
- `core/scoring.py`: Core risk-assessment logic (Decoupled from FastAPI).
- `core/wording.py`: SSOT (Single Source of Truth) for de-CH, fr-CH, and it-CH copy.
- `core/models.py`: Database schema for persistent audit and payment tracking.
- `core/pdf.py`: Centralized PDF generation logic using WeasyPrint.
- `templates/`: Jinja2 templates for localized UI, Reports, and Invoices.

## 🛡️ Security & Reliability

- **Secret Isolation**: Total masking of Stripe and Database credentials via environment variables.
- **Robust Verification**: Dual-layer payment confirmation (Webhook + Direct Session Check) to ensure zero-latency report unlocking.
- **Privacy by Design**: Strict `.gitignore` policy ensuring no sensitive patient-related data or generated reports enter version control.
- **Swiss-Optimized Layout**: Specialized CSS to handle long compound words (e.g., _Zahlungsbestätigung_) across professional PDF exports.

---

_Disclaimer: This tool provides general guidance aligned with Swiss technical standards. It does not replace professional legal or IT advice._
