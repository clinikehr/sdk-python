from enum import StrEnum


class InsuranceClaimSubmitClaimType(StrEnum):
    DENTAL = "dental"
    EMERGENCY = "emergency"
    INPATIENT = "inpatient"
    LAB = "lab"
    OPTICAL = "optical"
    OTHER = "other"
    OUTPATIENT = "outpatient"
    PHARMACY = "pharmacy"
    RADIOLOGY = "radiology"

    def __str__(self) -> str:
        return str(self.value)
