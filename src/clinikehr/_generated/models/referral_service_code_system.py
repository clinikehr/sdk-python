from enum import StrEnum


class ReferralServiceCodeSystem(StrEnum):
    LOCAL = "local"
    SNOMED_CT = "snomed-ct"

    def __str__(self) -> str:
        return str(self.value)
