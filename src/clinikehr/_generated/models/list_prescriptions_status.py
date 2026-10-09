from enum import StrEnum


class ListPrescriptionsStatus(StrEnum):
    CANCELLED = "cancelled"
    DISPENSED = "dispensed"
    OUT_OF_STOCK = "out_of_stock"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
