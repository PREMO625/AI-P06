from typing import Dict, List


class EmployeePerformanceExpertSystem:
    """Rule-based employee performance evaluation engine."""

    def evaluate(
        self,
        productivity: int,
        quality: int,
        collaboration: int,
        attendance: int,
        learning: int,
    ) -> Dict[str, str]:
        weighted_score = (
            productivity * 0.30
            + quality * 0.30
            + collaboration * 0.15
            + attendance * 0.15
            + learning * 0.10
        )

        if weighted_score >= 8.5:
            rating = "Outstanding"
            action = "Fast-track for leadership and high-impact projects."
        elif weighted_score >= 7.0:
            rating = "Exceeds Expectations"
            action = "Reward with stretch assignments and growth goals."
        elif weighted_score >= 5.5:
            rating = "Meets Expectations"
            action = "Maintain performance with periodic mentoring."
        else:
            rating = "Needs Improvement"
            action = "Create structured PIP with weekly review checkpoints."

        recommendations: List[str] = []
        if productivity < 6:
            recommendations.append("Set weekly output goals with measurable KPIs.")
        if quality < 6:
            recommendations.append("Increase quality reviews and peer code/work checks.")
        if collaboration < 6:
            recommendations.append("Assign cross-team collaboration goals.")
        if attendance < 6:
            recommendations.append("Discuss attendance blockers and support plan.")
        if learning < 6:
            recommendations.append("Enroll in role-focused upskilling track.")

        if not recommendations:
            recommendations.append("Sustain current performance and mentor junior members.")

        reasoning = (
            f"Weighted score = {weighted_score:.2f}/10 from productivity, quality, "
            f"collaboration, attendance, and learning indicators."
        )

        return {
            "score": f"{weighted_score:.2f}",
            "rating": rating,
            "action": action,
            "recommendations": "\n".join(f"- {rec}" for rec in recommendations),
            "reasoning": reasoning,
        }
