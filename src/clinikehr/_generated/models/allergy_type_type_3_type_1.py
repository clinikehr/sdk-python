from enum import StrEnum


class AllergyTypeType3Type1(StrEnum):
    ALLERGY = "allergy"
    INTOLERANCE = "intolerance"

    def __str__(self) -> str:
        return str(self.value)
