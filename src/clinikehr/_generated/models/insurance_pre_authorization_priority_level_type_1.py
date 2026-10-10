from enum import StrEnum


class InsurancePreAuthorizationPriorityLevelType1(StrEnum):
    EMERGENCY = "emergency"
    ROUTINE = "routine"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
