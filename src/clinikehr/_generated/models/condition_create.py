from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.condition_create_clinical_status import ConditionCreateClinicalStatus
from ..models.condition_create_code_system import ConditionCreateCodeSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionCreate")


@_attrs_define
class ConditionCreate:
    """An outside condition, submitted for a clinician to confirm. It does not enter the problem list until then. `code`
    and `code_system` go together. `client_reference` (your own id for the record, up to 200 characters) makes a second
    submission of the same record with different content a `client_reference_conflict`.

        Attributes:
            patient_id (UUID):
            title (str):
            code (str | Unset):
            code_system (ConditionCreateCodeSystem | Unset):
            clinical_status (ConditionCreateClinicalStatus | Unset):  Default: ConditionCreateClinicalStatus.ACTIVE.
            onset_date (datetime.date | Unset):
            resolved_date (datetime.date | Unset):
            notes (str | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    title: str
    code: str | Unset = UNSET
    code_system: ConditionCreateCodeSystem | Unset = UNSET
    clinical_status: ConditionCreateClinicalStatus | Unset = ConditionCreateClinicalStatus.ACTIVE
    onset_date: datetime.date | Unset = UNSET
    resolved_date: datetime.date | Unset = UNSET
    notes: str | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        title = self.title

        code = self.code

        code_system: str | Unset = UNSET
        if not isinstance(self.code_system, Unset):
            code_system = self.code_system.value

        clinical_status: str | Unset = UNSET
        if not isinstance(self.clinical_status, Unset):
            clinical_status = self.clinical_status.value

        onset_date: str | Unset = UNSET
        if not isinstance(self.onset_date, Unset):
            onset_date = self.onset_date.isoformat()

        resolved_date: str | Unset = UNSET
        if not isinstance(self.resolved_date, Unset):
            resolved_date = self.resolved_date.isoformat()

        notes = self.notes

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "title": title,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if code_system is not UNSET:
            field_dict["code_system"] = code_system
        if clinical_status is not UNSET:
            field_dict["clinical_status"] = clinical_status
        if onset_date is not UNSET:
            field_dict["onset_date"] = onset_date
        if resolved_date is not UNSET:
            field_dict["resolved_date"] = resolved_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        title = d.pop("title")

        code = d.pop("code", UNSET)

        _code_system = d.pop("code_system", UNSET)
        code_system: ConditionCreateCodeSystem | Unset
        if isinstance(_code_system, Unset):
            code_system = UNSET
        else:
            code_system = ConditionCreateCodeSystem(_code_system)

        _clinical_status = d.pop("clinical_status", UNSET)
        clinical_status: ConditionCreateClinicalStatus | Unset
        if isinstance(_clinical_status, Unset):
            clinical_status = UNSET
        else:
            clinical_status = ConditionCreateClinicalStatus(_clinical_status)

        _onset_date = d.pop("onset_date", UNSET)
        onset_date: datetime.date | Unset
        if isinstance(_onset_date, Unset):
            onset_date = UNSET
        else:
            onset_date = datetime.date.fromisoformat(_onset_date)

        _resolved_date = d.pop("resolved_date", UNSET)
        resolved_date: datetime.date | Unset
        if isinstance(_resolved_date, Unset):
            resolved_date = UNSET
        else:
            resolved_date = datetime.date.fromisoformat(_resolved_date)

        notes = d.pop("notes", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        condition_create = cls(
            patient_id=patient_id,
            title=title,
            code=code,
            code_system=code_system,
            clinical_status=clinical_status,
            onset_date=onset_date,
            resolved_date=resolved_date,
            notes=notes,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return condition_create
