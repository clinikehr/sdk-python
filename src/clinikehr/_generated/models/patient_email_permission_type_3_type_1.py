from enum import StrEnum


class PatientEmailPermissionType3Type1(StrEnum):
    EMAIL_OK = "email_ok"
    NO_EMAIL = "no_email"

    def __str__(self) -> str:
        return str(self.value)
