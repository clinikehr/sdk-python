from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.crm_activity_create_request_type import CrmActivityCreateRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crm_activity_create_request_metadata import CrmActivityCreateRequestMetadata


T = TypeVar("T", bound="CrmActivityCreateRequest")


@_attrs_define
class CrmActivityCreateRequest:
    """
    Attributes:
        type_ (CrmActivityCreateRequestType):
        subject (None | str | Unset):
        body (None | str | Unset):
        metadata (CrmActivityCreateRequestMetadata | Unset):
    """

    type_: CrmActivityCreateRequestType
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    metadata: CrmActivityCreateRequestMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crm_activity_create_request_metadata import CrmActivityCreateRequestMetadata  # noqa: PLC0415

        d = dict(src_dict)
        type_ = CrmActivityCreateRequestType(d.pop("type"))

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
        metadata: CrmActivityCreateRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CrmActivityCreateRequestMetadata.from_dict(_metadata)

        crm_activity_create_request = cls(
            type_=type_,
            subject=subject,
            body=body,
            metadata=metadata,
        )

        return crm_activity_create_request
