from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemUpdateRequest")


@_attrs_define
class InventoryItemUpdateRequest:
    """Absent ≠ null. Idempotency-Key optional — a PATCH is naturally idempotent.

    Attributes:
        name (str | Unset):
        generic_name (None | str | Unset):
        brand_name (None | str | Unset):
        strength (None | str | Unset):
        dosage_form (None | str | Unset):
        category (None | str | Unset):
        unit_of_measure (None | str | Unset):
        upc (None | str | Unset):
        nafdac_no (None | str | Unset):
        ndc (None | str | Unset):
        default_sale_price (float | Unset): Above the clinic's configured percentage threshold is refused
            (limit_exceeded).
        is_active (bool | Unset):
    """

    name: str | Unset = UNSET
    generic_name: None | str | Unset = UNSET
    brand_name: None | str | Unset = UNSET
    strength: None | str | Unset = UNSET
    dosage_form: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    unit_of_measure: None | str | Unset = UNSET
    upc: None | str | Unset = UNSET
    nafdac_no: None | str | Unset = UNSET
    ndc: None | str | Unset = UNSET
    default_sale_price: float | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        strength: None | str | Unset
        if isinstance(self.strength, Unset):
            strength = UNSET
        else:
            strength = self.strength

        dosage_form: None | str | Unset
        if isinstance(self.dosage_form, Unset):
            dosage_form = UNSET
        else:
            dosage_form = self.dosage_form

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        unit_of_measure: None | str | Unset
        if isinstance(self.unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = self.unit_of_measure

        upc: None | str | Unset
        if isinstance(self.upc, Unset):
            upc = UNSET
        else:
            upc = self.upc

        nafdac_no: None | str | Unset
        if isinstance(self.nafdac_no, Unset):
            nafdac_no = UNSET
        else:
            nafdac_no = self.nafdac_no

        ndc: None | str | Unset
        if isinstance(self.ndc, Unset):
            ndc = UNSET
        else:
            ndc = self.ndc

        default_sale_price = self.default_sale_price

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if generic_name is not UNSET:
            field_dict["generic_name"] = generic_name
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if strength is not UNSET:
            field_dict["strength"] = strength
        if dosage_form is not UNSET:
            field_dict["dosage_form"] = dosage_form
        if category is not UNSET:
            field_dict["category"] = category
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if upc is not UNSET:
            field_dict["upc"] = upc
        if nafdac_no is not UNSET:
            field_dict["nafdac_no"] = nafdac_no
        if ndc is not UNSET:
            field_dict["ndc"] = ndc
        if default_sale_price is not UNSET:
            field_dict["default_sale_price"] = default_sale_price
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        def _parse_strength(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strength = _parse_strength(d.pop("strength", UNSET))

        def _parse_dosage_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dosage_form = _parse_dosage_form(d.pop("dosage_form", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_unit_of_measure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_of_measure = _parse_unit_of_measure(d.pop("unit_of_measure", UNSET))

        def _parse_upc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upc = _parse_upc(d.pop("upc", UNSET))

        def _parse_nafdac_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nafdac_no = _parse_nafdac_no(d.pop("nafdac_no", UNSET))

        def _parse_ndc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ndc = _parse_ndc(d.pop("ndc", UNSET))

        default_sale_price = d.pop("default_sale_price", UNSET)

        is_active = d.pop("is_active", UNSET)

        inventory_item_update_request = cls(
            name=name,
            generic_name=generic_name,
            brand_name=brand_name,
            strength=strength,
            dosage_form=dosage_form,
            category=category,
            unit_of_measure=unit_of_measure,
            upc=upc,
            nafdac_no=nafdac_no,
            ndc=ndc,
            default_sale_price=default_sale_price,
            is_active=is_active,
        )

        inventory_item_update_request.additional_properties = d
        return inventory_item_update_request

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
