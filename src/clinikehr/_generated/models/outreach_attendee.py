from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outreach_station_progress import OutreachStationProgress


T = TypeVar("T", bound="OutreachAttendee")


@_attrs_define
class OutreachAttendee:
    """
    Attributes:
        id (UUID):
        event_id (UUID):
        patient_id (UUID):
        checked_in_at (datetime.datetime):
        progress (list[OutreachStationProgress] | Unset):
    """

    id: UUID
    event_id: UUID
    patient_id: UUID
    checked_in_at: datetime.datetime
    progress: list[OutreachStationProgress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        event_id = str(self.event_id)

        patient_id = str(self.patient_id)

        checked_in_at = self.checked_in_at.isoformat()

        progress: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = []
            for progress_item_data in self.progress:
                progress_item = progress_item_data.to_dict()
                progress.append(progress_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_id": event_id,
                "patient_id": patient_id,
                "checked_in_at": checked_in_at,
            }
        )
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outreach_station_progress import OutreachStationProgress  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        event_id = UUID(d.pop("event_id"))

        patient_id = UUID(d.pop("patient_id"))

        checked_in_at = datetime.datetime.fromisoformat(d.pop("checked_in_at"))

        _progress = d.pop("progress", UNSET)
        progress: list[OutreachStationProgress] | Unset = UNSET
        if _progress is not UNSET:
            progress = []
            for progress_item_data in _progress:
                progress_item = OutreachStationProgress.from_dict(progress_item_data)

                progress.append(progress_item)

        outreach_attendee = cls(
            id=id,
            event_id=event_id,
            patient_id=patient_id,
            checked_in_at=checked_in_at,
            progress=progress,
        )

        outreach_attendee.additional_properties = d
        return outreach_attendee

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
