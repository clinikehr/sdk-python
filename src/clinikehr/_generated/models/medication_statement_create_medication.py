from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medication_statement_create_medication_code import MedicationStatementCreateMedicationCode


T = TypeVar("T", bound="MedicationStatementCreateMedication")


@_attrs_define
class MedicationStatementCreateMedication:
    """
    Attributes:
        text (str):
        code (MedicationStatementCreateMedicationCode | Unset):
    """

    text: str
    code: MedicationStatementCreateMedicationCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medication_statement_create_medication_code import (
            MedicationStatementCreateMedicationCode,  # noqa: PLC0415
        )

        d = dict(src_dict)
        text = d.pop("text")

        _code = d.pop("code", UNSET)
        code: MedicationStatementCreateMedicationCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = MedicationStatementCreateMedicationCode.from_dict(_code)

        medication_statement_create_medication = cls(
            text=text,
            code=code,
        )

        return medication_statement_create_medication
