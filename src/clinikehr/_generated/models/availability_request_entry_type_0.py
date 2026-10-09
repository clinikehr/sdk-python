from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AvailabilityRequestEntryType0")


@_attrs_define
class AvailabilityRequestEntryType0:
    """
    Attributes:
        item_id (UUID):
    """

    item_id: UUID

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item_id": item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        availability_request_entry_type_0 = cls(
            item_id=item_id,
        )

        return availability_request_entry_type_0
