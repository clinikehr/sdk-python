from enum import StrEnum


class CrmContactLifecycleStageType2Type1(StrEnum):
    CUSTOMER = "customer"
    INQUIRY = "inquiry"
    LEAD = "lead"
    LOST = "lost"
    PROSPECT = "prospect"
    WAITLIST = "waitlist"

    def __str__(self) -> str:
        return str(self.value)
