from enum import StrEnum


class ListAppointmentsStatus(StrEnum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    NO_SHOW = "no_show"
    RESCHEDULED = "rescheduled"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
