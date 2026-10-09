from enum import StrEnum


class PatientMaritalStatusType2Type1(StrEnum):
    DIVORCED = "divorced"
    MARRIED = "married"
    SEPARATED = "separated"
    SINGLE = "single"
    WIDOWED = "widowed"

    def __str__(self) -> str:
        return str(self.value)
