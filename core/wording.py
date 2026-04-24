"""
MedSecure-Check Centralized Multilingual Store.
Locale: de-CH, fr-CH, it-CH
"""

LEXICON = {
    "de-CH": {
        # --- Questions for audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Verwenden Sie für geschäftliche Konten starke und einzigartige Passwörter?",
                "remedy": "Verwenden Sie einen Passwort-Manager und für jedes Konto ein eigenes Passwort.",
            },
            "q2": {
                "text": "Nutzen Sie einen Passwort-Manager?",
                "remedy": "Setzen Sie einen etablierten Passwort-Manager für sich und Ihre Mitarbeitenden ein.",
            },
            "q3": {
                "text": "Werden Passwörter bei Mitarbeiteraustritt oder Verdacht auf Missbrauch geändert?",
                "remedy": "Definieren Sie klare Regeln für Passwortänderungen bei Personalwechsel oder Sicherheitsvorfällen.",
            },
            "q4": {
                "text": "Werden Kunden- und Patientendaten sicher gespeichert?",
                "remedy": "Speichern Sie nur notwendige Personendaten und verwenden Sie wenn möglich verschlüsselte Systeme.",
            },
            "q5": {
                "text": "Erstellen Sie regelmässig automatische Backups Ihrer Geschäftsdaten?",
                "remedy": "Richten Sie tägliche automatische Backups ein und bewahren Sie mindestens eine Kopie extern auf.",
            },
            "q6": {
                "text": "Werden Backups regelmässig getestet?",
                "remedy": "Testen Sie mindestens vierteljährlich, ob sich Ihre Backups wiederherstellen lassen.",
            },
            "q7": {
                "text": "Ist auf allen Computern ein aktueller Viren- oder Endpunktschutz installiert?",
                "remedy": "Installieren Sie einen etablierten Endpunktschutz und halten Sie diesen aktuell.",
            },
            "q8": {
                "text": "Ist das Kunden-WLAN vom internen Geschäftsnetz getrennt?",
                "remedy": "Richten Sie ein separates Gäste-WLAN ein.",
            },
            "q9": {
                "text": "Werden Software-Updates und Sicherheitsupdates regelmässig installiert?",
                "remedy": "Aktivieren Sie automatische Updates oder planen Sie regelmässige Wartungsfenster ein.",
            },
            "q10": {
                "text": "Nutzen Sie Zwei-Faktor-Authentifizierung (2FA) für E-Mail- und Administrationskonten?",
                "remedy": "Aktivieren Sie 2FA für E-Mail-, Cloud- und Administrationszugänge.",
            },
        },
        # --- Product Identity ---
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
            "score_label": "Ihre Bewertung",
            "measure_label": "Massnahme",
            "priority_label": "PRIORITÄT",
            "priorities": {"high": "HOCH", "standard": "STANDARD"},
        },
        # --- PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "IT-Sicherheitsbericht",
            "header_suffix": "IT-Sicherheitsbericht für medizinische Einrichtungen",
            "generated_on": "Bewertung basierend auf Angaben vom",
            "footer_note": "Dieser Bericht dient ausschliesslich als Orientierungshilfe und ersetzt keine individuelle IT- oder Rechtsberatung.",
            "page": "Seite",
            "of": "von",
        },
        # --- Legal & Positioning ---
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
        # --- Questions for audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Utilisez-vous des mots de passe forts et uniques pour vos comptes professionnels ?",
                "remedy": "Utilisez un gestionnaire de mots de passe et un mot de passe distinct pour chaque compte.",
            },
            "q2": {
                "text": "Utilisez-vous un gestionnaire de mots de passe au sein du cabinet ?",
                "remedy": "Mettez en place un gestionnaire de mots de passe reconnu pour vous-même et vos collaborateurs.",
            },
            "q3": {
                "text": "Les mots de passe sont-ils modifiés lors du départ d'un collaborateur ou en cas de suspicion d'abus ?",
                "remedy": "Définissez des règles claires pour le changement des accès lors de changements de personnel ou d'incidents de sécurité.",
            },
            "q4": {
                "text": "Les données des patients sont-elles stockées de manière sécurisée ?",
                "remedy": "Ne conservez que les données personnelles nécessaires et utilisez, dans la mesure du possible, des systèmes cryptés.",
            },
            "q5": {
                "text": "Effectuez-vous régulièrement des sauvegardes automatiques de vos données professionnelles ?",
                "remedy": "Configurez des sauvegardes automatiques quotidiennes et conservez au moins une copie hors site.",
            },
            "q6": {
                "text": "Les sauvegardes (backups) sont-elles testées régulièrement ?",
                "remedy": "Testez au moins une fois par trimestre si vos sauvegardes peuvent être restaurées correctement.",
            },
            "q7": {
                "text": "Une protection antivirus ou « endpoint » à jour est-elle installée sur tous les ordinateurs ?",
                "remedy": "Installez une solution de protection reconnue et assurez-vous qu'elle soit constamment mise à jour.",
            },
            "q8": {
                "text": "Le Wi-Fi destiné aux patients est-il séparé du réseau interne du cabinet ?",
                "remedy": "Configurez un réseau Wi-Fi distinct pour les visiteurs et les patients.",
            },
            "q9": {
                "text": "Les mises à jour logicielles et de sécurité sont-elles installées régulièrement ?",
                "remedy": "Activez les mises à jour automatiques ou planifiez des fenêtres de maintenance régulières.",
            },
            "q10": {
                "text": "Utilisez-vous l'authentification à deux facteurs (2FA) pour vos comptes e-mail et administratifs ?",
                "remedy": "Activez la 2FA pour les accès e-mail, cloud et les comptes d'administration.",
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
        },
        # ---  PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "Rapport de sécurité informatique",
            "header_suffix": "Rapport de sécurité informatique pour institutions médicales",
            "generated_on": "Évaluation basée sur les informations du",
            "footer_note": "Ce rapport sert exclusivement de guide d'orientation et ne remplace pas un conseil informatique ou juridique individuel.",
            "page": "Page",
            "of": "sur",
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
        # --- Questions for audit ---
        "QUESTIONS": {
            "q1": {
                "text": "Utilizza password robuste e univoche per i Suoi account professionali?",
                "remedy": "Utilizzi un gestore di password e una password diversa per ogni account.",
            },
            "q2": {
                "text": "Utilizzate un gestore di password (password manager) nello studio?",
                "remedy": "Adotti un gestore di password affidabile per Lei e per i Suoi collaboratori.",
            },
            "q3": {
                "text": "Le password vengono modificate in caso di uscita di un collaboratore o sospetto abuso?",
                "remedy": "Definisca regole chiare per la modifica delle password in caso di avvicendamento del personale o incidenti di sicurezza.",
            },
            "q4": {
                "text": "I dati dei pazienti vengono archiviati in modo sicuro?",
                "remedy": "Conservi solo i dati personali necessari e utilizzi, laddove possibile, sistemi crittografati.",
            },
            "q5": {
                "text": "Esegue regolarmente backup automatici dei dati professionali?",
                "remedy": "Imposti backup automatici giornalieri e conservi almeno una copia esternamente allo studio.",
            },
            "q6": {
                "text": "I backup vengono testati regolarmente?",
                "remedy": "Verifichi almeno trimestralmente se i backup possono essere ripristinati correttamente.",
            },
            "q7": {
                "text": "Su tutti i computer è installata una protezione antivirus o endpoint aggiornata?",
                "remedy": "Installi una protezione endpoint affidabile e la mantenga costantemente aggiornata.",
            },
            "q8": {
                "text": "La rete Wi-Fi per i pazienti è separata dalla rete aziendale interna?",
                "remedy": "Configuri una rete Wi-Fi separata per ospiti e pazienti.",
            },
            "q9": {
                "text": "Gli aggiornamenti software e di sicurezza vengono installati regolarmente?",
                "remedy": "Attivi gli aggiornamenti automatici o pianifichi finestre di manutenzione regolari.",
            },
            "q10": {
                "text": "Utilizza l'autenticazione a due fattori (2FA) per l'e-mail e gli account amministrativi?",
                "remedy": "Attivi la 2FA per gli accessi e-mail, i servizi cloud e gli account di amministrazione.",
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
            "score_label": "La vostra valutazione",
            "measure_label": "Misura",
            "priority_label": "PRIORITÀ",
            "priorities": {"high": "ELEVATA", "standard": "STANDARD"},
        },
        # --- PDF Generation Content ---
        "REPORT_PDF": {
            "title_suffix": "Rapporto sulla sicurezza informatica",
            "header_suffix": "Rapporto sulla sicurezza informatica per strutture sanitarie",
            "generated_on": "Valutazione basata sui dati del",
            "footer_note": "Questo rapporto serve esclusivamente come guida orientativa e non sostituisce una consulenza informatica o legale individuale.",
            "page": "Pagina",
            "of": "di",
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
