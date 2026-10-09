from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partner_code_upload_entry import PartnerCodeUploadEntry


T = TypeVar("T", bound="PartnerCodesUploadRequest")


@_attrs_define
class PartnerCodesUploadRequest:
    """
    Attributes:
        entries (list[PartnerCodeUploadEntry]):
    """

    entries: list[PartnerCodeUploadEntry]

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_code_upload_entry import PartnerCodeUploadEntry  # noqa: PLC0415

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = PartnerCodeUploadEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        partner_codes_upload_request = cls(
            entries=entries,
        )

        return partner_codes_upload_request
