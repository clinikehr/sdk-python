from enum import StrEnum


class AllergyClinicalStatusType1(StrEnum):
    ACTIVE = "active"
    ENTERED_IN_ERROR = "entered_in_error"
    INACTIVE = "inactive"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
