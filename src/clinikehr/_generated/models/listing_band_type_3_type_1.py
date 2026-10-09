from enum import StrEnum


class ListingBandType3Type1(StrEnum):
    IN_STOCK = "in_stock"
    LOW = "low"
    OUT = "out"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
