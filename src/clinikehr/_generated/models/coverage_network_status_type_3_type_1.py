from enum import StrEnum


class CoverageNetworkStatusType3Type1(StrEnum):
    IN_NETWORK = "in_network"
    OUT_OF_NETWORK = "out_of_network"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
