from enum import StrEnum


class MedicationStatementAcceptedByType3Type1(StrEnum):
    AUTOMATIC = "automatic"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
