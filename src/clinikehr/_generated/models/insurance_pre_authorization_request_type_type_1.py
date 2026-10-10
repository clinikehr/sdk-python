from enum import StrEnum


class InsurancePreAuthorizationRequestTypeType1(StrEnum):
    CONSULTATION = "consultation"
    EQUIPMENT = "equipment"
    HOSPITALIZATION = "hospitalization"
    LAB_TEST = "lab_test"
    MEDICATION = "medication"
    PROCEDURE = "procedure"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
