from enum import StrEnum


class ConditionAcceptedByType3Type1(StrEnum):
    AUTOMATIC = "automatic"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
