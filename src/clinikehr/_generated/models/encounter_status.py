from enum import StrEnum


class EncounterStatus(StrEnum):
    COMPLETED = "completed"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
