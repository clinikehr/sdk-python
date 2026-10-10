from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsuranceDiagnosisInput")


@_attrs_define
class InsuranceDiagnosisInput:
    """
    Attributes:
        icd_code (str):
        name (str | Unset):
        is_primary (bool | Unset):
    """

    icd_code: str
    name: str | Unset = UNSET
    is_primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        icd_code = self.icd_code

        name = self.name

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "icd_code": icd_code,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icd_code = d.pop("icd_code")

        name = d.pop("name", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        insurance_diagnosis_input = cls(
            icd_code=icd_code,
            name=name,
            is_primary=is_primary,
        )

        return insurance_diagnosis_input
