from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingSearchRequestNear")


@_attrs_define
class ListingSearchRequestNear:
    """
    Attributes:
        lat (float | Unset):
        lng (float | Unset):
        radius_km (float | Unset):
    """

    lat: float | Unset = UNSET
    lng: float | Unset = UNSET
    radius_km: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lng = self.lng

        radius_km = self.radius_km

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if radius_km is not UNSET:
            field_dict["radius_km"] = radius_km

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        radius_km = d.pop("radius_km", UNSET)

        listing_search_request_near = cls(
            lat=lat,
            lng=lng,
            radius_km=radius_km,
        )

        return listing_search_request_near
