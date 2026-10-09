from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_pharmacy_hours_type_0 import ListingPharmacyHoursType0
    from ..models.listing_pin import ListingPin


T = TypeVar("T", bound="ListingPharmacy")


@_attrs_define
class ListingPharmacy:
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
        pin (ListingPin | None | Unset): Owner-placed on the "Get listed" sheet's map. Null = this pharmacy cannot be
            ranked by distance in network search.
        phone (None | str | Unset):
        hours (ListingPharmacyHoursType0 | None | Unset):
        open_now (bool | None | Unset): Computed from the clinic's own business hours. Null when hours are absent or
            malformed for today — never a guess.
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
    hours: ListingPharmacyHoursType0 | None | Unset = UNSET
    open_now: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pharmacy_hours_type_0 import ListingPharmacyHoursType0  # noqa: PLC0415
        from ..models.listing_pin import ListingPin  # noqa: PLC0415

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
        elif isinstance(self.hours, ListingPharmacyHoursType0):
            hours = self.hours.to_dict()
        else:
            hours = self.hours

        open_now: bool | None | Unset
        if isinstance(self.open_now, Unset):
            open_now = UNSET
        else:
            open_now = self.open_now

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
        if open_now is not UNSET:
            field_dict["open_now"] = open_now

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pharmacy_hours_type_0 import ListingPharmacyHoursType0  # noqa: PLC0415
        from ..models.listing_pin import ListingPin  # noqa: PLC0415

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

        def _parse_hours(data: object) -> ListingPharmacyHoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hours_type_0 = ListingPharmacyHoursType0.from_dict(data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPharmacyHoursType0 | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        def _parse_open_now(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        open_now = _parse_open_now(d.pop("open_now", UNSET))

        listing_pharmacy = cls(
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
            open_now=open_now,
        )

        listing_pharmacy.additional_properties = d
        return listing_pharmacy

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
