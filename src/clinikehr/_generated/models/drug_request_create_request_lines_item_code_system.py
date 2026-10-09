from enum import StrEnum


class DrugRequestCreateRequestLinesItemCodeSystem(StrEnum):
    GTIN = "gtin"
    NAFDAC = "nafdac"
    NDC = "ndc"
    PARTNER = "partner"
    RXCUI = "rxcui"

    def __str__(self) -> str:
        return str(self.value)
