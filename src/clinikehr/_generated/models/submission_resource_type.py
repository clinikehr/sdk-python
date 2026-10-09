from enum import StrEnum


class SubmissionResourceType(StrEnum):
    ALLERGY = "allergy"
    CONDITION = "condition"
    MEDICATION_STATEMENT = "medication_statement"
    REFERRAL = "referral"

    def __str__(self) -> str:
        return str(self.value)
