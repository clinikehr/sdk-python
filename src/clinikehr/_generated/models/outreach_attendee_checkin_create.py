from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutreachAttendeeCheckinCreate")


@_attrs_define
class OutreachAttendeeCheckinCreate:
    """A check-in for an EXISTING patient, submitted for clinician review. Create the patient first with `POST
    /v1/clinics/{clinic_id}/patients`.

        Attributes:
            patient_id (UUID):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
            }
        )
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        outreach_attendee_checkin_create = cls(
            patient_id=patient_id,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return outreach_attendee_checkin_create
