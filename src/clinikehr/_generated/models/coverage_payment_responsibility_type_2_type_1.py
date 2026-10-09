from enum import StrEnum


class CoveragePaymentResponsibilityType2Type1(StrEnum):
    P = "P"
    S = "S"
    T = "T"

    def __str__(self) -> str:
        return str(self.value)
