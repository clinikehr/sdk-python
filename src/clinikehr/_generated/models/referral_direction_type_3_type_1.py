from enum import StrEnum


class ReferralDirectionType3Type1(StrEnum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
