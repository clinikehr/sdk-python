from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.referral_update_priority import ReferralUpdatePriority
from ..models.referral_update_status import ReferralUpdateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_update_reason import ReferralUpdateReason
    from ..models.referral_update_requester import ReferralUpdateRequester


T = TypeVar("T", bound="ReferralUpdate")


@_attrs_define
class ReferralUpdate:
    """A proposed change to a referral, or a retraction. It becomes a NEW pending submission; the referral does not change
    until clinic staff confirm it. A change is always reviewed, even when the clinic accepts new referrals
    automatically. You can change a referral only while the clinic has not acted on it: once staff have accepted,
    declined, scheduled, completed or cancelled it, the change is refused. The service can never be changed (a different
    service is a new referral). `status` accepts only `entered_in_error`, which proposes retracting the referral as sent
    in error and cannot be combined with other changes. A sender cannot accept, decline, schedule, complete or cancel a
    referral.

        Attributes:
            status (ReferralUpdateStatus | Unset):
            priority (ReferralUpdatePriority | Unset):
            needed_by (datetime.date | Unset): Not earlier than yesterday.
            reason (ReferralUpdateReason | Unset):
            clinical_summary (str | Unset):
            requester (ReferralUpdateRequester | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    status: ReferralUpdateStatus | Unset = UNSET
    priority: ReferralUpdatePriority | Unset = UNSET
    needed_by: datetime.date | Unset = UNSET
    reason: ReferralUpdateReason | Unset = UNSET
    clinical_summary: str | Unset = UNSET
    requester: ReferralUpdateRequester | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        needed_by: str | Unset = UNSET
        if not isinstance(self.needed_by, Unset):
            needed_by = self.needed_by.isoformat()

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        clinical_summary = self.clinical_summary

        requester: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requester, Unset):
            requester = self.requester.to_dict()

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if priority is not UNSET:
            field_dict["priority"] = priority
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by
        if reason is not UNSET:
            field_dict["reason"] = reason
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
        from ..models.referral_update_reason import ReferralUpdateReason  # noqa: PLC0415
        from ..models.referral_update_requester import ReferralUpdateRequester  # noqa: PLC0415

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ReferralUpdateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReferralUpdateStatus(_status)

        _priority = d.pop("priority", UNSET)
        priority: ReferralUpdatePriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ReferralUpdatePriority(_priority)

        _needed_by = d.pop("needed_by", UNSET)
        needed_by: datetime.date | Unset
        if isinstance(_needed_by, Unset):
            needed_by = UNSET
        else:
            needed_by = datetime.date.fromisoformat(_needed_by)

        _reason = d.pop("reason", UNSET)
        reason: ReferralUpdateReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ReferralUpdateReason.from_dict(_reason)

        clinical_summary = d.pop("clinical_summary", UNSET)

        _requester = d.pop("requester", UNSET)
        requester: ReferralUpdateRequester | Unset
        if isinstance(_requester, Unset):
            requester = UNSET
        else:
            requester = ReferralUpdateRequester.from_dict(_requester)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        referral_update = cls(
            status=status,
            priority=priority,
            needed_by=needed_by,
            reason=reason,
            clinical_summary=clinical_summary,
            requester=requester,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return referral_update
