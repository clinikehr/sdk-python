from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0
    from ..models.listing_search_request_item_type_1 import ListingSearchRequestItemType1
    from ..models.listing_search_request_near import ListingSearchRequestNear


T = TypeVar("T", bound="ListingSearchRequest")


@_attrs_define
class ListingSearchRequest:
    """
    Attributes:
        item (ListingSearchRequestItemType0 | ListingSearchRequestItemType1): Exactly one of an identifier {system,
            value} or a free-text {q}.
        near (ListingSearchRequestNear | Unset):
        limit (int | Unset):  Default: 25.
    """

    item: ListingSearchRequestItemType0 | ListingSearchRequestItemType1
    near: ListingSearchRequestNear | Unset = UNSET
    limit: int | Unset = 25

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0  # noqa: PLC0415

        item: dict[str, Any]
        if isinstance(self.item, ListingSearchRequestItemType0):
            item = self.item.to_dict()
        else:
            item = self.item.to_dict()

        near: dict[str, Any] | Unset = UNSET
        if not isinstance(self.near, Unset):
            near = self.near.to_dict()

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item": item,
            }
        )
        if near is not UNSET:
            field_dict["near"] = near
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0  # noqa: PLC0415
        from ..models.listing_search_request_item_type_1 import ListingSearchRequestItemType1  # noqa: PLC0415
        from ..models.listing_search_request_near import ListingSearchRequestNear  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_item(data: object) -> ListingSearchRequestItemType0 | ListingSearchRequestItemType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_listing_search_request_item_type_0 = ListingSearchRequestItemType0.from_dict(data)

                return componentsschemas_listing_search_request_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_listing_search_request_item_type_1 = ListingSearchRequestItemType1.from_dict(data)

            return componentsschemas_listing_search_request_item_type_1

        item = _parse_item(d.pop("item"))

        _near = d.pop("near", UNSET)
        near: ListingSearchRequestNear | Unset
        if isinstance(_near, Unset):
            near = UNSET
        else:
            near = ListingSearchRequestNear.from_dict(_near)

        limit = d.pop("limit", UNSET)

        listing_search_request = cls(
            item=item,
            near=near,
            limit=limit,
        )

        return listing_search_request
