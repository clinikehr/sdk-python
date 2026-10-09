from enum import StrEnum


class PatientImportJobStatus(StrEnum):
    FAILED = "failed"
    NEEDS_REVIEW = "needs_review"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    VALIDATING = "validating"

    def __str__(self) -> str:
        return str(self.value)
