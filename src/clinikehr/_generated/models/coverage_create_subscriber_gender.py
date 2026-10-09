from enum import StrEnum


class CoverageCreateSubscriberGender(StrEnum):
    F = "F"
    M = "M"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
