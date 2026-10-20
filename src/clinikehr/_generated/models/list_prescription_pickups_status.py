from enum import StrEnum


class ListPrescriptionPickupsStatus(StrEnum):
    AWAITING = "awaiting"
    COLLECTED = "collected"
    REMOTE_PENDING = "remote_pending"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
