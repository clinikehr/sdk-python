from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.medication_code_system import MedicationCodeSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicationCode")


@_attrs_define
class MedicationCode:
    """A coded medicine. `system` is `rxnorm` or `local` (a clinic's or sender's own code, never mapped to a standard). An
    `rxnorm` code is accepted only when it is a recognised RxNorm code in the platform's own drug data; `display` is the
    platform's own name for it and is never taken from the sender. `display` is null for a `local` code.

        Attributes:
            system (MedicationCodeSystem):
            code (str):
            display (None | str | Unset):
    """

    system: MedicationCodeSystem
    code: str
    display: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        display: None | str | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        else:
            display = self.display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system": system,
                "code": code,
            }
        )
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = MedicationCodeSystem(d.pop("system"))

        code = d.pop("code")

        def _parse_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        medication_code = cls(
            system=system,
            code=code,
            display=display,
        )

        medication_code.additional_properties = d
        return medication_code

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
