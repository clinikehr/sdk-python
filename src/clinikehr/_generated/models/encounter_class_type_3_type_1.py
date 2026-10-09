from enum import StrEnum


class EncounterClassType3Type1(StrEnum):
    AMBULATORY = "ambulatory"
    EMERGENCY = "emergency"
    HOME_HEALTH = "home_health"
    INPATIENT = "inpatient"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
