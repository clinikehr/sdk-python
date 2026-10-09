from enum import StrEnum


class ExternalStockBatchStatusStatus(StrEnum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
