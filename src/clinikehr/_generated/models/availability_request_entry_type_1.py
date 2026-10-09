from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.availability_request_entry_type_1_system import AvailabilityRequestEntryType1System

T = TypeVar("T", bound="AvailabilityRequestEntryType1")


@_attrs_define
class AvailabilityRequestEntryType1:
    """
    Attributes:
        system (AvailabilityRequestEntryType1System):
        value (str):
    """

    system: AvailabilityRequestEntryType1System
    value: str

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "system": system,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = AvailabilityRequestEntryType1System(d.pop("system"))

        value = d.pop("value")

        availability_request_entry_type_1 = cls(
            system=system,
            value=value,
        )

        return availability_request_entry_type_1
