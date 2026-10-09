from enum import StrEnum


class AppointmentPaymentStatusType3Type1(StrEnum):
    FAILED = "failed"
    PAID = "paid"
    PARTIAL = "partial"
    PENDING = "pending"
    REFUNDED = "refunded"
    WAIVED = "waived"

    def __str__(self) -> str:
        return str(self.value)
