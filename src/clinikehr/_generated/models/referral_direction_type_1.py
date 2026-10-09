from enum import StrEnum


class ReferralDirectionType1(StrEnum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
