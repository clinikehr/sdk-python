from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_create_request_citations_item import NoteCreateRequestCitationsItem
    from ..models.note_create_request_content import NoteCreateRequestContent


T = TypeVar("T", bound="NoteCreateRequest")


@_attrs_define
class NoteCreateRequest:
    """
    Attributes:
        patient_id (UUID):
        clinician_id (UUID):
        content (NoteCreateRequestContent): Keyed by generateFieldId(section.title, index) for a template note, or free-
            form for a blank note. Unknown keys are refused (unknown_field), naming both the offending keys and the full
            valid list.
        note_type (None | str | Unset): A static template's exact name, or omitted for a blank note.
        custom_template_id (None | Unset | UUID): This clinic's own custom template id.
        origin_assistant_name (str | Unset): When given, origin=assistant_external instead of api.
        citations (list[NoteCreateRequestCitationsItem] | Unset):
    """

    patient_id: UUID
    clinician_id: UUID
    content: NoteCreateRequestContent
    note_type: None | str | Unset = UNSET
    custom_template_id: None | Unset | UUID = UNSET
    origin_assistant_name: str | Unset = UNSET
    citations: list[NoteCreateRequestCitationsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        clinician_id = str(self.clinician_id)

        content = self.content.to_dict()

        note_type: None | str | Unset
        if isinstance(self.note_type, Unset):
            note_type = UNSET
        else:
            note_type = self.note_type

        custom_template_id: None | str | Unset
        if isinstance(self.custom_template_id, Unset):
            custom_template_id = UNSET
        elif isinstance(self.custom_template_id, UUID):
            custom_template_id = str(self.custom_template_id)
        else:
            custom_template_id = self.custom_template_id

        origin_assistant_name = self.origin_assistant_name

        citations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.citations, Unset):
            citations = []
            for citations_item_data in self.citations:
                citations_item = citations_item_data.to_dict()
                citations.append(citations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "clinician_id": clinician_id,
                "content": content,
            }
        )
        if note_type is not UNSET:
            field_dict["note_type"] = note_type
        if custom_template_id is not UNSET:
            field_dict["custom_template_id"] = custom_template_id
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if citations is not UNSET:
            field_dict["citations"] = citations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_create_request_citations_item import NoteCreateRequestCitationsItem  # noqa: PLC0415
        from ..models.note_create_request_content import NoteCreateRequestContent  # noqa: PLC0415

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        clinician_id = UUID(d.pop("clinician_id"))

        content = NoteCreateRequestContent.from_dict(d.pop("content"))

        def _parse_note_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note_type = _parse_note_type(d.pop("note_type", UNSET))

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

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        _citations = d.pop("citations", UNSET)
        citations: list[NoteCreateRequestCitationsItem] | Unset = UNSET
        if _citations is not UNSET:
            citations = []
            for citations_item_data in _citations:
                citations_item = NoteCreateRequestCitationsItem.from_dict(citations_item_data)

                citations.append(citations_item)

        note_create_request = cls(
            patient_id=patient_id,
            clinician_id=clinician_id,
            content=content,
            note_type=note_type,
            custom_template_id=custom_template_id,
            origin_assistant_name=origin_assistant_name,
            citations=citations,
        )

        return note_create_request
