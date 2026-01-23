# scoring.py
# Minimal scoring engine and remediation templates(DE-CH).

QUESTIONS = [
    {
        "id": "q1",
        "text": "Verwenden Sie für geschäftliche Konten starke und einzigartige Passwörter?",
        "weight": 2,
        "remedy": "Verwenden Sie einen Passwort-Manager und für jedes Konto ein eigenes Passwort.",
    },
    {
        "id": "q2",
        "text": "Nutzen Sie einen Passwort-Manager?",
        "weight": 1.5,
        "remedy": "Setzen Sie einen etablierten Passwort-Manager für sich und Ihre Mitarbeitenden ein.",
    },
    {
        "id": "q3",
        "text": "Werden Passwörter bei Mitarbeiteraustritt oder Verdacht auf Missbrauch geändert?",
        "weight": 1,
        "remedy": "Definieren Sie klare Regeln für Passwortänderungen bei Personalwechsel oder Sicherheitsvorfällen.",
    },
    {
        "id": "q4",
        "text": "Werden Kunden- und Patientendaten sicher gespeichert?",
        "weight": 2,
        "remedy": "Speichern Sie nur notwendige Personendaten und verwenden Sie wenn möglich verschlüsselte Systeme.",
    },
    {
        "id": "q5",
        "text": "Erstellen Sie regelmässig automatische Backups Ihrer Geschäftsdaten?",
        "weight": 2,
        "remedy": "Richten Sie tägliche automatische Backups ein und bewahren Sie mindestens eine Kopie extern auf.",
    },
    {
        "id": "q6",
        "text": "Werden Backups regelmässig getestet?",
        "weight": 2,
        "remedy": "Testen Sie mindestens vierteljährlich, ob sich Ihre Backups wiederherstellen lassen.",
    },
    {
        "id": "q7",
        "text": "Ist auf allen Computern ein aktueller Viren- oder Endpunktschutz installiert?",
        "weight": 1.5,
        "remedy": "Installieren Sie einen etablierten Endpunktschutz und halten Sie diesen aktuell.",
    },
    {
        "id": "q8",
        "text": "Ist das Kunden-WLAN vom internen Geschäftsnetz getrennt?",
        "weight": 1,
        "remedy": "Richten Sie ein separates Gäste-WLAN ein.",
    },
    {
        "id": "q9",
        "text": "Werden Software-Updates und Sicherheitsupdates regelmässig installiert?",
        "weight": 2,
        "remedy": "Aktivieren Sie automatische Updates oder planen Sie regelmässige Wartungsfenster ein.",
    },
    {
        "id": "q10",
        "text": "Nutzen Sie Zwei-Faktor-Authentifizierung (2FA) für E-Mail- und Administrationskonten?",
        "weight": 2,
        "remedy": "Aktivieren Sie 2FA für E-Mail-, Cloud- und Administrationszugänge.",
    },
]


def compute_score(answers: dict):
    """answers: dict mapping question id to 'yes'/'no'/'na' {q1:"yes"}"""

    earned = 0.0
    possible = 0.0
    failed = []
    na_count = 0

    for q in QUESTIONS:

        w = q["weight"]
        possible += w
        ans = answers.get(q["id"], "").lower()

        if ans == "yes":
            earned += w
        elif ans == "no":
            # Collect failed items for remediation
            failed.append(
                {
                    "id": q["id"],
                    "text": q["text"],
                    "remedy": q["remedy"],
                    "severity": "Hoch" if w >= 2 else "Mittel",
                }
            )
        elif ans == "na":
            # Count unclear answer.
            na_count += 1
            # IMPORTNANT: remove from possible score.
            possible -= w

    score = round((earned / possible) * 100) if possible > 0 else 0

    return {
        "score": int(score),
        "failed": failed,
        "na_count": na_count,
    }
