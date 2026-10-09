from enum import StrEnum


class PatientImportJobInputFormat(StrEnum):
    FHIR_BUNDLE = "fhir_bundle"
    JSON_ARRAY = "json_array"
    NDJSON = "ndjson"

    def __str__(self) -> str:
        return str(self.value)
