from enum import StrEnum


class PatientGenotypeType3Type1(StrEnum):
    AA = "AA"
    AC = "AC"
    AS = "AS"
    SC = "SC"
    SS = "SS"

    def __str__(self) -> str:
        return str(self.value)
