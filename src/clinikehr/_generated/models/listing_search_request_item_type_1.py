from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListingSearchRequestItemType1")


@_attrs_define
class ListingSearchRequestItemType1:
    """
    Attributes:
        q (str): Free-text name match. Labelled as a text match, never as equivalence.
    """

    q: str

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "q": q,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        q = d.pop("q")

        listing_search_request_item_type_1 = cls(
            q=q,
        )

        return listing_search_request_item_type_1
