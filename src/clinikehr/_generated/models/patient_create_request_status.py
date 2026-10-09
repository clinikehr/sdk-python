from enum import StrEnum


class PatientCreateRequestStatus(StrEnum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    INACTIVE = "inactive"
    PROSPECT = "prospect"

    def __str__(self) -> str:
        return str(self.value)
