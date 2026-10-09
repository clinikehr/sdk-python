from enum import StrEnum


class CoverageUpdatePaymentResponsibility(StrEnum):
    P = "P"
    S = "S"
    T = "T"

    def __str__(self) -> str:
        return str(self.value)
