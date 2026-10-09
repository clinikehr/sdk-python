from enum import StrEnum


class PatientPhonePermissionType2Type1(StrEnum):
    NO_CALL = "no_call"
    TEXT_OK = "text_ok"
    TEXT_VOICEMAIL_OK = "text_voicemail_ok"
    VOICEMAIL_OK = "voicemail_ok"

    def __str__(self) -> str:
        return str(self.value)
