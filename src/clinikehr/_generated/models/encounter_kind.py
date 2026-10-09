from enum import StrEnum


class EncounterKind(StrEnum):
    CONSULTATION = "consultation"

    def __str__(self) -> str:
        return str(self.value)
