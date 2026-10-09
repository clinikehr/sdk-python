from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inventory_availability_band_type_1 import InventoryAvailabilityBandType1
from ..models.inventory_availability_band_type_2_type_1 import InventoryAvailabilityBandType2Type1
from ..models.inventory_availability_band_type_3_type_1 import InventoryAvailabilityBandType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryAvailability")


@_attrs_define
class InventoryAvailability:
    """
    Attributes:
        matched (bool):
        item_id (None | Unset | UUID):
        band (InventoryAvailabilityBandType1 | InventoryAvailabilityBandType2Type1 | InventoryAvailabilityBandType3Type1
            | None | Unset):
        as_of (datetime.datetime | None | Unset):
    """

    matched: bool
    item_id: None | Unset | UUID = UNSET
    band: (
        InventoryAvailabilityBandType1
        | InventoryAvailabilityBandType2Type1
        | InventoryAvailabilityBandType3Type1
        | None
        | Unset
    ) = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        band: None | str | Unset
        if isinstance(self.band, Unset):
            band = UNSET
        elif isinstance(self.band, InventoryAvailabilityBandType1):
            band = self.band.value
        elif isinstance(self.band, InventoryAvailabilityBandType2Type1):
            band = self.band.value
        elif isinstance(self.band, InventoryAvailabilityBandType3Type1):
            band = self.band.value
        else:
            band = self.band

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
                "matched": matched,
            }
        )
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if band is not UNSET:
            field_dict["band"] = band
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matched = d.pop("matched")

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

        def _parse_band(
            data: object,
        ) -> (
            InventoryAvailabilityBandType1
            | InventoryAvailabilityBandType2Type1
            | InventoryAvailabilityBandType3Type1
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
                band_type_1 = InventoryAvailabilityBandType1(data)

                return band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_2_type_1 = InventoryAvailabilityBandType2Type1(data)

                return band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_3_type_1 = InventoryAvailabilityBandType3Type1(data)

                return band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InventoryAvailabilityBandType1
                | InventoryAvailabilityBandType2Type1
                | InventoryAvailabilityBandType3Type1
                | None
                | Unset,
                data,
            )

        band = _parse_band(d.pop("band", UNSET))

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

        inventory_availability = cls(
            matched=matched,
            item_id=item_id,
            band=band,
            as_of=as_of,
        )

        inventory_availability.additional_properties = d
        return inventory_availability

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
