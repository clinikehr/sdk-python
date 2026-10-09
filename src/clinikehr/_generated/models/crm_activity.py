from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crm_activity_type_type_1 import CrmActivityTypeType1
from ..models.crm_activity_type_type_2_type_1 import CrmActivityTypeType2Type1
from ..models.crm_activity_type_type_3_type_1 import CrmActivityTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crm_activity_metadata import CrmActivityMetadata


T = TypeVar("T", bound="CrmActivity")


@_attrs_define
class CrmActivity:
    """
    Attributes:
        id (UUID):
        contact_id (None | Unset | UUID):
        actor_staff_id (None | Unset | UUID):
        type_ (CrmActivityTypeType1 | CrmActivityTypeType2Type1 | CrmActivityTypeType3Type1 | None | Unset):
        subject (None | str | Unset):
        body (None | str | Unset):
        metadata (CrmActivityMetadata | Unset):
        occurred_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    contact_id: None | Unset | UUID = UNSET
    actor_staff_id: None | Unset | UUID = UNSET
    type_: CrmActivityTypeType1 | CrmActivityTypeType2Type1 | CrmActivityTypeType3Type1 | None | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    metadata: CrmActivityMetadata | Unset = UNSET
    occurred_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        elif isinstance(self.contact_id, UUID):
            contact_id = str(self.contact_id)
        else:
            contact_id = self.contact_id

        actor_staff_id: None | str | Unset
        if isinstance(self.actor_staff_id, Unset):
            actor_staff_id = UNSET
        elif isinstance(self.actor_staff_id, UUID):
            actor_staff_id = str(self.actor_staff_id)
        else:
            actor_staff_id = self.actor_staff_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, CrmActivityTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, CrmActivityTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, CrmActivityTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        occurred_at: None | str | Unset
        if isinstance(self.occurred_at, Unset):
            occurred_at = UNSET
        elif isinstance(self.occurred_at, datetime.datetime):
            occurred_at = self.occurred_at.isoformat()
        else:
            occurred_at = self.occurred_at

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
            }
        )
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if actor_staff_id is not UNSET:
            field_dict["actor_staff_id"] = actor_staff_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crm_activity_metadata import CrmActivityMetadata  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_id_type_0 = UUID(data)

                return contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        def _parse_actor_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_staff_id_type_0 = UUID(data)

                return actor_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        actor_staff_id = _parse_actor_staff_id(d.pop("actor_staff_id", UNSET))

        def _parse_type_(
            data: object,
        ) -> CrmActivityTypeType1 | CrmActivityTypeType2Type1 | CrmActivityTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = CrmActivityTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = CrmActivityTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = CrmActivityTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CrmActivityTypeType1 | CrmActivityTypeType2Type1 | CrmActivityTypeType3Type1 | None | Unset, data
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: CrmActivityMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CrmActivityMetadata.from_dict(_metadata)

        def _parse_occurred_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurred_at_type_0 = datetime.datetime.fromisoformat(data)

                return occurred_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        occurred_at = _parse_occurred_at(d.pop("occurred_at", UNSET))

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

        crm_activity = cls(
            id=id,
            contact_id=contact_id,
            actor_staff_id=actor_staff_id,
            type_=type_,
            subject=subject,
            body=body,
            metadata=metadata,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        crm_activity.additional_properties = d
        return crm_activity

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
