from enum import StrEnum


class ListInsuranceEnrolleesStatus(StrEnum):
    AA = "AA"
    IA = "IA"
    PP = "PP"
    SX = "SX"
    WP = "WP"
    XX = "XX"

    def __str__(self) -> str:
        return str(self.value)
