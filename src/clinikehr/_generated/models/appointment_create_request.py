from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.appointment_create_request_payment_status import AppointmentCreateRequestPaymentStatus
from ..models.appointment_create_request_status import AppointmentCreateRequestStatus
from ..models.appointment_create_request_urgency_level import AppointmentCreateRequestUrgencyLevel
from ..models.appointment_create_request_venue_type import AppointmentCreateRequestVenueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentCreateRequest")


@_attrs_define
class AppointmentCreateRequest:
    """
    Attributes:
        patient_id (UUID):
        service_id (UUID):
        start_at (datetime.datetime): ISO 8601 WITH an explicit offset — a value with no offset is invalid_request,
            never a silent UTC/local guess.
        clinician_id (UUID | Unset): Omit to let the pool pick a free, eligible clinician.
        location_id (UUID | Unset):
        venue_type (AppointmentCreateRequestVenueType | Unset):  Default: AppointmentCreateRequestVenueType.PHYSICAL.
        urgency_level (AppointmentCreateRequestUrgencyLevel | Unset):  Default:
            AppointmentCreateRequestUrgencyLevel.NORMAL.
        patient_notes (str | Unset):
        clinic_notes (str | Unset):
        symptoms_description (str | Unset):
        status (AppointmentCreateRequestStatus | Unset):  Default: AppointmentCreateRequestStatus.SCHEDULED.
        payment_amount (float | Unset):
        payment_method (str | Unset):
        payment_status (AppointmentCreateRequestPaymentStatus | Unset):  Default:
            AppointmentCreateRequestPaymentStatus.PENDING.
        notify_patient (bool | Unset): false sets email_notifications/sms_notifications/voice_notifications false on the
            row itself — a real, persistent setting, not a one-time suppression, so the patient is also not emailed about
            later changes, cancellation or reminders. Default: True.
        run_automations (bool | Unset): Default false suppresses the appointment.created/*.status Agent Studio dispatch.
            Default: False.
    """

    patient_id: UUID
    service_id: UUID
    start_at: datetime.datetime
    clinician_id: UUID | Unset = UNSET
    location_id: UUID | Unset = UNSET
    venue_type: AppointmentCreateRequestVenueType | Unset = AppointmentCreateRequestVenueType.PHYSICAL
    urgency_level: AppointmentCreateRequestUrgencyLevel | Unset = AppointmentCreateRequestUrgencyLevel.NORMAL
    patient_notes: str | Unset = UNSET
    clinic_notes: str | Unset = UNSET
    symptoms_description: str | Unset = UNSET
    status: AppointmentCreateRequestStatus | Unset = AppointmentCreateRequestStatus.SCHEDULED
    payment_amount: float | Unset = UNSET
    payment_method: str | Unset = UNSET
    payment_status: AppointmentCreateRequestPaymentStatus | Unset = AppointmentCreateRequestPaymentStatus.PENDING
    notify_patient: bool | Unset = True
    run_automations: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        service_id = str(self.service_id)

        start_at = self.start_at.isoformat()

        clinician_id: str | Unset = UNSET
        if not isinstance(self.clinician_id, Unset):
            clinician_id = str(self.clinician_id)

        location_id: str | Unset = UNSET
        if not isinstance(self.location_id, Unset):
            location_id = str(self.location_id)

        venue_type: str | Unset = UNSET
        if not isinstance(self.venue_type, Unset):
            venue_type = self.venue_type.value

        urgency_level: str | Unset = UNSET
        if not isinstance(self.urgency_level, Unset):
            urgency_level = self.urgency_level.value

        patient_notes = self.patient_notes

        clinic_notes = self.clinic_notes

        symptoms_description = self.symptoms_description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_amount = self.payment_amount

        payment_method = self.payment_method

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        notify_patient = self.notify_patient

        run_automations = self.run_automations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "patient_id": patient_id,
                "service_id": service_id,
                "start_at": start_at,
            }
        )
        if clinician_id is not UNSET:
            field_dict["clinician_id"] = clinician_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
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
        if payment_amount is not UNSET:
            field_dict["payment_amount"] = payment_amount
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if notify_patient is not UNSET:
            field_dict["notify_patient"] = notify_patient
        if run_automations is not UNSET:
            field_dict["run_automations"] = run_automations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        service_id = UUID(d.pop("service_id"))

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        _clinician_id = d.pop("clinician_id", UNSET)
        clinician_id: UUID | Unset
        if isinstance(_clinician_id, Unset):
            clinician_id = UNSET
        else:
            clinician_id = UUID(_clinician_id)

        _location_id = d.pop("location_id", UNSET)
        location_id: UUID | Unset
        if isinstance(_location_id, Unset):
            location_id = UNSET
        else:
            location_id = UUID(_location_id)

        _venue_type = d.pop("venue_type", UNSET)
        venue_type: AppointmentCreateRequestVenueType | Unset
        if isinstance(_venue_type, Unset):
            venue_type = UNSET
        else:
            venue_type = AppointmentCreateRequestVenueType(_venue_type)

        _urgency_level = d.pop("urgency_level", UNSET)
        urgency_level: AppointmentCreateRequestUrgencyLevel | Unset
        if isinstance(_urgency_level, Unset):
            urgency_level = UNSET
        else:
            urgency_level = AppointmentCreateRequestUrgencyLevel(_urgency_level)

        patient_notes = d.pop("patient_notes", UNSET)

        clinic_notes = d.pop("clinic_notes", UNSET)

        symptoms_description = d.pop("symptoms_description", UNSET)

        _status = d.pop("status", UNSET)
        status: AppointmentCreateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppointmentCreateRequestStatus(_status)

        payment_amount = d.pop("payment_amount", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        _payment_status = d.pop("payment_status", UNSET)
        payment_status: AppointmentCreateRequestPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = AppointmentCreateRequestPaymentStatus(_payment_status)

        notify_patient = d.pop("notify_patient", UNSET)

        run_automations = d.pop("run_automations", UNSET)

        appointment_create_request = cls(
            patient_id=patient_id,
            service_id=service_id,
            start_at=start_at,
            clinician_id=clinician_id,
            location_id=location_id,
            venue_type=venue_type,
            urgency_level=urgency_level,
            patient_notes=patient_notes,
            clinic_notes=clinic_notes,
            symptoms_description=symptoms_description,
            status=status,
            payment_amount=payment_amount,
            payment_method=payment_method,
            payment_status=payment_status,
            notify_patient=notify_patient,
            run_automations=run_automations,
        )

        appointment_create_request.additional_properties = d
        return appointment_create_request

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
