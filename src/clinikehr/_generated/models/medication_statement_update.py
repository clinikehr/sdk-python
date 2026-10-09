from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.medication_statement_update_status import MedicationStatementUpdateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medication_statement_update_dosage import MedicationStatementUpdateDosage


T = TypeVar("T", bound="MedicationStatementUpdate")


@_attrs_define
class MedicationStatementUpdate:
    """A proposed change to a reported medicine. It becomes a NEW pending submission; the statement does not change until a
    clinician confirms it. The medicine itself can never be changed (a different medicine is a new statement). `status:
    entered_in_error` proposes retracting the statement and cannot be combined with other changes.

        Attributes:
            status (MedicationStatementUpdateStatus | Unset):
            dosage (MedicationStatementUpdateDosage | Unset):
            effective_start (datetime.date | Unset):
            effective_end (datetime.date | Unset):
            reason (str | Unset):
            note (str | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    status: MedicationStatementUpdateStatus | Unset = UNSET
    dosage: MedicationStatementUpdateDosage | Unset = UNSET
    effective_start: datetime.date | Unset = UNSET
    effective_end: datetime.date | Unset = UNSET
    reason: str | Unset = UNSET
    note: str | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        dosage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dosage, Unset):
            dosage = self.dosage.to_dict()

        effective_start: str | Unset = UNSET
        if not isinstance(self.effective_start, Unset):
            effective_start = self.effective_start.isoformat()

        effective_end: str | Unset = UNSET
        if not isinstance(self.effective_end, Unset):
            effective_end = self.effective_end.isoformat()

        reason = self.reason

        note = self.note

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if dosage is not UNSET:
            field_dict["dosage"] = dosage
        if effective_start is not UNSET:
            field_dict["effective_start"] = effective_start
        if effective_end is not UNSET:
            field_dict["effective_end"] = effective_end
        if reason is not UNSET:
            field_dict["reason"] = reason
        if note is not UNSET:
            field_dict["note"] = note
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medication_statement_update_dosage import MedicationStatementUpdateDosage  # noqa: PLC0415

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: MedicationStatementUpdateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MedicationStatementUpdateStatus(_status)

        _dosage = d.pop("dosage", UNSET)
        dosage: MedicationStatementUpdateDosage | Unset
        if isinstance(_dosage, Unset):
            dosage = UNSET
        else:
            dosage = MedicationStatementUpdateDosage.from_dict(_dosage)

        _effective_start = d.pop("effective_start", UNSET)
        effective_start: datetime.date | Unset
        if isinstance(_effective_start, Unset):
            effective_start = UNSET
        else:
            effective_start = datetime.date.fromisoformat(_effective_start)

        _effective_end = d.pop("effective_end", UNSET)
        effective_end: datetime.date | Unset
        if isinstance(_effective_end, Unset):
            effective_end = UNSET
        else:
            effective_end = datetime.date.fromisoformat(_effective_end)

        reason = d.pop("reason", UNSET)

        note = d.pop("note", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        medication_statement_update = cls(
            status=status,
            dosage=dosage,
            effective_start=effective_start,
            effective_end=effective_end,
            reason=reason,
            note=note,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return medication_statement_update
