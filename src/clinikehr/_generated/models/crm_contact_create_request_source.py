from enum import StrEnum


class CrmContactCreateRequestSource(StrEnum):
    BOOKING_PAGE = "booking_page"
    CONTACT_FORM = "contact_form"
    IMPORT = "import"
    MANUAL = "manual"
    PHONE = "phone"
    REFERRAL = "referral"
    SOCIAL = "social"
    WALK_IN = "walk_in"
    WEBSITE = "website"

    def __str__(self) -> str:
        return str(self.value)
