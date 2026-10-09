from enum import StrEnum


class AppointmentPaymentStatusType2Type1(StrEnum):
    FAILED = "failed"
    PAID = "paid"
    PARTIAL = "partial"
    PENDING = "pending"
    REFUNDED = "refunded"
    WAIVED = "waived"

    def __str__(self) -> str:
        return str(self.value)
