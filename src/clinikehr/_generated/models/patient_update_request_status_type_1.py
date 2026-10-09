from enum import StrEnum


class PatientUpdateRequestStatusType1(StrEnum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    INACTIVE = "inactive"
    PROSPECT = "prospect"

    def __str__(self) -> str:
        return str(self.value)
