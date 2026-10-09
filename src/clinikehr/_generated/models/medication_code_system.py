from enum import StrEnum


class MedicationCodeSystem(StrEnum):
    LOCAL = "local"
    RXNORM = "rxnorm"

    def __str__(self) -> str:
        return str(self.value)
