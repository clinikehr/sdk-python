from enum import StrEnum


class MedicationStatementAcceptedByType2Type1(StrEnum):
    AUTOMATIC = "automatic"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
