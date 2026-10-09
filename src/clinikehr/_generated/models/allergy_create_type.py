from enum import StrEnum


class AllergyCreateType(StrEnum):
    ALLERGY = "allergy"
    INTOLERANCE = "intolerance"

    def __str__(self) -> str:
        return str(self.value)
