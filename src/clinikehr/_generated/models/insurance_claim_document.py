from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsuranceClaimDocument")


@_attrs_define
class InsuranceClaimDocument:
    """Metadata of a document attached to a claim. The file itself is not served by this API.

    Attributes:
        id (UUID | Unset):
        document_type (None | str | Unset):
        file_name (None | str | Unset):
        mime_type (None | str | Unset):
        file_size (float | None | Unset):
        document_date (datetime.datetime | None | Unset):
        description (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    document_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    file_size: float | None | Unset = UNSET
    document_date: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        document_type: None | str | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        file_size: float | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        document_date: None | str | Unset
        if isinstance(self.document_date, Unset):
            document_date = UNSET
        elif isinstance(self.document_date, datetime.datetime):
            document_date = self.document_date.isoformat()
        else:
            document_date = self.document_date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if document_date is not UNSET:
            field_dict["document_date"] = document_date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_document_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_type = _parse_document_type(d.pop("document_type", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mime_type", UNSET))

        def _parse_file_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_document_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                document_date_type_0 = datetime.datetime.fromisoformat(data)

                return document_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        document_date = _parse_document_date(d.pop("document_date", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        insurance_claim_document = cls(
            id=id,
            document_type=document_type,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            document_date=document_date,
            description=description,
        )

        insurance_claim_document.additional_properties = d
        return insurance_claim_document

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
