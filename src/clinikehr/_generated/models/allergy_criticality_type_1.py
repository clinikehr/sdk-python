from enum import StrEnum


class AllergyCriticalityType1(StrEnum):
    HIGH = "high"
    LOW = "low"
    UNABLE_TO_ASSESS = "unable_to_assess"

    def __str__(self) -> str:
        return str(self.value)
