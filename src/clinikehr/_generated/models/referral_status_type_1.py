from enum import StrEnum


class ReferralStatusType1(StrEnum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DECLINED = "declined"
    ENTERED_IN_ERROR = "entered_in_error"
    RECEIVED = "received"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
