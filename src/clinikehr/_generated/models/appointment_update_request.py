from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.appointment_update_request_status import AppointmentUpdateRequestStatus
from ..models.appointment_update_request_urgency_level import AppointmentUpdateRequestUrgencyLevel
from ..models.appointment_update_request_venue_type import AppointmentUpdateRequestVenueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentUpdateRequest")


@_attrs_define
class AppointmentUpdateRequest:
    """Immutable after create, and refused if sent: patient_id, service_id, location_id, every payment field.

    Attributes:
        start_at (datetime.datetime | Unset): Present ⇒ reschedule, re-validated against availability/out-of-
            office/double-booking.
        clinician_id (UUID | Unset):
        venue_type (AppointmentUpdateRequestVenueType | Unset):
        urgency_level (AppointmentUpdateRequestUrgencyLevel | Unset):
        patient_notes (None | str | Unset):
        clinic_notes (None | str | Unset):
        symptoms_description (None | str | Unset):
        status (AppointmentUpdateRequestStatus | Unset): The only status this route may set.
        email_notifications (bool | Unset): Absent ≠ null — no notify_patient shorthand on update. Governs every email
            the patient receives about this appointment (confirmations, changes, cancellations, reminders); false does not
            stop the clinicians involved being told of a change.
        sms_notifications (bool | Unset): Text reminders for this appointment.
        voice_notifications (bool | Unset): Voice reminders for this appointment.
        run_automations (bool | Unset):  Default: False.
    """

    start_at: datetime.datetime | Unset = UNSET
    clinician_id: UUID | Unset = UNSET
    venue_type: AppointmentUpdateRequestVenueType | Unset = UNSET
    urgency_level: AppointmentUpdateRequestUrgencyLevel | Unset = UNSET
    patient_notes: None | str | Unset = UNSET
    clinic_notes: None | str | Unset = UNSET
    symptoms_description: None | str | Unset = UNSET
    status: AppointmentUpdateRequestStatus | Unset = UNSET
    email_notifications: bool | Unset = UNSET
    sms_notifications: bool | Unset = UNSET
    voice_notifications: bool | Unset = UNSET
    run_automations: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        clinician_id: str | Unset = UNSET
        if not isinstance(self.clinician_id, Unset):
            clinician_id = str(self.clinician_id)

        venue_type: str | Unset = UNSET
        if not isinstance(self.venue_type, Unset):
            venue_type = self.venue_type.value

        urgency_level: str | Unset = UNSET
        if not isinstance(self.urgency_level, Unset):
            urgency_level = self.urgency_level.value

        patient_notes: None | str | Unset
        if isinstance(self.patient_notes, Unset):
            patient_notes = UNSET
        else:
            patient_notes = self.patient_notes

        clinic_notes: None | str | Unset
        if isinstance(self.clinic_notes, Unset):
            clinic_notes = UNSET
        else:
            clinic_notes = self.clinic_notes

        symptoms_description: None | str | Unset
        if isinstance(self.symptoms_description, Unset):
            symptoms_description = UNSET
        else:
            symptoms_description = self.symptoms_description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        email_notifications = self.email_notifications

        sms_notifications = self.sms_notifications

        voice_notifications = self.voice_notifications

        run_automations = self.run_automations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if clinician_id is not UNSET:
            field_dict["clinician_id"] = clinician_id
        if venue_type is not UNSET:
            field_dict["venue_type"] = venue_type
        if urgency_level is not UNSET:
            field_dict["urgency_level"] = urgency_level
        if patient_notes is not UNSET:
            field_dict["patient_notes"] = patient_notes
        if clinic_notes is not UNSET:
            field_dict["clinic_notes"] = clinic_notes
        if symptoms_description is not UNSET:
            field_dict["symptoms_description"] = symptoms_description
        if status is not UNSET:
            field_dict["status"] = status
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if sms_notifications is not UNSET:
            field_dict["sms_notifications"] = sms_notifications
        if voice_notifications is not UNSET:
            field_dict["voice_notifications"] = voice_notifications
        if run_automations is not UNSET:
            field_dict["run_automations"] = run_automations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_at = d.pop("start_at", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)

        _clinician_id = d.pop("clinician_id", UNSET)
        clinician_id: UUID | Unset
        if isinstance(_clinician_id, Unset):
            clinician_id = UNSET
        else:
            clinician_id = UUID(_clinician_id)

        _venue_type = d.pop("venue_type", UNSET)
        venue_type: AppointmentUpdateRequestVenueType | Unset
        if isinstance(_venue_type, Unset):
            venue_type = UNSET
        else:
            venue_type = AppointmentUpdateRequestVenueType(_venue_type)

        _urgency_level = d.pop("urgency_level", UNSET)
        urgency_level: AppointmentUpdateRequestUrgencyLevel | Unset
        if isinstance(_urgency_level, Unset):
            urgency_level = UNSET
        else:
            urgency_level = AppointmentUpdateRequestUrgencyLevel(_urgency_level)

        def _parse_patient_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        patient_notes = _parse_patient_notes(d.pop("patient_notes", UNSET))

        def _parse_clinic_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        clinic_notes = _parse_clinic_notes(d.pop("clinic_notes", UNSET))

        def _parse_symptoms_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symptoms_description = _parse_symptoms_description(d.pop("symptoms_description", UNSET))

        _status = d.pop("status", UNSET)
        status: AppointmentUpdateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppointmentUpdateRequestStatus(_status)

        email_notifications = d.pop("email_notifications", UNSET)

        sms_notifications = d.pop("sms_notifications", UNSET)

        voice_notifications = d.pop("voice_notifications", UNSET)

        run_automations = d.pop("run_automations", UNSET)

        appointment_update_request = cls(
            start_at=start_at,
            clinician_id=clinician_id,
            venue_type=venue_type,
            urgency_level=urgency_level,
            patient_notes=patient_notes,
            clinic_notes=clinic_notes,
            symptoms_description=symptoms_description,
            status=status,
            email_notifications=email_notifications,
            sms_notifications=sms_notifications,
            voice_notifications=voice_notifications,
            run_automations=run_automations,
        )

        appointment_update_request.additional_properties = d
        return appointment_update_request

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
