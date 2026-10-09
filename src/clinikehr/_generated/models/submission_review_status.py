from enum import StrEnum


class SubmissionReviewStatus(StrEnum):
    CONFIRMED = "confirmed"
    PENDING = "pending"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
