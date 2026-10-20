from enum import StrEnum


class PickupCollectionCreateCollectedBy(StrEnum):
    AGENT = "agent"
    PATIENT = "patient"

    def __str__(self) -> str:
        return str(self.value)
