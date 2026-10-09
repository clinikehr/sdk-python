from enum import StrEnum


class AllergyCreateCategoryItem(StrEnum):
    BIOLOGIC = "biologic"
    ENVIRONMENT = "environment"
    FOOD = "food"
    MEDICATION = "medication"

    def __str__(self) -> str:
        return str(self.value)
