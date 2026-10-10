from enum import StrEnum


class InsuranceClaimItemHmoItemStatusType3Type1(StrEnum):
    ADJUSTED = "ADJUSTED"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
