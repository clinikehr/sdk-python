from enum import StrEnum


class InsurancePreAuthorizationStatus(StrEnum):
    AI_REVIEWED = "ai_reviewed"
    APPROVED = "approved"
    CANCELLED = "cancelled"
    DENIED = "denied"
    DRAFT = "draft"
    EXPIRED = "expired"
    REVIEWED = "reviewed"
    SENT_FOR_AUTHORIZATION = "sent_for_authorization"

    def __str__(self) -> str:
        return str(self.value)
