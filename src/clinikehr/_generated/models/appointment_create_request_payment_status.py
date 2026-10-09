from enum import StrEnum


class AppointmentCreateRequestPaymentStatus(StrEnum):
    PAID = "paid"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
