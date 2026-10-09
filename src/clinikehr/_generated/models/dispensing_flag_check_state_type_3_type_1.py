from enum import StrEnum


class DispensingFlagCheckStateType3Type1(StrEnum):
    CLEAR = "clear"
    NOT_SHOWN_OFFLINE = "not_shown_offline"
    NOT_SHOWN_PENDING = "not_shown_pending"
    SHOWN_ACKNOWLEDGED = "shown_acknowledged"

    def __str__(self) -> str:
        return str(self.value)
