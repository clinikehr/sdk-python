from enum import StrEnum


class CoverageCoverageTypeType2Type1(StrEnum):
    BEHAVIORAL_HEALTH = "behavioral_health"
    DENTAL = "dental"
    MEDICAL = "medical"
    OTHER = "other"
    VISION = "vision"

    def __str__(self) -> str:
        return str(self.value)
