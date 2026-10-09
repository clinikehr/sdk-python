from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drug_request_create_request_lines_item import DrugRequestCreateRequestLinesItem


T = TypeVar("T", bound="DrugRequestCreateRequest")


@_attrs_define
class DrugRequestCreateRequest:
    """
    Attributes:
        clinic_patient_id (UUID):
        lines (list[DrugRequestCreateRequestLinesItem]):
        requester_reference (str | Unset):
        authorization_reference (str | Unset):
        needed_by (datetime.datetime | Unset):
    """

    clinic_patient_id: UUID
    lines: list[DrugRequestCreateRequestLinesItem]
    requester_reference: str | Unset = UNSET
    authorization_reference: str | Unset = UNSET
    needed_by: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clinic_patient_id = str(self.clinic_patient_id)

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        requester_reference = self.requester_reference

        authorization_reference = self.authorization_reference

        needed_by: str | Unset = UNSET
        if not isinstance(self.needed_by, Unset):
            needed_by = self.needed_by.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clinic_patient_id": clinic_patient_id,
                "lines": lines,
            }
        )
        if requester_reference is not UNSET:
            field_dict["requester_reference"] = requester_reference
        if authorization_reference is not UNSET:
            field_dict["authorization_reference"] = authorization_reference
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drug_request_create_request_lines_item import DrugRequestCreateRequestLinesItem  # noqa: PLC0415

        d = dict(src_dict)
        clinic_patient_id = UUID(d.pop("clinic_patient_id"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = DrugRequestCreateRequestLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        requester_reference = d.pop("requester_reference", UNSET)

        authorization_reference = d.pop("authorization_reference", UNSET)

        _needed_by = d.pop("needed_by", UNSET)
        needed_by: datetime.datetime | Unset
        if isinstance(_needed_by, Unset):
            needed_by = UNSET
        else:
            needed_by = datetime.datetime.fromisoformat(_needed_by)

        drug_request_create_request = cls(
            clinic_patient_id=clinic_patient_id,
            lines=lines,
            requester_reference=requester_reference,
            authorization_reference=authorization_reference,
            needed_by=needed_by,
        )

        drug_request_create_request.additional_properties = d
        return drug_request_create_request

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
