from enum import StrEnum


class MedicationStatementCreateStatus(StrEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    NOT_TAKEN = "not_taken"
    ON_HOLD = "on_hold"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
