from typing import Dict, List


class AirlineSchedulingExpertSystem:
    """Rule-based advisor for airline scheduling and cargo routing."""

    def evaluate(
        self,
        weather: str,
        aircraft_status: str,
        crew_availability: str,
        cargo_priority: str,
        airport_congestion: str,
    ) -> Dict[str, str]:
        disruption_score = 0

        if weather == "Severe":
            disruption_score += 4
        elif weather == "Moderate":
            disruption_score += 2

        if aircraft_status == "Technical Issue":
            disruption_score += 4
        elif aircraft_status == "Minor Delay":
            disruption_score += 2

        if crew_availability == "Low":
            disruption_score += 3
        elif crew_availability == "Medium":
            disruption_score += 1

        if airport_congestion == "High":
            disruption_score += 3
        elif airport_congestion == "Medium":
            disruption_score += 1

        if cargo_priority == "Critical":
            disruption_score += 2

        if disruption_score >= 11:
            schedule_action = "Reschedule flight and reroute critical cargo immediately"
            risk = "High"
        elif disruption_score >= 7:
            schedule_action = "Delay with protected slots and partial cargo reroute"
            risk = "Medium"
        else:
            schedule_action = "Operate with current schedule and close monitoring"
            risk = "Low"

        checklist: List[str] = [
            f"Operational risk level: {risk}",
            schedule_action,
            "Confirm gate and slot availability with airport control.",
            "Publish updated ETA to all downstream handling teams.",
        ]

        if cargo_priority == "Critical":
            checklist.append("Allocate fastest available lane for critical cargo units.")

        if weather == "Severe":
            checklist.append("Activate alternate airport and contingency fuel planning.")

        reasoning = (
            f"Inputs -> Weather: {weather}, Aircraft: {aircraft_status}, Crew: {crew_availability}, "
            f"Cargo priority: {cargo_priority}, Congestion: {airport_congestion}."
        )

        return {
            "risk": risk,
            "decision": schedule_action,
            "checklist": "\n".join(f"- {item}" for item in checklist),
            "reasoning": reasoning,
        }
