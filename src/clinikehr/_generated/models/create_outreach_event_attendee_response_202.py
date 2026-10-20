from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submission import Submission


T = TypeVar("T", bound="CreateOutreachEventAttendeeResponse202")


@_attrs_define
class CreateOutreachEventAttendeeResponse202:
    """
    Attributes:
        data (Submission): What the clinic's review queue holds for something this key sent: one outside record waiting
            for, or already past, a clinician's decision.
        idempotent_replay (bool | Unset): Present and true when this Idempotency-Key was already used and the original
            submission is returned.
    """

    data: Submission
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
        from ..models.submission import Submission  # noqa: PLC0415

        d = dict(src_dict)
        data = Submission.from_dict(d.pop("data"))

        idempotent_replay = d.pop("idempotent_replay", UNSET)

        create_outreach_event_attendee_response_202 = cls(
            data=data,
            idempotent_replay=idempotent_replay,
        )

        create_outreach_event_attendee_response_202.additional_properties = d
        return create_outreach_event_attendee_response_202

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
