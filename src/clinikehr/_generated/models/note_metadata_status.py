from enum import StrEnum


class NoteMetadataStatus(StrEnum):
    COMPLETED = "completed"
    DRAFT = "draft"
    FINAL = "final"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)
