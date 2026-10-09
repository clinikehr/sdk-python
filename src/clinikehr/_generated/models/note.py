from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.note_metadata_origin_type_1 import NoteMetadataOriginType1
from ..models.note_metadata_origin_type_2_type_1 import NoteMetadataOriginType2Type1
from ..models.note_metadata_origin_type_3_type_1 import NoteMetadataOriginType3Type1
from ..models.note_metadata_status import NoteMetadataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_citations_type_0_item import NoteCitationsType0Item
    from ..models.note_content import NoteContent


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """
    Attributes:
        id (UUID):
        status (NoteMetadataStatus):
        patient_id (None | Unset | UUID):
        title (None | str | Unset):
        note_type (None | str | Unset):
        is_signed (bool | Unset):
        signed_at (datetime.datetime | None | Unset):
        origin (None | NoteMetadataOriginType1 | NoteMetadataOriginType2Type1 | NoteMetadataOriginType3Type1 | Unset):
        origin_assistant_name (None | str | Unset):
        is_reviewed (bool | Unset):
        reviewed_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        custom_template_id (None | Unset | UUID):
        content (NoteContent | Unset): note_content, stripped of internal/meta keys — shape depends on which template
            (blank/static/custom) produced it. Never note_content's raw form.
        citations (list[NoteCitationsType0Item] | None | Unset): notes_sessions.origin_citations — set only when the
            draft carries origin_assistant_name.
    """

    id: UUID
    status: NoteMetadataStatus
    patient_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    note_type: None | str | Unset = UNSET
    is_signed: bool | Unset = UNSET
    signed_at: datetime.datetime | None | Unset = UNSET
    origin: None | NoteMetadataOriginType1 | NoteMetadataOriginType2Type1 | NoteMetadataOriginType3Type1 | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    is_reviewed: bool | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    custom_template_id: None | Unset | UUID = UNSET
    content: NoteContent | Unset = UNSET
    citations: list[NoteCitationsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        patient_id: None | str | Unset
        if isinstance(self.patient_id, Unset):
            patient_id = UNSET
        elif isinstance(self.patient_id, UUID):
            patient_id = str(self.patient_id)
        else:
            patient_id = self.patient_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        note_type: None | str | Unset
        if isinstance(self.note_type, Unset):
            note_type = UNSET
        else:
            note_type = self.note_type

        is_signed = self.is_signed

        signed_at: None | str | Unset
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, NoteMetadataOriginType1):
            origin = self.origin.value
        elif isinstance(self.origin, NoteMetadataOriginType2Type1):
            origin = self.origin.value
        elif isinstance(self.origin, NoteMetadataOriginType3Type1):
            origin = self.origin.value
        else:
            origin = self.origin

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        is_reviewed = self.is_reviewed

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        custom_template_id: None | str | Unset
        if isinstance(self.custom_template_id, Unset):
            custom_template_id = UNSET
        elif isinstance(self.custom_template_id, UUID):
            custom_template_id = str(self.custom_template_id)
        else:
            custom_template_id = self.custom_template_id

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.citations, Unset):
            citations = UNSET
        elif isinstance(self.citations, list):
            citations = []
            for citations_type_0_item_data in self.citations:
                citations_type_0_item = citations_type_0_item_data.to_dict()
                citations.append(citations_type_0_item)

        else:
            citations = self.citations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if title is not UNSET:
            field_dict["title"] = title
        if note_type is not UNSET:
            field_dict["note_type"] = note_type
        if is_signed is not UNSET:
            field_dict["is_signed"] = is_signed
        if signed_at is not UNSET:
            field_dict["signed_at"] = signed_at
        if origin is not UNSET:
            field_dict["origin"] = origin
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if is_reviewed is not UNSET:
            field_dict["is_reviewed"] = is_reviewed
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if custom_template_id is not UNSET:
            field_dict["custom_template_id"] = custom_template_id
        if content is not UNSET:
            field_dict["content"] = content
        if citations is not UNSET:
            field_dict["citations"] = citations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_citations_type_0_item import NoteCitationsType0Item  # noqa: PLC0415
        from ..models.note_content import NoteContent  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = NoteMetadataStatus(d.pop("status"))

        def _parse_patient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patient_id_type_0 = UUID(data)

                return patient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        patient_id = _parse_patient_id(d.pop("patient_id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_note_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note_type = _parse_note_type(d.pop("note_type", UNSET))

        is_signed = d.pop("is_signed", UNSET)

        def _parse_signed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_at = _parse_signed_at(d.pop("signed_at", UNSET))

        def _parse_origin(
            data: object,
        ) -> None | NoteMetadataOriginType1 | NoteMetadataOriginType2Type1 | NoteMetadataOriginType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = NoteMetadataOriginType1(data)

                return origin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_2_type_1 = NoteMetadataOriginType2Type1(data)

                return origin_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_3_type_1 = NoteMetadataOriginType3Type1(data)

                return origin_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | NoteMetadataOriginType1 | NoteMetadataOriginType2Type1 | NoteMetadataOriginType3Type1 | Unset,
                data,
            )

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        is_reviewed = d.pop("is_reviewed", UNSET)

        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))

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

        def _parse_custom_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_template_id_type_0 = UUID(data)

                return custom_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        custom_template_id = _parse_custom_template_id(d.pop("custom_template_id", UNSET))

        _content = d.pop("content", UNSET)
        content: NoteContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = NoteContent.from_dict(_content)

        def _parse_citations(data: object) -> list[NoteCitationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                citations_type_0 = []
                _citations_type_0 = data
                for citations_type_0_item_data in _citations_type_0:
                    citations_type_0_item = NoteCitationsType0Item.from_dict(citations_type_0_item_data)

                    citations_type_0.append(citations_type_0_item)

                return citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NoteCitationsType0Item] | None | Unset, data)

        citations = _parse_citations(d.pop("citations", UNSET))

        note = cls(
            id=id,
            status=status,
            patient_id=patient_id,
            title=title,
            note_type=note_type,
            is_signed=is_signed,
            signed_at=signed_at,
            origin=origin,
            origin_assistant_name=origin_assistant_name,
            is_reviewed=is_reviewed,
            reviewed_at=reviewed_at,
            created_at=created_at,
            updated_at=updated_at,
            custom_template_id=custom_template_id,
            content=content,
            citations=citations,
        )

        note.additional_properties = d
        return note

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
