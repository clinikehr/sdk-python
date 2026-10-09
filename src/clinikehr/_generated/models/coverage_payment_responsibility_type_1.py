from enum import StrEnum


class CoveragePaymentResponsibilityType1(StrEnum):
    P = "P"
    S = "S"
    T = "T"

    def __str__(self) -> str:
        return str(self.value)
