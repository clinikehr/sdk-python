from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.encounter_update_class import EncounterUpdateClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncounterUpdate")


@_attrs_define
class EncounterUpdate:
    """A change to a visit's details. It is accepted only while the draft the same key opened is still untouched: once a
    clinician has edited or signed the note the answer is 409 `note_not_editable`, and another party's visit is a 404.
    Only these four fields can change; no note text can be sent and nothing is signed, locked or finalized. The
    `Idempotency-Key` header is optional. Send JSON; a FHIR Encounter body is not accepted.

        Attributes:
            class_ (EncounterUpdateClass | Unset):
            started_at (datetime.datetime | Unset):
            ended_at (datetime.datetime | Unset): Must not be before `started_at`.
            reason (str | Unset):
    """

    class_: EncounterUpdateClass | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    ended_at: datetime.datetime | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if class_ is not UNSET:
            field_dict["class"] = class_
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _class_ = d.pop("class", UNSET)
        class_: EncounterUpdateClass | Unset
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = EncounterUpdateClass(_class_)

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

        encounter_update = cls(
            class_=class_,
            started_at=started_at,
            ended_at=ended_at,
            reason=reason,
        )

        return encounter_update
