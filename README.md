# MedSecure-Check Schweiz 🇨🇭
**A Professional Cyber-Security & Compliance Assessment Tool for Swiss Medical Practices.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)
![Market](https://img.shields.io/badge/Market-Switzerland-red.svg)

## 🚀 Product Vision
A high-precision, 5-minute IT security assessment designed specifically for Swiss medical and health practices (physiotherapists, dentists, chiropractors). It delivers a professional PDF report and actionable insights without technical jargon.

### 🎯 Strategic Positioning
* **Target Persona:** Non-technical owners of Swiss SMEs (1-10 employees).
* **Core Value:** Converting anxiety over DSG/nDSG (Swiss Data Protection Act) into clarity and peace of mind.
* **Trust First:** Built with a "Swiss-native" feel—CHF pricing, DD.MM.YYYY formats, and neutral, factual language.



## 🛠️ Tech Stack & Architecture
* **Backend:** Python 3.12 / Flask (Clean Architecture).
* **Logic Engine:** Decoupled scoring system with confidence-penalty algorithms (`scoring.py`).
* **Payments:** Full Stripe API integration (Checkout + Webhooks for idempotency).
* **Document Generation:** Server-side PDF generation using WeasyPrint.
* **Deployment:** Production-ready for Heroku/Render via Gunicorn.

## 📂 Project Structure
* `app.py`: Clean routing and request handling.
* `scoring.py`: Professional scoring engine (Object-Oriented).
* `wording.py`: Centralized Source of Truth for all Swiss-German localized content.
* `config.py`: Environment-based secure configuration using `pathlib`.

## 🛡️ Founders' Boundary Contract
This project is built as a **Scalable Micro-SaaS**.
* **Automated:** No manual intervention needed for report delivery.
* **Secure:** No hardcoded secrets; strictly follows `.env` patterns.
* **Action-Oriented:** Every line of code serves the goal of providing the "3 most important actions" to the user.

---
*Disclaimer: This tool provides general guidance aligned with Swiss standards. It does not replace professional legal or IT advice.*
