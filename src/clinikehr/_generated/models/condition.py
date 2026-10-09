from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.condition_accepted_by_type_1 import ConditionAcceptedByType1
from ..models.condition_accepted_by_type_2_type_1 import ConditionAcceptedByType2Type1
from ..models.condition_accepted_by_type_3_type_1 import ConditionAcceptedByType3Type1
from ..models.condition_clinical_status import ConditionClinicalStatus
from ..models.condition_review_status import ConditionReviewStatus
from ..models.condition_source import ConditionSource
from ..models.condition_verification_status import ConditionVerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_code import ConditionCode


T = TypeVar("T", bound="Condition")


@_attrs_define
class Condition:
    """A diagnosis or problem-list entry — the exposed-field allow-list, field by field. `review_status` says where the
    record stands: `confirmed` is a row in the clinic's problem list (clinic truth; `verification_status: confirmed`, or
    `unconfirmed` while an item the clinic accepted automatically has not been reviewed by a clinician: see
    `accepted_by`); `pending` is an outside submission still waiting for a clinician (`verification_status:
    unconfirmed`); `rejected` and `withdrawn` are this key's own submissions that did not become chart truth. Only the
    submitting key or organization ever sees its own pending, rejected or withdrawn records.

        Attributes:
            id (None | UUID): The problem-list row's id once confirmed; null while the record is still a pending submission
                — use `submission_id` then.
            patient_id (UUID):
            title (str):
            clinical_status (ConditionClinicalStatus):
            verification_status (ConditionVerificationStatus):
            review_status (ConditionReviewStatus):
            code (ConditionCode | None | Unset):
            onset_date (datetime.date | None | Unset):
            resolved_date (datetime.date | None | Unset):
            notes (None | str | Unset):
            recorded_by (None | Unset | UUID):
            source (ConditionSource | Unset): `api` for a record that came in through the API and was confirmed by a
                clinician.
            origin_assistant_name (None | str | Unset):
            accepted_by (ConditionAcceptedByType1 | ConditionAcceptedByType2Type1 | ConditionAcceptedByType3Type1 | None |
                Unset): Who put this record on the chart: `clinic` (the clinic's own team, or a clinician who confirmed it) or
                `automatic` (the clinic chose to accept this kind of item from this key or connection without review; the record
                is on the chart but no clinician has reviewed it, so `verification_status` reads `unconfirmed` until one does).
                Null while the item is still a pending submission.
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
    title: str
    clinical_status: ConditionClinicalStatus
    verification_status: ConditionVerificationStatus
    review_status: ConditionReviewStatus
    code: ConditionCode | None | Unset = UNSET
    onset_date: datetime.date | None | Unset = UNSET
    resolved_date: datetime.date | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    recorded_by: None | Unset | UUID = UNSET
    source: ConditionSource | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    accepted_by: (
        ConditionAcceptedByType1 | ConditionAcceptedByType2Type1 | ConditionAcceptedByType3Type1 | None | Unset
    ) = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    reviewed_by_staff_id: None | Unset | UUID = UNSET
    submission_id: None | Unset | UUID = UNSET
    decision_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.condition_code import ConditionCode  # noqa: PLC0415

        id: None | str
        if isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        patient_id = str(self.patient_id)

        title = self.title

        clinical_status = self.clinical_status.value

        verification_status = self.verification_status.value

        review_status = self.review_status.value

        code: dict[str, Any] | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, ConditionCode):
            code = self.code.to_dict()
        else:
            code = self.code

        onset_date: None | str | Unset
        if isinstance(self.onset_date, Unset):
            onset_date = UNSET
        elif isinstance(self.onset_date, datetime.date):
            onset_date = self.onset_date.isoformat()
        else:
            onset_date = self.onset_date

        resolved_date: None | str | Unset
        if isinstance(self.resolved_date, Unset):
            resolved_date = UNSET
        elif isinstance(self.resolved_date, datetime.date):
            resolved_date = self.resolved_date.isoformat()
        else:
            resolved_date = self.resolved_date

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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
        elif isinstance(self.accepted_by, ConditionAcceptedByType1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, ConditionAcceptedByType2Type1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, ConditionAcceptedByType3Type1):
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
                "title": title,
                "clinical_status": clinical_status,
                "verification_status": verification_status,
                "review_status": review_status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if onset_date is not UNSET:
            field_dict["onset_date"] = onset_date
        if resolved_date is not UNSET:
            field_dict["resolved_date"] = resolved_date
        if notes is not UNSET:
            field_dict["notes"] = notes
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
        from ..models.condition_code import ConditionCode  # noqa: PLC0415

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

        title = d.pop("title")

        clinical_status = ConditionClinicalStatus(d.pop("clinical_status"))

        verification_status = ConditionVerificationStatus(d.pop("verification_status"))

        review_status = ConditionReviewStatus(d.pop("review_status"))

        def _parse_code(data: object) -> ConditionCode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                code_type_0 = ConditionCode.from_dict(data)

                return code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionCode | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_onset_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                onset_date_type_0 = datetime.date.fromisoformat(data)

                return onset_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        onset_date = _parse_onset_date(d.pop("onset_date", UNSET))

        def _parse_resolved_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_date_type_0 = datetime.date.fromisoformat(data)

                return resolved_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        resolved_date = _parse_resolved_date(d.pop("resolved_date", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

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
        source: ConditionSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ConditionSource(_source)

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_accepted_by(
            data: object,
        ) -> ConditionAcceptedByType1 | ConditionAcceptedByType2Type1 | ConditionAcceptedByType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_1 = ConditionAcceptedByType1(data)

                return accepted_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_2_type_1 = ConditionAcceptedByType2Type1(data)

                return accepted_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_3_type_1 = ConditionAcceptedByType3Type1(data)

                return accepted_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ConditionAcceptedByType1 | ConditionAcceptedByType2Type1 | ConditionAcceptedByType3Type1 | None | Unset,
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

        condition = cls(
            id=id,
            patient_id=patient_id,
            title=title,
            clinical_status=clinical_status,
            verification_status=verification_status,
            review_status=review_status,
            code=code,
            onset_date=onset_date,
            resolved_date=resolved_date,
            notes=notes,
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

        condition.additional_properties = d
        return condition

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
