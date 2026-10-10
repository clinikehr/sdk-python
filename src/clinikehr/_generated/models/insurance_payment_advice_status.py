from enum import StrEnum


class InsurancePaymentAdviceStatus(StrEnum):
    ADVISED = "advised"
    DECLINED = "declined"
    RECORDED = "recorded"

    def __str__(self) -> str:
        return str(self.value)
