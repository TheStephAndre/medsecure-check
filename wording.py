# This canonical wording file is one single source of truth for all important phrases that:
# - Appear in multiple templates.
# - Express risk levels, disclaimers, product descriptions.
# - Must stay legally and tonally consistent.
# Instead of hard-coding text repeatedly in: index.html, result.html, report.html, report_pdf.html
# The voice of MedSecure-Check — frozen, defensible, and consistent.

# Define product identity =>
# Avoids name drift (Swiss Medical / MedSecure / Med-Check etc.)
# Prevents marketing inflation later
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


# Define Landing page texts =>
LANDING = {
    "headline": "IT-Sicherheit für Arztpraxen - verständlich geprüft",
    "intro": (
        "Ein strukturierter IT-Sicherheits-Check für Arztpraxen und medizinische "
        "Einrichtungen in der Schweiz."
    ),
    "promise": (
        "In wenigen Minuten erhalten Sie eine erste Einschätzung Ihrer "
        "Datensicherheits- und IT-Risiken."
    ),
    "value_statement": (
        "Die Auswertung ist verständlich aufbereitet, sachlich formuliert "
        "und erfolgt ohne kommerziellen Verkaufsansatz."
    ),
    "price_label": "CHF 49.-",
    "cta": "IT-Sicherheits-Check starten",
}

# Define Audit page texts =>
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


# Define risk classification texts =>
# Two texts per level:
# summary: short UI text
# pdf_text: formal written language for printed reports
# This avoids tone mismatch without duplication.
RISK_LEVELS = {
    "high": {
        "label": "Erhöhtes Risiko",
        "summary": (
            "Es bestehen relevante Schwachstellen, die überprüft "
            "und priorisiert adressiert werden sollten."
        ),
        "pdf_text": (
            "Die aktuelle IT-Sicherheitslage weist relevante Schwachstellen auf. "
            "Eine strukturierte Überprüfung und priorisierte Umsetzung "
            "geeigneter Massnahmen wird empfohlen."
        ),
    },
    "medium": {
        "label": "Mittleres Risiko",
        "summary": ("Die wichtigsten Massnahmen sollten priorisiert umgesetzt werden."),
        "pdf_text": (
            "Die IT-Sicherheitslage ist insgesamt solide, weist jedoch "
            "Verbesserungspotenzial in einzelnen Bereichen auf."
        ),
    },
    "low": {
        "label": "Geringes Risiko",
        "summary": (
            "Gute Grundlagen sind vorhanden. "
            "Eine regelmässige Überprüfung wird empfohlen."
        ),
        "pdf_text": (
            "Die IT-Sicherheitsgrundlagen sind weitgehend etabliert. "
            "Eine regelmässige Überprüfung und Aktualisierung "
            "der Massnahmen wird empfohlen."
        ),
    },
}

# Define result page texts =>
RESULT = {
    "title": "Ihre Auswertung",
    "risk_levels": {
        "high": {
            "label": "Erhöhtes Risiko",
            "description": (
                "Es bestehen relevante Schwachstellen, die überprüft "
                "und priorisiert adressiert werden sollten."
            ),
        },
        "medium": {
            "label": "Mittleres Risiko",
            "description": (
                "Die wichtigsten Massnahmen sollten priorisiert umgesetzt werden."
            ),
        },
        "low": {
            "label": "Geringes Risiko",
            "description": (
                "Gute Basis, die bestehenden Massnahmen sollten regelmässig überprüft werden."
            ),
        },
    },
    "offer_title": "Persönlicher IT-Sicherheitsbericht für Ihre Praxis",
    "offer_price": "CHF 49.-",
    "benefits": [
        "Übersichtliche Einordnung Ihrer IT-Sicherheitslage",
        "Priorisierte Massnahmen mit Fokus auf Patientendaten",
        "Verständlich für Praxen ohne eigene IT-Abteilung",
        "Berücksichtigung typischer Abläufe in Arztpraxen",
    ],
    "audience": (
        "Dieser Bericht richtet sich an Arztpraxen und kleinere medizinische "
        "Einrichtungen ohne eigene IT-Abteilung."
    ),
    "scope": (
        "Der Bericht enthält priorisierte Massnahmen und klare Empfehlungen "
        "zur Verbesserung der IT-Sicherheit."
    ),
    "value_explanation": (
        "Der Bericht wurde speziell für medizinische Einrichtungen in der Schweiz "
        "entwickelt. Er ersetzt keine Fachberatung, bietet jedoch eine fundierte "
        "und unabhängige Ersteinschätzung."
    ),
    "price_context": (
        "Zum Vergleich: Bereits eine kurze IT-Sicherheitsberatung verursacht "
        "häufig Kosten im dreistelligen Bereich. Dieser Bericht ermöglicht eine "
        "strukturierte Standortbestimmung zu einem fixen, transparenten Preis."
    ),
    "payment_note": (
        "Die Rechnung wird ohne Mehrwertsteuer ausgestellt "
        "(nicht mehrwertsteuerpflichtig)."
    ),
    "delivery": (
        "Nach Zahlungseingang erhalten Sie Ihren persönlichen PDF-Bericht per E-Mail "
        "(in der Regel innerhalb von 24 Stunden)."
    ),
    "preview_note": "Hinweis: Dies ist eine Vorschau-Version.",
    "preview_cta": "PDF-Bericht anzeigen",
}

