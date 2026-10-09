from enum import StrEnum


class ConnectionSummaryEnvironment(StrEnum):
    LIVE = "live"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
