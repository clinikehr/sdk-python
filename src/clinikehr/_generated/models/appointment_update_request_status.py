from enum import StrEnum


class AppointmentUpdateRequestStatus(StrEnum):
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
