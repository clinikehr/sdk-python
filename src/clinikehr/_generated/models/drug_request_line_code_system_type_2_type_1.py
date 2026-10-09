from enum import StrEnum


class DrugRequestLineCodeSystemType2Type1(StrEnum):
    GTIN = "gtin"
    NAFDAC = "nafdac"
    NDC = "ndc"
    PARTNER = "partner"
    RXCUI = "rxcui"

    def __str__(self) -> str:
        return str(self.value)
