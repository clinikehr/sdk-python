from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.encounter_create_class import EncounterCreateClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncounterCreate")


@_attrs_define
class EncounterCreate:
    """A visit to open for a patient. It opens a DRAFT note for a clinician to complete: nothing is ordered, prescribed,
    signed, locked or billed, and no note text can be sent (there is no field for it). The draft appears in the clinic's
    consultation list for the clinician to finish. `clinician_id` must be a clinician the clinic lists (see `GET …/note-
    clinicians`). The `Idempotency-Key` header is REQUIRED. Send JSON; a FHIR Encounter body is not accepted.

        Attributes:
            patient_id (UUID):
            clinician_id (UUID):
            class_ (EncounterCreateClass | Unset):
            started_at (datetime.datetime | Unset):
            ended_at (datetime.datetime | Unset): Must not be before `started_at`.
            reason (str | Unset): The administrative reason for the visit — not clinical note text.
            origin_assistant_name (str | Unset): Name of the assistant or connected app that opened the visit.
    """

    patient_id: UUID
    clinician_id: UUID
    class_: EncounterCreateClass | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    ended_at: datetime.datetime | Unset = UNSET
    reason: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        clinician_id = str(self.clinician_id)

        class_: str | Unset = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        ended_at: str | Unset = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        reason = self.reason

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "clinician_id": clinician_id,
            }
        )
        if class_ is not UNSET:
            field_dict["class"] = class_
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        clinician_id = UUID(d.pop("clinician_id"))

        _class_ = d.pop("class", UNSET)
        class_: EncounterCreateClass | Unset
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = EncounterCreateClass(_class_)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        _ended_at = d.pop("ended_at", UNSET)
        ended_at: datetime.datetime | Unset
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = datetime.datetime.fromisoformat(_ended_at)

        reason = d.pop("reason", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        encounter_create = cls(
            patient_id=patient_id,
            clinician_id=clinician_id,
            class_=class_,
            started_at=started_at,
            ended_at=ended_at,
            reason=reason,
            origin_assistant_name=origin_assistant_name,
        )

        return encounter_create
