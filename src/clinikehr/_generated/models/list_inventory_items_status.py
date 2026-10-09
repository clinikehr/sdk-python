from enum import StrEnum


class ListInventoryItemsStatus(StrEnum):
    ACTIVE = "active"
    ALL = "all"
    ARCHIVED = "archived"

    def __str__(self) -> str:
        return str(self.value)
