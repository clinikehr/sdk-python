from enum import StrEnum


class ListingSearchResultMatchType3Type1(StrEnum):
    CODE = "code"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
