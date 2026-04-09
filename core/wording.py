"""
MedSecure-Check Centralized Multilingual Store.
Locale: de-CH, fr-CH, it-CH
"""

LEXICON = {
    "de-CH": {
        "PRODUCT": {
            "name": "MedSecure-Check",
            "short_name": "MedSecure-Check Schweiz",
            "report_name": "IT-Sicherheitsbericht",
            "tagline": "IT-Sicherheitscheck für Arztpraxen in der Schweiz",
            "short_description": (
                "Ein strukturierter IT-Sicherheits-Check für Arztpraxen "
                "und kleinere medizinische Einrichtungen in der Schweiz."
            ),
        },
        "LANDING": {
            "headline": "IT-Sicherheit für Arztpraxen - verständlich geprüft",
            "intro": "Ein strukturierter IT-Sicherheits-Check für Arztpraxen und medizinische Einrichtungen in der Schweiz.",
            "promise": "In wenigen Minuten erhalten Sie eine erste Einschätzung Ihrer Datensicherheits- und IT-Risiken.",
            "value_statement": "Die Auswertung ist verständlich aufbereitet, sachlich formuliert und erfolgt ohne kommerziellen Verkaufsansatz.",
            "price_label": "CHF 49.-",
            "cta": "IT-Sicherheits-Check starten",
        },
        "AUDIT": {
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
        },
        "RISK_LEVELS": {
            "inconclusive": {
                "label": "Nicht bewertbar",
                "summary": "Es wurden zu viele Fragen mit 'N/A' beantwortet, um eine verlässliche Risikoanalyse zu erstellen.",
                "pdf_text": "Aufgrund der hohen Anzahl an nicht beantworteten Fragen (N/A) kann keine abschliessende Beurteilung der IT-Sicherheit vorgenommen werden. Eine detaillierte manuelle Überprüfung wird empfohlen.",
            },
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
        },
        "RESULT": {
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
            "delivery": "Sofortiger Download: Nach erfolgreicher Zahlung wird Ihr PDF-Bericht umgehend freigeschaltet.",
            "payment_note": "Einmalzahlung für die vollständige Auswertung",
            "preview_cta": "PDF-Bericht anzeigen",
        },
        "REPORT": {
            "print_cta": "Als PDF speichern",
            "date_label": "Datum",
            "assessment_title": "IT-Sicherheits-Einordnung",
            "sections": {
                "classification": "Einordnung",
                "measures": "Empfohlene Massnahmen",
                "next_steps": "Nächste Schritte",
            },
            "next_steps": {
                "orientation": "Notieren Sie hier Ihre nächsten geplanten Schritte oder Anmerkungen für Ihr Team:",
            },
            "unclear": {
                "title": "Unklare Risikolage",
                "description": "Auf Basis Ihrer Angaben konnte keine zuverlässige Bewertung erstellt werden.",
                "note": "Viele Fragen wurden als „nicht zutreffend“ beantwortet.",
            },
            "findings_intro": "Die folgenden Massnahmen haben den grössten Einfluss auf Ihre IT-Sicherheit:",
            "priority_label": "Priorität",
        },
        "REPORT_PDF": {
            "title_suffix": "IT-Sicherheitsbericht",
            "header_suffix": "IT-Sicherheitsbericht für medizinische Einrichtungen",
            "generated_on": "Bewertung basierend auf Angaben vom",
            "footer_note": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT- oder Rechtsberatung.",
        },
        "DISCLAIMERS": {
            "website": "Dieser Check stellt keine rechtliche, regulatorische oder medizinische Beratung dar.",
            "report": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT-, Rechts- oder Fachberatung.",
        },
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Kreditkarte / Stripe",
            "delivery": "Sofortiger Zugriff nach erfolgreicher Zahlung.",
        },
    },
    # ---- SWISS FRENCH ---
    "fr-CH": {
        # --- Product Identity ---
        "PRODUCT": {
            "name": "MedSecure-Check",
            "short_name": "MedSecure-Check Suisse",
            "report_name": "Rapport de sécurité informatique",
            "tagline": "Audit de sécurité IT pour les cabinets médicaux en Suisse",
            "short_description": (
                "Un audit structuré de sécurité informatique pour les cabinets médicaux "
                "et les petites institutions médicales en Suisse."
            ),
        },
        # --- Landing Page Content ---
        "LANDING": {
            "headline": "Sécurité informatique pour cabinets médicaux – un audit clair",
            "intro": "Un check-up structuré de la sécurité informatique pour les cabinets médicaux et les établissements de santé en Suisse.",
            "promise": "En quelques minutes, obtenez une première évaluation de vos risques informatiques et de la protection de vos données.",
            "value_statement": "L'évaluation est claire, formulée de manière factuelle et réalisée sans approche commerciale.",
            "price_label": "CHF 49.-",
            "cta": "Lancer l'audit de sécurité",
        },
        # --- Audit Interface ---
        "AUDIT": {
            "title": "Audit structuré de sécurité informatique pour institutions médicales (env. 5 minutes)",
            "fields": {
                "business_name": "Nom du cabinet ou de l'organisation",
                "email": "Adresse e-mail professionnelle",
            },
            "answers": {
                "yes": "Oui",
                "no": "Non",
                "na": "Non applicable",
            },
            "submit": "Générer l'évaluation de sécurité",
        },
        # --- Risk Classifications (UI & PDF) ---
        "RISK_LEVELS": {
            "inconclusive": {
                "label": "Non évaluable",
                "summary": "Trop de questions ont reçu la réponse 'N/A' pour établir une analyse de risques fiable.",
                "pdf_text": "En raison du nombre élevé de questions sans réponse (N/A), aucune évaluation définitive de la sécurité informatique ne peut être effectuée. Une vérification manuelle détaillée est recommandée.",
            },
            "high": {
                "label": "Risque élevé",
                "summary": "Des vulnérabilités pertinentes existent et doivent être examinées et traitées prioritairement.",
                "pdf_text": "La situation actuelle de la sécurité informatique présente des vulnérabilités importantes. Une révision structurée et la mise en œuvre prioritaire de mesures appropriées sont recommandées.",
            },
            "medium": {
                "label": "Risque moyen",
                "summary": "Les mesures les plus importantes doivent être mises en œuvre de manière prioritaire.",
                "pdf_text": "La sécurité informatique est globalement solide, mais présente un potentiel d'amélioration dans certains domaines spécifiques.",
            },
            "low": {
                "label": "Risque faible",
                "summary": "De bonnes bases sont en place. Une vérification régulière est recommandée.",
                "pdf_text": "Les bases de la sécurité informatique sont largement établies. Une vérification régulière et une mise à jour des mesures sont recommandées.",
            },
        },
        # --- Results & Sales Page ---
        "RESULT": {
            "title": "Votre évaluation",
            "offer_title": "Rapport de sécurité personnalisé pour votre cabinet",
            "offer_price": "CHF 49.-",
            "benefits": [
                "Classification claire de votre situation de sécurité informatique",
                "Mesures prioritaires axées sur les données des patients",
                "Compréhensible pour les cabinets sans département informatique",
                "Prise en compte des processus typiques des cabinets médicaux",
            ],
            "value_explanation": "Le rapport a été spécialement conçu pour les institutions médicales en Suisse. Il ne remplace pas un conseil spécialisé, mais offre une première évaluation indépendante et fondée.",
            "delivery": "Téléchargement immédiat : après paiement, votre rapport PDF est débloqué instantanément.",
            "payment_note": "Paiement unique pour l'évaluation complète",
            "preview_cta": "Afficher le rapport PDF",
        },
        # --- Report & PDF Generation Content ---
        "REPORT": {
            "print_cta": "Enregistrer en PDF",
            "date_label": "Date",
            "assessment_title": "Classification de la sécurité informatique",
            "sections": {
                "classification": "Évaluation",
                "measures": "Mesures recommandées",
                "next_steps": "Prochaines étapes",
            },
            "next_steps": {
                "orientation": "Notez ici vos prochaines étapes prévues ou des remarques pour votre équipe :",
            },
            "unclear": {
                "title": "Situation de risque incertaine",
                "description": "Sur la base de vos indications, aucune évaluation fiable n'a pu être établie.",
                "note": "De nombreuses questions ont été marquées comme 'non applicables'.",
            },
            "findings_intro": "Les mesures suivantes ont le plus grand impact sur votre sécurité informatique :",
            "priority_label": "Priorité",
        },
        "REPORT_PDF": {
            "title_suffix": "Rapport de sécurité informatique",
            "header_suffix": "Rapport de sécurité informatique pour institutions médicales",
            "generated_on": "Évaluation basée sur les informations du",
            "footer_note": "Ce rapport sert exclusivement de guide d'orientation et ne remplace pas un conseil informatique ou juridique individuel.",
        },
        # --- Legal & Positioning ---
        "DISCLAIMERS": {
            "website": "Ce check-up ne constitue pas un conseil juridique, réglementaire ou médical.",
            "report": "Ce rapport sert exclusivement de guide d'orientation et ne remplace pas un conseil informatique, juridique ou technique individuel.",
        },
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Paiement par carte de crédit / Stripe",
            "delivery": "Accès immédiat : votre rapport PDF est disponible dès la confirmation du paiement.",
        },
    },
    # --- SWISS ITALIAN ---
    "it-CH": {
        # --- Product Identity ---
        "PRODUCT": {
            "name": "MedSecure-Check",
            "short_name": "MedSecure-Check Svizzera",
            "report_name": "Rapporto sulla sicurezza informatica",
            "tagline": "Check della sicurezza informatica per studi medici in Svizzera",
            "short_description": (
                "Un controllo strutturato della sicurezza informatica per studi medici "
                "e piccole strutture sanitarie in Svizzera."
            ),
        },
        # --- Landing Page Content ---
        "LANDING": {
            "headline": "Sicurezza informatica per studi medici – verificata in modo chiaro",
            "intro": "Un check-up strutturato della sicurezza informatica per studi medici e strutture sanitarie in Svizzera.",
            "promise": "In pochi minuti otterrete una prima valutazione dei rischi informatici e della protezione dei dati.",
            "value_statement": "La valutazione è chiara, formulata in modo obiettivo e senza finalità commerciali.",
            "price_label": "CHF 49.-",
            "cta": "Avvia il check della sicurezza",
        },
        # --- Audit Interface ---
        "AUDIT": {
            "title": "Check strutturato della sicurezza informatica per strutture sanitarie (ca. 5 minuti)",
            "fields": {
                "business_name": "Nome dello studio o dell'organizzazione",
                "email": "Indirizzo e-mail aziendale",
            },
            "answers": {
                "yes": "Sì",
                "no": "No",
                "na": "Non applicabile",
            },
            "submit": "Genera valutazione della sicurezza",
        },
        # --- Risk Classifications (UI & PDF) ---
        "RISK_LEVELS": {
            "inconclusive": {
                "label": "Non valutabile",
                "summary": "Sono state fornite troppe risposte 'N/A' per generare un'analisi dei rischi affidabile.",
                "pdf_text": "A causa dell'elevato numero di domande senza risposta (N/A), non è possibile effettuare una valutazione definitiva della sicurezza informatica. Si raccomanda una verifica manuale dettagliata.",
            },
            "high": {
                "label": "Rischio elevato",
                "summary": "Esistono vulnerabilità rilevanti che dovrebbero essere verificate e affrontate con priorità.",
                "pdf_text": "L'attuale situazione della sicurezza informatica presenta vulnerabilità rilevanti. Si raccomanda una revisione strutturata e l'attuazione prioritaria di misure adeguate.",
            },
            "medium": {
                "label": "Rischio medio",
                "summary": "Le misure più importanti dovrebbero essere attuate in modo prioritario.",
                "pdf_text": "La situazione della sicurezza informatica è complessivamente solida, ma presenta margini di miglioramento in singole aree.",
            },
            "low": {
                "label": "Rischio basso",
                "summary": "Sono presenti buone basi. Si raccomanda una verifica regolare.",
                "pdf_text": "Le basi della sicurezza informatica sono ampiamente stabilite. Si raccomanda una verifica regolare e l'aggiornamento delle misure.",
            },
        },
        # --- Results & Sales Page ---
        "RESULT": {
            "title": "La vostra valutazione",
            "offer_title": "Rapporto sulla sicurezza personalizzato per il vostro studio",
            "offer_price": "CHF 49.-",
            "benefits": [
                "Classificazione chiara della vostra sicurezza informatica",
                "Misure prioritarie focalizzate sui dati dei pazienti",
                "Comprensibile per studi senza un reparto IT dedicato",
                "Considerazione dei processi tipici degli studi medici",
            ],
            "value_explanation": "Il rapporto è stato sviluppato specificamente per le strutture sanitarie in Svizzera. Non sostituisce una consulenza specialistica, ma offre una prima valutazione indipendente.",
            "delivery": "Download immediato: dopo il pagamento, il rapporto PDF sarà sbloccato istantaneamente.",
            "payment_note": "Pagamento unico per la valutazione completa",
            "preview_cta": "Visualizza il rapporto PDF",
        },
        # --- Report & PDF Generation Content ---
        "REPORT": {
            "print_cta": "Salva come PDF",
            "date_label": "Data",
            "assessment_title": "Classificazione della sicurezza informatica",
            "sections": {
                "classification": "Valutazione",
                "measures": "Misure raccomandate",
                "next_steps": "Prossimi passi",
            },
            "next_steps": {
                "orientation": "Annotate qui i prossimi passi pianificati o le note per il vostro team:",
            },
            "unclear": {
                "title": "Situazione di rischio incerta",
                "description": "Sulla base dei dati forniti, non è stato possibile generare una valutazione affidabile.",
                "note": "Molte domande hanno ricevuto la risposta 'non applicabile'.",
            },
            "findings_intro": "Le seguenti misure hanno il maggiore impatto sulla vostra sicurezza informatica:",
            "priority_label": "Priorità",
        },
        "REPORT_PDF": {
            "title_suffix": "Rapporto sulla sicurezza informatica",
            "header_suffix": "Rapporto sulla sicurezza informatica per strutture sanitarie",
            "generated_on": "Valutazione basata sui dati del",
            "footer_note": "Questo rapporto serve esclusivamente come guida orientativa e non sostituisce una consulenza informatica o legale individuale.",
        },
        # --- Legal & Positioning ---
        "DISCLAIMERS": {
            "website": "Questo check non costituisce una consulenza legale, normativa o medica.",
            "report": "Questo rapporto serve esclusivamente come guida orientativa e non sostituisce una consulenza individuale informatica, legale o specialistica.",
        },
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Pagamento tramite carta di credito / Stripe",
            "delivery": "Accesso immediato: il rapporto PDF è disponibile subito dopo la conferma del pagamento.",
        },
    },
}

# --- Default Pointers for Legacy Support ---
PRODUCT = LEXICON["de-CH"]["PRODUCT"]
LANDING = LEXICON["de-CH"]["LANDING"]
AUDIT = LEXICON["de-CH"]["AUDIT"]
RESULT = LEXICON["de-CH"]["RESULT"]
REPORT = LEXICON["de-CH"]["REPORT"]
REPORT_PDF = LEXICON["de-CH"]["REPORT_PDF"]
DISCLAIMERS = LEXICON["de-CH"]["DISCLAIMERS"]
RISK_LEVELS = LEXICON["de-CH"]["RISK_LEVELS"]
PAYMENT = LEXICON["de-CH"]["PAYMENT"]
