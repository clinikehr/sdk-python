from enum import StrEnum


class AllergyVerificationStatus(StrEnum):
    CONFIRMED = "confirmed"
    ENTERED_IN_ERROR = "entered_in_error"
    REFUTED = "refuted"
    UNCONFIRMED = "unconfirmed"

    def __str__(self) -> str:
        return str(self.value)
