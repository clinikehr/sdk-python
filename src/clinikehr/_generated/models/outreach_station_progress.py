from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outreach_station_progress_kind import OutreachStationProgressKind
from ..models.outreach_station_progress_status import OutreachStationProgressStatus

T = TypeVar("T", bound="OutreachStationProgress")


@_attrs_define
class OutreachStationProgress:
    """
    Attributes:
        station_id (UUID):
        name (str):
        kind (OutreachStationProgressKind):
        position (int):
        status (OutreachStationProgressStatus):
    """

    station_id: UUID
    name: str
    kind: OutreachStationProgressKind
    position: int
    status: OutreachStationProgressStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        station_id = str(self.station_id)

        name = self.name

        kind = self.kind.value

        position = self.position

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "station_id": station_id,
                "name": name,
                "kind": kind,
                "position": position,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        station_id = UUID(d.pop("station_id"))

        name = d.pop("name")

        kind = OutreachStationProgressKind(d.pop("kind"))

        position = d.pop("position")

        status = OutreachStationProgressStatus(d.pop("status"))

        outreach_station_progress = cls(
            station_id=station_id,
            name=name,
            kind=kind,
            position=position,
            status=status,
        )

        outreach_station_progress.additional_properties = d
        return outreach_station_progress

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
