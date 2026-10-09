from enum import StrEnum


class DrugRequestStatusType2Type1(StrEnum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    DECLINED = "declined"
    DISPENSED = "dispensed"
    EXPIRED = "expired"
    PARTLY_ACCEPTED = "partly_accepted"
    READY = "ready"
    SUBMITTED = "submitted"
    SUBSTITUTED = "substituted"

    def __str__(self) -> str:
        return str(self.value)
