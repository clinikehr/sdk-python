from enum import StrEnum


class ConditionClinicalStatus(StrEnum):
    ACTIVE = "active"
    ENTERED_IN_ERROR = "entered_in_error"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
