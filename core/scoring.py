"""
Cyber Risk Scoring Engine - Professional Edition
Handles assessment logic, confidence penalties, and remediation mapping.
"""

# Hardcoded for clarity and performance
QUESTIONS = [
    {"id": "q1", "text": "Verwenden Sie für geschäftliche Konten starke und einzigartige Passwörter?", "weight": 2, "remedy": "Verwenden Sie einen Passwort-Manager und für jedes Konto ein eigenes Passwort."},
    {"id": "q2", "text": "Nutzen Sie einen Passwort-Manager?", "weight": 1.5, "remedy": "Setzen Sie einen etablierten Passwort-Manager für sich und Ihre Mitarbeitenden ein."},
    {"id": "q3", "text": "Werden Passwörter bei Mitarbeiteraustritt oder Verdacht auf Missbrauch geändert?", "weight": 1, "remedy": "Definieren Sie klare Regeln für Passwortänderungen bei Personalwechsel oder Sicherheitsvorfällen."},
    {"id": "q4", "text": "Werden Kunden- und Patientendaten sicher gespeichert?", "weight": 2, "remedy": "Speichern Sie nur notwendige Personendaten und verwenden Sie wenn möglich verschlüsselte Systeme."},
    {"id": "q5", "text": "Erstellen Sie regelmässig automatische Backups Ihrer Geschäftsdaten?", "weight": 2, "remedy": "Richten Sie tägliche automatische Backups ein und bewahren Sie mindestens eine Kopie extern auf."},
    {"id": "q6", "text": "Werden Backups regelmässig getestet?", "weight": 2, "remedy": "Testen Sie mindestens vierteljährlich, ob sich Ihre Backups wiederherstellen lassen."},
    {"id": "q7", "text": "Ist auf allen Computern ein aktueller Viren- oder Endpunktschutz installiert?", "weight": 1.5, "remedy": "Installieren Sie einen etablierten Endpunktschutz und halten Sie diesen aktuell."},
    {"id": "q8", "text": "Ist das Kunden-WLAN vom internen Geschäftsnetz getrennt?", "weight": 1, "remedy": "Richten Sie ein separates Gäste-WLAN ein."},
    {"id": "q9", "text": "Werden Software-Updates und Sicherheitsupdates regelmässig installiert?", "weight": 2, "remedy": "Aktivieren Sie automatische Updates oder planen Sie regelmässige Wartungsfenster ein."},
    {"id": "q10", "text": "Nutzen Sie Zwei-Faktor-Authentifizierung (2FA) für E-Mail- und Administrationskonten?", "weight": 2, "remedy": "Aktivieren Sie 2FA für E-Mail-, Cloud- und Administrationszugänge."},
]

class AuditEngine:
    """
    Core business logic for calculating Swiss cyber-risk scores.
    Separates calculation from the web delivery layer.
    """
    def __init__(self, user_answers):
        self.answers = {k: v.lower() for k, v in user_answers.items()}
        self.earned = 0.0
        self.possible = 0.0
        self.failed_items = []
        self.na_count = 0

    def compute(self) -> dict:
        """Process all questions and return a detailed assessment dictionary."""
        for q in QUESTIONS:
            w = q["weight"]
            self.possible += w
            ans = self.answers.get(q["id"], "na")

            if ans == "yes":
                self.earned += w
            elif ans == "no":
                self._record_failure(q, w)
            elif ans == "na":
                self.na_count += 1
                self.possible -= w

        return self._finalize_results()

    def _record_failure(self, q, weight):
        """Builds a list of failed items with remediation steps."""
        self.failed_items.append({
            "id": q["id"],
            "text": q["text"],
            "remedy": q["remedy"],
            "severity": "High Priority" if weight >= 2 else "Standard Priority",
        })

    def _finalize_results(self) -> dict:
        """Applies penalties and determines risk level."""
        raw_score = round((self.earned / self.possible) * 100) if self.possible > 0 else 0
        
        # Swiss Confidence Penalty Logic
        penalty = 0
        if 3 <= self.na_count <= 5: penalty = 5
        elif self.na_count > 5: penalty = 10

        final_score = max(raw_score - penalty, 0)
        
        return {
            "assessment": final_score,
            "assessment_raw": raw_score,
            "confidence_penalty": penalty,
            "risk_level": self._classify_risk(final_score),
            "failed": self.failed_items,
            "na_count": self.na_count,
        }

    @staticmethod
    def _classify_risk(score: int) -> str:
        if score < 40: return "high"
        if score < 70: return "medium"
        return "low"
