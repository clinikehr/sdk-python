from enum import StrEnum


class AllergyEntry(StrEnum):
    LEGACY_TEXT = "legacy_text"
    NO_KNOWN_ALLERGIES = "no_known_allergies"
    STRUCTURED = "structured"

    def __str__(self) -> str:
        return str(self.value)
