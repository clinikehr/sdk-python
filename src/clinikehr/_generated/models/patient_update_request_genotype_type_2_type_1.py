from enum import StrEnum


class PatientUpdateRequestGenotypeType2Type1(StrEnum):
    AA = "AA"
    AC = "AC"
    AS = "AS"
    SC = "SC"
    SS = "SS"

    def __str__(self) -> str:
        return str(self.value)
