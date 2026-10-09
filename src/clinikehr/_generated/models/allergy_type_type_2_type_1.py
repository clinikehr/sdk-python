from enum import StrEnum


class AllergyTypeType2Type1(StrEnum):
    ALLERGY = "allergy"
    INTOLERANCE = "intolerance"

    def __str__(self) -> str:
        return str(self.value)
