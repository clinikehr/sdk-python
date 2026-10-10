from enum import StrEnum


class InsuranceClaimAdjudicationDecision(StrEnum):
    APPROVED = "approved"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
