from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryStock")


@_attrs_define
class InventoryStock:
    """
    Attributes:
        item_id (UUID):
        quantity (str): Decimal string.
        location_id (None | Unset | UUID):
        lot_id (None | str | Unset):
        reserved_quantity (str | Unset): Decimal string. Units already committed elsewhere — never counted as sellable.
        expiry_date (datetime.date | None | Unset): The lot's expiry date. Null for stock held without a lot, or a lot
            with none recorded.
        lot_status (None | str | Unset): The lot's own status (e.g. active, quarantined, recalled). Null when there is
            no lot.
        as_of (datetime.datetime | None | Unset):
    """

    item_id: UUID
    quantity: str
    location_id: None | Unset | UUID = UNSET
    lot_id: None | str | Unset = UNSET
    reserved_quantity: str | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    lot_status: None | str | Unset = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        quantity = self.quantity

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        elif isinstance(self.location_id, UUID):
            location_id = str(self.location_id)
        else:
            location_id = self.location_id

        lot_id: None | str | Unset
        if isinstance(self.lot_id, Unset):
            lot_id = UNSET
        else:
            lot_id = self.lot_id

        reserved_quantity = self.reserved_quantity

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        lot_status: None | str | Unset
        if isinstance(self.lot_status, Unset):
            lot_status = UNSET
        else:
            lot_status = self.lot_status

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "quantity": quantity,
            }
        )
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if lot_id is not UNSET:
            field_dict["lot_id"] = lot_id
        if reserved_quantity is not UNSET:
            field_dict["reserved_quantity"] = reserved_quantity
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if lot_status is not UNSET:
            field_dict["lot_status"] = lot_status
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        quantity = d.pop("quantity")

        def _parse_location_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_id_type_0 = UUID(data)

                return location_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        def _parse_lot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_id = _parse_lot_id(d.pop("lot_id", UNSET))

        reserved_quantity = d.pop("reserved_quantity", UNSET)

        def _parse_expiry_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        def _parse_lot_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_status = _parse_lot_status(d.pop("lot_status", UNSET))

        def _parse_as_of(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        as_of = _parse_as_of(d.pop("as_of", UNSET))

        inventory_stock = cls(
            item_id=item_id,
            quantity=quantity,
            location_id=location_id,
            lot_id=lot_id,
            reserved_quantity=reserved_quantity,
            expiry_date=expiry_date,
            lot_status=lot_status,
            as_of=as_of,
        )

        inventory_stock.additional_properties = d
        return inventory_stock

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
