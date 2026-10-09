from enum import StrEnum


class CrmContactCreateRequestPriority(StrEnum):
    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
