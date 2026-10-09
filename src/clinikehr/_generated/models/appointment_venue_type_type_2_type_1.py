from enum import StrEnum


class AppointmentVenueTypeType2Type1(StrEnum):
    MOBILE_CLINIC = "mobile_clinic"
    ONLINE = "online"
    PHYSICAL = "physical"

    def __str__(self) -> str:
        return str(self.value)
