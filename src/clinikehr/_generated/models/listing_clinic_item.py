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
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingClinicItem")


@_attrs_define
class ListingClinicItem:
    """
    Attributes:
        band (ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None): Unlike inventory availability's
            band, listing carries a fourth value, `unknown` — the till heartbeat is missing or stale during open hours.
            Never coerced to another value; a listing route never returns an exact quantity.
        item_id (None | Unset | UUID):
        name (None | str | Unset):
        as_of (datetime.datetime | None | Unset):
    """

    band: ListingBandType1 | ListingBandType2Type1 | ListingBandType3Type1 | None
    item_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
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

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "band": band,
            }
        )
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if name is not UNSET:
            field_dict["name"] = name
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        listing_clinic_item = cls(
            band=band,
            item_id=item_id,
            name=name,
            as_of=as_of,
        )

        listing_clinic_item.additional_properties = d
        return listing_clinic_item

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
