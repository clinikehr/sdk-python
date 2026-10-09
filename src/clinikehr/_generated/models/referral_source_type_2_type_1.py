from enum import StrEnum


class ReferralSourceType2Type1(StrEnum):
    API = "api"
    CLINIC = "clinic"

    def __str__(self) -> str:
        return str(self.value)
