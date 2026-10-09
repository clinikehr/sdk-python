from enum import StrEnum


class ListCareProvidersType(StrEnum):
    OTHER = "other"
    PCP = "pcp"
    REFERRING = "referring"
    SPECIALIST = "specialist"

    def __str__(self) -> str:
        return str(self.value)
