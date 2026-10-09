from enum import StrEnum


class InventoryAvailabilityBandType3Type1(StrEnum):
    IN_STOCK = "in_stock"
    LOW = "low"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
