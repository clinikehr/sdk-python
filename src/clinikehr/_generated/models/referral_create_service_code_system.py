from enum import StrEnum


class ReferralCreateServiceCodeSystem(StrEnum):
    LOCAL = "local"
    SNOMED_CT = "snomed-ct"

    def __str__(self) -> str:
        return str(self.value)
