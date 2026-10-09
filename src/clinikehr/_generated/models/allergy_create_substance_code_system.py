from enum import StrEnum


class AllergyCreateSubstanceCodeSystem(StrEnum):
    LOCAL = "local"
    RXNORM = "rxnorm"
    SNOMED_CT = "snomed-ct"

    def __str__(self) -> str:
        return str(self.value)
