from enum import StrEnum


class ListEncountersStatus(StrEnum):
    COMPLETED = "completed"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
