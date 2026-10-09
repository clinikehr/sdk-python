from enum import StrEnum


class AllergyReactionSeverityType1(StrEnum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"

    def __str__(self) -> str:
        return str(self.value)
