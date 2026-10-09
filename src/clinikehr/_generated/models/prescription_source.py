from enum import StrEnum


class PrescriptionSource(StrEnum):
    CLINIC = "clinic"
    EPRESCRIBE = "eprescribe"

    def __str__(self) -> str:
        return str(self.value)
