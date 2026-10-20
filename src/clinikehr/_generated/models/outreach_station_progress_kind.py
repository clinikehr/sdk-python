from enum import StrEnum


class OutreachStationProgressKind(StrEnum):
    CONSULTATION = "consultation"
    CUSTOM = "custom"
    DENTAL = "dental"
    INTAKE = "intake"
    LAB = "lab"
    PHARMACY = "pharmacy"
    RADIOLOGY = "radiology"
    VISION = "vision"
    VITALS = "vitals"

    def __str__(self) -> str:
        return str(self.value)
