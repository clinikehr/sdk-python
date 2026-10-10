from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insurance_claim_claim_type_type_1 import InsuranceClaimClaimTypeType1
from ..models.insurance_claim_claim_type_type_2_type_1 import InsuranceClaimClaimTypeType2Type1
from ..models.insurance_claim_claim_type_type_3_type_1 import InsuranceClaimClaimTypeType3Type1
from ..models.insurance_claim_hmo_status_type_1 import InsuranceClaimHmoStatusType1
from ..models.insurance_claim_hmo_status_type_2_type_1 import InsuranceClaimHmoStatusType2Type1
from ..models.insurance_claim_hmo_status_type_3_type_1 import InsuranceClaimHmoStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_claim_document import InsuranceClaimDocument
    from ..models.insurance_claim_item import InsuranceClaimItem
    from ..models.insurance_diagnosis import InsuranceDiagnosis


T = TypeVar("T", bound="InsuranceClaim")


@_attrs_define
class InsuranceClaim:
    """A claim the clinic submitted to an insurer. `status` is the clinic-side lifecycle (`submitted`, `approved`,
    `partially_approved`, `denied`, `partially_paid`, `paid`, ...); `hmo_status` is the insurer's verdict (`PENDING`,
    `APPROVED`, `PARTIALLY_APPROVED`, `REJECTED`). `paid_amount` and `written_off_amount` are what the CLINIC has
    recorded - no API call changes them. `items`, `diagnoses` and `documents` are on the single-claim read only. The
    clinic's notes and internal analysis are never exposed.

        Attributes:
            id (UUID):
            claim_number (str):
            insurance_company_id (UUID):
            status (str):
            insurance_plan_id (None | Unset | UUID):
            enrollee_id (None | Unset | UUID):
            patient_id (UUID | Unset):
            encounter_id (None | Unset | UUID):
            pre_auth_ids (list[UUID] | Unset):
            pa_code (None | str | Unset):
            claim_type (InsuranceClaimClaimTypeType1 | InsuranceClaimClaimTypeType2Type1 | InsuranceClaimClaimTypeType3Type1
                | None | Unset):
            hmo_status (InsuranceClaimHmoStatusType1 | InsuranceClaimHmoStatusType2Type1 | InsuranceClaimHmoStatusType3Type1
                | None | Unset):
            currency (None | str | Unset):
            amount_billed (float | None | Unset):
            amount_approved (float | None | Unset):
            paid_amount (float | None | Unset):
            written_off_amount (float | None | Unset):
            patient_responsibility (float | None | Unset):
            service_date_from (datetime.datetime | None | Unset):
            service_date_to (datetime.datetime | None | Unset):
            admission_date (datetime.datetime | None | Unset):
            discharge_date (datetime.datetime | None | Unset):
            is_floating (bool | None | Unset):
            submitted_at (datetime.datetime | None | Unset):
            vetted_at (datetime.datetime | None | Unset):
            approved_at (datetime.datetime | None | Unset):
            paid_at (datetime.datetime | None | Unset):
            denial_reason (None | str | Unset):
            denial_code (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            items (list[InsuranceClaimItem] | Unset):
            diagnoses (list[InsuranceDiagnosis] | Unset):
            documents (list[InsuranceClaimDocument] | Unset):
    """

    id: UUID
    claim_number: str
    insurance_company_id: UUID
    status: str
    insurance_plan_id: None | Unset | UUID = UNSET
    enrollee_id: None | Unset | UUID = UNSET
    patient_id: UUID | Unset = UNSET
    encounter_id: None | Unset | UUID = UNSET
    pre_auth_ids: list[UUID] | Unset = UNSET
    pa_code: None | str | Unset = UNSET
    claim_type: (
        InsuranceClaimClaimTypeType1
        | InsuranceClaimClaimTypeType2Type1
        | InsuranceClaimClaimTypeType3Type1
        | None
        | Unset
    ) = UNSET
    hmo_status: (
        InsuranceClaimHmoStatusType1
        | InsuranceClaimHmoStatusType2Type1
        | InsuranceClaimHmoStatusType3Type1
        | None
        | Unset
    ) = UNSET
    currency: None | str | Unset = UNSET
    amount_billed: float | None | Unset = UNSET
    amount_approved: float | None | Unset = UNSET
    paid_amount: float | None | Unset = UNSET
    written_off_amount: float | None | Unset = UNSET
    patient_responsibility: float | None | Unset = UNSET
    service_date_from: datetime.datetime | None | Unset = UNSET
    service_date_to: datetime.datetime | None | Unset = UNSET
    admission_date: datetime.datetime | None | Unset = UNSET
    discharge_date: datetime.datetime | None | Unset = UNSET
    is_floating: bool | None | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    vetted_at: datetime.datetime | None | Unset = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    paid_at: datetime.datetime | None | Unset = UNSET
    denial_reason: None | str | Unset = UNSET
    denial_code: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    items: list[InsuranceClaimItem] | Unset = UNSET
    diagnoses: list[InsuranceDiagnosis] | Unset = UNSET
    documents: list[InsuranceClaimDocument] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        claim_number = self.claim_number

        insurance_company_id = str(self.insurance_company_id)

        status = self.status

        insurance_plan_id: None | str | Unset
        if isinstance(self.insurance_plan_id, Unset):
            insurance_plan_id = UNSET
        elif isinstance(self.insurance_plan_id, UUID):
            insurance_plan_id = str(self.insurance_plan_id)
        else:
            insurance_plan_id = self.insurance_plan_id

        enrollee_id: None | str | Unset
        if isinstance(self.enrollee_id, Unset):
            enrollee_id = UNSET
        elif isinstance(self.enrollee_id, UUID):
            enrollee_id = str(self.enrollee_id)
        else:
            enrollee_id = self.enrollee_id

        patient_id: str | Unset = UNSET
        if not isinstance(self.patient_id, Unset):
            patient_id = str(self.patient_id)

        encounter_id: None | str | Unset
        if isinstance(self.encounter_id, Unset):
            encounter_id = UNSET
        elif isinstance(self.encounter_id, UUID):
            encounter_id = str(self.encounter_id)
        else:
            encounter_id = self.encounter_id

        pre_auth_ids: list[str] | Unset = UNSET
        if not isinstance(self.pre_auth_ids, Unset):
            pre_auth_ids = []
            for pre_auth_ids_item_data in self.pre_auth_ids:
                pre_auth_ids_item = str(pre_auth_ids_item_data)
                pre_auth_ids.append(pre_auth_ids_item)

        pa_code: None | str | Unset
        if isinstance(self.pa_code, Unset):
            pa_code = UNSET
        else:
            pa_code = self.pa_code

        claim_type: None | str | Unset
        if isinstance(self.claim_type, Unset):
            claim_type = UNSET
        elif isinstance(self.claim_type, InsuranceClaimClaimTypeType1):
            claim_type = self.claim_type.value
        elif isinstance(self.claim_type, InsuranceClaimClaimTypeType2Type1):
            claim_type = self.claim_type.value
        elif isinstance(self.claim_type, InsuranceClaimClaimTypeType3Type1):
            claim_type = self.claim_type.value
        else:
            claim_type = self.claim_type

        hmo_status: None | str | Unset
        if isinstance(self.hmo_status, Unset):
            hmo_status = UNSET
        elif isinstance(self.hmo_status, InsuranceClaimHmoStatusType1):
            hmo_status = self.hmo_status.value
        elif isinstance(self.hmo_status, InsuranceClaimHmoStatusType2Type1):
            hmo_status = self.hmo_status.value
        elif isinstance(self.hmo_status, InsuranceClaimHmoStatusType3Type1):
            hmo_status = self.hmo_status.value
        else:
            hmo_status = self.hmo_status

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        amount_billed: float | None | Unset
        if isinstance(self.amount_billed, Unset):
            amount_billed = UNSET
        else:
            amount_billed = self.amount_billed

        amount_approved: float | None | Unset
        if isinstance(self.amount_approved, Unset):
            amount_approved = UNSET
        else:
            amount_approved = self.amount_approved

        paid_amount: float | None | Unset
        if isinstance(self.paid_amount, Unset):
            paid_amount = UNSET
        else:
            paid_amount = self.paid_amount

        written_off_amount: float | None | Unset
        if isinstance(self.written_off_amount, Unset):
            written_off_amount = UNSET
        else:
            written_off_amount = self.written_off_amount

        patient_responsibility: float | None | Unset
        if isinstance(self.patient_responsibility, Unset):
            patient_responsibility = UNSET
        else:
            patient_responsibility = self.patient_responsibility

        service_date_from: None | str | Unset
        if isinstance(self.service_date_from, Unset):
            service_date_from = UNSET
        elif isinstance(self.service_date_from, datetime.datetime):
            service_date_from = self.service_date_from.isoformat()
        else:
            service_date_from = self.service_date_from

        service_date_to: None | str | Unset
        if isinstance(self.service_date_to, Unset):
            service_date_to = UNSET
        elif isinstance(self.service_date_to, datetime.datetime):
            service_date_to = self.service_date_to.isoformat()
        else:
            service_date_to = self.service_date_to

        admission_date: None | str | Unset
        if isinstance(self.admission_date, Unset):
            admission_date = UNSET
        elif isinstance(self.admission_date, datetime.datetime):
            admission_date = self.admission_date.isoformat()
        else:
            admission_date = self.admission_date

        discharge_date: None | str | Unset
        if isinstance(self.discharge_date, Unset):
            discharge_date = UNSET
        elif isinstance(self.discharge_date, datetime.datetime):
            discharge_date = self.discharge_date.isoformat()
        else:
            discharge_date = self.discharge_date

        is_floating: bool | None | Unset
        if isinstance(self.is_floating, Unset):
            is_floating = UNSET
        else:
            is_floating = self.is_floating

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        vetted_at: None | str | Unset
        if isinstance(self.vetted_at, Unset):
            vetted_at = UNSET
        elif isinstance(self.vetted_at, datetime.datetime):
            vetted_at = self.vetted_at.isoformat()
        else:
            vetted_at = self.vetted_at

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        denial_reason: None | str | Unset
        if isinstance(self.denial_reason, Unset):
            denial_reason = UNSET
        else:
            denial_reason = self.denial_reason

        denial_code: None | str | Unset
        if isinstance(self.denial_code, Unset):
            denial_code = UNSET
        else:
            denial_code = self.denial_code

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        diagnoses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnoses, Unset):
            diagnoses = []
            for diagnoses_item_data in self.diagnoses:
                diagnoses_item = diagnoses_item_data.to_dict()
                diagnoses.append(diagnoses_item)

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "claim_number": claim_number,
                "insurance_company_id": insurance_company_id,
                "status": status,
            }
        )
        if insurance_plan_id is not UNSET:
            field_dict["insurance_plan_id"] = insurance_plan_id
        if enrollee_id is not UNSET:
            field_dict["enrollee_id"] = enrollee_id
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if encounter_id is not UNSET:
            field_dict["encounter_id"] = encounter_id
        if pre_auth_ids is not UNSET:
            field_dict["pre_auth_ids"] = pre_auth_ids
        if pa_code is not UNSET:
            field_dict["pa_code"] = pa_code
        if claim_type is not UNSET:
            field_dict["claim_type"] = claim_type
        if hmo_status is not UNSET:
            field_dict["hmo_status"] = hmo_status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount_billed is not UNSET:
            field_dict["amount_billed"] = amount_billed
        if amount_approved is not UNSET:
            field_dict["amount_approved"] = amount_approved
        if paid_amount is not UNSET:
            field_dict["paid_amount"] = paid_amount
        if written_off_amount is not UNSET:
            field_dict["written_off_amount"] = written_off_amount
        if patient_responsibility is not UNSET:
            field_dict["patient_responsibility"] = patient_responsibility
        if service_date_from is not UNSET:
            field_dict["service_date_from"] = service_date_from
        if service_date_to is not UNSET:
            field_dict["service_date_to"] = service_date_to
        if admission_date is not UNSET:
            field_dict["admission_date"] = admission_date
        if discharge_date is not UNSET:
            field_dict["discharge_date"] = discharge_date
        if is_floating is not UNSET:
            field_dict["is_floating"] = is_floating
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if vetted_at is not UNSET:
            field_dict["vetted_at"] = vetted_at
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if denial_reason is not UNSET:
            field_dict["denial_reason"] = denial_reason
        if denial_code is not UNSET:
            field_dict["denial_code"] = denial_code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if items is not UNSET:
            field_dict["items"] = items
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_claim_document import InsuranceClaimDocument  # noqa: PLC0415
        from ..models.insurance_claim_item import InsuranceClaimItem  # noqa: PLC0415
        from ..models.insurance_diagnosis import InsuranceDiagnosis  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        claim_number = d.pop("claim_number")

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        status = d.pop("status")

        def _parse_insurance_plan_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                insurance_plan_id_type_0 = UUID(data)

                return insurance_plan_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        insurance_plan_id = _parse_insurance_plan_id(d.pop("insurance_plan_id", UNSET))

        def _parse_enrollee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollee_id_type_0 = UUID(data)

                return enrollee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        enrollee_id = _parse_enrollee_id(d.pop("enrollee_id", UNSET))

        _patient_id = d.pop("patient_id", UNSET)
        patient_id: UUID | Unset
        if isinstance(_patient_id, Unset):
            patient_id = UNSET
        else:
            patient_id = UUID(_patient_id)

        def _parse_encounter_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encounter_id_type_0 = UUID(data)

                return encounter_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        encounter_id = _parse_encounter_id(d.pop("encounter_id", UNSET))

        _pre_auth_ids = d.pop("pre_auth_ids", UNSET)
        pre_auth_ids: list[UUID] | Unset = UNSET
        if _pre_auth_ids is not UNSET:
            pre_auth_ids = []
            for pre_auth_ids_item_data in _pre_auth_ids:
                pre_auth_ids_item = UUID(pre_auth_ids_item_data)

                pre_auth_ids.append(pre_auth_ids_item)

        def _parse_pa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_code = _parse_pa_code(d.pop("pa_code", UNSET))

        def _parse_claim_type(
            data: object,
        ) -> (
            InsuranceClaimClaimTypeType1
            | InsuranceClaimClaimTypeType2Type1
            | InsuranceClaimClaimTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                claim_type_type_1 = InsuranceClaimClaimTypeType1(data)

                return claim_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                claim_type_type_2_type_1 = InsuranceClaimClaimTypeType2Type1(data)

                return claim_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                claim_type_type_3_type_1 = InsuranceClaimClaimTypeType3Type1(data)

                return claim_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InsuranceClaimClaimTypeType1
                | InsuranceClaimClaimTypeType2Type1
                | InsuranceClaimClaimTypeType3Type1
                | None
                | Unset,
                data,
            )

        claim_type = _parse_claim_type(d.pop("claim_type", UNSET))

        def _parse_hmo_status(
            data: object,
        ) -> (
            InsuranceClaimHmoStatusType1
            | InsuranceClaimHmoStatusType2Type1
            | InsuranceClaimHmoStatusType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_status_type_1 = InsuranceClaimHmoStatusType1(data)

                return hmo_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_status_type_2_type_1 = InsuranceClaimHmoStatusType2Type1(data)

                return hmo_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_status_type_3_type_1 = InsuranceClaimHmoStatusType3Type1(data)

                return hmo_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InsuranceClaimHmoStatusType1
                | InsuranceClaimHmoStatusType2Type1
                | InsuranceClaimHmoStatusType3Type1
                | None
                | Unset,
                data,
            )

        hmo_status = _parse_hmo_status(d.pop("hmo_status", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_amount_billed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_billed = _parse_amount_billed(d.pop("amount_billed", UNSET))

        def _parse_amount_approved(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_approved = _parse_amount_approved(d.pop("amount_approved", UNSET))

        def _parse_paid_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        paid_amount = _parse_paid_amount(d.pop("paid_amount", UNSET))

        def _parse_written_off_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        written_off_amount = _parse_written_off_amount(d.pop("written_off_amount", UNSET))

        def _parse_patient_responsibility(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        patient_responsibility = _parse_patient_responsibility(d.pop("patient_responsibility", UNSET))

        def _parse_service_date_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_from_type_0 = datetime.datetime.fromisoformat(data)

                return service_date_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        service_date_from = _parse_service_date_from(d.pop("service_date_from", UNSET))

        def _parse_service_date_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_to_type_0 = datetime.datetime.fromisoformat(data)

                return service_date_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        service_date_to = _parse_service_date_to(d.pop("service_date_to", UNSET))

        def _parse_admission_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admission_date_type_0 = datetime.datetime.fromisoformat(data)

                return admission_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        admission_date = _parse_admission_date(d.pop("admission_date", UNSET))

        def _parse_discharge_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discharge_date_type_0 = datetime.datetime.fromisoformat(data)

                return discharge_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        discharge_date = _parse_discharge_date(d.pop("discharge_date", UNSET))

        def _parse_is_floating(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_floating = _parse_is_floating(d.pop("is_floating", UNSET))

        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)

                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))

        def _parse_vetted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vetted_at_type_0 = datetime.datetime.fromisoformat(data)

                return vetted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        vetted_at = _parse_vetted_at(d.pop("vetted_at", UNSET))

        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approved_at", UNSET))

        def _parse_paid_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = datetime.datetime.fromisoformat(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))

        def _parse_denial_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        denial_reason = _parse_denial_reason(d.pop("denial_reason", UNSET))

        def _parse_denial_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        denial_code = _parse_denial_code(d.pop("denial_code", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        _items = d.pop("items", UNSET)
        items: list[InsuranceClaimItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = InsuranceClaimItem.from_dict(items_item_data)

                items.append(items_item)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[InsuranceDiagnosis] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = InsuranceDiagnosis.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        _documents = d.pop("documents", UNSET)
        documents: list[InsuranceClaimDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = InsuranceClaimDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        insurance_claim = cls(
            id=id,
            claim_number=claim_number,
            insurance_company_id=insurance_company_id,
            status=status,
            insurance_plan_id=insurance_plan_id,
            enrollee_id=enrollee_id,
            patient_id=patient_id,
            encounter_id=encounter_id,
            pre_auth_ids=pre_auth_ids,
            pa_code=pa_code,
            claim_type=claim_type,
            hmo_status=hmo_status,
            currency=currency,
            amount_billed=amount_billed,
            amount_approved=amount_approved,
            paid_amount=paid_amount,
            written_off_amount=written_off_amount,
            patient_responsibility=patient_responsibility,
            service_date_from=service_date_from,
            service_date_to=service_date_to,
            admission_date=admission_date,
            discharge_date=discharge_date,
            is_floating=is_floating,
            submitted_at=submitted_at,
            vetted_at=vetted_at,
            approved_at=approved_at,
            paid_at=paid_at,
            denial_reason=denial_reason,
            denial_code=denial_code,
            created_at=created_at,
            updated_at=updated_at,
            items=items,
            diagnoses=diagnoses,
            documents=documents,
        )

        insurance_claim.additional_properties = d
        return insurance_claim

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
