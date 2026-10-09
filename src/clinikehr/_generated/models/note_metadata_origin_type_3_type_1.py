from enum import StrEnum


class NoteMetadataOriginType3Type1(StrEnum):
    API = "api"
    ASSISTANT_EXTERNAL = "assistant_external"
    ASSISTANT_INTERNAL = "assistant_internal"
    STAFF = "staff"

    def __str__(self) -> str:
        return str(self.value)
