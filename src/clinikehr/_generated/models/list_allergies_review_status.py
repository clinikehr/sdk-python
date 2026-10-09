from enum import StrEnum


class ListAllergiesReviewStatus(StrEnum):
    ALL = "all"
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
