from enum import StrEnum


class PickupCounsellingType2Type1(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"

    def __str__(self) -> str:
        return str(self.value)
