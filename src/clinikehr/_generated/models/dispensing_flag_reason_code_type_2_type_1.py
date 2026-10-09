from enum import StrEnum


class DispensingFlagReasonCodeType2Type1(StrEnum):
    DAMAGED = "damaged"
    DOSE_CHANGED = "dose_changed"
    LOST = "lost"
    OTHER = "other"
    PRESCRIBER_INSTRUCTION = "prescriber_instruction"
    TRAVELLING = "travelling"

    def __str__(self) -> str:
        return str(self.value)
