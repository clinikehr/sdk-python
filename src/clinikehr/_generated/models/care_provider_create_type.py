from enum import StrEnum


class CareProviderCreateType(StrEnum):
    OTHER = "other"
    PCP = "pcp"
    REFERRING = "referring"
    SPECIALIST = "specialist"

    def __str__(self) -> str:
        return str(self.value)
