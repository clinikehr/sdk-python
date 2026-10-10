from enum import StrEnum


class ListInsuranceClaimsStatus(StrEnum):
    ADDITIONAL_INFO_REQUIRED = "additional_info_required"
    AI_REVIEWED = "ai_reviewed"
    APPEALED = "appealed"
    APPROVED = "approved"
    CLOSED = "closed"
    DENIED = "denied"
    DRAFT = "draft"
    PAID = "paid"
    PARTIALLY_APPROVED = "partially_approved"
    PARTIALLY_PAID = "partially_paid"
    READY_TO_SUBMIT = "ready_to_submit"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    WRITTEN_OFF = "written_off"

    def __str__(self) -> str:
        return str(self.value)
