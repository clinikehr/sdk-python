from enum import StrEnum


class MedicationStatementStatusType2Type1(StrEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    ENTERED_IN_ERROR = "entered_in_error"
    NOT_TAKEN = "not_taken"
    ON_HOLD = "on_hold"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
