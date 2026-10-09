from enum import StrEnum


class CrmActivityCreateRequestType(StrEnum):
    CALL = "call"
    CAMPAIGN_SEND = "campaign_send"
    EMAIL = "email"
    MEETING = "meeting"
    NOTE = "note"
    SMS = "sms"
    STAGE_CHANGE = "stage_change"
    STATUS_CHANGE = "status_change"
    SYSTEM = "system"
    TASK_DONE = "task_done"

    def __str__(self) -> str:
        return str(self.value)
