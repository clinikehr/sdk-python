from enum import StrEnum


class ConditionVerificationStatus(StrEnum):
    CONFIRMED = "confirmed"
    UNCONFIRMED = "unconfirmed"

    def __str__(self) -> str:
        return str(self.value)
