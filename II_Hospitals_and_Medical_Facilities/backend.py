from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass(frozen=True)
class ConditionRule:
    name: str
    description: str
    department: str
    urgency: str
    symptom_weights: Dict[str, int]
    first_response: str
    treatment_path: str


class HospitalExpertSystem:
    """Rule-based triage expert system for hospital and medical facilities."""

    def __init__(self) -> None:
        self.rules: List[ConditionRule] = [
            ConditionRule(
                name="Acute Viral Fever",
                description="Likely self-limiting viral infection with systemic symptoms.",
                department="General Medicine",
                urgency="Medium",
                symptom_weights={
                    "Fever": 4,
                    "Fatigue": 3,
                    "Sore throat": 3,
                    "Headache": 2,
                    "Nausea": 1,
                },
                first_response="Hydration, rest, monitor temperature every 6 hours.",
                treatment_path="OPD consultation, CBC if fever persists for >48 hours.",
            ),
            ConditionRule(
                name="Asthma Exacerbation",
                description="Airway narrowing episode that may need bronchodilator support.",
                department="Pulmonology",
                urgency="High",
                symptom_weights={
                    "Shortness of breath": 5,
                    "Cough": 3,
                    "Chest pain": 2,
                    "Restlessness": 2,
                    "Wheezing": 4,
                },
                first_response="Use rescue inhaler if prescribed; keep patient upright.",
                treatment_path="Urgent pulmonology evaluation and oxygen saturation check.",
            ),
            ConditionRule(
                name="Possible Cardiac Event",
                description="Pattern suggests possible acute coronary syndrome risk.",
                department="Cardiology",
                urgency="Critical",
                symptom_weights={
                    "Chest pain": 6,
                    "Shortness of breath": 4,
                    "Nausea": 2,
                    "Fainting": 3,
                    "Sweating": 2,
                },
                first_response="Do not delay. Immediate ECG-enabled emergency assessment.",
                treatment_path="Emergency room triage, ECG, troponin tests, cardiology review.",
            ),
            ConditionRule(
                name="Migraine Episode",
                description="Neurological headache pattern with sensory sensitivity.",
                department="Neurology",
                urgency="Medium",
                symptom_weights={
                    "Headache": 5,
                    "Blurred vision": 3,
                    "Nausea": 2,
                    "Light sensitivity": 3,
                    "Fatigue": 1,
                },
                first_response="Move to low-light room and hydrate.",
                treatment_path="Neurology OPD review and trigger-management guidance.",
            ),
            ConditionRule(
                name="Gastroenteritis / Food Infection",
                description="Likely acute GI infection with dehydration risk.",
                department="Gastroenterology",
                urgency="Medium",
                symptom_weights={
                    "Nausea": 4,
                    "Vomiting": 4,
                    "Fever": 2,
                    "Abdominal pain": 3,
                    "Fatigue": 2,
                },
                first_response="Oral rehydration and fluid-electrolyte balancing.",
                treatment_path="Stool/culture guidance if severe; gastro consultation.",
            ),
        ]

        self.emergency_flags: Set[str] = {
            "Chest pain",
            "Shortness of breath",
            "Fainting",
            "Confusion",
            "Severe bleeding",
        }

    def list_symptoms(self) -> List[str]:
        catalog: Set[str] = set(self.emergency_flags)
        for rule in self.rules:
            catalog.update(rule.symptom_weights.keys())
        return sorted(catalog)

    def evaluate(
        self,
        selected_symptoms: Set[str],
        age: int,
        pain_scale: int,
        symptom_duration: str,
    ) -> Dict[str, str]:
        if not selected_symptoms:
            return {
                "triage": "Insufficient Data",
                "diagnosis": "Please select at least one symptom.",
                "care_plan": "No recommendation generated.",
                "reasoning": "No symptom signals provided for inference.",
            }

        scored = []
        for rule in self.rules:
            max_score = sum(rule.symptom_weights.values()) + 6
            symptom_score = 0

            for symptom, weight in rule.symptom_weights.items():
                if symptom in selected_symptoms:
                    symptom_score += weight

            if age >= 60 and rule.name in {"Possible Cardiac Event", "Asthma Exacerbation"}:
                symptom_score += 2

            if symptom_duration in {"3-7 days", "> 1 week"}:
                symptom_score += 1

            if pain_scale >= 8 and "Chest pain" in rule.symptom_weights:
                symptom_score += 3

            probability = round((symptom_score / max_score) * 100)
            scored.append((probability, rule))

        scored.sort(key=lambda item: item[0], reverse=True)
        top_probability, top_rule = scored[0]

        emergency_detected = bool(self.emergency_flags.intersection(selected_symptoms))
        if top_rule.urgency == "Critical" or (emergency_detected and pain_scale >= 8):
            triage = "Critical - Immediate Emergency Care"
        elif top_rule.urgency == "High" or emergency_detected:
            triage = "High - Same Day Evaluation"
        else:
            triage = "Moderate - Outpatient Consultation"

        top3 = scored[:3]
        diagnosis_lines = ["### Most Probable Conditions"]
        for probability, rule in top3:
            diagnosis_lines.append(
                f"- **{rule.name}** ({probability}%) | Department: {rule.department}"
            )

        care_plan = (
            f"### Recommended First Response\n"
            f"{top_rule.first_response}\n\n"
            f"### Suggested Care Path\n"
            f"{top_rule.treatment_path}"
        )

        matched_symptoms = sorted(selected_symptoms.intersection(top_rule.symptom_weights.keys()))
        reasoning = (
            f"### Inference Reasoning\n"
            f"Top rule matched symptoms: {', '.join(matched_symptoms) if matched_symptoms else 'None'}\n\n"
            f"Rule description: {top_rule.description}"
        )

        return {
            "triage": triage,
            "diagnosis": "\n".join(diagnosis_lines),
            "care_plan": care_plan,
            "reasoning": reasoning,
        }
