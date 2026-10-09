from enum import StrEnum


class PrescriptionStatus(StrEnum):
    CANCELLED = "cancelled"
    DISPENSED = "dispensed"
    OUT_OF_STOCK = "out_of_stock"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
