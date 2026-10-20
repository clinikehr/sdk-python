from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_pin import ListingPin
    from ..models.listing_profile_hours_type_0 import ListingProfileHoursType0


T = TypeVar("T", bound="ListingProfile")


@_attrs_define
class ListingProfile:
    """
    Attributes:
        clinic_id (UUID):
        display_name (None | str | Unset):
        address_line1 (None | str | Unset):
        address_line2 (None | str | Unset):
        city (None | str | Unset):
        region (None | str | Unset):
        country (None | str | Unset):
        postal_code (None | str | Unset):
        pin (ListingPin | None | Unset):
        phone (None | str | Unset):
        hours (ListingProfileHoursType0 | None | Unset):
        price_opt_in (bool | Unset): Separate opt-in for listing.prices:read. Off by default.
        profile_completed_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        store_url (None | str | Unset): The pharmacy's online store. Present ONLY when the store is safe to advertise:
            its page is enabled, it can take payment, the pharmacy is not on the listing-only plan, and ClinikEHR (not
            another system) holds its stock. Otherwise null. A pharmacy's own web address, when it has connected one, is
            used instead of the hosted address.
    """

    clinic_id: UUID
    display_name: None | str | Unset = UNSET
    address_line1: None | str | Unset = UNSET
    address_line2: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    pin: ListingPin | None | Unset = UNSET
    phone: None | str | Unset = UNSET
    hours: ListingProfileHoursType0 | None | Unset = UNSET
    price_opt_in: bool | Unset = UNSET
    profile_completed_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    store_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pin import ListingPin  # noqa: PLC0415
        from ..models.listing_profile_hours_type_0 import ListingProfileHoursType0  # noqa: PLC0415

        clinic_id = str(self.clinic_id)

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        address_line1: None | str | Unset
        if isinstance(self.address_line1, Unset):
            address_line1 = UNSET
        else:
            address_line1 = self.address_line1

        address_line2: None | str | Unset
        if isinstance(self.address_line2, Unset):
            address_line2 = UNSET
        else:
            address_line2 = self.address_line2

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        pin: dict[str, Any] | None | Unset
        if isinstance(self.pin, Unset):
            pin = UNSET
        elif isinstance(self.pin, ListingPin):
            pin = self.pin.to_dict()
        else:
            pin = self.pin

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        hours: dict[str, Any] | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        elif isinstance(self.hours, ListingProfileHoursType0):
            hours = self.hours.to_dict()
        else:
            hours = self.hours

        price_opt_in = self.price_opt_in

        profile_completed_at: None | str | Unset
        if isinstance(self.profile_completed_at, Unset):
            profile_completed_at = UNSET
        elif isinstance(self.profile_completed_at, datetime.datetime):
            profile_completed_at = self.profile_completed_at.isoformat()
        else:
            profile_completed_at = self.profile_completed_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        store_url: None | str | Unset
        if isinstance(self.store_url, Unset):
            store_url = UNSET
        else:
            store_url = self.store_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clinic_id": clinic_id,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if pin is not UNSET:
            field_dict["pin"] = pin
        if phone is not UNSET:
            field_dict["phone"] = phone
        if hours is not UNSET:
            field_dict["hours"] = hours
        if price_opt_in is not UNSET:
            field_dict["price_opt_in"] = price_opt_in
        if profile_completed_at is not UNSET:
            field_dict["profile_completed_at"] = profile_completed_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if store_url is not UNSET:
            field_dict["store_url"] = store_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pin import ListingPin  # noqa: PLC0415
        from ..models.listing_profile_hours_type_0 import ListingProfileHoursType0  # noqa: PLC0415

        d = dict(src_dict)
        clinic_id = UUID(d.pop("clinic_id"))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_address_line1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line1 = _parse_address_line1(d.pop("address_line1", UNSET))

        def _parse_address_line2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line2 = _parse_address_line2(d.pop("address_line2", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_pin(data: object) -> ListingPin | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pin_type_0 = ListingPin.from_dict(data)

                return pin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPin | None | Unset, data)

        pin = _parse_pin(d.pop("pin", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_hours(data: object) -> ListingProfileHoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hours_type_0 = ListingProfileHoursType0.from_dict(data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingProfileHoursType0 | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        price_opt_in = d.pop("price_opt_in", UNSET)

        def _parse_profile_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return profile_completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        profile_completed_at = _parse_profile_completed_at(d.pop("profile_completed_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_store_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        store_url = _parse_store_url(d.pop("store_url", UNSET))

        listing_profile = cls(
            clinic_id=clinic_id,
            display_name=display_name,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            region=region,
            country=country,
            postal_code=postal_code,
            pin=pin,
            phone=phone,
            hours=hours,
            price_opt_in=price_opt_in,
            profile_completed_at=profile_completed_at,
            updated_at=updated_at,
            store_url=store_url,
        )

        listing_profile.additional_properties = d
        return listing_profile

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
