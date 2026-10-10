from enum import StrEnum


class InsurancePreAuthorizationDecisionDecision(StrEnum):
    APPROVED = "approved"
    DENIED = "denied"

    def __str__(self) -> str:
        return str(self.value)
