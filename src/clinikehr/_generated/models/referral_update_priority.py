from enum import StrEnum


class ReferralUpdatePriority(StrEnum):
    ASAP = "asap"
    ROUTINE = "routine"
    STAT = "stat"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
