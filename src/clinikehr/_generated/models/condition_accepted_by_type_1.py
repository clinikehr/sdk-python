from enum import StrEnum


class ConditionAcceptedByType1(StrEnum):
    AUTOMATIC = "automatic"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
