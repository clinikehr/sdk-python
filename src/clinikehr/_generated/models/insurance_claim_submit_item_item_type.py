from enum import StrEnum


class InsuranceClaimSubmitItemItemType(StrEnum):
    CONSULTATION = "consultation"
    EQUIPMENT = "equipment"
    HOSPITALIZATION = "hospitalization"
    IMAGING = "imaging"
    LAB_TEST = "lab_test"
    MEDICATION = "medication"
    OTHER = "other"
    PROCEDURE = "procedure"
    RADIOLOGY = "radiology"
    ROOM_CHARGE = "room_charge"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
