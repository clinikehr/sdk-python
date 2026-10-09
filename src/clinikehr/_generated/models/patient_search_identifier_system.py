from enum import StrEnum


class PatientSearchIdentifierSystem(StrEnum):
    EMAIL = "email"
    MRN = "mrn"
    PHONE = "phone"

    def __str__(self) -> str:
        return str(self.value)
