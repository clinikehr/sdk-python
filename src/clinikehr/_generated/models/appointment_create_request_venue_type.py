from enum import StrEnum


class AppointmentCreateRequestVenueType(StrEnum):
    MOBILE_CLINIC = "mobile_clinic"
    ONLINE = "online"
    PHYSICAL = "physical"

    def __str__(self) -> str:
        return str(self.value)
