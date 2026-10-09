from enum import StrEnum


class AppointmentCreateRequestStatus(StrEnum):
    CONFIRMED = "confirmed"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
