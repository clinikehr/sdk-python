from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier import Identifier
    from ..models.money import Money


T = TypeVar("T", bound="InventoryItem")


@_attrs_define
class InventoryItem:
    """
    Attributes:
        id (UUID):
        name (str):
        is_active (bool): False while the item is archived.
        identifiers (list[Identifier]):
        generic_name (None | str | Unset):
        brand_name (None | str | Unset):
        strength (None | str | Unset):
        dosage_form (None | str | Unset):
        category (None | str | Unset):
        item_type (None | str | Unset):
        unit_of_measure (None | str | Unset):
        archived_at (datetime.datetime | None | Unset): When the item was archived, or null while it is active.
        retail_price (Money | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    name: str
    is_active: bool
    identifiers: list[Identifier]
    generic_name: None | str | Unset = UNSET
    brand_name: None | str | Unset = UNSET
    strength: None | str | Unset = UNSET
    dosage_form: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    item_type: None | str | Unset = UNSET
    unit_of_measure: None | str | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    retail_price: Money | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money import Money  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        is_active = self.is_active

        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.to_dict()
            identifiers.append(identifiers_item)

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

        item_type: None | str | Unset
        if isinstance(self.item_type, Unset):
            item_type = UNSET
        else:
            item_type = self.item_type

        unit_of_measure: None | str | Unset
        if isinstance(self.unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = self.unit_of_measure

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        retail_price: dict[str, Any] | None | Unset
        if isinstance(self.retail_price, Unset):
            retail_price = UNSET
        elif isinstance(self.retail_price, Money):
            retail_price = self.retail_price.to_dict()
        else:
            retail_price = self.retail_price

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_active": is_active,
                "identifiers": identifiers,
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
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if retail_price is not UNSET:
            field_dict["retail_price"] = retail_price
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identifier import Identifier  # noqa: PLC0415
        from ..models.money import Money  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        is_active = d.pop("is_active")

        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = Identifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

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

        def _parse_item_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_type = _parse_item_type(d.pop("item_type", UNSET))

        def _parse_unit_of_measure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_of_measure = _parse_unit_of_measure(d.pop("unit_of_measure", UNSET))

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_retail_price(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retail_price_type_0 = Money.from_dict(data)

                return retail_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        retail_price = _parse_retail_price(d.pop("retail_price", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        inventory_item = cls(
            id=id,
            name=name,
            is_active=is_active,
            identifiers=identifiers,
            generic_name=generic_name,
            brand_name=brand_name,
            strength=strength,
            dosage_form=dosage_form,
            category=category,
            item_type=item_type,
            unit_of_measure=unit_of_measure,
            archived_at=archived_at,
            retail_price=retail_price,
            updated_at=updated_at,
        )

        inventory_item.additional_properties = d
        return inventory_item

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
