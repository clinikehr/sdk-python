from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.condition_update_clinical_status import ConditionUpdateClinicalStatus
from ..models.condition_update_code_system import ConditionUpdateCodeSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionUpdate")


@_attrs_define
class ConditionUpdate:
    """A proposed change to an existing problem-list entry. It becomes a NEW pending submission; the entry itself does not
    change until a clinician confirms it. `clinical_status: entered_in_error` proposes retracting the entry (nothing is
    ever deleted). `code` and `code_system` go together.

        Attributes:
            title (str | Unset):
            code (str | Unset):
            code_system (ConditionUpdateCodeSystem | Unset):
            clinical_status (ConditionUpdateClinicalStatus | Unset):
            onset_date (datetime.date | Unset):
            resolved_date (datetime.date | Unset):
            notes (str | Unset):
    """

    title: str | Unset = UNSET
    code: str | Unset = UNSET
    code_system: ConditionUpdateCodeSystem | Unset = UNSET
    clinical_status: ConditionUpdateClinicalStatus | Unset = UNSET
    onset_date: datetime.date | Unset = UNSET
    resolved_date: datetime.date | Unset = UNSET
    notes: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        code = d.pop("code", UNSET)

        _code_system = d.pop("code_system", UNSET)
        code_system: ConditionUpdateCodeSystem | Unset
        if isinstance(_code_system, Unset):
            code_system = UNSET
        else:
            code_system = ConditionUpdateCodeSystem(_code_system)

        _clinical_status = d.pop("clinical_status", UNSET)
        clinical_status: ConditionUpdateClinicalStatus | Unset
        if isinstance(_clinical_status, Unset):
            clinical_status = UNSET
        else:
            clinical_status = ConditionUpdateClinicalStatus(_clinical_status)

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

        condition_update = cls(
            title=title,
            code=code,
            code_system=code_system,
            clinical_status=clinical_status,
            onset_date=onset_date,
            resolved_date=resolved_date,
            notes=notes,
        )

        return condition_update
