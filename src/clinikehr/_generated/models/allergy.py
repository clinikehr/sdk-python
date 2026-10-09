from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.allergy_accepted_by_type_1 import AllergyAcceptedByType1
from ..models.allergy_accepted_by_type_2_type_1 import AllergyAcceptedByType2Type1
from ..models.allergy_accepted_by_type_3_type_1 import AllergyAcceptedByType3Type1
from ..models.allergy_category_item import AllergyCategoryItem
from ..models.allergy_clinical_status_type_1 import AllergyClinicalStatusType1
from ..models.allergy_clinical_status_type_2_type_1 import AllergyClinicalStatusType2Type1
from ..models.allergy_clinical_status_type_3_type_1 import AllergyClinicalStatusType3Type1
from ..models.allergy_criticality_type_1 import AllergyCriticalityType1
from ..models.allergy_criticality_type_2_type_1 import AllergyCriticalityType2Type1
from ..models.allergy_criticality_type_3_type_1 import AllergyCriticalityType3Type1
from ..models.allergy_entry import AllergyEntry
from ..models.allergy_review_status import AllergyReviewStatus
from ..models.allergy_source import AllergySource
from ..models.allergy_type_type_1 import AllergyTypeType1
from ..models.allergy_type_type_2_type_1 import AllergyTypeType2Type1
from ..models.allergy_type_type_3_type_1 import AllergyTypeType3Type1
from ..models.allergy_verification_status import AllergyVerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allergy_reaction import AllergyReaction
    from ..models.allergy_substance import AllergySubstance


T = TypeVar("T", bound="Allergy")


