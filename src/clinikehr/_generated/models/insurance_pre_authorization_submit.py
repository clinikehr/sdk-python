from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.insurance_pre_authorization_submit_priority_level import InsurancePreAuthorizationSubmitPriorityLevel
from ..models.insurance_pre_authorization_submit_request_type import InsurancePreAuthorizationSubmitRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_diagnosis_input import InsuranceDiagnosisInput
    from ..models.insurance_pre_authorization_submit_item import InsurancePreAuthorizationSubmitItem


T = TypeVar("T", bound="InsurancePreAuthorizationSubmit")


@_attrs_define
class InsurancePreAuthorizationSubmit:
    """A pre-authorization request to send to one of the clinic's insurers. It is saved as `sent_for_authorization`.
    `patient_id` must be a patient your organization is linked to.

        Attributes:
            patient_id (UUID):
            insurance_company_id (UUID):
            request_type (InsurancePreAuthorizationSubmitRequestType):
            items (list[InsurancePreAuthorizationSubmitItem]):
            enrollee_id (UUID | Unset):
            priority_level (InsurancePreAuthorizationSubmitPriorityLevel | Unset):  Default:
                InsurancePreAuthorizationSubmitPriorityLevel.ROUTINE.
            encounter_date (datetime.datetime | Unset):
            diagnoses (list[InsuranceDiagnosisInput] | Unset):
    """

    patient_id: UUID
    insurance_company_id: UUID
    request_type: InsurancePreAuthorizationSubmitRequestType
    items: list[InsurancePreAuthorizationSubmitItem]
    enrollee_id: UUID | Unset = UNSET
    priority_level: InsurancePreAuthorizationSubmitPriorityLevel | Unset = (
        InsurancePreAuthorizationSubmitPriorityLevel.ROUTINE
    )
    encounter_date: datetime.datetime | Unset = UNSET
    diagnoses: list[InsuranceDiagnosisInput] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        insurance_company_id = str(self.insurance_company_id)

        request_type = self.request_type.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        enrollee_id: str | Unset = UNSET
        if not isinstance(self.enrollee_id, Unset):
            enrollee_id = str(self.enrollee_id)

        priority_level: str | Unset = UNSET
        if not isinstance(self.priority_level, Unset):
            priority_level = self.priority_level.value

        encounter_date: str | Unset = UNSET
        if not isinstance(self.encounter_date, Unset):
            encounter_date = self.encounter_date.isoformat()

        diagnoses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnoses, Unset):
            diagnoses = []
            for diagnoses_item_data in self.diagnoses:
                diagnoses_item = diagnoses_item_data.to_dict()
                diagnoses.append(diagnoses_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "insurance_company_id": insurance_company_id,
                "request_type": request_type,
                "items": items,
            }
        )
        if enrollee_id is not UNSET:
            field_dict["enrollee_id"] = enrollee_id
        if priority_level is not UNSET:
            field_dict["priority_level"] = priority_level
        if encounter_date is not UNSET:
            field_dict["encounter_date"] = encounter_date
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_diagnosis_input import InsuranceDiagnosisInput  # noqa: PLC0415
        from ..models.insurance_pre_authorization_submit_item import (
            InsurancePreAuthorizationSubmitItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        request_type = InsurancePreAuthorizationSubmitRequestType(d.pop("request_type"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InsurancePreAuthorizationSubmitItem.from_dict(items_item_data)

            items.append(items_item)

        _enrollee_id = d.pop("enrollee_id", UNSET)
        enrollee_id: UUID | Unset
        if isinstance(_enrollee_id, Unset):
            enrollee_id = UNSET
        else:
            enrollee_id = UUID(_enrollee_id)

        _priority_level = d.pop("priority_level", UNSET)
        priority_level: InsurancePreAuthorizationSubmitPriorityLevel | Unset
        if isinstance(_priority_level, Unset):
            priority_level = UNSET
        else:
            priority_level = InsurancePreAuthorizationSubmitPriorityLevel(_priority_level)

        _encounter_date = d.pop("encounter_date", UNSET)
        encounter_date: datetime.datetime | Unset
        if isinstance(_encounter_date, Unset):
            encounter_date = UNSET
        else:
            encounter_date = datetime.datetime.fromisoformat(_encounter_date)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[InsuranceDiagnosisInput] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = InsuranceDiagnosisInput.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        insurance_pre_authorization_submit = cls(
            patient_id=patient_id,
            insurance_company_id=insurance_company_id,
            request_type=request_type,
            items=items,
            enrollee_id=enrollee_id,
            priority_level=priority_level,
            encounter_date=encounter_date,
            diagnoses=diagnoses,
        )

        return insurance_pre_authorization_submit
