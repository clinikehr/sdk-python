from enum import StrEnum


class ListPartnerCodesState(StrEnum):
    LINKED = "linked"
    NEEDS_REVIEW = "needs_review"
    REJECTED = "rejected"
    UNMATCHED = "unmatched"

    def __str__(self) -> str:
        return str(self.value)
