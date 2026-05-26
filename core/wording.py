"""
MedSecure-Check Centralized Multilingual Store.
Locale: de-CH, fr-CH, it-CH
"""

LEXICON = {
    "de-CH": {
        # --- Questions for pre-audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Verwenden Sie starke und einzigartige Passwörter für Ihre geschäftlichen Konten?",
                "remedy": "Verwenden Sie einen Passwort-Manager und ein separates Passwort für jedes Konto.",
                "pillar": "Vertraulichkeit",
                "standard": "NCSC 5.1.1",
            },
            "q2": {
                "text": "Wird in der Praxis ein Passwort-Manager eingesetzt?",
                "remedy": "Führen Sie einen anerkannten Passwort-Manager für sich und Ihre Mitarbeitenden ein.",
                "pillar": "Vertraulichkeit",
                "standard": "NCSC 5.1.1",
            },
            "q3": {
                "text": "Werden Zugriffsrechte beim Austritt von Mitarbeitenden umgehend entzogen?",
                "remedy": "Definieren Sie klare Regeln für die Änderung von Zugängen bei Personalwechseln.",
                "pillar": "Rückverfolgbarkeit & Zugriff",
                "standard": "NCSC 5.1.2",
            },
            "q4": {
                "text": "Sind die Patientendaten auf Ihren Speichermedien verschlüsselt?",
                "remedy": "Nutzen Sie Verschlüsselungssysteme (wie BitLocker oder FileVault), um Daten im Ruhezustand zu schützen.",
                "pillar": "Integrität & Schutz",
                "standard": "DSG Art. 8",
            },
            "q5": {
                "text": "Führen Sie regelmässig automatische Backups Ihrer Daten durch?",
                "remedy": "Konfigurieren Sie tägliche automatische Backups und bewahren Sie mindestens eine Kopie extern auf.",
                "pillar": "Verfügbarkeit",
                "standard": "NCSC 5.4.1",
            },
            "q6": {
                "text": "Werden die Datensicherungen (Backups) regelmässig getestet?",
                "remedy": "Prüfen Sie mindestens einmal pro Quartal, ob Ihre Backups korrekt wiederhergestellt werden können.",
                "pillar": "Verfügbarkeit",
                "standard": "NCSC 5.4.2",
            },
            "q7": {
                "text": "Ist auf allen Computern ein aktueller Virenschutz installiert?",
                "remedy": "Installieren Sie eine anerkannte 'Endpoint'-Schutzlösung und stellen Sie sicher, dass diese ständig aktualisiert wird.",
                "pillar": "Integrität",
                "standard": "NCSC 5.2.1",
            },
            "q8": {
                "text": "Ist das Patienten-WLAN vom internen Praxisnetzwerk getrennt?",
                "remedy": "Richten Sie ein separates 'Gast-WLAN' ein, um Patienten vom medizinischen Netzwerk zu isolieren.",
                "pillar": "Netzwerkschutz",
                "standard": "NCSC 5.2.3",
            },
            "q9": {
                "text": "Werden Software-Updates automatisch installiert?",
                "remedy": "Aktivieren Sie automatische Updates für das Betriebssystem und die medizinische Software.",
                "pillar": "Integrität",
                "standard": "NCSC 5.2.2",
            },
            "q10": {
                "text": "Verwenden Sie die Zwei-Faktor-Authentisierung (2FA) für Ihre E-Mails?",
                "remedy": "Aktivieren Sie 2FA (SMS, App) für alle geschäftlichen Cloud- und E-Mail-Zugänge.",
                "pillar": "Vertraulichkeit",
                "standard": "NCSC 5.1.1",
            },
        },
        # --- Product Identity ---
        "PRODUCT": {
            "name": "MedSecure-Check",
            "short_name": "MedSecure-Check",
            "report_name": "IT-Sicherheitsbericht",
            "tagline": "IT-Sicherheitscheck für Arztpraxen in der Schweiz",
            "short_description": (
                "Ein strukturierter IT-Sicherheits-Check für Arztpraxen "
                "und kleinere medizinische Einrichtungen in der Schweiz."
            ),
        },
        # --- Landing Page Content ---
        "LANDING": {
            "headline": "IT-Sicherheit für Arztpraxen - verständlich geprüft",
            "intro": "Ein strukturierter IT-Sicherheits-Check für Arztpraxen und medizinische Einrichtungen in der Schweiz.",
            "promise": "In wenigen Minuten erhalten Sie eine erste Einschätzung Ihrer Datensicherheits- und IT-Risiken.",
            "value_statement": "Die Auswertung ist verständlich aufbereitet, sachlich formuliert und erfolgt ohne kommerziellen Verkaufsansatz.",
            "price_label": "CHF 49.-",
            "cta": "IT-Sicherheits-Check starten",
        },
        # --- Audit Interface --
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
        # --- Risk Classifications (UI & PDF) ---
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
        # --- Results & Sales Page ---
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
            "cta_button": "Vollständigen Bericht jetzt freischalten (Stripe)",
            "inconclusive": {
                "label": "Hinweis",
                "text": "Ihr Audit enthält zu viele 'N/A' Antworten...",
                "button": "Audit vervollständigen",
            },
            "delivery": "Sofortiger Download: Nach erfolgreicher Zahlung wird Ihr PDF-Bericht umgehend freigeschaltet.",
            "payment_note": "Einmalzahlung für die vollständige Auswertung",
            "preview_cta": "PDF-Bericht anzeigen",
        },
        # --- Payment successful ---
        "SUCCESS": {
            "title": "Zahlung Erfolgreich",
            "message": "Vielen Dank, Ihr Bericht wurde freigeschaltet.",
            "transaction_prefix": "Die Transaktion für",
            "transaction_suffix": "wurde erfolgreich abgeschlossen.",
            "download_button": "Bericht jetzt als PDF herunterladen",
            "invoice_note": "Eine Kopie der Rechnung wird für Ihre Unterlagen erstellt.",
            "back_home": "Zurück zur Startseite",
        },
        # --- Report  ---
        "REPORT": {
            "print_cta": "Als PDF speichern",
            "date_label": "Datum",
            "assessment_title": "IT-Sicherheitsklassifizierung",
            "sections": {
                "classification": "Bewertung",
                "measures": "Empfohlene Massnahmen",
                "next_steps": "Nächste Schritte",
                "table_a_title": 'Tabelle A: Umgesetzte technische Massnahmen (Der "Schutzschild")',
                "table_b_title": 'Tabelle B: Erforderlicher Verbesserungsplan (Die "Roadmap")',
            },
            "table_headers": {
                "pillar": "Säule",
                "maturity": "Reifegrad",
                "status": "Status",
                "priority": "Priorität",
                "gap": "Identifizierte Lücke / Standard",
                "remedy": "Empfohlene Abhilfe",
            },
            "status_labels": {
                "optimal": "Optimal",
                "partial": "Teilweise",
                "review": "Überprüfen",
                "important": "WICHTIG",
                "shield_intro": "Die folgende Tabelle fasst die Sicherheitsbereiche zusammen, in denen Ihre Praxis gemäss NCSC-Standards Sorgfalt walten lässt.",
            },
            "next_steps": {
                "orientation": "Notieren Sie hier Ihre geplanten nächsten Schritte oder Anmerkungen für Ihr Team:",
            },
            "unclear": {
                "title": "Unklare Risikolage",
                "description": "Auf Basis Ihrer Angaben konnte keine zuverlässige Bewertung erstellt werden.",
                "note": "Viele Fragen wurden als „nicht zutreffend“ beantwortet.",
            },
            "findings_intro": "Die folgenden Massnahmen haben den grössten Einfluss auf Ihre IT-Sicherheit:",
            "score_label": "Ihre Bewertung",
            "measure_label": "Massnahme",
            "priority_label": "PRIORITÄT",
            "priorities": {"high": "HOCH", "standard": "STANDARD"},
            "no_findings": {
                "title": "Keine kritischen Schwachstellen identifiziert",
                "description": "Herzlichen Glückwunsch! Auf Basis Ihrer Antworten wurden keine kritischen Sicherheitslücken festgestellt. Ihre aktuelle Konfiguration entspricht den gängigen Best Practices.",
            },
            "executive_summary": "Basierend auf Ihren Antworten hat Ihre Praxis {percentage}% der technischen Massnahmen umgesetzt, die nach Schweizer Recht erforderlich sind.",
            "status_implemented": "Umgesetzt",
            "status_improvement": "Verbesserungsbedarf",
        },
        # --- PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "IT-Sicherheitsbericht",
            "header_suffix": "IT-Sicherheitsbericht für medizinische Einrichtungen",
            "generated_on": "Bewertung basierend auf Angaben vom",
            "footer_note": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT- oder Rechtsberatung.",
            "page": "Seite",
            "of": "von",
            "filename_prefix": "Bericht",
            "methodology_label": "Methodik",
            "methodology_text": (
                "Diese Bewertung folgt den 'Minimalstandards für Cybersicherheit' des "
                "Nationalen Zentrums für Cybersicherheit (NCSC) und orientiert sich an den "
                "technischen Anforderungen von Art. 8 nDSG."
            ),
        },
        # --- Legal & Positioning ---
        "DISCLAIMERS": {
            "website": "Dieser Check stellt keine rechtliche, regulatorische oder medizinische Beratung dar.",
            "report": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT-, Rechts- oder Fachberatung.",
            "non_certification": (
                "Dieser Bericht stellt eine technische Selbsteinschätzung dar und ist keine "
                "offizielle Zertifizierung der Konformität mit dem DSG oder den NCSC-Standards."
            ),
        },
        # --- Paymeent ---
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Kreditkarte / Stripe",
            "delivery": "Sofortiger Zugriff nach erfolgreicher Zahlung.",
        },
        # --- Invoice / Receipt (de-CH) ---
        "INVOICE": {
            "title": "ZAHLUNGSBESTÄTIGUNG",
            "date_label": "Datum",
            "number_label": "Bestellnummer",
            "service_label": "Leistung",
            "amount_label": "Betrag",
            "description_suffix": "(Individuelle Analyse)",
            "total_label": "Gesamtbetrag (inkl. MwSt)",
            "status_paid": "BEZAHLT",
            "thanks_message": "Vielen Dank für Ihr Vertrauen. Dieses Dokument dient als Zahlungsbeleg.",
            "vat_note": "Nicht MWST-pflichtig.",
            "generated_on": "Automatisch generiert am",
            "filename_prefix": "Quittung",
        },
        # --- Email Templates ---
        "EMAIL": {
            "subject": "Ihr DSG-Konformitätsbericht - MedSecure",
            "body": (
                "Guten Tag,\n\n"
                "Vielen Dank, dass Sie MedSecure verwendet haben, um die Cyber-Sicherheit Ihrer Praxis zu überprüfen.\n\n"
                "Im Anhang dieser E-Mail finden Sie:\n"
                "1. Ihren detaillierten technischen Audit-Bericht, abgestimmt auf die Anforderungen des neuen DSG und die NCSC-Standards.\n"
                "2. Ihren Beleg über die erfolgte Zahlung.\n\n"
                "Sollten Sie Fragen zu den in Ihrem Fahrplan empfohlenen Massnahmen haben, steht Ihnen unser Team "
                "jederzeit gerne zur Verfügung.\n\n"
                "Freundliche Grüsse,\n"
                "Ihr MedSecure Schweiz Team"
            ),
        },
    },
    # ---- SWISS FRENCH ---
    "fr-CH": {
        # --- Questions for pre-audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Utilisez-vous des mots de passe forts et uniques pour vos comptes professionnels ?",
                "remedy": "Utilisez un gestionnaire de mots de passe et un mot de passe distinct pour chaque compte.",
                "pillar": "Confidentialité",
                "standard": "NCSC 5.1.1",
            },
            "q2": {
                "text": "Utilisez-vous un gestionnaire de mots de passe au sein du cabinet ?",
                "remedy": "Mettez en place un gestionnaire de mots de passe reconnu pour vous-même et vos collaborateurs.",
                "pillar": "Confidentialité",
                "standard": "NCSC 5.1.1",
            },
            "q3": {
                "text": "Les accès sont-ils révoqués lors du départ d'un collaborateur ?",
                "remedy": "Définissez des règles claires pour le changement des accès lors de changements de personnel.",
                "pillar": "Traçabilité & Accès",
                "standard": "NCSC 5.1.2",
            },
            "q4": {
                "text": "Les données des patients sont-elles chiffrées sur vos supports de stockage ?",
                "remedy": "Utilisez des systèmes de chiffrement (type BitLocker ou FileVault) pour protéger les données au repos.",
                "pillar": "Intégrité & Protection",
                "standard": "LPD Art. 8",
            },
            "q5": {
                "text": "Effectuez-vous régulièrement des sauvegardes automatiques de vos données ?",
                "remedy": "Configurez des sauvegardes automatiques quotidiennes et conservez au moins une copie hors site.",
                "pillar": "Disponibilité",
                "standard": "NCSC 5.4.1",
            },
            "q6": {
                "text": "Les sauvegardes (backups) sont-elles testées régulièrement ?",
                "remedy": "Testez au moins une fois par trimestre si vos sauvegardes peuvent être restaurées correctement.",
                "pillar": "Disponibilité",
                "standard": "NCSC 5.4.2",
            },
            "q7": {
                "text": "Une protection antivirus à jour est-elle installée sur tous les postes ?",
                "remedy": "Installez une solution 'Endpoint' reconnue et assurez-vous qu'elle soit constamment mise à jour.",
                "pillar": "Intégrité",
                "standard": "NCSC 5.2.1",
            },
            "q8": {
                "text": "Le Wi-Fi destiné aux patients est-il séparé du réseau interne du cabinet ?",
                "remedy": "Configurez un réseau Wi-Fi 'Invité' distinct pour isoler les patients du réseau médical.",
                "pillar": "Protection Réseau",
                "standard": "NCSC 5.2.3",
            },
            "q9": {
                "text": "Les mises à jour logicielles sont-elles installées automatiquement ?",
                "remedy": "Activez les mises à jour automatiques pour le système d'exploitation et les logiciels médicaux.",
                "pillar": "Intégrité",
                "standard": "NCSC 5.2.2",
            },
            "q10": {
                "text": "Utilisez-vous l'authentification à deux facteurs (2FA) pour vos e-mails ?",
                "remedy": "Activez la 2FA (SMS, Application) pour tous les accès cloud et e-mail professionnels.",
                "pillar": "Confidentialité",
                "standard": "NCSC 5.1.1",
            },
        },
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
            "cta_button": "Débloquer le rapport complet maintenant (Stripe)",  # This fixes your button
            "inconclusive": {
                "label": "Remarque",
                "text": "Votre audit contient trop de réponses 'N/A' pour une évaluation précise.",
                "button": "Compléter l'audit",
            },
            "delivery": "Téléchargement immédiat : après paiement, votre rapport PDF est débloqué instantanément.",
            "payment_note": "Paiement unique pour l'évaluation complète",
            "preview_cta": "Afficher le rapport PDF",
        },
        # ---- Payment successful ---
        "SUCCESS": {
            "title": "Paiement réussi",
            "message": "Merci, votre rapport a été débloqué.",
            "transaction_prefix": "La transaction pour",
            "transaction_suffix": "a été complétée avec succès.",
            "download_button": "Télécharger le rapport PDF maintenant",
            "invoice_note": "Une copie de la facture sera générée pour vos dossiers.",
            "back_home": "Retour à l'accueil",
        },
        # --- Report ---
        "REPORT": {
            "print_cta": "Enregistrer en PDF",
            "date_label": "Date",
            "assessment_title": "Classification de la sécurité informatique",
            "sections": {
                "classification": "Évaluation",
                "measures": "Mesures recommandées",
                "next_steps": "Prochaines étapes",
                "table_a_title": 'Tableau A : Mesures Techniques en Place (Le "Bouclier")',
                "table_b_title": 'Tableau B : Plan d\'Amélioration Requis (La "Feuille de Route")',
            },
            "table_headers": {
                "pillar": "Pilier",
                "maturity": "Maturité",
                "status": "Statut",
                "priority": "Priorité",
                "gap": "Lacune Identifiée / Standard",
                "remedy": "Remède Préconisé",
            },
            "status_labels": {
                "optimal": "Optimal",
                "partial": "Partiel",
                "review": "À revoir",
                "important": "IMPORTANT",
                "shield_intro": "Le tableau suivant récapitule les domaines de sécurité où votre cabinet fait preuve de diligence conformément aux standards NCSC.",
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
            "score_label": "Votre évaluation",
            "measure_label": "Mesure",
            "priority_label": "PRIORITÉ",
            "priorities": {"high": "ÉLEVÉE", "standard": "STANDARD"},
            "no_findings": {
                "title": "Aucune lacune critique identifiée",
                "description": "Félicitations ! Sur la base de vos réponses, aucune faille de sécurité critique n'a été détectée. Votre configuration actuelle respecte les bonnes pratiques.",
            },
            "executive_summary": "Sur la base de vos réponses, votre cabinet a mis en œuvre {percentage}% des mesures techniques requises par le droit suisse.",
            "status_implemented": "Implémenté",
            "status_improvement": "À améliorer",
        },
        # ---  PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "Rapport de sécurité informatique",
            "header_suffix": "Rapport de sécurité informatique pour institutions médicales",
            "generated_on": "Évaluation basée sur les informations du",
            "footer_note": "Ce rapport sert exclusivement de guide d'orientation et ne remplace pas un conseil informatique ou juridique individuel.",
            "page": "Page",
            "of": "sur",
            "filename_prefix": "Rapport",
            "methodology_label": "Méthodologie",
            "methodology_text": (
                "Cette évaluation suit les 'Standards minimaux de cybersécurité' émis par le "
                "Centre national pour la cybersécurité (NCSC) et s'aligne sur les exigences "
                "techniques de l'Art. 8 LPD."
            ),
        },
        # --- Legal & Positioning ---
        "DISCLAIMERS": {
            "website": "Ce check-up ne constitue pas un conseil juridique, réglementaire ou médical.",
            "report": "Ce rapport sert exclusivement de guide d'orientation et ne remplace pas un conseil informatique, juridique ou technique individuel.",
            "non_certification": (
                "Ce rapport constitue une auto-évaluation technique et ne constitue pas "
                "une certification officielle de conformité à la LPD ou aux normes NCSC."
            ),
        },
        # ---Payment ---
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Paiement par carte de crédit / Stripe",
            "delivery": "Accès immédiat : votre rapport PDF est disponible dès la confirmation du paiement.",
        },
        # --- Invoice / Receipt ---
        "INVOICE": {
            "title": "QUITTANCE DE PAIEMENT",  # "Payment Receipt"
            "date_label": "Date",
            "number_label": "No de commande",
            "service_label": "Prestation",
            "amount_label": "Montant",
            "description_suffix": "(Analyse individuelle)",
            "total_label": "Montant total (TTC)",
            "status_paid": "PAYÉ",
            "thanks_message": "Merci de votre confiance. Ce document sert de justificatif de paiement.",
            "vat_note": "Non soumis à la TVA.",
            "generated_on": "Généré automatiquement le",
            "filename_prefix": "Quittance",
        },
        # --- Email Templates ---
        "EMAIL": {
            "subject": "Votre Rapport de Conformité nDSG - MedSecure",
            "body": (
                "Bonjour,\n\n"
                "Nous vous remercions d'avoir utilisé MedSecure pour évaluer la maturité cyber de votre cabinet.\n\n"
                "Vous trouverez en pièces jointes de cet e-mail :\n"
                "1. Votre rapport technique d'audit détaillé, aligné sur les exigences de la LPD et des standards NCSC.\n"
                "2. Votre quittance de paiement pour vos dossiers.\n\n"
                "Si vous avez des questions concernant les remèdes préconisés dans votre feuille de route, "
                "notre équipe reste à votre entière disposition.\n\n"
                "Cordiales salutations,\n"
                "L'équipe MedSecure Suisse"
            ),
        },
    },
    # --- SWISS ITALIAN ---
    "it-CH": {
        # --- Questions for pre-audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Utilizzate password forti e univoche per i vostri account professionali?",
                "remedy": "Utilizzate un gestore di password e una password distinta per ogni account.",
                "pillar": "Riservatezza",
                "standard": "NCSC 5.1.1",
            },
            "q2": {
                "text": "Utilizzate un gestore di password all'interno dello studio?",
                "remedy": "Implementate un gestore di password riconosciuto per voi e i vostri collaboratori.",
                "pillar": "Riservatezza",
                "standard": "NCSC 5.1.1",
            },
            "q3": {
                "text": "Gli accessi vengono revocati in caso di partenza di un collaboratore?",
                "remedy": "Definite regole chiare per la modifica degli accessi in caso di cambiamenti di personale.",
                "pillar": "Tracciabilità e Accesso",
                "standard": "NCSC 5.1.2",
            },
            "q4": {
                "text": "I dati dei pazienti sono crittografati sui vostri supporti di memoria?",
                "remedy": "Utilizzate sistemi di crittografia (come BitLocker o FileVault) per proteggere i dati a riposo.",
                "pillar": "Integrità e Protezione",
                "standard": "LPD Art. 8",
            },
            "q5": {
                "text": "Effettuate regolarmente backup automatici dei vostri dati?",
                "remedy": "Configurate backup automatici giornalieri e conservate almeno una copia fuori sede.",
                "pillar": "Disponibilità",
                "standard": "NCSC 5.4.1",
            },
            "q6": {
                "text": "I backup vengono testati regolarmente?",
                "remedy": "Verificate almeno una volta a trimestre se i vostri backup possono essere ripristinati correttamente.",
                "pillar": "Disponibilità",
                "standard": "NCSC 5.4.2",
            },
            "q7": {
                "text": "È installata una protezione antivirus aggiornata su tutti i computer?",
                "remedy": "Installate una soluzione di protezione 'Endpoint' riconosciuta e assicuratevi che sia costantemente aggiornata.",
                "pillar": "Integrità",
                "standard": "NCSC 5.2.1",
            },
            "q8": {
                "text": "Il Wi-Fi per i pazienti è separato dalla rete interna dello studio?",
                "remedy": "Configurate una rete Wi-Fi 'Ospiti' distinta per isolare i pazienti dalla rete medica.",
                "pillar": "Protezione della rete",
                "standard": "NCSC 5.2.3",
            },
            "q9": {
                "text": "Gli aggiornamenti software vengono installati automaticamente?",
                "remedy": "Attivate gli aggiornamenti automatici per il sistema operativo e i software medici.",
                "pillar": "Integrità",
                "standard": "NCSC 5.2.2",
            },
            "q10": {
                "text": "Utilizzate l'autenticazione a due fattori (2FA) per le vostre e-mail?",
                "remedy": "Attivate la 2FA (SMS, App) per tutti gli accessi cloud e e-mail professionali.",
                "pillar": "Riservatezza",
                "standard": "NCSC 5.1.1",
            },
        },
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
            "cta_button": "Sblocca il rapporto completo ora (Stripe)",
            "inconclusive": {
                "label": "Avviso",
                "title": "Valutazione non conclusiva",
                "text": "Il vostro audit contiene troppe risposte 'N/A' per una valutazione precisa.",
                "button": "Completare l'audit",
            },
            "delivery": "Download immediato: dopo il pagamento, il rapporto PDF sarà sbloccato istantaneamente.",
            "payment_note": "Pagamento unico per la valutazione completa",
            "preview_cta": "Visualizza il rapporto PDF",
        },
        # --- Payment successful ---
        "SUCCESS": {
            "title": "Pagamento riuscito",
            "message": "Grazie, il Suo rapporto è stato sbloccato.",
            "transaction_prefix": "La transazione per",
            "transaction_suffix": "è stata completata con successo.",
            "download_button": "Scarica il rapporto PDF ora",
            "invoice_note": "Una copia della fattura sarà generata per i Suoi archivi.",
            "back_home": "Torna alla pagina iniziale",
        },
        # --- Report  ---
        "REPORT": {
            "print_cta": "Salva in PDF",
            "date_label": "Data",
            "assessment_title": "Classificazione della sicurezza informatica",
            "sections": {
                "classification": "Valutazione",
                "measures": "Misure raccomandate",
                "next_steps": "Prossimi passi",
                "table_a_title": 'Tabella A: Misure tecniche implementate (Lo "Scudo")',
                "table_b_title": 'Tabella B: Piano di miglioramento richiesto (La "Roadmap")',
            },
            "table_headers": {
                "pillar": "Pilastro",
                "maturity": "Maturità",
                "status": "Stato",
                "priority": "Priorità",
                "gap": "Lacuna identificata / Standard",
                "remedy": "Rimedio raccomandato",
            },
            "status_labels": {
                "optimal": "Ottimale",
                "partial": "Parziale",
                "review": "Da rivedere",
                "important": "AVVISO",
                "shield_intro": "La seguente tabella riassume i settori di sicurezza in cui il vostro studio dimostra diligenza in conformità con gli standard NCSC.",
            },
            "next_steps": {
                "orientation": "Annotate qui i vostri prossimi passi pianificati o note per il vostro team:",
            },
            "unclear": {
                "title": "Situazione di rischio incerta",
                "description": "Sulla base dei dati forniti, non è stato possibile generare una valutazione affidabile.",
                "note": "Molte domande hanno ricevuto la risposta 'non applicabile'.",
            },
            "findings_intro": "Le seguenti misure hanno il maggiore impatto sulla vostra sicurezza informatica:",
            "score_label": "La vostra valutazione",
            "measure_label": "Misura",
            "priority_label": "PRIORITÀ",
            "priorities": {"high": "ELEVATA", "standard": "STANDARD"},
            "no_findings": {
                "title": "Nessuna lacuna critica identificata",
                "description": "Congratulazioni! Sulla base delle vostre risposte, non sono state rilevate falle di sicurezza critiche. La vostra configurazione attuale rispetta le buone pratiche.",
            },
            "executive_summary": "Sulla base delle vostre risposte, il vostro studio ha implementato il {percentage}% delle misure tecniche richieste dalla legislazione svizzera.",
            "status_implemented": "Implementato",
            "status_improvement": "Da migliorare",
        },
        # --- PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "Rapporto sulla sicurezza informatica",
            "header_suffix": "Rapporto sulla sicurezza informatica per strutture sanitarie",
            "generated_on": "Valutazione basata sui dati del",
            "footer_note": "Questo rapporto serve esclusivamente come guida orientativa e non sostituisce una consulenza informatica o legale individuale.",
            "page": "Pagina",
            "of": "di",
            "filename_prefix": "Rapporto",
            "methodology_label": "Metodologia",
            "methodology_text": (
                "Questa valutazione segue gli 'Standard minimi di cibersicurezza' emessi dal "
                "Centro nazionale per la cibersicurezza (NCSC) e si allinea ai requisiti "
                "tecnici dell'Art. 8 nLPD."
            ),
        },
        # --- Legal & Positioning ---
        "DISCLAIMERS": {
            "website": "Questo check non costituisce una consulenza legale, normativa o medica.",
            "report": "Questo rapporto serve esclusivamente come guida orientativa e non sostituisce una consulenza individuale informatica, legale o specialistica.",
            "non_certification": (
                "Questo rapporto costituisce un'autovalutazione tecnica e non rappresenta "
                "una certificazione ufficiale di conformità alla LPD o agli standard NCSC."
            ),
        },
        # --- Payment ---
        "PAYMENT": {
            "price": "CHF 49.-",
            "method": "Pagamento tramite carta di credito / Stripe",
            "delivery": "Accesso immediato: il rapporto PDF è disponibile subito dopo la conferma del pagamento.",
        },
        # --- Invoice / Receipt (it-CH) ---
        "INVOICE": {
            "title": "RICEVUTA DI PAGAMENTO",
            "date_label": "Data",
            "number_label": "No. d'ordine",
            "service_label": "Prestazione",
            "amount_label": "Importo",
            "description_suffix": "(Analisi individuale)",
            "total_label": "Importo totale (IVA incl.)",
            "status_paid": "PAGATO",
            "thanks_message": "Grazie per la fiducia. Questo documento funge da giustificativo di pagamento.",
            "vat_note": "Non soggetto a IVA.",
            "generated_on": "Generato automaticamente il",
            "filename_prefix": "Ricevuta",
        },
        # --- Email Templates ---
        "EMAIL": {
            "subject": "Il vostro Rapporto di Conformità nLPD - MedSecure",
            "body": (
                "Gentile Utente,\n\n"
                "La ringraziamo per aver utilizzato MedSecure per valutare la sicurezza informatica del Suo studio.\n\n"
                "In allegato a questa e-mail troverà:\n"
                "1. Il Suo rapporto tecnico di audit dettagliato, allineato ai requisiti della LPD e agli standard NCSC.\n"
                "2. La ricevuta di pagamento per la contabilità.\n\n"
                "Se ha domande relative alle soluzioni raccomandate nella Sua tabella di marcia, il nostro team "
                "rimane a Sua completa disposizione.\n\n"
                "Cordiali saluti,\n"
                "Il team MedSecure Svizzera"
            ),
        },
    },
}


# --- Helper function for the OS language of the user ---
def get_lexicon(lang: str = "de-CH"):
    """Fetch the correct language dictionary from core.wording"""
    # Fallback to German if the requested language doesn't exist
    return LEXICON.get(lang, LEXICON["de-CH"])


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
