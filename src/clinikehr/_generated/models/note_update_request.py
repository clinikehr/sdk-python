from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.note_update_request_content import NoteUpdateRequestContent


T = TypeVar("T", bound="NoteUpdateRequest")


@_attrs_define
class NoteUpdateRequest:
    """
    Attributes:
        content (NoteUpdateRequestContent): Replaces note_content whole. Refused (note_not_editable) unless the note is
            still status=draft AND was last touched by THIS key.
    """

    content: NoteUpdateRequestContent

    def to_dict(self) -> dict[str, Any]:
        content = self.content.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_update_request_content import NoteUpdateRequestContent  # noqa: PLC0415

        d = dict(src_dict)
        content = NoteUpdateRequestContent.from_dict(d.pop("content"))

        note_update_request = cls(
            content=content,
        )

        return note_update_request
