from enum import StrEnum


class AllergyCreateClinicalStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
