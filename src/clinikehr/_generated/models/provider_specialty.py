from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProviderSpecialty")


@_attrs_define
class ProviderSpecialty:
    """
    Attributes:
        code (str):
        display_name (str):
        is_primary (bool):
    """

    code: str
    display_name: str
    is_primary: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        display_name = self.display_name

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "display_name": display_name,
                "is_primary": is_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        display_name = d.pop("display_name")

        is_primary = d.pop("is_primary")

        provider_specialty = cls(
            code=code,
            display_name=display_name,
            is_primary=is_primary,
        )

        provider_specialty.additional_properties = d
        return provider_specialty

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
