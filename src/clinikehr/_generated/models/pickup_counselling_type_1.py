from enum import StrEnum


class PickupCounsellingType1(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
