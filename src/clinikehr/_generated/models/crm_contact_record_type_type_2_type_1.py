from enum import StrEnum


class CrmContactRecordTypeType2Type1(StrEnum):
    CONTACT = "contact"
    LEAD = "lead"
    PROSPECT = "prospect"
    REFERRAL = "referral"
    WAITLIST = "waitlist"

    def __str__(self) -> str:
        return str(self.value)
