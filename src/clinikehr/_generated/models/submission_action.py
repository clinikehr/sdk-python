from enum import StrEnum


class SubmissionAction(StrEnum):
    CREATE = "create"
    RETRACT = "retract"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
