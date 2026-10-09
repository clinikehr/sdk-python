from enum import StrEnum


class ListConditionsReviewStatus(StrEnum):
    ALL = "all"
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
