from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.insurance_claim_submit_claim_type import InsuranceClaimSubmitClaimType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_claim_submit_item import InsuranceClaimSubmitItem
    from ..models.insurance_diagnosis_input import InsuranceDiagnosisInput


T = TypeVar("T", bound="InsuranceClaimSubmit")


@_attrs_define
class InsuranceClaimSubmit:
    """A claim to submit to one of the clinic's insurers for a patient. It is saved as `submitted` with no money on it.
    `patient_id` must be a patient your organization is linked to (a clinic-owned key may use any of its clinic's
    patients). There is no field for a paid or written-off amount; sending one is refused as an unknown field.

        Attributes:
            patient_id (UUID):
            insurance_company_id (UUID):
            service_date_from (datetime.datetime):
            items (list[InsuranceClaimSubmitItem]):
            enrollee_id (UUID | Unset): Must be an enrollee of that patient with that insurer.
            claim_type (InsuranceClaimSubmitClaimType | Unset):  Default: InsuranceClaimSubmitClaimType.OUTPATIENT.
            service_date_to (datetime.datetime | Unset):
            admission_date (datetime.datetime | Unset):
            discharge_date (datetime.datetime | Unset):
            pa_code (str | Unset):
            diagnoses (list[InsuranceDiagnosisInput] | Unset):
    """

    patient_id: UUID
    insurance_company_id: UUID
    service_date_from: datetime.datetime
    items: list[InsuranceClaimSubmitItem]
    enrollee_id: UUID | Unset = UNSET
    claim_type: InsuranceClaimSubmitClaimType | Unset = InsuranceClaimSubmitClaimType.OUTPATIENT
    service_date_to: datetime.datetime | Unset = UNSET
    admission_date: datetime.datetime | Unset = UNSET
    discharge_date: datetime.datetime | Unset = UNSET
    pa_code: str | Unset = UNSET
    diagnoses: list[InsuranceDiagnosisInput] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        insurance_company_id = str(self.insurance_company_id)

        service_date_from = self.service_date_from.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        enrollee_id: str | Unset = UNSET
        if not isinstance(self.enrollee_id, Unset):
            enrollee_id = str(self.enrollee_id)

        claim_type: str | Unset = UNSET
        if not isinstance(self.claim_type, Unset):
            claim_type = self.claim_type.value

        service_date_to: str | Unset = UNSET
        if not isinstance(self.service_date_to, Unset):
            service_date_to = self.service_date_to.isoformat()

        admission_date: str | Unset = UNSET
        if not isinstance(self.admission_date, Unset):
            admission_date = self.admission_date.isoformat()

        discharge_date: str | Unset = UNSET
        if not isinstance(self.discharge_date, Unset):
            discharge_date = self.discharge_date.isoformat()

        pa_code = self.pa_code

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
                "service_date_from": service_date_from,
                "items": items,
            }
        )
        if enrollee_id is not UNSET:
            field_dict["enrollee_id"] = enrollee_id
        if claim_type is not UNSET:
            field_dict["claim_type"] = claim_type
        if service_date_to is not UNSET:
            field_dict["service_date_to"] = service_date_to
        if admission_date is not UNSET:
            field_dict["admission_date"] = admission_date
        if discharge_date is not UNSET:
            field_dict["discharge_date"] = discharge_date
        if pa_code is not UNSET:
            field_dict["pa_code"] = pa_code
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_claim_submit_item import InsuranceClaimSubmitItem  # noqa: PLC0415
        from ..models.insurance_diagnosis_input import InsuranceDiagnosisInput  # noqa: PLC0415

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        service_date_from = datetime.datetime.fromisoformat(d.pop("service_date_from"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InsuranceClaimSubmitItem.from_dict(items_item_data)

            items.append(items_item)

        _enrollee_id = d.pop("enrollee_id", UNSET)
        enrollee_id: UUID | Unset
        if isinstance(_enrollee_id, Unset):
            enrollee_id = UNSET
        else:
            enrollee_id = UUID(_enrollee_id)

        _claim_type = d.pop("claim_type", UNSET)
        claim_type: InsuranceClaimSubmitClaimType | Unset
        if isinstance(_claim_type, Unset):
            claim_type = UNSET
        else:
            claim_type = InsuranceClaimSubmitClaimType(_claim_type)

        _service_date_to = d.pop("service_date_to", UNSET)
        service_date_to: datetime.datetime | Unset
        if isinstance(_service_date_to, Unset):
            service_date_to = UNSET
        else:
            service_date_to = datetime.datetime.fromisoformat(_service_date_to)

        _admission_date = d.pop("admission_date", UNSET)
        admission_date: datetime.datetime | Unset
        if isinstance(_admission_date, Unset):
            admission_date = UNSET
        else:
            admission_date = datetime.datetime.fromisoformat(_admission_date)

        _discharge_date = d.pop("discharge_date", UNSET)
        discharge_date: datetime.datetime | Unset
        if isinstance(_discharge_date, Unset):
            discharge_date = UNSET
        else:
            discharge_date = datetime.datetime.fromisoformat(_discharge_date)

        pa_code = d.pop("pa_code", UNSET)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[InsuranceDiagnosisInput] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = InsuranceDiagnosisInput.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        insurance_claim_submit = cls(
            patient_id=patient_id,
            insurance_company_id=insurance_company_id,
            service_date_from=service_date_from,
            items=items,
            enrollee_id=enrollee_id,
            claim_type=claim_type,
            service_date_to=service_date_to,
            admission_date=admission_date,
            discharge_date=discharge_date,
            pa_code=pa_code,
            diagnoses=diagnoses,
        )

        return insurance_claim_submit
