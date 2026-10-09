from enum import StrEnum


class AllergyUpdateType(StrEnum):
    ALLERGY = "allergy"
    INTOLERANCE = "intolerance"

    def __str__(self) -> str:
        return str(self.value)
