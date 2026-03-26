from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class StoragePolicy:
    bucket: str
    description: str
    security_level: str
    retention_policy: str
    backup_policy: str


class InformationManagementExpertSystem:
    """Rule-based information management advisor."""

    def __init__(self) -> None:
        self.policies: Dict[str, StoragePolicy] = {
            "Public Knowledge": StoragePolicy(
                bucket="Public Knowledge",
                description="Non-sensitive documents for broad internal consumption.",
                security_level="Low",
                retention_policy="Retain for 1 year and archive.",
                backup_policy="Weekly backup.",
            ),
            "Operational Internal": StoragePolicy(
                bucket="Operational Internal",
                description="Department-level operational content and process notes.",
                security_level="Medium",
                retention_policy="Retain for 3 years with quarterly review.",
                backup_policy="Daily incremental backup.",
            ),
            "Confidential Business": StoragePolicy(
                bucket="Confidential Business",
                description="Sensitive business records, contracts, and finance-related data.",
                security_level="High",
                retention_policy="Retain for 7 years with legal hold support.",
                backup_policy="Daily full backup with offsite replication.",
            ),
            "Restricted Critical": StoragePolicy(
                bucket="Restricted Critical",
                description="Highly sensitive strategic or regulated records.",
                security_level="Very High",
                retention_policy="Retain per compliance mandate and legal retention.",
                backup_policy="Near real-time replication and immutable backup.",
            ),
        }

    def evaluate(
        self,
        data_type: str,
        sensitivity: str,
        access_frequency: str,
        regulatory_required: str,
        business_criticality: str,
    ) -> Dict[str, str]:
        score = 0

        if sensitivity == "High":
            score += 3
        elif sensitivity == "Medium":
            score += 2
        else:
            score += 1

        if regulatory_required == "Yes":
            score += 3

        if business_criticality == "High":
            score += 3
        elif business_criticality == "Medium":
            score += 2
        else:
            score += 1

        if access_frequency == "Daily":
            score += 2
        elif access_frequency == "Weekly":
            score += 1

        if data_type in {"Financial", "Legal", "Employee Records"}:
            score += 2

        if score >= 10:
            bucket = self.policies["Restricted Critical"]
        elif score >= 8:
            bucket = self.policies["Confidential Business"]
        elif score >= 5:
            bucket = self.policies["Operational Internal"]
        else:
            bucket = self.policies["Public Knowledge"]

        actions: List[str] = [
            f"Store under: {bucket.bucket}",
            f"Security level: {bucket.security_level}",
            bucket.retention_policy,
            bucket.backup_policy,
        ]

        if regulatory_required == "Yes":
            actions.append("Enable audit logs and role-based access controls.")

        if sensitivity == "High":
            actions.append("Apply encryption at rest and in transit.")

        if access_frequency == "Rarely":
            actions.append("Move to warm/cold tier after 90 days of inactivity.")

        reasoning = (
            f"Decision inputs -> Type: {data_type}, Sensitivity: {sensitivity}, "
            f"Access: {access_frequency}, Regulatory: {regulatory_required}, "
            f"Criticality: {business_criticality}."
        )

        return {
            "classification": bucket.bucket,
            "summary": bucket.description,
            "actions": "\n".join(f"- {item}" for item in actions),
            "reasoning": reasoning,
        }
