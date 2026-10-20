from enum import StrEnum


class OutreachStationProgressStatus(StrEnum):
    DONE = "done"
    PENDING = "pending"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
