from enum import StrEnum


class InsurancePreAuthorizationSubmitPriorityLevel(StrEnum):
    EMERGENCY = "emergency"
    ROUTINE = "routine"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
