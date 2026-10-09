from enum import StrEnum


class ReferralAcceptedByType2Type1(StrEnum):
    AUTOMATIC = "automatic"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
