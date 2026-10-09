from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.medication_statement_create_status import MedicationStatementCreateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medication_statement_create_dosage import MedicationStatementCreateDosage
    from ..models.medication_statement_create_medication import MedicationStatementCreateMedication


T = TypeVar("T", bound="MedicationStatementCreate")


@_attrs_define
class MedicationStatementCreate:
    """A reported medicine, submitted for a clinician to confirm. It does not enter the chart until then and it prescribes
    nothing. A medicine may be reported more than once. `medication.code` is optional: send `{system: rxnorm, code}`
    only for a real RxNorm code (it is checked against the platform's drug data and an unrecognised one is refused), or
    `{system: local, code}` for your own code. `client_reference` (your own id, up to 200 characters) makes a second
    submission of the same record with different content a `client_reference_conflict`.

        Attributes:
            patient_id (UUID):
            medication (MedicationStatementCreateMedication):
            dosage (MedicationStatementCreateDosage | Unset):
            status (MedicationStatementCreateStatus | Unset):  Default: MedicationStatementCreateStatus.ACTIVE.
            effective_start (datetime.date | Unset):
            effective_end (datetime.date | Unset): Not before `effective_start`.
            reason (str | Unset):
            note (str | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    medication: MedicationStatementCreateMedication
    dosage: MedicationStatementCreateDosage | Unset = UNSET
    status: MedicationStatementCreateStatus | Unset = MedicationStatementCreateStatus.ACTIVE
    effective_start: datetime.date | Unset = UNSET
    effective_end: datetime.date | Unset = UNSET
    reason: str | Unset = UNSET
    note: str | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        medication = self.medication.to_dict()

        dosage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dosage, Unset):
            dosage = self.dosage.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        field_dict.update(
            {
                "patient_id": patient_id,
                "medication": medication,
            }
        )
        if dosage is not UNSET:
            field_dict["dosage"] = dosage
        if status is not UNSET:
            field_dict["status"] = status
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
        from ..models.medication_statement_create_dosage import MedicationStatementCreateDosage  # noqa: PLC0415
        from ..models.medication_statement_create_medication import MedicationStatementCreateMedication  # noqa: PLC0415

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        medication = MedicationStatementCreateMedication.from_dict(d.pop("medication"))

        _dosage = d.pop("dosage", UNSET)
        dosage: MedicationStatementCreateDosage | Unset
        if isinstance(_dosage, Unset):
            dosage = UNSET
        else:
            dosage = MedicationStatementCreateDosage.from_dict(_dosage)

        _status = d.pop("status", UNSET)
        status: MedicationStatementCreateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MedicationStatementCreateStatus(_status)

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

        medication_statement_create = cls(
            patient_id=patient_id,
            medication=medication,
            dosage=dosage,
            status=status,
            effective_start=effective_start,
            effective_end=effective_end,
            reason=reason,
            note=note,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return medication_statement_create
