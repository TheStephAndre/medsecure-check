# MedSecure-Check Schweiz 🇨🇭
**Automated Cyber-Security Assessment & Reporting for Swiss Medical Practices.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Framework](https://img.shields.io/badge/Flask-3.1.2-black.svg)
![Stripe](https://img.shields.io/badge/Payments-Stripe-6772e5.svg)
![Security](https://img.shields.io/badge/Compliance-nDSG_Ready-red.svg)

## 🎯 Product Vision
MedSecure-Check is a professional Micro-SaaS prototype designed to solve "compliance anxiety" for small Swiss medical clinics (dentists, physiotherapists, chiropractors). It automates the gap between a security audit and a formal, actionable PDF report, specifically aligned with the Swiss **nDSG** (Federal Act on Data Protection) expectations.

### Why this project stands out:
* **Domain Specific**: Built for a high-stakes niche (Healthcare) with strict data privacy requirements.
* **Zero-Touch Automation**: 100% automated flow from user input to Stripe payment and PDF delivery.
* **Swiss-Native UX**: Handles CHF currency, Swiss date formats (DD.MM.YYYY), and localized High German (de-CH).



## 🏗️ Technical Architecture
The application follows **Clean Architecture** principles, ensuring that business logic remains independent of the web framework.

* **Logic Engine (`scoring.py`)**: A decoupled, Object-Oriented engine that identifies vulnerabilities and applies a *Confidence Penalty* algorithm (adjusting scores based on "N/A" answer frequency).
* **Single Source of Truth (`wording.py`)**: A centralized localization system. A single change here updates the Web UI, PDF reports, and Invoices simultaneously.
* **Document Orchestration**: Server-side PDF generation using **WeasyPrint** with custom CSS optimized for A4 print standards.
* **Secure Payment Flow**: Integration with **Stripe Checkout** utilizing **Webhooks** for secure, asynchronous payment confirmation and state management.



## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.12, Flask |
| **Server** | Gunicorn (optimized worker/thread configuration) |
| **PDF Engine** | WeasyPrint, Jinja2, HTML5/CSS3 |
| **Payments** | Stripe API (v14.0+) |
| **Frontend** | Pico.css (Semantic HTML & Minimalist UI) |
| **DevOps** | Pathlib (OS-agnostic paths), Dotenv (Secret masking) |

## 📂 Project Structure
* `app.py`: Web routing and payment orchestration.
* `scoring.py`: Core risk-assessment logic (Decoupled from Flask).
* `wording.py`: SSOT (Single Source of Truth) for all UI and legal copy.
* `config.py`: Secure environment-based configuration using `pathlib`.
* `gunicorn_config.py`: Production-grade server tuning (Timeouts & Workers).

## 🛡️ Security & Reliability
* **Secret Isolation**: Total masking of API keys and credentials via environment variables.
* **Privacy by Design**: Strict `.gitignore` policy ensuring no user data or generated reports enter version control.
* **Idempotency**: Stripe Webhook integration ensures payments are processed reliably even in case of network interruptions.
* **Scalability**: Designed as a stateless application, ready for containerization or PaaS deployment (Heroku, Render).

---
*Disclaimer: This tool provides general guidance aligned with Swiss standards. It does not replace professional legal or IT advice.*
