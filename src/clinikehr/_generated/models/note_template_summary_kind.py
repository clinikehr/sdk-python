from enum import StrEnum


class NoteTemplateSummaryKind(StrEnum):
    CUSTOM_TEMPLATE = "custom_template"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
