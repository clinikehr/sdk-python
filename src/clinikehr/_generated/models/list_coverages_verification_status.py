from enum import StrEnum


class ListCoveragesVerificationStatus(StrEnum):
    ALL = "all"
    CONFIRMED = "confirmed"
    UNCONFIRMED = "unconfirmed"

    def __str__(self) -> str:
        return str(self.value)
