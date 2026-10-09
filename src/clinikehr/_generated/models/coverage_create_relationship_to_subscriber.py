from enum import StrEnum


class CoverageCreateRelationshipToSubscriber(StrEnum):
    CADAVER_DONOR = "cadaver_donor"
    CHILD = "child"
    EMPLOYEE = "employee"
    LIFE_PARTNER = "life_partner"
    ORGAN_DONOR = "organ_donor"
    OTHER = "other"
    SELF = "self"
    SPOUSE = "spouse"

    def __str__(self) -> str:
        return str(self.value)
