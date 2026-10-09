from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.patient_search_identifier_system import PatientSearchIdentifierSystem

T = TypeVar("T", bound="PatientSearchIdentifier")


@_attrs_define
class PatientSearchIdentifier:
    """
    Attributes:
        system (PatientSearchIdentifierSystem):
        value (str):
    """

    system: PatientSearchIdentifierSystem
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
        system = PatientSearchIdentifierSystem(d.pop("system"))

        value = d.pop("value")

        patient_search_identifier = cls(
            system=system,
            value=value,
        )

        return patient_search_identifier