@_attrs_define
class Allergy:
    """An allergy or intolerance - the exposed-field allow-list, field by field. `review_status` says where the record
    stands: `confirmed` is on the clinic's chart (clinic truth); `pending` is an outside submission still waiting for a
    clinician (`verification_status: unconfirmed`); `rejected` and `withdrawn` are this key's own submissions that did
    not become chart truth. `entry` is `structured` for a detailed allergy record and `legacy_text` for an allergy that
    is only a name on the clinic's simple allergy list: it has `id: null`, no detail, and cannot be fetched or changed
    by id. An empty list does NOT mean "no known allergies".

        Attributes:
            id (None | UUID): The allergy record's id once confirmed; null for a pending submission (use `submission_id`)
                and for a `legacy_text` entry.
            patient_id (UUID):
            entry (AllergyEntry): `no_known_allergies` is a record saying the patient has no known allergies; its substance
                text is `No known allergies`. A clinician confirms it like any other allergy record.
            substance (AllergySubstance):
            verification_status (AllergyVerificationStatus):
            review_status (AllergyReviewStatus):
            category (list[AllergyCategoryItem] | Unset):
            criticality (AllergyCriticalityType1 | AllergyCriticalityType2Type1 | AllergyCriticalityType3Type1 | None |
                Unset):
            type_ (AllergyTypeType1 | AllergyTypeType2Type1 | AllergyTypeType3Type1 | None | Unset):
            clinical_status (AllergyClinicalStatusType1 | AllergyClinicalStatusType2Type1 | AllergyClinicalStatusType3Type1
                | None | Unset):
            reactions (list[AllergyReaction] | Unset):
            onset_date (datetime.date | None | Unset):
            note (None | str | Unset):
            recorded_by (None | Unset | UUID):
            source (AllergySource | Unset):
            origin_assistant_name (None | str | Unset):
            accepted_by (AllergyAcceptedByType1 | AllergyAcceptedByType2Type1 | AllergyAcceptedByType3Type1 | None | Unset):
                Who put this record on the chart: `clinic` (the clinic's own team, or a clinician who confirmed it) or
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
    entry: AllergyEntry
    substance: AllergySubstance
    verification_status: AllergyVerificationStatus
    review_status: AllergyReviewStatus
    category: list[AllergyCategoryItem] | Unset = UNSET
    criticality: (
        AllergyCriticalityType1 | AllergyCriticalityType2Type1 | AllergyCriticalityType3Type1 | None | Unset
    ) = UNSET
    type_: AllergyTypeType1 | AllergyTypeType2Type1 | AllergyTypeType3Type1 | None | Unset = UNSET
    clinical_status: (
        AllergyClinicalStatusType1 | AllergyClinicalStatusType2Type1 | AllergyClinicalStatusType3Type1 | None | Unset
    ) = UNSET
    reactions: list[AllergyReaction] | Unset = UNSET
    onset_date: datetime.date | None | Unset = UNSET
    note: None | str | Unset = UNSET
    recorded_by: None | Unset | UUID = UNSET
    source: AllergySource | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    accepted_by: AllergyAcceptedByType1 | AllergyAcceptedByType2Type1 | AllergyAcceptedByType3Type1 | None | Unset = (
        UNSET
    )
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

        entry = self.entry.value

        substance = self.substance.to_dict()

        verification_status = self.verification_status.value

        review_status = self.review_status.value

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, AllergyCriticalityType1):
            criticality = self.criticality.value
        elif isinstance(self.criticality, AllergyCriticalityType2Type1):
            criticality = self.criticality.value
        elif isinstance(self.criticality, AllergyCriticalityType3Type1):
            criticality = self.criticality.value
        else:
            criticality = self.criticality

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, AllergyTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, AllergyTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, AllergyTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        clinical_status: None | str | Unset
        if isinstance(self.clinical_status, Unset):
            clinical_status = UNSET
        elif isinstance(self.clinical_status, AllergyClinicalStatusType1):
            clinical_status = self.clinical_status.value
        elif isinstance(self.clinical_status, AllergyClinicalStatusType2Type1):
            clinical_status = self.clinical_status.value
        elif isinstance(self.clinical_status, AllergyClinicalStatusType3Type1):
            clinical_status = self.clinical_status.value
        else:
            clinical_status = self.clinical_status

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)

        onset_date: None | str | Unset
        if isinstance(self.onset_date, Unset):
            onset_date = UNSET
        elif isinstance(self.onset_date, datetime.date):
            onset_date = self.onset_date.isoformat()
        else:
            onset_date = self.onset_date

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
        elif isinstance(self.accepted_by, AllergyAcceptedByType1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, AllergyAcceptedByType2Type1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, AllergyAcceptedByType3Type1):
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
                "entry": entry,
                "substance": substance,
                "verification_status": verification_status,
                "review_status": review_status,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if type_ is not UNSET:
            field_dict["type"] = type_
        if clinical_status is not UNSET:
            field_dict["clinical_status"] = clinical_status
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if onset_date is not UNSET:
            field_dict["onset_date"] = onset_date
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
        from ..models.allergy_reaction import AllergyReaction  # noqa: PLC0415
        from ..models.allergy_substance import AllergySubstance  # noqa: PLC0415

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

        entry = AllergyEntry(d.pop("entry"))

        substance = AllergySubstance.from_dict(d.pop("substance"))

        verification_status = AllergyVerificationStatus(d.pop("verification_status"))

        review_status = AllergyReviewStatus(d.pop("review_status"))

        _category = d.pop("category", UNSET)
        category: list[AllergyCategoryItem] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = AllergyCategoryItem(category_item_data)

                category.append(category_item)

        def _parse_criticality(
            data: object,
        ) -> AllergyCriticalityType1 | AllergyCriticalityType2Type1 | AllergyCriticalityType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = AllergyCriticalityType1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = AllergyCriticalityType2Type1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = AllergyCriticalityType3Type1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AllergyCriticalityType1 | AllergyCriticalityType2Type1 | AllergyCriticalityType3Type1 | None | Unset,
                data,
            )

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_type_(
            data: object,
        ) -> AllergyTypeType1 | AllergyTypeType2Type1 | AllergyTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = AllergyTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = AllergyTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = AllergyTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AllergyTypeType1 | AllergyTypeType2Type1 | AllergyTypeType3Type1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_clinical_status(
            data: object,
        ) -> (
            AllergyClinicalStatusType1
            | AllergyClinicalStatusType2Type1
            | AllergyClinicalStatusType3Type1
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
                clinical_status_type_1 = AllergyClinicalStatusType1(data)

                return clinical_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinical_status_type_2_type_1 = AllergyClinicalStatusType2Type1(data)

                return clinical_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinical_status_type_3_type_1 = AllergyClinicalStatusType3Type1(data)

                return clinical_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AllergyClinicalStatusType1
                | AllergyClinicalStatusType2Type1
                | AllergyClinicalStatusType3Type1
                | None
                | Unset,
                data,
            )

        clinical_status = _parse_clinical_status(d.pop("clinical_status", UNSET))

        _reactions = d.pop("reactions", UNSET)
        reactions: list[AllergyReaction] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = AllergyReaction.from_dict(reactions_item_data)

                reactions.append(reactions_item)

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
        source: AllergySource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AllergySource(_source)

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_accepted_by(
            data: object,
        ) -> AllergyAcceptedByType1 | AllergyAcceptedByType2Type1 | AllergyAcceptedByType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_1 = AllergyAcceptedByType1(data)

                return accepted_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_2_type_1 = AllergyAcceptedByType2Type1(data)

                return accepted_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_3_type_1 = AllergyAcceptedByType3Type1(data)

                return accepted_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AllergyAcceptedByType1 | AllergyAcceptedByType2Type1 | AllergyAcceptedByType3Type1 | None | Unset, data
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

        allergy = cls(
            id=id,
            patient_id=patient_id,
            entry=entry,
            substance=substance,
            verification_status=verification_status,
            review_status=review_status,
            category=category,
            criticality=criticality,
            type_=type_,
            clinical_status=clinical_status,
            reactions=reactions,
            onset_date=onset_date,
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

        allergy.additional_properties = d
        return allergy

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
