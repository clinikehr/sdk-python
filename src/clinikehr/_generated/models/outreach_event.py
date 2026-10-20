from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outreach_event_status import OutreachEventStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outreach_station import OutreachStation


T = TypeVar("T", bound="OutreachEvent")


@_attrs_define
class OutreachEvent:
    """
    Attributes:
        id (UUID):
        name (str):
        starts_on (datetime.date):
        ends_on (datetime.date):
        status (OutreachEventStatus):
        location_text (None | str | Unset):
        closed_at (datetime.datetime | None | Unset):
        stations (list[OutreachStation] | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: UUID
    name: str
    starts_on: datetime.date
    ends_on: datetime.date
    status: OutreachEventStatus
    location_text: None | str | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    stations: list[OutreachStation] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        starts_on = self.starts_on.isoformat()

        ends_on = self.ends_on.isoformat()

        status = self.status.value

        location_text: None | str | Unset
        if isinstance(self.location_text, Unset):
            location_text = UNSET
        else:
            location_text = self.location_text

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        stations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stations, Unset):
            stations = []
            for stations_item_data in self.stations:
                stations_item = stations_item_data.to_dict()
                stations.append(stations_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "starts_on": starts_on,
                "ends_on": ends_on,
                "status": status,
            }
        )
        if location_text is not UNSET:
            field_dict["location_text"] = location_text
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if stations is not UNSET:
            field_dict["stations"] = stations
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outreach_station import OutreachStation  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        starts_on = datetime.date.fromisoformat(d.pop("starts_on"))

        ends_on = datetime.date.fromisoformat(d.pop("ends_on"))

        status = OutreachEventStatus(d.pop("status"))

        def _parse_location_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_text = _parse_location_text(d.pop("location_text", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        _stations = d.pop("stations", UNSET)
        stations: list[OutreachStation] | Unset = UNSET
        if _stations is not UNSET:
            stations = []
            for stations_item_data in _stations:
                stations_item = OutreachStation.from_dict(stations_item_data)

                stations.append(stations_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        outreach_event = cls(
            id=id,
            name=name,
            starts_on=starts_on,
            ends_on=ends_on,
            status=status,
            location_text=location_text,
            closed_at=closed_at,
            stations=stations,
            created_at=created_at,
            updated_at=updated_at,
        )

        outreach_event.additional_properties = d
        return outreach_event

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
