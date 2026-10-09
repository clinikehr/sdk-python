from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.drug_request_status_type_1 import DrugRequestStatusType1
from ..models.drug_request_status_type_2_type_1 import DrugRequestStatusType2Type1
from ..models.drug_request_status_type_3_type_1 import DrugRequestStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drug_request_line import DrugRequestLine


T = TypeVar("T", bound="DrugRequest")


@_attrs_define
class DrugRequest:
    """Never carries a price/cost/amount field — a request is a commitment to fill medicine, never a billing document.

    Attributes:
        id (UUID):
        clinic_patient_id (None | Unset | UUID):
        status (DrugRequestStatusType1 | DrugRequestStatusType2Type1 | DrugRequestStatusType3Type1 | None | Unset):
        requester_reference (None | str | Unset):
        authorization_reference (None | str | Unset):
        needed_by (datetime.datetime | None | Unset):
        pharmacist_note (None | str | Unset):
        decline_reason (None | str | Unset):
        cancel_reason (None | str | Unset):
        cancelled_by_actor (None | str | Unset):
        decided_at (datetime.datetime | None | Unset):
        ready_at (datetime.datetime | None | Unset):
        dispensed_at (datetime.datetime | None | Unset):
        cancelled_at (datetime.datetime | None | Unset):
        expired_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        lines (list[DrugRequestLine] | Unset):
    """

    id: UUID
    clinic_patient_id: None | Unset | UUID = UNSET
    status: DrugRequestStatusType1 | DrugRequestStatusType2Type1 | DrugRequestStatusType3Type1 | None | Unset = UNSET
    requester_reference: None | str | Unset = UNSET
    authorization_reference: None | str | Unset = UNSET
    needed_by: datetime.datetime | None | Unset = UNSET
    pharmacist_note: None | str | Unset = UNSET
    decline_reason: None | str | Unset = UNSET
    cancel_reason: None | str | Unset = UNSET
    cancelled_by_actor: None | str | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    ready_at: datetime.datetime | None | Unset = UNSET
    dispensed_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    expired_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    lines: list[DrugRequestLine] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        clinic_patient_id: None | str | Unset
        if isinstance(self.clinic_patient_id, Unset):
            clinic_patient_id = UNSET
        elif isinstance(self.clinic_patient_id, UUID):
            clinic_patient_id = str(self.clinic_patient_id)
        else:
            clinic_patient_id = self.clinic_patient_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, DrugRequestStatusType1):
            status = self.status.value
        elif isinstance(self.status, DrugRequestStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, DrugRequestStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        requester_reference: None | str | Unset
        if isinstance(self.requester_reference, Unset):
            requester_reference = UNSET
        else:
            requester_reference = self.requester_reference

        authorization_reference: None | str | Unset
        if isinstance(self.authorization_reference, Unset):
            authorization_reference = UNSET
        else:
            authorization_reference = self.authorization_reference

        needed_by: None | str | Unset
        if isinstance(self.needed_by, Unset):
            needed_by = UNSET
        elif isinstance(self.needed_by, datetime.datetime):
            needed_by = self.needed_by.isoformat()
        else:
            needed_by = self.needed_by

        pharmacist_note: None | str | Unset
        if isinstance(self.pharmacist_note, Unset):
            pharmacist_note = UNSET
        else:
            pharmacist_note = self.pharmacist_note

        decline_reason: None | str | Unset
        if isinstance(self.decline_reason, Unset):
            decline_reason = UNSET
        else:
            decline_reason = self.decline_reason

        cancel_reason: None | str | Unset
        if isinstance(self.cancel_reason, Unset):
            cancel_reason = UNSET
        else:
            cancel_reason = self.cancel_reason

        cancelled_by_actor: None | str | Unset
        if isinstance(self.cancelled_by_actor, Unset):
            cancelled_by_actor = UNSET
        else:
            cancelled_by_actor = self.cancelled_by_actor

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        ready_at: None | str | Unset
        if isinstance(self.ready_at, Unset):
            ready_at = UNSET
        elif isinstance(self.ready_at, datetime.datetime):
            ready_at = self.ready_at.isoformat()
        else:
            ready_at = self.ready_at

        dispensed_at: None | str | Unset
        if isinstance(self.dispensed_at, Unset):
            dispensed_at = UNSET
        elif isinstance(self.dispensed_at, datetime.datetime):
            dispensed_at = self.dispensed_at.isoformat()
        else:
            dispensed_at = self.dispensed_at

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        expired_at: None | str | Unset
        if isinstance(self.expired_at, Unset):
            expired_at = UNSET
        elif isinstance(self.expired_at, datetime.datetime):
            expired_at = self.expired_at.isoformat()
        else:
            expired_at = self.expired_at

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

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if clinic_patient_id is not UNSET:
            field_dict["clinic_patient_id"] = clinic_patient_id
        if status is not UNSET:
            field_dict["status"] = status
        if requester_reference is not UNSET:
            field_dict["requester_reference"] = requester_reference
        if authorization_reference is not UNSET:
            field_dict["authorization_reference"] = authorization_reference
        if needed_by is not UNSET:
            field_dict["needed_by"] = needed_by
        if pharmacist_note is not UNSET:
            field_dict["pharmacist_note"] = pharmacist_note
        if decline_reason is not UNSET:
            field_dict["decline_reason"] = decline_reason
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if cancelled_by_actor is not UNSET:
            field_dict["cancelled_by_actor"] = cancelled_by_actor
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if ready_at is not UNSET:
            field_dict["ready_at"] = ready_at
        if dispensed_at is not UNSET:
            field_dict["dispensed_at"] = dispensed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if expired_at is not UNSET:
            field_dict["expired_at"] = expired_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drug_request_line import DrugRequestLine  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_clinic_patient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinic_patient_id_type_0 = UUID(data)

                return clinic_patient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clinic_patient_id = _parse_clinic_patient_id(d.pop("clinic_patient_id", UNSET))

        def _parse_status(
            data: object,
        ) -> DrugRequestStatusType1 | DrugRequestStatusType2Type1 | DrugRequestStatusType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = DrugRequestStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = DrugRequestStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = DrugRequestStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DrugRequestStatusType1 | DrugRequestStatusType2Type1 | DrugRequestStatusType3Type1 | None | Unset, data
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_requester_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_reference = _parse_requester_reference(d.pop("requester_reference", UNSET))

        def _parse_authorization_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_reference = _parse_authorization_reference(d.pop("authorization_reference", UNSET))

        def _parse_needed_by(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                needed_by_type_0 = datetime.datetime.fromisoformat(data)

                return needed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        needed_by = _parse_needed_by(d.pop("needed_by", UNSET))

        def _parse_pharmacist_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pharmacist_note = _parse_pharmacist_note(d.pop("pharmacist_note", UNSET))

        def _parse_decline_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decline_reason = _parse_decline_reason(d.pop("decline_reason", UNSET))

        def _parse_cancel_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancel_reason = _parse_cancel_reason(d.pop("cancel_reason", UNSET))

        def _parse_cancelled_by_actor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancelled_by_actor = _parse_cancelled_by_actor(d.pop("cancelled_by_actor", UNSET))

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

        def _parse_ready_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ready_at_type_0 = datetime.datetime.fromisoformat(data)

                return ready_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ready_at = _parse_ready_at(d.pop("ready_at", UNSET))

        def _parse_dispensed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispensed_at_type_0 = datetime.datetime.fromisoformat(data)

                return dispensed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dispensed_at = _parse_dispensed_at(d.pop("dispensed_at", UNSET))

        def _parse_cancelled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_at_type_0 = datetime.datetime.fromisoformat(data)

                return cancelled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        def _parse_expired_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expired_at_type_0 = datetime.datetime.fromisoformat(data)

                return expired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expired_at = _parse_expired_at(d.pop("expired_at", UNSET))

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

        _lines = d.pop("lines", UNSET)
        lines: list[DrugRequestLine] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = DrugRequestLine.from_dict(lines_item_data)

                lines.append(lines_item)

        drug_request = cls(
            id=id,
            clinic_patient_id=clinic_patient_id,
            status=status,
            requester_reference=requester_reference,
            authorization_reference=authorization_reference,
            needed_by=needed_by,
            pharmacist_note=pharmacist_note,
            decline_reason=decline_reason,
            cancel_reason=cancel_reason,
            cancelled_by_actor=cancelled_by_actor,
            decided_at=decided_at,
            ready_at=ready_at,
            dispensed_at=dispensed_at,
            cancelled_at=cancelled_at,
            expired_at=expired_at,
            created_at=created_at,
            updated_at=updated_at,
            lines=lines,
        )

        drug_request.additional_properties = d
        return drug_request

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
