from enum import StrEnum


class AppointmentCreateRequestUrgencyLevel(StrEnum):
    EMERGENCY = "emergency"
    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
