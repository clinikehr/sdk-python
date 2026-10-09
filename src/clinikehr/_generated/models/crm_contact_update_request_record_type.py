from enum import StrEnum


class CrmContactUpdateRequestRecordType(StrEnum):
    CONTACT = "contact"
    LEAD = "lead"
    PROSPECT = "prospect"
    REFERRAL = "referral"
    WAITLIST = "waitlist"

    def __str__(self) -> str:
        return str(self.value)
