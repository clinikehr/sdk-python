from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemCreateRequest")


@_attrs_define
class InventoryItemCreateRequest:
    """Unknown fields refused by name. container_sale_price/container_cost are refused outright.

    Attributes:
        name (str):
        item_type (str):
        generic_name (str | Unset):
        brand_name (str | Unset):
        strength (str | Unset):
        dosage_form (str | Unset):
        category (str | Unset):
        unit_of_measure (str | Unset):
        upc (str | Unset): gtin identifier.
        nafdac_no (str | Unset):
        ndc (str | Unset):
        default_sale_price (float | Unset):
        container_quantity (float | Unset):
        container_label (str | Unset):
    """

    name: str
    item_type: str
    generic_name: str | Unset = UNSET
    brand_name: str | Unset = UNSET
    strength: str | Unset = UNSET
    dosage_form: str | Unset = UNSET
    category: str | Unset = UNSET
    unit_of_measure: str | Unset = UNSET
    upc: str | Unset = UNSET
    nafdac_no: str | Unset = UNSET
    ndc: str | Unset = UNSET
    default_sale_price: float | Unset = UNSET
    container_quantity: float | Unset = UNSET
    container_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        item_type = self.item_type

        generic_name = self.generic_name

        brand_name = self.brand_name

        strength = self.strength

        dosage_form = self.dosage_form

        category = self.category

        unit_of_measure = self.unit_of_measure

        upc = self.upc

        nafdac_no = self.nafdac_no

        ndc = self.ndc

        default_sale_price = self.default_sale_price

        container_quantity = self.container_quantity

        container_label = self.container_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "item_type": item_type,
            }
        )
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
        if container_quantity is not UNSET:
            field_dict["container_quantity"] = container_quantity
        if container_label is not UNSET:
            field_dict["container_label"] = container_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        item_type = d.pop("item_type")

        generic_name = d.pop("generic_name", UNSET)

        brand_name = d.pop("brand_name", UNSET)

        strength = d.pop("strength", UNSET)

        dosage_form = d.pop("dosage_form", UNSET)

        category = d.pop("category", UNSET)

        unit_of_measure = d.pop("unit_of_measure", UNSET)

        upc = d.pop("upc", UNSET)

        nafdac_no = d.pop("nafdac_no", UNSET)

        ndc = d.pop("ndc", UNSET)

        default_sale_price = d.pop("default_sale_price", UNSET)

        container_quantity = d.pop("container_quantity", UNSET)

        container_label = d.pop("container_label", UNSET)

        inventory_item_create_request = cls(
            name=name,
            item_type=item_type,
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
            container_quantity=container_quantity,
            container_label=container_label,
        )

        inventory_item_create_request.additional_properties = d
        return inventory_item_create_request

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
