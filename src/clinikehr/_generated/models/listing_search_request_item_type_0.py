from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.listing_search_request_item_type_0_system import ListingSearchRequestItemType0System

T = TypeVar("T", bound="ListingSearchRequestItemType0")


@_attrs_define
class ListingSearchRequestItemType0:
    """
    Attributes:
        system (ListingSearchRequestItemType0System):
        value (str):
    """

    system: ListingSearchRequestItemType0System
    value: str

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "system": system,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = ListingSearchRequestItemType0System(d.pop("system"))

        value = d.pop("value")

        listing_search_request_item_type_0 = cls(
            system=system,
            value=value,
        )

        return listing_search_request_item_type_0
