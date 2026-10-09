from enum import StrEnum


class ListAllergiesClinicalStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
