from enum import StrEnum


class InsuranceClaimLineDecisionStatus(StrEnum):
    ADJUSTED = "adjusted"
    APPROVED = "approved"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
