from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.condition_code_system import ConditionCodeSystem

T = TypeVar("T", bound="ConditionCode")


@_attrs_define
class ConditionCode:
    """A coded diagnosis. `system` names the code system: `icd-10-cm`, `icd-10`, `snomed-ct`, or `local` (a clinic's own
    code, never mapped to an HL7 system). The code is checked for SHAPE only — it is not looked up in a terminology.

        Attributes:
            system (ConditionCodeSystem):
            code (str):
    """

    system: ConditionCodeSystem
    code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        system = ConditionCodeSystem(d.pop("system"))

        code = d.pop("code")

        condition_code = cls(
            system=system,
            code=code,
        )

        condition_code.additional_properties = d
        return condition_code

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
