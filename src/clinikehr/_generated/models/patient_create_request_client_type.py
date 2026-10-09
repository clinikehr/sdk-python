from enum import StrEnum


class PatientCreateRequestClientType(StrEnum):
    ADULT = "adult"
    MINOR = "minor"

    def __str__(self) -> str:
        return str(self.value)
