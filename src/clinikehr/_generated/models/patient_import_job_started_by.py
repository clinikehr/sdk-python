from enum import StrEnum


class PatientImportJobStartedBy(StrEnum):
    KEY = "key"
    SESSION = "session"

    def __str__(self) -> str:
        return str(self.value)
