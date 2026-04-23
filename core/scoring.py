"""
Cyber Risk Scoring Engine - Professional Edition
Handles assessment logic, confidence penalties, and remediation mapping.
"""

from core.wording import get_lexicon

# Weight for each questions to compute
QUESTION_CONFIG = [
    {"id": "q1", "weight": 2},
    {"id": "q2", "weight": 1.5},
    {"id": "q3", "weight": 1},
    {"id": "q4", "weight": 2},
    {"id": "q5", "weight": 2},
    {"id": "q6", "weight": 2},
    {"id": "q7", "weight": 1.5},
    {"id": "q8", "weight": 1},
    {"id": "q9", "weight": 2},
    {"id": "q10", "weight": 2},
]


class AuditEngine:
    """
    Core business logic for calculating Swiss cyber-risk scores.
    Separates calculation from the web delivery layer.
    """

    def __init__(self, user_answers, lang="de-CH"):
        self.answers = {k: v.lower() for k, v in user_answers.items()}
        self.lang = lang  # Store the language
        self.earned = 0.0
        self.possible = 0.0
        self.failed_items = []
        self.na_count = 0

    def compute(self) -> dict:
        """Process all questions and return a detailed assessment dictionary."""

        lex = get_lexicon(self.lang)

        for cfg in QUESTION_CONFIG:
            q_id = cfg["id"]
            w = cfg["weight"]
            self.possible += w
            ans = self.answers.get(q_id, "na")

            if ans == "yes":
                self.earned += w
            elif ans == "no":
                # Get the translated text for the report
                q_text = lex["QUESTIONS"][q_id]["text"]
                q_remedy = lex["QUESTIONS"][q_id]["remedy"]
                # Pass all 4 required arguments
                self._record_failure(q_id, q_text, q_remedy, w)
            elif ans == "na":
                self.na_count += 1
                self.possible -= w
        return self._finalize_results()

    def _record_failure(self, q_id, text, remedy, weight):
        """Builds a list of failed items with remediation steps."""
        self.failed_items.append(
            {
                "id": q_id,
                "text": text,
                "remedy": remedy,
                "severity_key": "high" if weight >= 2 else "standard",
            }
        )

    def _finalize_results(self) -> dict:
        """Applies penalties, determines risk level, and checks data density."""
        # 1. Calculate raw score
        raw_score = (
            round((self.earned / self.possible) * 100) if self.possible > 0 else 0
        )

        # 2. Swiss Confidence Penalty Logic
        # We still apply penalties, but we add a "Hard Stop" for N/A count
        penalty = 0
        if 3 <= self.na_count <= 5:
            penalty = 5
        elif self.na_count > 5:
            penalty = 10

        final_score = max(raw_score - penalty, 0)

        # 3. Data Density Check (The "Insufficient Data" Flag)
        # If > 70% of the audit is skipped, we flag the result as inconclusive.
        is_inconclusive = self.na_count > 7

        return {
            "assessment": final_score,
            "assessment_raw": raw_score,
            "confidence_penalty": penalty,
            # If inconclusive, we override the classification
            "risk_level": (
                "inconclusive" if is_inconclusive else self._classify_risk(final_score)
            ),
            "is_valid": not is_inconclusive,
            "failed": self.failed_items,
            "na_count": self.na_count,
        }

    @staticmethod
    def _classify_risk(score: int) -> str:
        if score < 40:
            return "high"
        if score < 70:
            return "medium"
        return "low"
