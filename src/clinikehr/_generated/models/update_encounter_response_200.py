from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encounter import Encounter


T = TypeVar("T", bound="UpdateEncounterResponse200")


@_attrs_define
class UpdateEncounterResponse200:
    """
    Attributes:
        data (Encounter): A visit as documented in the clinic: a clinical note seen as a visit — the exposed-field
            allow-list, field by field. The `id` is the note's id, so the same visit reads under Notes. It carries the
            visit's status, dates, administrative reason and clinician only: no note text, title, diagnosis, plan, service,
            signature or billing is ever exposed here (clinical text is read through Notes). Every encounter is a
            `consultation`; triage, ward and appointment records are not encounters in this API. A visit opened through the
            API is a `draft` with `review_status: pending` until a clinician has reviewed it.
        idempotent_replay (bool | Unset): Present and true when this Idempotency-Key was already used and the original
            answer is returned.
    """

    data: Encounter
    idempotent_replay: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        idempotent_replay = self.idempotent_replay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if idempotent_replay is not UNSET:
            field_dict["idempotent_replay"] = idempotent_replay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encounter import Encounter  # noqa: PLC0415

        d = dict(src_dict)
        data = Encounter.from_dict(d.pop("data"))

        idempotent_replay = d.pop("idempotent_replay", UNSET)

        update_encounter_response_200 = cls(
            data=data,
            idempotent_replay=idempotent_replay,
        )

        update_encounter_response_200.additional_properties = d
        return update_encounter_response_200

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
