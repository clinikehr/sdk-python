from enum import StrEnum


class PatientBillingIndividualTypeType2Type1(StrEnum):
    INSURANCE = "insurance"
    SELF_PAY = "self_pay"

    def __str__(self) -> str:
        return str(self.value)
