from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_accepted_by_type_1 import ReferralAcceptedByType1
from ..models.referral_accepted_by_type_2_type_1 import ReferralAcceptedByType2Type1
from ..models.referral_accepted_by_type_3_type_1 import ReferralAcceptedByType3Type1
from ..models.referral_direction_type_1 import ReferralDirectionType1
from ..models.referral_direction_type_2_type_1 import ReferralDirectionType2Type1
from ..models.referral_direction_type_3_type_1 import ReferralDirectionType3Type1
from ..models.referral_priority_type_1 import ReferralPriorityType1
from ..models.referral_priority_type_2_type_1 import ReferralPriorityType2Type1
from ..models.referral_priority_type_3_type_1 import ReferralPriorityType3Type1
from ..models.referral_review_status import ReferralReviewStatus
from ..models.referral_source_type_1 import ReferralSourceType1
from ..models.referral_source_type_2_type_1 import ReferralSourceType2Type1
from ..models.referral_source_type_3_type_1 import ReferralSourceType3Type1
from ..models.referral_status_type_1 import ReferralStatusType1
from ..models.referral_status_type_2_type_1 import ReferralStatusType2Type1
from ..models.referral_status_type_3_type_1 import ReferralStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_reason import ReferralReason
    from ..models.referral_recipient import ReferralRecipient
    from ..models.referral_requester import ReferralRequester
    from ..models.referral_service import ReferralService


T = TypeVar("T", bound="Referral")


