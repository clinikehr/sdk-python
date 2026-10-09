from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryLotWriteOff")


@_attrs_define
class InventoryLotWriteOff:
    """What a lot write-off did. The lot is archived; the ledger keeps the movement.

    Attributes:
        lot_id (UUID):
        item_id (UUID):
        quantity_written_off (str): Decimal string. The quantity that was on hand across the clinic's locations when the
            write-off ran.
        reason (str):
        archived_at (datetime.datetime | None | Unset):
    """

    lot_id: UUID
    item_id: UUID
    quantity_written_off: str
    reason: str
    archived_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lot_id = str(self.lot_id)

        item_id = str(self.item_id)

        quantity_written_off = self.quantity_written_off

        reason = self.reason

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lot_id": lot_id,
                "item_id": item_id,
                "quantity_written_off": quantity_written_off,
                "reason": reason,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lot_id = UUID(d.pop("lot_id"))

        item_id = UUID(d.pop("item_id"))

        quantity_written_off = d.pop("quantity_written_off")

        reason = d.pop("reason")

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

        inventory_lot_write_off = cls(
            lot_id=lot_id,
            item_id=item_id,
            quantity_written_off=quantity_written_off,
            reason=reason,
            archived_at=archived_at,
        )

        inventory_lot_write_off.additional_properties = d
        return inventory_lot_write_off

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
