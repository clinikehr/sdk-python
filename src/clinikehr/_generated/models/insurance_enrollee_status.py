from enum import StrEnum


class InsuranceEnrolleeStatus(StrEnum):
    AA = "AA"
    IA = "IA"
    PP = "PP"
    SX = "SX"
    WP = "WP"
    XX = "XX"

    def __str__(self) -> str:
        return str(self.value)
