from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InventoryAdjustRequest")


@_attrs_define
class InventoryAdjustRequest:
    """
    Attributes:
        item_id (UUID):
        location_id (UUID):
        lot_id (UUID):
        delta (float): Positive or negative.
        reason (str):
    """

    item_id: UUID
    location_id: UUID
    lot_id: UUID
    delta: float
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        location_id = str(self.location_id)

        lot_id = str(self.lot_id)

        delta = self.delta

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "location_id": location_id,
                "lot_id": lot_id,
                "delta": delta,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        location_id = UUID(d.pop("location_id"))

        lot_id = UUID(d.pop("lot_id"))

        delta = d.pop("delta")

        reason = d.pop("reason")

        inventory_adjust_request = cls(
            item_id=item_id,
            location_id=location_id,
            lot_id=lot_id,
            delta=delta,
            reason=reason,
        )

        inventory_adjust_request.additional_properties = d
        return inventory_adjust_request

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
