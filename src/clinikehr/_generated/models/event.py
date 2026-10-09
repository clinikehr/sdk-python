from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_data import EventData


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """`data` never carries a patient-shaped value for any type reachable today (every is_patient_data type is refused at
    emit, unconditionally).

        Attributes:
            id (str):
            type_ (None | str):
            seq (int | None):
            clinic_id (None | Unset | UUID):
            subject_id (None | str | Unset):
            data (EventData | Unset):
            created_at (datetime.datetime | None | Unset):
    """

    id: str
    type_: None | str
    seq: int | None
    clinic_id: None | Unset | UUID = UNSET
    subject_id: None | str | Unset = UNSET
    data: EventData | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: None | str
        type_ = self.type_

        seq: int | None
        seq = self.seq

        clinic_id: None | str | Unset
        if isinstance(self.clinic_id, Unset):
            clinic_id = UNSET
        elif isinstance(self.clinic_id, UUID):
            clinic_id = str(self.clinic_id)
        else:
            clinic_id = self.clinic_id

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "seq": seq,
            }
        )
        if clinic_id is not UNSET:
            field_dict["clinic_id"] = clinic_id
        if subject_id is not UNSET:
            field_dict["subject_id"] = subject_id
        if data is not UNSET:
            field_dict["data"] = data
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data import EventData  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_seq(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        seq = _parse_seq(d.pop("seq"))

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

        def _parse_subject_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_id = _parse_subject_id(d.pop("subject_id", UNSET))

        _data = d.pop("data", UNSET)
        data: EventData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EventData.from_dict(_data)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        event = cls(
            id=id,
            type_=type_,
            seq=seq,
            clinic_id=clinic_id,
            subject_id=subject_id,
            data=data,
            created_at=created_at,
        )

        event.additional_properties = d
        return event

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
