from enum import StrEnum


class EncounterSource(StrEnum):
    API = "api"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
