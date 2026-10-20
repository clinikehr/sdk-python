from enum import StrEnum


class PickupCollectedByType1(StrEnum):
    AGENT = "agent"
    PATIENT = "patient"

    def __str__(self) -> str:
        return str(self.value)
