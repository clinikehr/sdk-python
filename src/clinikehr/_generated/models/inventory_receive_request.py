from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryReceiveRequest")


@_attrs_define
class InventoryReceiveRequest:
    """
    Attributes:
        item_id (UUID):
        location_id (UUID):
        quantity (float):
        lot_number (str | Unset):
        expiry_date (datetime.date | Unset): Required, and refused if in the past, for item_type IN (medication,
            vaccine, injectable) — regardless of the clinic's own setting.
        unit_cost (float | Unset):
        vendor_id (UUID | Unset):
        reference (str | Unset): Echoed back only — no column exists on inventory_transactions to persist it.
    """

    item_id: UUID
    location_id: UUID
    quantity: float
    lot_number: str | Unset = UNSET
    expiry_date: datetime.date | Unset = UNSET
    unit_cost: float | Unset = UNSET
    vendor_id: UUID | Unset = UNSET
    reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        location_id = str(self.location_id)

        quantity = self.quantity

        lot_number = self.lot_number

        expiry_date: str | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        unit_cost = self.unit_cost

        vendor_id: str | Unset = UNSET
        if not isinstance(self.vendor_id, Unset):
            vendor_id = str(self.vendor_id)

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "location_id": location_id,
                "quantity": quantity,
            }
        )
        if lot_number is not UNSET:
            field_dict["lot_number"] = lot_number
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if unit_cost is not UNSET:
            field_dict["unit_cost"] = unit_cost
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        location_id = UUID(d.pop("location_id"))

        quantity = d.pop("quantity")

        lot_number = d.pop("lot_number", UNSET)

        _expiry_date = d.pop("expiry_date", UNSET)
        expiry_date: datetime.date | Unset
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = datetime.date.fromisoformat(_expiry_date)

        unit_cost = d.pop("unit_cost", UNSET)

        _vendor_id = d.pop("vendor_id", UNSET)
        vendor_id: UUID | Unset
        if isinstance(_vendor_id, Unset):
            vendor_id = UNSET
        else:
            vendor_id = UUID(_vendor_id)

        reference = d.pop("reference", UNSET)

        inventory_receive_request = cls(
            item_id=item_id,
            location_id=location_id,
            quantity=quantity,
            lot_number=lot_number,
            expiry_date=expiry_date,
            unit_cost=unit_cost,
            vendor_id=vendor_id,
            reference=reference,
        )

        inventory_receive_request.additional_properties = d
        return inventory_receive_request

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
