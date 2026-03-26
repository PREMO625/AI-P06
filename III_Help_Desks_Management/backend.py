from typing import Dict, List


class HelpDeskExpertSystem:
    """Rule-based help desk ticket classification and routing."""

    def evaluate(
        self,
        issue_type: str,
        impact: str,
        urgency: str,
        vip_user: str,
        downtime: str,
    ) -> Dict[str, str]:
        priority_score = 0

        if impact == "High":
            priority_score += 3
        elif impact == "Medium":
            priority_score += 2
        else:
            priority_score += 1

        if urgency == "High":
            priority_score += 3
        elif urgency == "Medium":
            priority_score += 2
        else:
            priority_score += 1

        if vip_user == "Yes":
            priority_score += 2

        if downtime == "Yes":
            priority_score += 3

        if issue_type in {"Security", "Network"}:
            priority_score += 1

        if priority_score >= 10:
            priority = "P1 - Critical"
            sla = "Respond in 15 minutes, resolve target: 4 hours"
        elif priority_score >= 7:
            priority = "P2 - High"
            sla = "Respond in 30 minutes, resolve target: 8 hours"
        elif priority_score >= 5:
            priority = "P3 - Medium"
            sla = "Respond in 2 hours, resolve target: 2 business days"
        else:
            priority = "P4 - Low"
            sla = "Respond in 4 hours, resolve target: 5 business days"

        team_map = {
            "Software": "Application Support Team",
            "Hardware": "Infrastructure Team",
            "Network": "Network Operations Center",
            "Security": "Security Operations Team",
            "Access": "Identity and Access Management Team",
        }

        routed_team = team_map.get(issue_type, "General Support Team")

        checklist: List[str] = [
            f"Assign to: {routed_team}",
            f"Apply SLA: {sla}",
            "Record root-cause category in ticket notes.",
            "Update customer at each status transition.",
        ]

        if priority == "P1 - Critical":
            checklist.append("Trigger incident bridge call and notify duty manager.")

        if issue_type == "Security":
            checklist.append("Preserve logs and enforce immediate containment workflow.")

        reasoning = (
            f"Inputs -> Type: {issue_type}, Impact: {impact}, Urgency: {urgency}, "
            f"VIP: {vip_user}, Downtime: {downtime}."
        )

        return {
            "priority": priority,
            "team": routed_team,
            "sla": sla,
            "checklist": "\n".join(f"- {item}" for item in checklist),
            "reasoning": reasoning,
        }
