from enum import StrEnum


class ConditionCreateClinicalStatus(StrEnum):
    ACTIVE = "active"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
