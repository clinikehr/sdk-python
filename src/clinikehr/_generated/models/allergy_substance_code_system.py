from enum import StrEnum


class AllergySubstanceCodeSystem(StrEnum):
    LOCAL = "local"
    RXNORM = "rxnorm"
    SNOMED_CT = "snomed-ct"

    def __str__(self) -> str:
        return str(self.value)
