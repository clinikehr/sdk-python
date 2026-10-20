from enum import StrEnum


class ListOutreachEventsStatus(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
