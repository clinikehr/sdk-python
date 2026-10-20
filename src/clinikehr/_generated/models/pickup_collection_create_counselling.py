from enum import StrEnum


class PickupCollectionCreateCounselling(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
