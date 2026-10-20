from enum import StrEnum


class SubmissionResourceType(StrEnum):
    ALLERGY = "allergy"
    CONDITION = "condition"
    MEDICATION_STATEMENT = "medication_statement"
    OUTREACH_CHECKIN = "outreach_checkin"
    PRESCRIPTION_PICKUP_COLLECTION = "prescription_pickup_collection"
    REFERRAL = "referral"

    def __str__(self) -> str:
        return str(self.value)
