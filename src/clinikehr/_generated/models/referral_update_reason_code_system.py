from enum import StrEnum


class ReferralUpdateReasonCodeSystem(StrEnum):
    ICD_10 = "icd-10"
    ICD_10_CM = "icd-10-cm"
    LOCAL = "local"
    SNOMED_CT = "snomed-ct"

    def __str__(self) -> str:
        return str(self.value)
