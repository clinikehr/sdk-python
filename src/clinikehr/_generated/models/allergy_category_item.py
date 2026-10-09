from enum import StrEnum


class AllergyCategoryItem(StrEnum):
    BIOLOGIC = "biologic"
    ENVIRONMENT = "environment"
    FOOD = "food"
    MEDICATION = "medication"

    def __str__(self) -> str:
        return str(self.value)
