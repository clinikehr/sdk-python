from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.availability_request_entry_type_0 import AvailabilityRequestEntryType0
    from ..models.availability_request_entry_type_1 import AvailabilityRequestEntryType1


T = TypeVar("T", bound="AvailabilityRequest")


@_attrs_define
class AvailabilityRequest:
    """
    Attributes:
        entries (list[AvailabilityRequestEntryType0 | AvailabilityRequestEntryType1]):
    """

    entries: list[AvailabilityRequestEntryType0 | AvailabilityRequestEntryType1]

    def to_dict(self) -> dict[str, Any]:
        from ..models.availability_request_entry_type_0 import AvailabilityRequestEntryType0  # noqa: PLC0415

        entries = []
        for entries_item_data in self.entries:
            entries_item: dict[str, Any]
            if isinstance(entries_item_data, AvailabilityRequestEntryType0):
                entries_item = entries_item_data.to_dict()
            else:
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
        from ..models.availability_request_entry_type_0 import AvailabilityRequestEntryType0  # noqa: PLC0415
        from ..models.availability_request_entry_type_1 import AvailabilityRequestEntryType1  # noqa: PLC0415

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:

            def _parse_entries_item(data: object) -> AvailabilityRequestEntryType0 | AvailabilityRequestEntryType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_availability_request_entry_type_0 = AvailabilityRequestEntryType0.from_dict(data)

                    return componentsschemas_availability_request_entry_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_availability_request_entry_type_1 = AvailabilityRequestEntryType1.from_dict(data)

                return componentsschemas_availability_request_entry_type_1

            entries_item = _parse_entries_item(entries_item_data)

            entries.append(entries_item)

        availability_request = cls(
            entries=entries,
        )

        return availability_request
