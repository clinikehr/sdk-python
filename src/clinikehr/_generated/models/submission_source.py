from enum import StrEnum


class SubmissionSource(StrEnum):
    API = "api"

    def __str__(self) -> str:
        return str(self.value)
