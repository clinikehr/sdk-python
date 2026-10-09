from enum import StrEnum


class ListingSearchResultMatchType1(StrEnum):
    CODE = "code"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
