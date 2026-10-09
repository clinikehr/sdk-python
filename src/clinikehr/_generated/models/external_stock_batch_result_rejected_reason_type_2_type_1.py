from enum import StrEnum


class ExternalStockBatchResultRejectedReasonType2Type1(StrEnum):
    EMPTY = "empty"
    INVALID_ROWS = "invalid_rows"
    SUSPICIOUS_SHRINK = "suspicious_shrink"

    def __str__(self) -> str:
        return str(self.value)
