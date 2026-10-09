from enum import StrEnum


class PatientBillingIndividualTypeType3Type1(StrEnum):
    INSURANCE = "insurance"
    SELF_PAY = "self_pay"

    def __str__(self) -> str:
        return str(self.value)