# Define report page texts =>
REPORT = {
    "print_cta": "Als PDF speichern",
    "date_label": "Datum",
    "score_title": "IT-Sicherheitsbewertung",
    "sections": {
        "classification": "Einordnung",
        "measures": "Empfohlene Massnahmen",
        "next_steps": "Nächste Schritte",
    },
    "risk_levels": {
        "high": (
            "Erhöhtes Risiko - es bestehen relevante Schwachstellen, "
            "die überprüft und priorisiert adressiert werden sollten."
        ),
        "medium": (
            "Mittleres Risiko - die wichtigsten Punkte sollten zeitnah umgesetzt werden."
        ),
        "low": (
            "Geringes Risiko - gute Grundlagen, die bestehenden Massnahmen "
            "sollten regelmässig überprüft werden."
        ),
    },
    "unclear": {
        "title": "Unklare Risikolage",
        "description": (
            "Auf Basis Ihrer Angaben konnte keine zuverlässige Bewertung erstellt werden."
        ),
        "note": (
            "Viele Fragen wurden als „nicht zutreffend“ beantwortet. "
            "Das Ergebnis ist daher nur eingeschränkt aussagekräftig."
        ),
        "recommendation": (
            "Beantworten Sie den Check erneut mit möglichst konkreten Angaben, "
            "um eine aussagekräftige Bewertung zu erhalten."
        ),
    },
    "no_findings": {
        "title": "Sehr gut.",
        "description": (
            "In diesem Check wurden keine kritischen Schwachstellen festgestellt."
        ),
        "maintenance": (
            "Wir empfehlen, die bestehenden Sicherheitsmassnahmen beizubehalten "
            "und den Check mindestens einmal pro Jahr oder nach relevanten "
            "Änderungen erneut durchzuführen."
        ),
        "examples": [
            "Regelmässige Software-Updates sicherstellen",
            "Backups weiterhin regelmässig testen",
            "Mitarbeitende fortlaufend für Phishing sensibilisieren",
        ],
    },
    "findings_intro": (
        "Die folgenden Massnahmen haben den grössten Einfluss auf Ihre IT-Sicherheit:"
    ),
    "priority_label": "Priorität",
    "next_steps": {
        "orientation": (
            "Dieser Bericht bietet eine erste Orientierung zur Verbesserung "
            "der IT-Sicherheit und ersetzt keine individuelle Fachberatung."
        ),
        "feasibility": (
            "Für viele Arztpraxen und kleinere medizinische Einrichtungen "
            "reicht es aus, diese Punkte intern schrittweise umzusetzen."
        ),
    },
}

# Define report_pdf page texts =>
REPORT_PDF = {
    "title_suffix": "IT-Sicherheitsbericht",
    "header_suffix": "IT-Sicherheitsbericht für medizinische Einrichtungen",
    "score_label": "Bewertung zum Schutz sensibler Patientendaten",
    "generated_on": "Erstellt am",
    "footer_note": (
        "Dieser Bericht dient ausschliesslich als Orientierungshilfe "
        "und ersetzt keine individuelle IT- oder Rechtsberatung."
    ),
}


# Define scope and positioning =>
# Used in:
# - Result page explanation
# - PDF introduction
# - Emails or Invoices
SCOPE = {
    "target_audience": (
        "Arztpraxen und kleinere medizinische Einrichtungen "
        "ohne eigene IT-Abteilung."
    ),
    "positioning": (
        "Der MedSecure-Check bietet eine strukturierte "
        "Ersteinschätzung der IT-Sicherheitslage."
    ),
}

# Define disclaimers =>
# Do not rewrite these in templates. Ever.
DISCLAIMERS = {
    "website": (
        "Dieser Check stellt keine rechtliche, regulatorische "
        "oder medizinische Beratung dar."
    ),
    "report": (
        "Dieser Bericht dient ausschliesslich als Orientierungshilfe "
        "und ersetzt keine individuelle IT-, Rechts- oder Fachberatung."
    ),
}

# Define payment and delivery wording =>
# This avoids:
# - Emotional selling
# - Justification drift
# - Defensive pricing language
PAYMENT = {
    "price": "CHF 49.-",
    "method": "Zahlung per Rechnung / Banküberweisung",
    "delivery": (
        "Nach Zahlungseingang erhalten Sie Ihren persönlichen "
        "PDF-Bericht in der Regel innerhalb von 24 Stunden."
    ),
    "justification": (
        "Der Bericht ermöglicht eine strukturierte Standortbestimmung "
        "zu einem fixen, transparenten Preis."
    ),
}
