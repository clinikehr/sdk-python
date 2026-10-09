from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InventoryTransferRequest")


@_attrs_define
class InventoryTransferRequest:
    """
    Attributes:
        item_id (UUID):
        from_location_id (UUID):
        to_location_id (UUID):
        quantity (float):
    """

    item_id: UUID
    from_location_id: UUID
    to_location_id: UUID
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        from_location_id = str(self.from_location_id)

        to_location_id = str(self.to_location_id)

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "from_location_id": from_location_id,
                "to_location_id": to_location_id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        from_location_id = UUID(d.pop("from_location_id"))

        to_location_id = UUID(d.pop("to_location_id"))

        quantity = d.pop("quantity")

        inventory_transfer_request = cls(
            item_id=item_id,
            from_location_id=from_location_id,
            to_location_id=to_location_id,
            quantity=quantity,
        )

        inventory_transfer_request.additional_properties = d
        return inventory_transfer_request

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
