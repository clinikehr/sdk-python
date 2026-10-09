from enum import StrEnum


class PatientUpdateRequestClientType(StrEnum):
    ADULT = "adult"
    MINOR = "minor"

    def __str__(self) -> str:
        return str(self.value)
