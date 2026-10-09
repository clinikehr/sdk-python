from enum import StrEnum


class PatientClientTypeType1(StrEnum):
    ADULT = "adult"
    COUPLE = "couple"
    MINOR = "minor"

    def __str__(self) -> str:
        return str(self.value)
