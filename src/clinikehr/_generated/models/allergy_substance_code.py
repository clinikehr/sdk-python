from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.allergy_substance_code_system import AllergySubstanceCodeSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="AllergySubstanceCode")


@_attrs_define
class AllergySubstanceCode:
    """A coded substance. `system` is `rxnorm`, `snomed-ct` or `local` (a clinic's own code, never mapped to an HL7
    system). An `rxnorm` code is accepted only when it is a verified RxNorm code the platform recognises; `display` is
    the platform's own term for a verified RxNorm code and is never taken from the sender.

        Attributes:
            system (AllergySubstanceCodeSystem):
            code (str):
            display (None | str | Unset):
    """

    system: AllergySubstanceCodeSystem
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
        system = AllergySubstanceCodeSystem(d.pop("system"))

        code = d.pop("code")

        def _parse_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        allergy_substance_code = cls(
            system=system,
            code=code,
            display=display,
        )

        allergy_substance_code.additional_properties = d
        return allergy_substance_code

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
