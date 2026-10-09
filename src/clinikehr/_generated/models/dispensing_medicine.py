from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier import Identifier


T = TypeVar("T", bound="DispensingMedicine")


@_attrs_define
class DispensingMedicine:
    """
    Attributes:
        name (None | str | Unset):
        generic_name (None | str | Unset):
        brand_name (None | str | Unset):
        identifiers (list[Identifier] | Unset):
    """

    name: None | str | Unset = UNSET
    generic_name: None | str | Unset = UNSET
    brand_name: None | str | Unset = UNSET
    identifiers: list[Identifier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        generic_name: None | str | Unset
        if isinstance(self.generic_name, Unset):
            generic_name = UNSET
        else:
            generic_name = self.generic_name

        brand_name: None | str | Unset
        if isinstance(self.brand_name, Unset):
            brand_name = UNSET
        else:
            brand_name = self.brand_name

        identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if generic_name is not UNSET:
            field_dict["generic_name"] = generic_name
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identifier import Identifier  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_generic_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_name = _parse_generic_name(d.pop("generic_name", UNSET))

        def _parse_brand_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_name = _parse_brand_name(d.pop("brand_name", UNSET))

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: list[Identifier] | Unset = UNSET
        if _identifiers is not UNSET:
            identifiers = []
            for identifiers_item_data in _identifiers:
                identifiers_item = Identifier.from_dict(identifiers_item_data)

                identifiers.append(identifiers_item)

        dispensing_medicine = cls(
            name=name,
            generic_name=generic_name,
            brand_name=brand_name,
            identifiers=identifiers,
        )

        dispensing_medicine.additional_properties = d
        return dispensing_medicine

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
