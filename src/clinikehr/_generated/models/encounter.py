from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.encounter_class_type_1 import EncounterClassType1
from ..models.encounter_class_type_2_type_1 import EncounterClassType2Type1
from ..models.encounter_class_type_3_type_1 import EncounterClassType3Type1
from ..models.encounter_kind import EncounterKind
from ..models.encounter_review_status import EncounterReviewStatus
from ..models.encounter_source import EncounterSource
from ..models.encounter_status import EncounterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encounter_period import EncounterPeriod


T = TypeVar("T", bound="Encounter")


@_attrs_define
class Encounter:
    """A visit as documented in the clinic: a clinical note seen as a visit — the exposed-field allow-list, field by field.
    The `id` is the note's id, so the same visit reads under Notes. It carries the visit's status, dates, administrative
    reason and clinician only: no note text, title, diagnosis, plan, service, signature or billing is ever exposed here
    (clinical text is read through Notes). Every encounter is a `consultation`; triage, ward and appointment records are
    not encounters in this API. A visit opened through the API is a `draft` with `review_status: pending` until a
    clinician has reviewed it.

        Attributes:
            id (UUID): The visit note's id.
            patient_id (UUID):
            kind (EncounterKind):
            status (EncounterStatus): `draft` until a clinician signs, locks or finalizes the note; `completed` after.
            period (EncounterPeriod):
            source (EncounterSource): `api` for a visit opened through the API.
            review_status (EncounterReviewStatus): `confirmed` for a visit the clinic opened itself, and for an API draft
                once a clinician has reviewed it.
            class_ (EncounterClassType1 | EncounterClassType2Type1 | EncounterClassType3Type1 | None | Unset): Null when no
                class was recorded for the visit.
            reason (None | str | Unset): The administrative reason for the visit (at most 500 characters), not note text.
            clinician_id (None | Unset | UUID): The clinician's id as listed by `GET …/providers` and `GET …/note-
                clinicians`.
            origin_assistant_name (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    patient_id: UUID
    kind: EncounterKind
    status: EncounterStatus
    period: EncounterPeriod
    source: EncounterSource
    review_status: EncounterReviewStatus
    class_: EncounterClassType1 | EncounterClassType2Type1 | EncounterClassType3Type1 | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    clinician_id: None | Unset | UUID = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        patient_id = str(self.patient_id)

        kind = self.kind.value

        status = self.status.value

        period = self.period.to_dict()

        source = self.source.value

        review_status = self.review_status.value

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        elif isinstance(self.class_, EncounterClassType1):
            class_ = self.class_.value
        elif isinstance(self.class_, EncounterClassType2Type1):
            class_ = self.class_.value
        elif isinstance(self.class_, EncounterClassType3Type1):
            class_ = self.class_.value
        else:
            class_ = self.class_

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        clinician_id: None | str | Unset
        if isinstance(self.clinician_id, Unset):
            clinician_id = UNSET
        elif isinstance(self.clinician_id, UUID):
            clinician_id = str(self.clinician_id)
        else:
            clinician_id = self.clinician_id

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

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
                "kind": kind,
                "status": status,
                "period": period,
                "source": source,
                "review_status": review_status,
            }
        )
        if class_ is not UNSET:
            field_dict["class"] = class_
        if reason is not UNSET:
            field_dict["reason"] = reason
        if clinician_id is not UNSET:
            field_dict["clinician_id"] = clinician_id
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encounter_period import EncounterPeriod  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        kind = EncounterKind(d.pop("kind"))

        status = EncounterStatus(d.pop("status"))

        period = EncounterPeriod.from_dict(d.pop("period"))

        source = EncounterSource(d.pop("source"))

        review_status = EncounterReviewStatus(d.pop("review_status"))

        def _parse_class_(
            data: object,
        ) -> EncounterClassType1 | EncounterClassType2Type1 | EncounterClassType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                class_type_1 = EncounterClassType1(data)

                return class_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                class_type_2_type_1 = EncounterClassType2Type1(data)

                return class_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                class_type_3_type_1 = EncounterClassType3Type1(data)

                return class_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EncounterClassType1 | EncounterClassType2Type1 | EncounterClassType3Type1 | None | Unset, data)

        class_ = _parse_class_(d.pop("class", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_clinician_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinician_id_type_0 = UUID(data)

                return clinician_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clinician_id = _parse_clinician_id(d.pop("clinician_id", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

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

        encounter = cls(
            id=id,
            patient_id=patient_id,
            kind=kind,
            status=status,
            period=period,
            source=source,
            review_status=review_status,
            class_=class_,
            reason=reason,
            clinician_id=clinician_id,
            origin_assistant_name=origin_assistant_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        encounter.additional_properties = d
        return encounter

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
