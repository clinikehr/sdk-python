from enum import StrEnum


class AllergyUpdateClinicalStatus(StrEnum):
    ACTIVE = "active"
    ENTERED_IN_ERROR = "entered_in_error"
    INACTIVE = "inactive"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
