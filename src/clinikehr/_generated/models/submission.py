from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.submission_action import SubmissionAction
from ..models.submission_resource_type import SubmissionResourceType
from ..models.submission_review_status import SubmissionReviewStatus
from ..models.submission_source import SubmissionSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submission_payload import SubmissionPayload


T = TypeVar("T", bound="Submission")


@_attrs_define
class Submission:
    """What the clinic's review queue holds for something this key sent: one outside record waiting for, or already past, a
    clinician's decision.

        Attributes:
            submission_id (UUID):
            patient_id (UUID):
            resource_type (SubmissionResourceType): The kind of record.
            action (SubmissionAction):
            review_status (SubmissionReviewStatus):
            target_id (None | Unset | UUID): The existing record an update or retract is about — for
                `prescription_pickup_collection` this is the pickup being completed.
            accepted_automatically (bool | Unset): True when the clinic has chosen to accept this kind of item from this key
                or connection without review; the item is then already on the chart and `review_status` is `confirmed`. False
                for everything a clinician decides, and while it is pending.
            source (SubmissionSource | Unset):
            submitted_at (datetime.datetime | None | Unset):
            decided_at (datetime.datetime | None | Unset):
            decision_reason (None | str | Unset): Present only when rejected.
            result_record_id (None | Unset | UUID): The record this became, once confirmed.
            client_reference (None | str | Unset):
            origin_assistant_name (None | str | Unset):
            payload (SubmissionPayload | Unset): What was submitted. For `prescription_pickup_collection` this never carries
                the signature image — see `has_signature`.
            has_signature (bool | None | Unset): `prescription_pickup_collection` only: whether a signature was included.
                The signature image itself is never returned. Null for every other resource_type.
    """

    submission_id: UUID
    patient_id: UUID
    resource_type: SubmissionResourceType
    action: SubmissionAction
    review_status: SubmissionReviewStatus
    target_id: None | Unset | UUID = UNSET
    accepted_automatically: bool | Unset = UNSET
    source: SubmissionSource | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    decision_reason: None | str | Unset = UNSET
    result_record_id: None | Unset | UUID = UNSET
    client_reference: None | str | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    payload: SubmissionPayload | Unset = UNSET
    has_signature: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_id = str(self.submission_id)

        patient_id = str(self.patient_id)

        resource_type = self.resource_type.value

        action = self.action.value

        review_status = self.review_status.value

        target_id: None | str | Unset
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        elif isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        accepted_automatically = self.accepted_automatically

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        decision_reason: None | str | Unset
        if isinstance(self.decision_reason, Unset):
            decision_reason = UNSET
        else:
            decision_reason = self.decision_reason

        result_record_id: None | str | Unset
        if isinstance(self.result_record_id, Unset):
            result_record_id = UNSET
        elif isinstance(self.result_record_id, UUID):
            result_record_id = str(self.result_record_id)
        else:
            result_record_id = self.result_record_id

        client_reference: None | str | Unset
        if isinstance(self.client_reference, Unset):
            client_reference = UNSET
        else:
            client_reference = self.client_reference

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        has_signature: bool | None | Unset
        if isinstance(self.has_signature, Unset):
            has_signature = UNSET
        else:
            has_signature = self.has_signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submission_id": submission_id,
                "patient_id": patient_id,
                "resource_type": resource_type,
                "action": action,
                "review_status": review_status,
            }
        )
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if accepted_automatically is not UNSET:
            field_dict["accepted_automatically"] = accepted_automatically
        if source is not UNSET:
            field_dict["source"] = source
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if decision_reason is not UNSET:
            field_dict["decision_reason"] = decision_reason
        if result_record_id is not UNSET:
            field_dict["result_record_id"] = result_record_id
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if payload is not UNSET:
            field_dict["payload"] = payload
        if has_signature is not UNSET:
            field_dict["has_signature"] = has_signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submission_payload import SubmissionPayload  # noqa: PLC0415

        d = dict(src_dict)
        submission_id = UUID(d.pop("submission_id"))

        patient_id = UUID(d.pop("patient_id"))

        resource_type = SubmissionResourceType(d.pop("resource_type"))

        action = SubmissionAction(d.pop("action"))

        review_status = SubmissionReviewStatus(d.pop("review_status"))

        def _parse_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)

                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_id = _parse_target_id(d.pop("target_id", UNSET))

        accepted_automatically = d.pop("accepted_automatically", UNSET)

        _source = d.pop("source", UNSET)
        source: SubmissionSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SubmissionSource(_source)

        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)

                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))

        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)

                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decided_at", UNSET))

        def _parse_decision_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_reason = _parse_decision_reason(d.pop("decision_reason", UNSET))

        def _parse_result_record_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_record_id_type_0 = UUID(data)

                return result_record_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        result_record_id = _parse_result_record_id(d.pop("result_record_id", UNSET))

        def _parse_client_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference = _parse_client_reference(d.pop("client_reference", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        _payload = d.pop("payload", UNSET)
        payload: SubmissionPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = SubmissionPayload.from_dict(_payload)

        def _parse_has_signature(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_signature = _parse_has_signature(d.pop("has_signature", UNSET))

        submission = cls(
            submission_id=submission_id,
            patient_id=patient_id,
            resource_type=resource_type,
            action=action,
            review_status=review_status,
            target_id=target_id,
            accepted_automatically=accepted_automatically,
            source=source,
            submitted_at=submitted_at,
            decided_at=decided_at,
            decision_reason=decision_reason,
            result_record_id=result_record_id,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
            payload=payload,
            has_signature=has_signature,
        )

        submission.additional_properties = d
        return submission

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
