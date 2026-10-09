from enum import StrEnum


class PatientDuplicateFlagStatus(StrEnum):
    DISMISSED = "dismissed"
    MERGED = "merged"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
