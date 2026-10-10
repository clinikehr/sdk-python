from enum import StrEnum


class InsurancePaymentAdviceCreateMethod(StrEnum):
    BANK_TRANSFER = "bank_transfer"
    CHEQUE = "cheque"
    EFT = "eft"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
