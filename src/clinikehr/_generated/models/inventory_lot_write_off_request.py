from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryLotWriteOffRequest")


@_attrs_define
class InventoryLotWriteOffRequest:
    """
    Attributes:
        reason (str): Why the remaining stock is being written off (expired, damaged, recalled…). Required.
    """

    reason: str

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        inventory_lot_write_off_request = cls(
            reason=reason,
        )

        return inventory_lot_write_off_request
