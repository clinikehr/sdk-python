from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_band_type_1 import ListingBandType1
from ..models.listing_band_type_2_type_1 import ListingBandType2Type1
from ..models.listing_band_type_3_type_1 import ListingBandType3Type1
from ..models.listing_search_result_match_type_1 import ListingSearchResultMatchType1
from ..models.listing_search_result_match_type_2_type_1 import ListingSearchResultMatchType2Type1
from ..models.listing_search_result_match_type_3_type_1 import ListingSearchResultMatchType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingSearchResult")


@_attrs_define
class ListingSearchResult:
    """
    Attributes:
        band (ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None): Unlike inventory availability's
            band, listing carries a fourth value, `unknown` — the till heartbeat is missing or stale during open hours.
            Never coerced to another value; a listing route never returns an exact quantity.
        clinic_id (None | Unset | UUID):
        display_name (None | str | Unset):
        item_id (None | Unset | UUID):
        match (ListingSearchResultMatchType1 | ListingSearchResultMatchType2Type1 | ListingSearchResultMatchType3Type1 |
            None | Unset): Equivalence confidence label, never a license to surface an unlinked or excluded item.
        distance_km (float | None | Unset): Null when the pharmacy has no owner-placed pin, or no `near` was given —
            ranked last, never excluded.
        as_of (datetime.datetime | None | Unset):
        store_url (None | str | Unset): This product's page in the pharmacy's online store. Present ONLY when the store
            is safe to advertise (enabled page, able to take payment, not a listing-only plan, ClinikEHR holds the stock),
            the item is listed and not excluded, and an active, public store product is backed by this exact item. Otherwise
            null - never a guess, and never a link to the store's front page in place of the product. A pharmacy's own web
            address, when it has connected one, is used instead of the hosted address.
    """

    band: ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None
    clinic_id: None | Unset | UUID = UNSET
    display_name: None | str | Unset = UNSET
    item_id: None | Unset | UUID = UNSET
    match: (
        ListingSearchResultMatchType1
        | ListingSearchResultMatchType2Type1
        | ListingSearchResultMatchType3Type1
        | None
        | Unset
    ) = UNSET
    distance_km: float | None | Unset = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
    store_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band: None | str
        if isinstance(self.band, ListingBandType1):
            band = self.band.value
        elif isinstance(self.band, ListingBandType2Type1):
            band = self.band.value
        elif isinstance(self.band, ListingBandType3Type1):
            band = self.band.value
        else:
            band = self.band

        clinic_id: None | str | Unset
        if isinstance(self.clinic_id, Unset):
            clinic_id = UNSET
        elif isinstance(self.clinic_id, UUID):
            clinic_id = str(self.clinic_id)
        else:
            clinic_id = self.clinic_id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        match: None | str | Unset
        if isinstance(self.match, Unset):
            match = UNSET
        elif isinstance(self.match, ListingSearchResultMatchType1):
            match = self.match.value
        elif isinstance(self.match, ListingSearchResultMatchType2Type1):
            match = self.match.value
        elif isinstance(self.match, ListingSearchResultMatchType3Type1):
            match = self.match.value
        else:
            match = self.match

        distance_km: float | None | Unset
        if isinstance(self.distance_km, Unset):
            distance_km = UNSET
        else:
            distance_km = self.distance_km

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        store_url: None | str | Unset
        if isinstance(self.store_url, Unset):
            store_url = UNSET
        else:
            store_url = self.store_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "band": band,
            }
        )
        if clinic_id is not UNSET:
            field_dict["clinic_id"] = clinic_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if match is not UNSET:
            field_dict["match"] = match
        if distance_km is not UNSET:
            field_dict["distance_km"] = distance_km
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if store_url is not UNSET:
            field_dict["store_url"] = store_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_band(data: object) -> ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_listing_band_type_1 = ListingBandType1(data)

                return componentsschemas_listing_band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_listing_band_type_2_type_1 = ListingBandType2Type1(data)

                return componentsschemas_listing_band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_listing_band_type_3_type_1 = ListingBandType3Type1(data)

                return componentsschemas_listing_band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None, data)

        band = _parse_band(d.pop("band"))

        def _parse_clinic_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinic_id_type_0 = UUID(data)

                return clinic_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clinic_id = _parse_clinic_id(d.pop("clinic_id", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

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

        def _parse_match(
            data: object,
        ) -> (
            ListingSearchResultMatchType1
            | ListingSearchResultMatchType2Type1
            | ListingSearchResultMatchType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                match_type_1 = ListingSearchResultMatchType1(data)

                return match_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                match_type_2_type_1 = ListingSearchResultMatchType2Type1(data)

                return match_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                match_type_3_type_1 = ListingSearchResultMatchType3Type1(data)

                return match_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListingSearchResultMatchType1
                | ListingSearchResultMatchType2Type1
                | ListingSearchResultMatchType3Type1
                | None
                | Unset,
                data,
            )

        match = _parse_match(d.pop("match", UNSET))

        def _parse_distance_km(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_km = _parse_distance_km(d.pop("distance_km", UNSET))

        def _parse_as_of(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        as_of = _parse_as_of(d.pop("as_of", UNSET))

        def _parse_store_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        store_url = _parse_store_url(d.pop("store_url", UNSET))

        listing_search_result = cls(
            band=band,
            clinic_id=clinic_id,
            display_name=display_name,
            item_id=item_id,
            match=match,
            distance_km=distance_km,
            as_of=as_of,
            store_url=store_url,
        )

        listing_search_result.additional_properties = d
        return listing_search_result

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
