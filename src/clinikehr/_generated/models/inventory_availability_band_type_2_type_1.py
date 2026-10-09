from enum import StrEnum


class InventoryAvailabilityBandType2Type1(StrEnum):
    IN_STOCK = "in_stock"
    LOW = "low"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
