"""
MedSecure-Check Centralized Wording Store.
Acts as a Single Source of Truth (SSOT) for all UI/PDF copy.
Locale: de-CH (Swiss High German)
"""

# --- Product Identity ---
PRODUCT = {
    "name": "MedSecure-Check",
    "short_name": "MedSecure-Check Schweiz",
    "report_name": "IT-Sicherheitsbericht",
    "tagline": "IT-Sicherheitscheck für Arztpraxen in der Schweiz",
    "short_description": (
        "Ein strukturierter IT-Sicherheits-Check für Arztpraxen "
        "und kleinere medizinische Einrichtungen in der Schweiz."
    ),
}

# --- Landing Page Content ---
LANDING = {
    "headline": "IT-Sicherheit für Arztpraxen - verständlich geprüft",
    "intro": "Ein strukturierter IT-Sicherheits-Check für Arztpraxen und medizinische Einrichtungen in der Schweiz.",
    "promise": "In wenigen Minuten erhalten Sie eine erste Einschätzung Ihrer Datensicherheits- und IT-Risiken.",
    "value_statement": "Die Auswertung ist verständlich aufbereitet, sachlich formuliert und erfolgt ohne kommerziellen Verkaufsansatz.",
    "price_label": "CHF 49.-",
    "cta": "IT-Sicherheits-Check starten",
}

# --- Audit Interface ---
AUDIT = {
    "title": "Strukturierter IT-Sicherheits-Check für medizinische Einrichtungen (ca. 5 Minuten)",
    "fields": {
        "business_name": "Name der Praxis oder Organisation",
        "email": "Geschäftliche E-Mail-Adresse",
    },
    "answers": {
        "yes": "Ja",
        "no": "Nein",
        "na": "Nicht zutreffend",
    },
    "submit": "IT-Sicherheitsbewertung erstellen",
}

# --- Risk Classifications (UI & PDF) ---
RISK_LEVELS = {
    "high": {
        "label": "Erhöhtes Risiko",
        "summary": "Es bestehen relevante Schwachstellen, die überprüft und priorisiert adressiert werden sollten.",
        "pdf_text": "Die aktuelle IT-Sicherheitslage weist relevante Schwachstellen auf. Eine strukturierte Überprüfung und priorisierte Umsetzung geeigneter Massnahmen wird empfohlen.",
    },
    "medium": {
        "label": "Mittleres Risiko",
        "summary": "Die wichtigsten Massnahmen sollten priorisiert umgesetzt werden.",
        "pdf_text": "Die IT-Sicherheitslage ist insgesamt solide, weist jedoch Verbesserungspotenzial in einzelnen Bereichen auf.",
    },
    "low": {
        "label": "Geringes Risiko",
        "summary": "Gute Grundlagen sind vorhanden. Eine regelmässige Überprüfung wird empfohlen.",
        "pdf_text": "Die IT-Sicherheitsgrundlagen sind weitgehend etabliert. Eine regelmässige Überprüfung und Aktualisierung der Massnahmen wird empfohlen.",
    },
}

# --- Results & Sales Page ---
RESULT = {
    "title": "Ihre Auswertung",
    "offer_title": "Persönlicher IT-Sicherheitsbericht für Ihre Praxis",
    "offer_price": "CHF 49.-",
    "benefits": [
        "Übersichtliche Einordnung Ihrer IT-Sicherheitslage",
        "Priorisierte Massnahmen mit Fokus auf Patientendaten",
        "Verständlich für Praxen ohne eigene IT-Abteilung",
        "Berücksichtigung typischer Abläufe in Arztpraxen",
    ],
    "value_explanation": "Der Bericht wurde speziell für medizinische Einrichtungen in der Schweiz entwickelt. Er ersetzt keine Fachberatung, bietet jedoch eine fundierte und unabhängige Ersteinschätzung.",
    "delivery": "Nach Zahlungseingang erhalten Sie Ihren persönlichen PDF-Bericht per E-Mail (in der Regel innerhalb von 24 Stunden).",
    "preview_cta": "PDF-Bericht anzeigen",
}

# --- Report & PDF Generation Content ---
REPORT = {
    "print_cta": "Als PDF speichern",
    "date_label": "Datum",
    "assessment_title": "IT-Sicherheits-Einordnung",
    "sections": {
        "classification": "Einordnung",
        "measures": "Empfohlene Massnahmen",
        "next_steps": "Nächste Schritte",
    },
    "unclear": {
        "title": "Unklare Risikolage",
        "description": "Auf Basis Ihrer Angaben konnte keine zuverlässige Bewertung erstellt werden.",
        "note": "Viele Fragen wurden als „nicht zutreffend“ beantwortet.",
    },
    "findings_intro": "Die folgenden Massnahmen haben den grössten Einfluss auf Ihre IT-Sicherheit:",
    "priority_label": "Priorität",
}

REPORT_PDF = {
    "title_suffix": "IT-Sicherheitsbericht",
    "header_suffix": "IT-Sicherheitsbericht für medizinische Einrichtungen",
    "generated_on": "Bewertung basierend auf Angaben vom",
    "footer_note": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT- oder Rechtsberatung.",
}

# --- Legal & Positioning ---
DISCLAIMERS = {
    "website": "Dieser Check stellt keine rechtliche, regulatorische oder medizinische Beratung dar.",
    "report": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT-, Rechts- oder Fachberatung.",
}

PAYMENT = {
    "price": "CHF 49.-",
    "method": "Zahlung per Rechnung / Banküberweisung",
    "delivery": "Nach Zahlungseingang erhalten Sie Ihren persönlichen PDF-Bericht in der Regel innerhalb von 24 Stunden.",
}
