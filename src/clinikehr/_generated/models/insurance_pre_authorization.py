from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insurance_pre_authorization_priority_level_type_1 import InsurancePreAuthorizationPriorityLevelType1
from ..models.insurance_pre_authorization_priority_level_type_2_type_1 import (
    InsurancePreAuthorizationPriorityLevelType2Type1,
)
from ..models.insurance_pre_authorization_priority_level_type_3_type_1 import (
    InsurancePreAuthorizationPriorityLevelType3Type1,
)
from ..models.insurance_pre_authorization_request_type_type_1 import InsurancePreAuthorizationRequestTypeType1
from ..models.insurance_pre_authorization_request_type_type_2_type_1 import (
    InsurancePreAuthorizationRequestTypeType2Type1,
)
from ..models.insurance_pre_authorization_request_type_type_3_type_1 import (
    InsurancePreAuthorizationRequestTypeType3Type1,
)
from ..models.insurance_pre_authorization_status import InsurancePreAuthorizationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_diagnosis import InsuranceDiagnosis
    from ..models.insurance_pre_authorization_item import InsurancePreAuthorizationItem


T = TypeVar("T", bound="InsurancePreAuthorization")


@_attrs_define
class InsurancePreAuthorization:
    """A pre-authorization request the clinic sent to an insurer. `status` is `sent_for_authorization` until the insurer
    decides, then `approved` or `denied` (with `pa_code` on approval). `items` and `diagnoses` are on the single read
    only.

        Attributes:
            id (UUID):
            request_number (str):
            insurance_company_id (UUID):
            status (InsurancePreAuthorizationStatus):
            insurance_plan_id (None | Unset | UUID):
            enrollee_id (None | Unset | UUID):
            patient_id (UUID | Unset):
            encounter_id (None | Unset | UUID):
            request_type (InsurancePreAuthorizationRequestTypeType1 | InsurancePreAuthorizationRequestTypeType2Type1 |
                InsurancePreAuthorizationRequestTypeType3Type1 | None | Unset):
            priority_level (InsurancePreAuthorizationPriorityLevelType1 | InsurancePreAuthorizationPriorityLevelType2Type1 |
                InsurancePreAuthorizationPriorityLevelType3Type1 | None | Unset):
            estimated_cost (float | None | Unset):
            approved_amount (float | None | Unset):
            pa_code (None | str | Unset):
            pr_code (None | str | Unset):
            is_approved (bool | None | Unset):
            is_handled (bool | None | Unset):
            handled_at (datetime.datetime | None | Unset):
            rejection_reason (None | str | Unset):
            encounter_date (datetime.datetime | None | Unset):
            admission_start (datetime.datetime | None | Unset):
            admission_end (datetime.datetime | None | Unset):
            is_floating (bool | None | Unset):
            submitted_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            items (list[InsurancePreAuthorizationItem] | Unset):
            diagnoses (list[InsuranceDiagnosis] | Unset):
    """

    id: UUID
    request_number: str
    insurance_company_id: UUID
    status: InsurancePreAuthorizationStatus
    insurance_plan_id: None | Unset | UUID = UNSET
    enrollee_id: None | Unset | UUID = UNSET
    patient_id: UUID | Unset = UNSET
    encounter_id: None | Unset | UUID = UNSET
    request_type: (
        InsurancePreAuthorizationRequestTypeType1
        | InsurancePreAuthorizationRequestTypeType2Type1
        | InsurancePreAuthorizationRequestTypeType3Type1
        | None
        | Unset
    ) = UNSET
    priority_level: (
        InsurancePreAuthorizationPriorityLevelType1
        | InsurancePreAuthorizationPriorityLevelType2Type1
        | InsurancePreAuthorizationPriorityLevelType3Type1
        | None
        | Unset
    ) = UNSET
    estimated_cost: float | None | Unset = UNSET
    approved_amount: float | None | Unset = UNSET
    pa_code: None | str | Unset = UNSET
    pr_code: None | str | Unset = UNSET
    is_approved: bool | None | Unset = UNSET
    is_handled: bool | None | Unset = UNSET
    handled_at: datetime.datetime | None | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    encounter_date: datetime.datetime | None | Unset = UNSET
    admission_start: datetime.datetime | None | Unset = UNSET
    admission_end: datetime.datetime | None | Unset = UNSET
    is_floating: bool | None | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    items: list[InsurancePreAuthorizationItem] | Unset = UNSET
    diagnoses: list[InsuranceDiagnosis] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        request_number = self.request_number

        insurance_company_id = str(self.insurance_company_id)

        status = self.status.value

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

        request_type: None | str | Unset
        if isinstance(self.request_type, Unset):
            request_type = UNSET
        elif isinstance(self.request_type, InsurancePreAuthorizationRequestTypeType1):
            request_type = self.request_type.value
        elif isinstance(self.request_type, InsurancePreAuthorizationRequestTypeType2Type1):
            request_type = self.request_type.value
        elif isinstance(self.request_type, InsurancePreAuthorizationRequestTypeType3Type1):
            request_type = self.request_type.value
        else:
            request_type = self.request_type

        priority_level: None | str | Unset
        if isinstance(self.priority_level, Unset):
            priority_level = UNSET
        elif isinstance(self.priority_level, InsurancePreAuthorizationPriorityLevelType1):
            priority_level = self.priority_level.value
        elif isinstance(self.priority_level, InsurancePreAuthorizationPriorityLevelType2Type1):
            priority_level = self.priority_level.value
        elif isinstance(self.priority_level, InsurancePreAuthorizationPriorityLevelType3Type1):
            priority_level = self.priority_level.value
        else:
            priority_level = self.priority_level

        estimated_cost: float | None | Unset
        if isinstance(self.estimated_cost, Unset):
            estimated_cost = UNSET
        else:
            estimated_cost = self.estimated_cost

        approved_amount: float | None | Unset
        if isinstance(self.approved_amount, Unset):
            approved_amount = UNSET
        else:
            approved_amount = self.approved_amount

        pa_code: None | str | Unset
        if isinstance(self.pa_code, Unset):
            pa_code = UNSET
        else:
            pa_code = self.pa_code

        pr_code: None | str | Unset
        if isinstance(self.pr_code, Unset):
            pr_code = UNSET
        else:
            pr_code = self.pr_code

        is_approved: bool | None | Unset
        if isinstance(self.is_approved, Unset):
            is_approved = UNSET
        else:
            is_approved = self.is_approved

        is_handled: bool | None | Unset
        if isinstance(self.is_handled, Unset):
            is_handled = UNSET
        else:
            is_handled = self.is_handled

        handled_at: None | str | Unset
        if isinstance(self.handled_at, Unset):
            handled_at = UNSET
        elif isinstance(self.handled_at, datetime.datetime):
            handled_at = self.handled_at.isoformat()
        else:
            handled_at = self.handled_at

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        encounter_date: None | str | Unset
        if isinstance(self.encounter_date, Unset):
            encounter_date = UNSET
        elif isinstance(self.encounter_date, datetime.datetime):
            encounter_date = self.encounter_date.isoformat()
        else:
            encounter_date = self.encounter_date

        admission_start: None | str | Unset
        if isinstance(self.admission_start, Unset):
            admission_start = UNSET
        elif isinstance(self.admission_start, datetime.datetime):
            admission_start = self.admission_start.isoformat()
        else:
            admission_start = self.admission_start

        admission_end: None | str | Unset
        if isinstance(self.admission_end, Unset):
            admission_end = UNSET
        elif isinstance(self.admission_end, datetime.datetime):
            admission_end = self.admission_end.isoformat()
        else:
            admission_end = self.admission_end

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "request_number": request_number,
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
        if request_type is not UNSET:
            field_dict["request_type"] = request_type
        if priority_level is not UNSET:
            field_dict["priority_level"] = priority_level
        if estimated_cost is not UNSET:
            field_dict["estimated_cost"] = estimated_cost
        if approved_amount is not UNSET:
            field_dict["approved_amount"] = approved_amount
        if pa_code is not UNSET:
            field_dict["pa_code"] = pa_code
        if pr_code is not UNSET:
            field_dict["pr_code"] = pr_code
        if is_approved is not UNSET:
            field_dict["is_approved"] = is_approved
        if is_handled is not UNSET:
            field_dict["is_handled"] = is_handled
        if handled_at is not UNSET:
            field_dict["handled_at"] = handled_at
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason
        if encounter_date is not UNSET:
            field_dict["encounter_date"] = encounter_date
        if admission_start is not UNSET:
            field_dict["admission_start"] = admission_start
        if admission_end is not UNSET:
            field_dict["admission_end"] = admission_end
        if is_floating is not UNSET:
            field_dict["is_floating"] = is_floating
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if items is not UNSET:
            field_dict["items"] = items
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_diagnosis import InsuranceDiagnosis  # noqa: PLC0415
        from ..models.insurance_pre_authorization_item import InsurancePreAuthorizationItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        request_number = d.pop("request_number")

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        status = InsurancePreAuthorizationStatus(d.pop("status"))

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

        def _parse_request_type(
            data: object,
        ) -> (
            InsurancePreAuthorizationRequestTypeType1
            | InsurancePreAuthorizationRequestTypeType2Type1
            | InsurancePreAuthorizationRequestTypeType3Type1
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
                request_type_type_1 = InsurancePreAuthorizationRequestTypeType1(data)

                return request_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_type_type_2_type_1 = InsurancePreAuthorizationRequestTypeType2Type1(data)

                return request_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_type_type_3_type_1 = InsurancePreAuthorizationRequestTypeType3Type1(data)

                return request_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InsurancePreAuthorizationRequestTypeType1
                | InsurancePreAuthorizationRequestTypeType2Type1
                | InsurancePreAuthorizationRequestTypeType3Type1
                | None
                | Unset,
                data,
            )

        request_type = _parse_request_type(d.pop("request_type", UNSET))

        def _parse_priority_level(
            data: object,
        ) -> (
            InsurancePreAuthorizationPriorityLevelType1
            | InsurancePreAuthorizationPriorityLevelType2Type1
            | InsurancePreAuthorizationPriorityLevelType3Type1
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
                priority_level_type_1 = InsurancePreAuthorizationPriorityLevelType1(data)

                return priority_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_level_type_2_type_1 = InsurancePreAuthorizationPriorityLevelType2Type1(data)

                return priority_level_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_level_type_3_type_1 = InsurancePreAuthorizationPriorityLevelType3Type1(data)

                return priority_level_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InsurancePreAuthorizationPriorityLevelType1
                | InsurancePreAuthorizationPriorityLevelType2Type1
                | InsurancePreAuthorizationPriorityLevelType3Type1
                | None
                | Unset,
                data,
            )

        priority_level = _parse_priority_level(d.pop("priority_level", UNSET))

        def _parse_estimated_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_cost = _parse_estimated_cost(d.pop("estimated_cost", UNSET))

        def _parse_approved_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        approved_amount = _parse_approved_amount(d.pop("approved_amount", UNSET))

        def _parse_pa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_code = _parse_pa_code(d.pop("pa_code", UNSET))

        def _parse_pr_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pr_code = _parse_pr_code(d.pop("pr_code", UNSET))

        def _parse_is_approved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_approved = _parse_is_approved(d.pop("is_approved", UNSET))

        def _parse_is_handled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_handled = _parse_is_handled(d.pop("is_handled", UNSET))

        def _parse_handled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                handled_at_type_0 = datetime.datetime.fromisoformat(data)

                return handled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        handled_at = _parse_handled_at(d.pop("handled_at", UNSET))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))

        def _parse_encounter_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encounter_date_type_0 = datetime.datetime.fromisoformat(data)

                return encounter_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        encounter_date = _parse_encounter_date(d.pop("encounter_date", UNSET))

        def _parse_admission_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admission_start_type_0 = datetime.datetime.fromisoformat(data)

                return admission_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        admission_start = _parse_admission_start(d.pop("admission_start", UNSET))

        def _parse_admission_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admission_end_type_0 = datetime.datetime.fromisoformat(data)

                return admission_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        admission_end = _parse_admission_end(d.pop("admission_end", UNSET))

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
        items: list[InsurancePreAuthorizationItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = InsurancePreAuthorizationItem.from_dict(items_item_data)

                items.append(items_item)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[InsuranceDiagnosis] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = InsuranceDiagnosis.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        insurance_pre_authorization = cls(
            id=id,
            request_number=request_number,
            insurance_company_id=insurance_company_id,
            status=status,
            insurance_plan_id=insurance_plan_id,
            enrollee_id=enrollee_id,
            patient_id=patient_id,
            encounter_id=encounter_id,
            request_type=request_type,
            priority_level=priority_level,
            estimated_cost=estimated_cost,
            approved_amount=approved_amount,
            pa_code=pa_code,
            pr_code=pr_code,
            is_approved=is_approved,
            is_handled=is_handled,
            handled_at=handled_at,
            rejection_reason=rejection_reason,
            encounter_date=encounter_date,
            admission_start=admission_start,
            admission_end=admission_end,
            is_floating=is_floating,
            submitted_at=submitted_at,
            created_at=created_at,
            updated_at=updated_at,
            items=items,
            diagnoses=diagnoses,
        )

        insurance_pre_authorization.additional_properties = d
        return insurance_pre_authorization

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
