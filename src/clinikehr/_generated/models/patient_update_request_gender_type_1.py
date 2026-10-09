from enum import StrEnum


class PatientUpdateRequestGenderType1(StrEnum):
    FEMALE = "female"
    MALE = "male"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
