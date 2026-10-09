from enum import StrEnum


class ReferralUpdateStatus(StrEnum):
    ENTERED_IN_ERROR = "entered_in_error"

    def __str__(self) -> str:
        return str(self.value)
