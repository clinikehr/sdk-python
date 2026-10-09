from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryMovement")


@_attrs_define
class InventoryMovement:
    """The ledger movement receive/adjust/transfer just recorded — never the whole inventory_transactions row.

    Attributes:
        transaction_id (None | Unset | UUID):
        item_id (None | Unset | UUID):
        location_id (None | Unset | UUID):
        lot_id (None | str | Unset):
        quantity (None | str | Unset): Decimal string.
        idempotent_replay (bool | Unset):
    """

    transaction_id: None | Unset | UUID = UNSET
    item_id: None | Unset | UUID = UNSET
    location_id: None | Unset | UUID = UNSET
    lot_id: None | str | Unset = UNSET
    quantity: None | str | Unset = UNSET
    idempotent_replay: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id: None | str | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        elif isinstance(self.transaction_id, UUID):
            transaction_id = str(self.transaction_id)
        else:
            transaction_id = self.transaction_id

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

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

        quantity: None | str | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        idempotent_replay = self.idempotent_replay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if lot_id is not UNSET:
            field_dict["lot_id"] = lot_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if idempotent_replay is not UNSET:
            field_dict["idempotent_replay"] = idempotent_replay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transaction_id_type_0 = UUID(data)

                return transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transaction_id = _parse_transaction_id(d.pop("transaction_id", UNSET))

        def _parse_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_id_type_0 = UUID(data)

                return item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        item_id = _parse_item_id(d.pop("item_id", UNSET))

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

        def _parse_quantity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        idempotent_replay = d.pop("idempotent_replay", UNSET)

        inventory_movement = cls(
            transaction_id=transaction_id,
            item_id=item_id,
            location_id=location_id,
            lot_id=lot_id,
            quantity=quantity,
            idempotent_replay=idempotent_replay,
        )

        inventory_movement.additional_properties = d
        return inventory_movement

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
