from enum import StrEnum


class ReferralPriorityType1(StrEnum):
    ASAP = "asap"
    ROUTINE = "routine"
    STAT = "stat"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
