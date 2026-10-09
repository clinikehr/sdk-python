from enum import StrEnum


class MedicationStatementSource(StrEnum):
    API = "api"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
