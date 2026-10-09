from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.referral_create_priority import ReferralCreatePriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_create_reason import ReferralCreateReason
    from ..models.referral_create_requester import ReferralCreateRequester
    from ..models.referral_create_service import ReferralCreateService


T = TypeVar("T", bound="ReferralCreate")


@_attrs_define
class ReferralCreate:
    """A referral to this clinic, submitted for clinic staff to confirm. It does not appear on the clinic's referral list
    until they do (unless the clinic has chosen to accept such submissions automatically); either way it lands as
    `received` and the clinic decides whether to accept, decline or schedule it. This is a clinical referral, not the
    clinic referral programme. Send `code` on `service` or `reason` only with its `system`. `client_reference` (your own
    id, up to 200 characters) makes a second submission of the same record with different content a
    `client_reference_conflict`.

        Attributes:
            patient_id (UUID):
            service (ReferralCreateService):
            reason (ReferralCreateReason):
            priority (ReferralCreatePriority | Unset):  Default: ReferralCreatePriority.ROUTINE.
            needed_by (datetime.date | Unset): Not earlier than yesterday.
            clinical_summary (str | Unset):
            requester (ReferralCreateRequester | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    service: ReferralCreateService
    reason: ReferralCreateReason
    priority: ReferralCreatePriority | Unset = ReferralCreatePriority.ROUTINE
    needed_by: datetime.date | Unset = UNSET
    clinical_summary: str | Unset = UNSET
    requester: ReferralCreateRequester | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        service = self.service.to_dict()

        reason = self.reason.to_dict()

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        needed_by: str | Unset = UNSET
        if not isinstance(self.needed_by, Unset):
            needed_by = self.needed_by.isoformat()

        clinical_summary = self.clinical_summary

        requester: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requester, Unset):
            requester = self.requester.to_dict()

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "service": service,
                "reason": reason,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by
        if clinical_summary is not UNSET:
            field_dict["clinical_summary"] = clinical_summary
        if requester is not UNSET:
            field_dict["requester"] = requester
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_create_reason import ReferralCreateReason  # noqa: PLC0415
        from ..models.referral_create_requester import ReferralCreateRequester  # noqa: PLC0415
        from ..models.referral_create_service import ReferralCreateService  # noqa: PLC0415

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        service = ReferralCreateService.from_dict(d.pop("service"))

        reason = ReferralCreateReason.from_dict(d.pop("reason"))

        _priority = d.pop("priority", UNSET)
        priority: ReferralCreatePriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ReferralCreatePriority(_priority)

        _needed_by = d.pop("needed_by", UNSET)
        needed_by: datetime.date | Unset
        if isinstance(_needed_by, Unset):
            needed_by = UNSET
        else:
            needed_by = datetime.date.fromisoformat(_needed_by)

        clinical_summary = d.pop("clinical_summary", UNSET)

        _requester = d.pop("requester", UNSET)
        requester: ReferralCreateRequester | Unset
        if isinstance(_requester, Unset):
            requester = UNSET
        else:
            requester = ReferralCreateRequester.from_dict(_requester)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        referral_create = cls(
            patient_id=patient_id,
            service=service,
            reason=reason,
            priority=priority,
            needed_by=needed_by,
            clinical_summary=clinical_summary,
            requester=requester,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return referral_create
