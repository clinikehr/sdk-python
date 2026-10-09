from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.patient_search_identifier import PatientSearchIdentifier


T = TypeVar("T", bound="PatientSearchRequest")


@_attrs_define
class PatientSearchRequest:
    """
    Attributes:
        identifiers (list[PatientSearchIdentifier]): At least two identifiers of DIFFERENT kinds (email, phone, mrn).
            Exact match only.
    """

    identifiers: list[PatientSearchIdentifier]

    def to_dict(self) -> dict[str, Any]:
        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.to_dict()
            identifiers.append(identifiers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identifiers": identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patient_search_identifier import PatientSearchIdentifier  # noqa: PLC0415

        d = dict(src_dict)
        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = PatientSearchIdentifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        patient_search_request = cls(
            identifiers=identifiers,
        )

        return patient_search_request
