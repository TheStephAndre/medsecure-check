"""
Cyber Risk Scoring Engine - Pillar Edition
Aggregates scores by Security Pillar: Confidentiality, Integrity, Availability, Traceability.
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
        self.failed_items = []
        self.na_count = 0
        # Pillar tracking: { "Pillar Name": {"earned": 0.0, "possible": 0.0} }
        self.pillars = {}

    def compute(self) -> dict:
        """Process all questions and return a detailed assessment dictionary."""

        lex = get_lexicon(self.lang)
        questions_lex = lex["QUESTIONS"]

        for cfg in QUESTION_CONFIG:
            q_id = cfg["id"]
            w = cfg["weight"]

            # Identify the pillar for this question from wording.py
            q_data = questions_lex.get(q_id, {})
            pillar_name = q_data.get("pillar", "General")

            # Initialize pillar tracking
            if pillar_name not in self.pillars:
                self.pillars[pillar_name] = {"earned": 0.0, "possible": 0.0}

            ans = self.answers.get(q_id, "na")

            if ans == "na":
                self.na_count += 1
                continue  # Skip N/A for both earned and possible

            # Update Pillar Totals
            self.pillars[pillar_name]["possible"] += w

            if ans == "yes":
                self.pillars[pillar_name]["earned"] += w
            elif ans == "no":
                # Record detailed failure for the report
                self._record_failure(
                    q_id=q_id,
                    text=q_data.get("text", ""),
                    remedy=q_data.get("remedy", ""),
                    pillar=pillar_name,
                    standard=q_data.get("standard", ""),
                    weight=w,
                )

        return self._finalize_results()

    def _record_failure(self, q_id, text, remedy, pillar, standard, weight):
        """Builds a list of failed items with remediation steps."""
        self.failed_items.append(
            {
                "id": q_id,
                "text": text,
                "remedy": remedy,
                "pillar": pillar,
                "standard": standard,
                "severity_key": "high" if weight >= 2 else "standard",
            }
        )

    def _finalize_results(self) -> dict:
        """Applies penalties, determines risk level, and checks data density."""
        # 1. Calculate Per-Pillar Percentages
        pillar_scores = {}
        total_earned = 0.0
        total_possible = 0.0

        for name, scores in self.pillars.items():
            if scores["possible"] > 0:
                perc = round((scores["earned"] / scores["possible"]) * 100)
                pillar_scores[name] = perc
                total_earned += scores["earned"]
                total_possible += scores["possible"]
            else:
                pillar_scores[name] = 0

        # 2. Overall Score & Penalties
        raw_score = (
            round((total_earned / total_possible) * 100) if total_possible > 0 else 0
        )

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
            "pillar_scores": pillar_scores,
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
