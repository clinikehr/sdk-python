from enum import StrEnum


class ListingFeedbackRequestOutcome(StrEnum):
    CONFIRMED_AVAILABLE = "confirmed_available"
    CONFIRMED_UNAVAILABLE = "confirmed_unavailable"
    STALE = "stale"
    WRONG_MATCH = "wrong_match"

    def __str__(self) -> str:
        return str(self.value)