@_attrs_define
class Referral:
    """A clinical referral: another provider or service asks this clinic to see a patient. It is NOT the clinic referral
    programme (clinic-to-clinic credits for recommending ClinikEHR), the marketing "referred by" source on a client, or
    an antenatal or postnatal referral note. The exposed-field allow-list, field by field. `review_status` says where
    the record stands: `confirmed` is on the clinic's referral list; `pending` is an outside submission still waiting
    for clinic staff; `rejected` and `withdrawn` are this key's own submissions that did not become a referral. For a
    confirmed referral `status` is the clinic's workflow: it lands `received`, and only the clinic accepts, declines,
    schedules, completes or cancels it. A sender can never change `status`, `recipient` or `scheduled_appointment_id`.
    `decision_reason` on a confirmed referral (the clinic's reason for declining or cancelling) is shown only to the key
    or organization that sent it; everyone else sees null.

        Attributes:
            id (None | UUID): The referral's id once confirmed; null for a pending create (use `submission_id`). A pending
                update or retraction carries the id of the referral it targets.
            patient_id (UUID):
            direction (None | ReferralDirectionType1 | ReferralDirectionType2Type1 | ReferralDirectionType3Type1):
                `incoming` is a referral to this clinic. Only `incoming` is written today.
            status (None | ReferralStatusType1 | ReferralStatusType2Type1 | ReferralStatusType3Type1): The clinic's workflow
                state. Null for a pending submission.
            service (ReferralService):
            reason (ReferralReason):
            review_status (ReferralReviewStatus):
            priority (None | ReferralPriorityType1 | ReferralPriorityType2Type1 | ReferralPriorityType3Type1 | Unset):
            clinical_summary (None | str | Unset):
            requester (ReferralRequester | Unset): Who sent the referral, as the sender states it. Nothing here is checked
                against a directory.
            recipient (ReferralRecipient | Unset): Who at the clinic will see the patient. Set by clinic staff when they
                accept the referral; never by a sender.
            requested_at (datetime.datetime | None | Unset):
            needed_by (datetime.date | None | Unset):
            scheduled_appointment_id (None | Unset | UUID):
            source (None | ReferralSourceType1 | ReferralSourceType2Type1 | ReferralSourceType3Type1 | Unset):
            origin_assistant_name (None | str | Unset):
            accepted_by (None | ReferralAcceptedByType1 | ReferralAcceptedByType2Type1 | ReferralAcceptedByType3Type1 |
                Unset): Who put this record on the chart: `clinic` (the clinic's own team, or a clinician who confirmed it) or
                `automatic` (the clinic chose to accept this kind of item from this key or connection without review; the record
                is on the chart but no clinician has reviewed it, so `verification_status` reads `unconfirmed` until one does).
                Null while the item is still a pending submission.
            reviewed_at (datetime.datetime | None | Unset): Set when a clinician marked an automatically accepted item
                reviewed; null otherwise.
            reviewed_by_staff_id (None | Unset | UUID):
            submission_id (None | Unset | UUID):
            decision_reason (None | str | Unset): On a rejected submission, why clinic staff rejected it. On a confirmed
                referral, the clinic's reason for declining or cancelling - shown only to the key or organization that sent it.
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: None | UUID
    patient_id: UUID
    direction: None | ReferralDirectionType1 | ReferralDirectionType2Type1 | ReferralDirectionType3Type1
    status: None | ReferralStatusType1 | ReferralStatusType2Type1 | ReferralStatusType3Type1
    service: ReferralService
    reason: ReferralReason
    review_status: ReferralReviewStatus
    priority: None | ReferralPriorityType1 | ReferralPriorityType2Type1 | ReferralPriorityType3Type1 | Unset = UNSET
    clinical_summary: None | str | Unset = UNSET
    requester: ReferralRequester | Unset = UNSET
    recipient: ReferralRecipient | Unset = UNSET
    requested_at: datetime.datetime | None | Unset = UNSET
    needed_by: datetime.date | None | Unset = UNSET
    scheduled_appointment_id: None | Unset | UUID = UNSET
    source: None | ReferralSourceType1 | ReferralSourceType2Type1 | ReferralSourceType3Type1 | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    accepted_by: (
        None | ReferralAcceptedByType1 | ReferralAcceptedByType2Type1 | ReferralAcceptedByType3Type1 | Unset
    ) = UNSET
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

        direction: None | str
        if isinstance(self.direction, ReferralDirectionType1):
            direction = self.direction.value
        elif isinstance(self.direction, ReferralDirectionType2Type1):
            direction = self.direction.value
        elif isinstance(self.direction, ReferralDirectionType3Type1):
            direction = self.direction.value
        else:
            direction = self.direction

        status: None | str
        if isinstance(self.status, ReferralStatusType1):
            status = self.status.value
        elif isinstance(self.status, ReferralStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, ReferralStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        service = self.service.to_dict()

        reason = self.reason.to_dict()

        review_status = self.review_status.value

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, ReferralPriorityType1):
            priority = self.priority.value
        elif isinstance(self.priority, ReferralPriorityType2Type1):
            priority = self.priority.value
        elif isinstance(self.priority, ReferralPriorityType3Type1):
            priority = self.priority.value
        else:
            priority = self.priority

        clinical_summary: None | str | Unset
        if isinstance(self.clinical_summary, Unset):
            clinical_summary = UNSET
        else:
            clinical_summary = self.clinical_summary

        requester: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requester, Unset):
            requester = self.requester.to_dict()

        recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        requested_at: None | str | Unset
        if isinstance(self.requested_at, Unset):
            requested_at = UNSET
        elif isinstance(self.requested_at, datetime.datetime):
            requested_at = self.requested_at.isoformat()
        else:
            requested_at = self.requested_at

        needed_by: None | str | Unset
        if isinstance(self.needed_by, Unset):
            needed_by = UNSET
        elif isinstance(self.needed_by, datetime.date):
            needed_by = self.needed_by.isoformat()
        else:
            needed_by = self.needed_by

        scheduled_appointment_id: None | str | Unset
        if isinstance(self.scheduled_appointment_id, Unset):
            scheduled_appointment_id = UNSET
        elif isinstance(self.scheduled_appointment_id, UUID):
            scheduled_appointment_id = str(self.scheduled_appointment_id)
        else:
            scheduled_appointment_id = self.scheduled_appointment_id

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, ReferralSourceType1):
            source = self.source.value
        elif isinstance(self.source, ReferralSourceType2Type1):
            source = self.source.value
        elif isinstance(self.source, ReferralSourceType3Type1):
            source = self.source.value
        else:
            source = self.source

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        accepted_by: None | str | Unset
        if isinstance(self.accepted_by, Unset):
            accepted_by = UNSET
        elif isinstance(self.accepted_by, ReferralAcceptedByType1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, ReferralAcceptedByType2Type1):
            accepted_by = self.accepted_by.value
        elif isinstance(self.accepted_by, ReferralAcceptedByType3Type1):
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
                "direction": direction,
                "status": status,
                "service": service,
                "reason": reason,
                "review_status": review_status,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if clinical_summary is not UNSET:
            field_dict["clinical_summary"] = clinical_summary
        if requester is not UNSET:
            field_dict["requester"] = requester
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by
        if scheduled_appointment_id is not UNSET:
            field_dict["scheduled_appointment_id"] = scheduled_appointment_id
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
        from ..models.referral_reason import ReferralReason  # noqa: PLC0415
        from ..models.referral_recipient import ReferralRecipient  # noqa: PLC0415
        from ..models.referral_requester import ReferralRequester  # noqa: PLC0415
        from ..models.referral_service import ReferralService  # noqa: PLC0415

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

        def _parse_direction(
            data: object,
        ) -> None | ReferralDirectionType1 | ReferralDirectionType2Type1 | ReferralDirectionType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_1 = ReferralDirectionType1(data)

                return direction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_2_type_1 = ReferralDirectionType2Type1(data)

                return direction_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direction_type_3_type_1 = ReferralDirectionType3Type1(data)

                return direction_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReferralDirectionType1 | ReferralDirectionType2Type1 | ReferralDirectionType3Type1, data)

        direction = _parse_direction(d.pop("direction"))

        def _parse_status(
            data: object,
        ) -> None | ReferralStatusType1 | ReferralStatusType2Type1 | ReferralStatusType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = ReferralStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = ReferralStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = ReferralStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReferralStatusType1 | ReferralStatusType2Type1 | ReferralStatusType3Type1, data)

        status = _parse_status(d.pop("status"))

        service = ReferralService.from_dict(d.pop("service"))

        reason = ReferralReason.from_dict(d.pop("reason"))

        review_status = ReferralReviewStatus(d.pop("review_status"))

        def _parse_priority(
            data: object,
        ) -> None | ReferralPriorityType1 | ReferralPriorityType2Type1 | ReferralPriorityType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_1 = ReferralPriorityType1(data)

                return priority_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_2_type_1 = ReferralPriorityType2Type1(data)

                return priority_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_3_type_1 = ReferralPriorityType3Type1(data)

                return priority_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ReferralPriorityType1 | ReferralPriorityType2Type1 | ReferralPriorityType3Type1 | Unset, data
            )

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_clinical_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        clinical_summary = _parse_clinical_summary(d.pop("clinical_summary", UNSET))

        _requester = d.pop("requester", UNSET)
        requester: ReferralRequester | Unset
        if isinstance(_requester, Unset):
            requester = UNSET
        else:
            requester = ReferralRequester.from_dict(_requester)

        _recipient = d.pop("recipient", UNSET)
        recipient: ReferralRecipient | Unset
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = ReferralRecipient.from_dict(_recipient)

        def _parse_requested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_at_type_0 = datetime.datetime.fromisoformat(data)

                return requested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        requested_at = _parse_requested_at(d.pop("requested_at", UNSET))

        def _parse_needed_by(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                needed_by_type_0 = datetime.date.fromisoformat(data)

                return needed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        needed_by = _parse_needed_by(d.pop("needed_by", UNSET))

        def _parse_scheduled_appointment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_appointment_id_type_0 = UUID(data)

                return scheduled_appointment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        scheduled_appointment_id = _parse_scheduled_appointment_id(d.pop("scheduled_appointment_id", UNSET))

        def _parse_source(
            data: object,
        ) -> None | ReferralSourceType1 | ReferralSourceType2Type1 | ReferralSourceType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_1 = ReferralSourceType1(data)

                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_2_type_1 = ReferralSourceType2Type1(data)

                return source_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_3_type_1 = ReferralSourceType3Type1(data)

                return source_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReferralSourceType1 | ReferralSourceType2Type1 | ReferralSourceType3Type1 | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_accepted_by(
            data: object,
        ) -> None | ReferralAcceptedByType1 | ReferralAcceptedByType2Type1 | ReferralAcceptedByType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_1 = ReferralAcceptedByType1(data)

                return accepted_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_2_type_1 = ReferralAcceptedByType2Type1(data)

                return accepted_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_by_type_3_type_1 = ReferralAcceptedByType3Type1(data)

                return accepted_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ReferralAcceptedByType1 | ReferralAcceptedByType2Type1 | ReferralAcceptedByType3Type1 | Unset,
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

        referral = cls(
            id=id,
            patient_id=patient_id,
            direction=direction,
            status=status,
            service=service,
            reason=reason,
            review_status=review_status,
            priority=priority,
            clinical_summary=clinical_summary,
            requester=requester,
            recipient=recipient,
            requested_at=requested_at,
            needed_by=needed_by,
            scheduled_appointment_id=scheduled_appointment_id,
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

        referral.additional_properties = d
        return referral

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
