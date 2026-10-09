from enum import StrEnum


class PatientGuardianRelationshipType3Type1(StrEnum):
    AUNT_UNCLE = "aunt_uncle"
    FOSTER_PARENT = "foster_parent"
    GRANDPARENT = "grandparent"
    LEGAL_GUARDIAN = "legal_guardian"
    OTHER = "other"
    PARENT = "parent"
    SIBLING = "sibling"
    STEP_PARENT = "step_parent"

    def __str__(self) -> str:
        return str(self.value)
