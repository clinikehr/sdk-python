from enum import StrEnum


class InsurancePreAuthorizationSubmitItemItemType(StrEnum):
    CONSULTATION = "consultation"
    EQUIPMENT = "equipment"
    HOSPITALIZATION = "hospitalization"
    IMAGING = "imaging"
    LAB_TEST = "lab_test"
    MEDICATION = "medication"
    PROCEDURE = "procedure"
    RADIOLOGY = "radiology"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
