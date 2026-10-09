from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.medication_statement_accepted_by_type_1 import MedicationStatementAcceptedByType1
from ..models.medication_statement_accepted_by_type_2_type_1 import MedicationStatementAcceptedByType2Type1
from ..models.medication_statement_accepted_by_type_3_type_1 import MedicationStatementAcceptedByType3Type1
from ..models.medication_statement_review_status import MedicationStatementReviewStatus
from ..models.medication_statement_source import MedicationStatementSource
from ..models.medication_statement_status_type_1 import MedicationStatementStatusType1
from ..models.medication_statement_status_type_2_type_1 import MedicationStatementStatusType2Type1
from ..models.medication_statement_status_type_3_type_1 import MedicationStatementStatusType3Type1
from ..models.medication_statement_verification_status import MedicationStatementVerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medication_statement_dosage import MedicationStatementDosage
    from ..models.medication_statement_effective import MedicationStatementEffective
    from ..models.medication_statement_medication import MedicationStatementMedication


T = TypeVar("T", bound="MedicationStatement")


@_attrs_define
class MedicationStatement:
    """A reported medicine - the patient (or a connected app) says they take it. It is NOT a prescription and nothing is
    dispensed from it. The exposed-field allow-list, field by field. `review_status` says where the record stands:
    `confirmed` is on the clinic's chart; `pending` is an outside submission still waiting for a clinician
    (`verification_status: unconfirmed`); `rejected` and `withdrawn` are this key's own submissions that did not become
    chart truth. A statement with a recognised RxNorm code is used by the clinic's pharmacy interaction checks while it
    is `active`; a free-text or `local` one is listed there as not checked.

        Attributes:
            id (None | UUID): The statement's id once confirmed; null for a pending create (use `submission_id`). A pending
                update or retraction carries the id of the statement it targets.
            patient_id (UUID):
            medication (MedicationStatementMedication):
            verification_status (MedicationStatementVerificationStatus):
            review_status (MedicationStatementReviewStatus):
            dosage (MedicationStatementDosage | Unset): How the medicine is taken, as stated. Free text; nothing here is an
                order.
            status (MedicationStatementStatusType1 | MedicationStatementStatusType2Type1 |
                MedicationStatementStatusType3Type1 | None | Unset): Null for a pending update that does not change the status.
            effective (MedicationStatementEffective | Unset):
            reason (None | str | Unset):
            note (None | str | Unset):
            recorded_by (None | Unset | UUID):
            source (MedicationStatementSource | Unset):
            origin_assistant_name (None | str | Unset):
            accepted_by (MedicationStatementAcceptedByType1 | MedicationStatementAcceptedByType2Type1 |
                MedicationStatementAcceptedByType3Type1 | None | Unset): Who put this record on the chart: `clinic` (the
                clinic's own team, or a clinician who confirmed it) or `automatic` (the clinic chose to accept this kind of item
                from this key or connection without review; the record is on the chart but no clinician has reviewed it, so
                `verification_status` reads `unconfirmed` until one does). Null while the item is still a pending submission.
            reviewed_at (datetime.datetime | None | Unset): Set when a clinician marked an automatically accepted item
                reviewed; null otherwise.
            reviewed_by_staff_id (None | Unset | UUID):
            submission_id (None | Unset | UUID):
            decision_reason (None | str | Unset): Why a clinician rejected it. Present only when `review_status` is
                `rejected`.
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: None | UUID
    patient_id: UUID
    medication: MedicationStatementMedication
    verification_status: MedicationStatementVerificationStatus
    review_status: MedicationStatementReviewStatus
    dosage: MedicationStatementDosage | Unset = UNSET
    status: (
        MedicationStatementStatusType1
        | MedicationStatementStatusType2Type1
        | MedicationStatementStatusType3Type1
        | None
        | Unset
    ) = UNSET
    effective: MedicationStatementEffective | Unset = UNSET
    reason: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    recorded_by: None | Unset | UUID = UNSET
    source: MedicationStatementSource | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    accepted_by: (
        MedicationStatementAcceptedByType1
        | MedicationStatementAcceptedByType2Type1
        | MedicationStatementAcceptedByType3Type1
        | None
        | Unset
    ) = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    reviewed_by_staff_id: None | Unset | UUID = UNSET
    submission_id: None | Unset | UUID = UNSET
    decision_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        if isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        patient_id = str(self.patient_id)

        medication = self.medication.to_dict()

        verification_status = self.verification_status.value

        review_status = self.review_status.value

        dosage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dosage, Unset):
            dosage = self.dosage.to_dict()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, MedicationStatementStatusType1):
            status = self.status.value
        elif isinstance(self.status, MedicationStatementStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, MedicationStatementStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        effective: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective, Unset):
            effective = self.effective.to_dict()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        recorded_by: None | str | Unset
        if isinstance(self.recorded_by, Unset):
            recorded_by = UNSET
        elif isinstance(self.recorded_by, UUID):
            recorded_by = str(self.recorded_by)
        else:
            recorded_by = self.recorded_by

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        accepted_by: None | str | Unset
        if isinstance(self.accepted_by, Unset):
            accepted_by = UNSET
        elif isinstance(self.accepted_by, MedicationStatementAcceptedByType1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, MedicationStatementAcceptedByType2Type1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, MedicationStatementAcceptedByType3Type1):
            accepted_by = self.accepted_by.value
        else:
            accepted_by = self.accepted_by

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        reviewed_by_staff_id: None | str | Unset
        if isinstance(self.reviewed_by_staff_id, Unset):
            reviewed_by_staff_id = UNSET
        elif isinstance(self.reviewed_by_staff_id, UUID):
            reviewed_by_staff_id = str(self.reviewed_by_staff_id)
        else:
            reviewed_by_staff_id = self.reviewed_by_staff_id

        submission_id: None | str | Unset
        if isinstance(self.submission_id, Unset):
            submission_id = UNSET
        elif isinstance(self.submission_id, UUID):
            submission_id = str(self.submission_id)
        else:
            submission_id = self.submission_id

        decision_reason: None | str | Unset
        if isinstance(self.decision_reason, Unset):
            decision_reason = UNSET
        else:
            decision_reason = self.decision_reason

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "medication": medication,
                "verification_status": verification_status,
                "review_status": review_status,
            }
        )
        if dosage is not UNSET:
            field_dict["dosage"] = dosage
        if status is not UNSET:
            field_dict["status"] = status
        if effective is not UNSET:
            field_dict["effective"] = effective
        if reason is not UNSET:
            field_dict["reason"] = reason
        if note is not UNSET:
            field_dict["note"] = note
        if recorded_by is not UNSET:
            field_dict["recorded_by"] = recorded_by
        if source is not UNSET:
            field_dict["source"] = source
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if accepted_by is not UNSET:
            field_dict["accepted_by"] = accepted_by
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if reviewed_by_staff_id is not UNSET:
            field_dict["reviewed_by_staff_id"] = reviewed_by_staff_id
        if submission_id is not UNSET:
            field_dict["submission_id"] = submission_id
        if decision_reason is not UNSET:
            field_dict["decision_reason"] = decision_reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medication_statement_dosage import MedicationStatementDosage  # noqa: PLC0415
        from ..models.medication_statement_effective import MedicationStatementEffective  # noqa: PLC0415
        from ..models.medication_statement_medication import MedicationStatementMedication  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        id = _parse_id(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        medication = MedicationStatementMedication.from_dict(d.pop("medication"))

        verification_status = MedicationStatementVerificationStatus(d.pop("verification_status"))

        review_status = MedicationStatementReviewStatus(d.pop("review_status"))

        _dosage = d.pop("dosage", UNSET)
        dosage: MedicationStatementDosage | Unset
        if isinstance(_dosage, Unset):
            dosage = UNSET
        else:
            dosage = MedicationStatementDosage.from_dict(_dosage)

        def _parse_status(
            data: object,
        ) -> (
            MedicationStatementStatusType1
            | MedicationStatementStatusType2Type1
            | MedicationStatementStatusType3Type1
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
                status_type_1 = MedicationStatementStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = MedicationStatementStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = MedicationStatementStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MedicationStatementStatusType1
                | MedicationStatementStatusType2Type1
                | MedicationStatementStatusType3Type1
                | None
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        _effective = d.pop("effective", UNSET)
        effective: MedicationStatementEffective | Unset
        if isinstance(_effective, Unset):
            effective = UNSET
        else:
            effective = MedicationStatementEffective.from_dict(_effective)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_recorded_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recorded_by_type_0 = UUID(data)

                return recorded_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recorded_by = _parse_recorded_by(d.pop("recorded_by", UNSET))

        _source = d.pop("source", UNSET)
        source: MedicationStatementSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = MedicationStatementSource(_source)

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_accepted_by(
            data: object,
        ) -> (
            MedicationStatementAcceptedByType1
            | MedicationStatementAcceptedByType2Type1
            | MedicationStatementAcceptedByType3Type1
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
                accepted_by_type_1 = MedicationStatementAcceptedByType1(data)

                return accepted_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_2_type_1 = MedicationStatementAcceptedByType2Type1(data)

                return accepted_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_3_type_1 = MedicationStatementAcceptedByType3Type1(data)

                return accepted_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MedicationStatementAcceptedByType1
                | MedicationStatementAcceptedByType2Type1
                | MedicationStatementAcceptedByType3Type1
                | None
                | Unset,
                data,
            )

        accepted_by = _parse_accepted_by(d.pop("accepted_by", UNSET))

        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))

        def _parse_reviewed_by_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_by_staff_id_type_0 = UUID(data)

                return reviewed_by_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewed_by_staff_id = _parse_reviewed_by_staff_id(d.pop("reviewed_by_staff_id", UNSET))

        def _parse_submission_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submission_id_type_0 = UUID(data)

                return submission_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        submission_id = _parse_submission_id(d.pop("submission_id", UNSET))

        def _parse_decision_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_reason = _parse_decision_reason(d.pop("decision_reason", UNSET))

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

        medication_statement = cls(
            id=id,
            patient_id=patient_id,
            medication=medication,
            verification_status=verification_status,
            review_status=review_status,
            dosage=dosage,
            status=status,
            effective=effective,
            reason=reason,
            note=note,
            recorded_by=recorded_by,
            source=source,
            origin_assistant_name=origin_assistant_name,
            accepted_by=accepted_by,
            reviewed_at=reviewed_at,
            reviewed_by_staff_id=reviewed_by_staff_id,
            submission_id=submission_id,
            decision_reason=decision_reason,
            created_at=created_at,
            updated_at=updated_at,
        )

        medication_statement.additional_properties = d
        return medication_statement

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
