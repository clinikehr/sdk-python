from enum import StrEnum


class PatientUpdateRequestBloodTypeType3Type1(StrEnum):
    A = "A-"
    AB = "AB-"
    B = "B-"
    O = "O-"

    def __str__(self) -> str:
        return str(self.value)
