from enum import StrEnum


class CrmContactPriorityType2Type1(StrEnum):
    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
