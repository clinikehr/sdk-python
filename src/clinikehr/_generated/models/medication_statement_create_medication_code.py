from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.medication_statement_create_medication_code_system import MedicationStatementCreateMedicationCodeSystem

T = TypeVar("T", bound="MedicationStatementCreateMedicationCode")


@_attrs_define
class MedicationStatementCreateMedicationCode:
    """
    Attributes:
        system (MedicationStatementCreateMedicationCodeSystem):
        code (str): An `rxnorm` code is 1 to 8 digits.
    """

    system: MedicationStatementCreateMedicationCodeSystem
    code: str

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "system": system,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = MedicationStatementCreateMedicationCodeSystem(d.pop("system"))

        code = d.pop("code")

        medication_statement_create_medication_code = cls(
            system=system,
            code=code,
        )

        return medication_statement_create_medication_code
