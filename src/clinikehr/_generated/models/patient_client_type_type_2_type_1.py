from enum import StrEnum


class PatientClientTypeType2Type1(StrEnum):
    ADULT = "adult"
    COUPLE = "couple"
    MINOR = "minor"

    def __str__(self) -> str:
        return str(self.value)
