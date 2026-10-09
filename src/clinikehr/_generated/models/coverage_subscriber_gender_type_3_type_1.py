from enum import StrEnum


class CoverageSubscriberGenderType3Type1(StrEnum):
    F = "F"
    M = "M"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
