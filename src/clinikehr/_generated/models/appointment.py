from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.appointment_payment_status_type_1 import AppointmentPaymentStatusType1
from ..models.appointment_payment_status_type_2_type_1 import AppointmentPaymentStatusType2Type1
from ..models.appointment_payment_status_type_3_type_1 import AppointmentPaymentStatusType3Type1
from ..models.appointment_status import AppointmentStatus
from ..models.appointment_urgency_level_type_1 import AppointmentUrgencyLevelType1
from ..models.appointment_urgency_level_type_2_type_1 import AppointmentUrgencyLevelType2Type1
from ..models.appointment_urgency_level_type_3_type_1 import AppointmentUrgencyLevelType3Type1
from ..models.appointment_venue_type_type_1 import AppointmentVenueTypeType1
from ..models.appointment_venue_type_type_2_type_1 import AppointmentVenueTypeType2Type1
from ..models.appointment_venue_type_type_3_type_1 import AppointmentVenueTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_participant import AppointmentParticipant
    from ..models.appointment_venue_details_type_0 import AppointmentVenueDetailsType0


T = TypeVar("T", bound="Appointment")


@_attrs_define
class Appointment:
    """Never present here, by name: client_appointment_date/client_start_time/ client_end_time/client_timezone, form_data,
    custom_color, provider_user_id, time_range, excluded_from_overlap_check, booking_identity_review,
    provider_busy_minutes, out_of_office_confirmed_at, booking_confirmation_deferred, clinic_id.

        Attributes:
            id (UUID):
            status (AppointmentStatus):
            patient_id (None | Unset | UUID):
            service_id (None | Unset | UUID):
            clinician_id (None | Unset | UUID):
            start_at (datetime.datetime | None | Unset):
            end_at (datetime.datetime | None | Unset): Derived from the service's duration — never independent input.
            duration_minutes (int | None | Unset):
            timezone (None | str | Unset):
            venue_type (AppointmentVenueTypeType1 | AppointmentVenueTypeType2Type1 | AppointmentVenueTypeType3Type1 | None |
                Unset):
            venue_details (AppointmentVenueDetailsType0 | None | Unset): Read-only.
            booking_source (None | str | Unset): Always "api" for a row this API created.
            patient_notes (None | str | Unset):
            clinic_notes (None | str | Unset):
            symptoms_description (None | str | Unset):
            urgency_level (AppointmentUrgencyLevelType1 | AppointmentUrgencyLevelType2Type1 |
                AppointmentUrgencyLevelType3Type1 | None | Unset):
            ai_category (None | str | Unset): Read-only.
            ai_priority_score (float | None | Unset): Read-only.
            ai_suggested_duration (float | None | Unset): Read-only.
            predicted_show_probability (float | None | Unset): Read-only.
            confirmation_sent_at (datetime.datetime | None | Unset):
            confirmation_method (None | str | Unset):
            reminder_sent_at (datetime.datetime | None | Unset):
            reminder_method (None | str | Unset):
            reminder_sent (bool | None | Unset):
            payment_status (AppointmentPaymentStatusType1 | AppointmentPaymentStatusType2Type1 |
                AppointmentPaymentStatusType3Type1 | None | Unset):
            payment_method (None | str | Unset):
            payment_amount (float | None | Unset):
            payment_due_date (datetime.date | None | Unset):
            amount_paid (float | None | Unset): Read-only.
            payment_id (None | str | Unset): Read-only.
            confirmation_code (None | str | Unset): Read-only.
            cancellation_reason (None | str | Unset):
            cancelled_at (datetime.datetime | None | Unset):
            completed_at (datetime.datetime | None | Unset):
            is_group_appointment (bool | None | Unset): Read-only.
            max_participants (int | None | Unset): Read-only.
            group_name (None | str | Unset): Read-only.
            recurrence_pattern_id (None | Unset | UUID): Read-only. Creating/editing a whole series is refused.
            series_id (None | Unset | UUID): Read-only.
            series_index (int | None | Unset): Read-only.
            email_notifications (bool | None | Unset): Whether the patient is emailed about this appointment: confirmations,
                changes, cancellations and reminders. false silences all of them. The clinicians involved are still told about a
                change.
            sms_notifications (bool | None | Unset): Whether the patient is sent text reminders for this appointment.
            voice_notifications (bool | None | Unset): Whether the patient is sent voice reminders for this appointment.
            notes_session_ids (list[UUID] | Unset): Read-only.
            class_session_id (None | Unset | UUID): Read-only.
            self_reschedule_count (int | None | Unset): Read-only. Tracks PATIENT-initiated portal reschedules only — never
                incremented by this API.
            location_id (None | Unset | UUID):
            participants (list[AppointmentParticipant] | Unset): Read-only group roster — group creation is a scope cut in
                v1.
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    status: AppointmentStatus
    patient_id: None | Unset | UUID = UNSET
    service_id: None | Unset | UUID = UNSET
    clinician_id: None | Unset | UUID = UNSET
    start_at: datetime.datetime | None | Unset = UNSET
    end_at: datetime.datetime | None | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    timezone: None | str | Unset = UNSET
    venue_type: (
        AppointmentVenueTypeType1 | AppointmentVenueTypeType2Type1 | AppointmentVenueTypeType3Type1 | None | Unset
    ) = UNSET
    venue_details: AppointmentVenueDetailsType0 | None | Unset = UNSET
    booking_source: None | str | Unset = UNSET
    patient_notes: None | str | Unset = UNSET
    clinic_notes: None | str | Unset = UNSET
    symptoms_description: None | str | Unset = UNSET
    urgency_level: (
        AppointmentUrgencyLevelType1
        | AppointmentUrgencyLevelType2Type1
        | AppointmentUrgencyLevelType3Type1
        | None
        | Unset
    ) = UNSET
    ai_category: None | str | Unset = UNSET
    ai_priority_score: float | None | Unset = UNSET
    ai_suggested_duration: float | None | Unset = UNSET
    predicted_show_probability: float | None | Unset = UNSET
    confirmation_sent_at: datetime.datetime | None | Unset = UNSET
    confirmation_method: None | str | Unset = UNSET
    reminder_sent_at: datetime.datetime | None | Unset = UNSET
    reminder_method: None | str | Unset = UNSET
    reminder_sent: bool | None | Unset = UNSET
    payment_status: (
        AppointmentPaymentStatusType1
        | AppointmentPaymentStatusType2Type1
        | AppointmentPaymentStatusType3Type1
        | None
        | Unset
    ) = UNSET
    payment_method: None | str | Unset = UNSET
    payment_amount: float | None | Unset = UNSET
    payment_due_date: datetime.date | None | Unset = UNSET
    amount_paid: float | None | Unset = UNSET
    payment_id: None | str | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    cancellation_reason: None | str | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    is_group_appointment: bool | None | Unset = UNSET
    max_participants: int | None | Unset = UNSET
    group_name: None | str | Unset = UNSET
    recurrence_pattern_id: None | Unset | UUID = UNSET
    series_id: None | Unset | UUID = UNSET
    series_index: int | None | Unset = UNSET
    email_notifications: bool | None | Unset = UNSET
    sms_notifications: bool | None | Unset = UNSET
    voice_notifications: bool | None | Unset = UNSET
    notes_session_ids: list[UUID] | Unset = UNSET
    class_session_id: None | Unset | UUID = UNSET
    self_reschedule_count: int | None | Unset = UNSET
    location_id: None | Unset | UUID = UNSET
    participants: list[AppointmentParticipant] | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.appointment_venue_details_type_0 import AppointmentVenueDetailsType0  # noqa: PLC0415

        id = str(self.id)

        status = self.status.value

        patient_id: None | str | Unset
        if isinstance(self.patient_id, Unset):
            patient_id = UNSET
        elif isinstance(self.patient_id, UUID):
            patient_id = str(self.patient_id)
        else:
            patient_id = self.patient_id

        service_id: None | str | Unset
        if isinstance(self.service_id, Unset):
            service_id = UNSET
        elif isinstance(self.service_id, UUID):
            service_id = str(self.service_id)
        else:
            service_id = self.service_id

        clinician_id: None | str | Unset
        if isinstance(self.clinician_id, Unset):
            clinician_id = UNSET
        elif isinstance(self.clinician_id, UUID):
            clinician_id = str(self.clinician_id)
        else:
            clinician_id = self.clinician_id

        start_at: None | str | Unset
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        elif isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        end_at: None | str | Unset
        if isinstance(self.end_at, Unset):
            end_at = UNSET
        elif isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        venue_type: None | str | Unset
        if isinstance(self.venue_type, Unset):
            venue_type = UNSET
        elif isinstance(self.venue_type, AppointmentVenueTypeType1):
            venue_type = self.venue_type.value
        elif isinstance(self.venue_type, AppointmentVenueTypeType2Type1):
            venue_type = self.venue_type.value
        elif isinstance(self.venue_type, AppointmentVenueTypeType3Type1):
            venue_type = self.venue_type.value
        else:
            venue_type = self.venue_type

        venue_details: dict[str, Any] | None | Unset
        if isinstance(self.venue_details, Unset):
            venue_details = UNSET
        elif isinstance(self.venue_details, AppointmentVenueDetailsType0):
            venue_details = self.venue_details.to_dict()
        else:
            venue_details = self.venue_details

        booking_source: None | str | Unset
        if isinstance(self.booking_source, Unset):
            booking_source = UNSET
        else:
            booking_source = self.booking_source

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

        urgency_level: None | str | Unset
        if isinstance(self.urgency_level, Unset):
            urgency_level = UNSET
        elif isinstance(self.urgency_level, AppointmentUrgencyLevelType1):
            urgency_level = self.urgency_level.value
        elif isinstance(self.urgency_level, AppointmentUrgencyLevelType2Type1):
            urgency_level = self.urgency_level.value
        elif isinstance(self.urgency_level, AppointmentUrgencyLevelType3Type1):
            urgency_level = self.urgency_level.value
        else:
            urgency_level = self.urgency_level

        ai_category: None | str | Unset
        if isinstance(self.ai_category, Unset):
            ai_category = UNSET
        else:
            ai_category = self.ai_category

        ai_priority_score: float | None | Unset
        if isinstance(self.ai_priority_score, Unset):
            ai_priority_score = UNSET
        else:
            ai_priority_score = self.ai_priority_score

        ai_suggested_duration: float | None | Unset
        if isinstance(self.ai_suggested_duration, Unset):
            ai_suggested_duration = UNSET
        else:
            ai_suggested_duration = self.ai_suggested_duration

        predicted_show_probability: float | None | Unset
        if isinstance(self.predicted_show_probability, Unset):
            predicted_show_probability = UNSET
        else:
            predicted_show_probability = self.predicted_show_probability

        confirmation_sent_at: None | str | Unset
        if isinstance(self.confirmation_sent_at, Unset):
            confirmation_sent_at = UNSET
        elif isinstance(self.confirmation_sent_at, datetime.datetime):
            confirmation_sent_at = self.confirmation_sent_at.isoformat()
        else:
            confirmation_sent_at = self.confirmation_sent_at

        confirmation_method: None | str | Unset
        if isinstance(self.confirmation_method, Unset):
            confirmation_method = UNSET
        else:
            confirmation_method = self.confirmation_method

        reminder_sent_at: None | str | Unset
        if isinstance(self.reminder_sent_at, Unset):
            reminder_sent_at = UNSET
        elif isinstance(self.reminder_sent_at, datetime.datetime):
            reminder_sent_at = self.reminder_sent_at.isoformat()
        else:
            reminder_sent_at = self.reminder_sent_at

        reminder_method: None | str | Unset
        if isinstance(self.reminder_method, Unset):
            reminder_method = UNSET
        else:
            reminder_method = self.reminder_method

        reminder_sent: bool | None | Unset
        if isinstance(self.reminder_sent, Unset):
            reminder_sent = UNSET
        else:
            reminder_sent = self.reminder_sent

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        elif isinstance(self.payment_status, AppointmentPaymentStatusType1):
            payment_status = self.payment_status.value
        elif isinstance(self.payment_status, AppointmentPaymentStatusType2Type1):
            payment_status = self.payment_status.value
        elif isinstance(self.payment_status, AppointmentPaymentStatusType3Type1):
            payment_status = self.payment_status.value
        else:
            payment_status = self.payment_status

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        payment_amount: float | None | Unset
        if isinstance(self.payment_amount, Unset):
            payment_amount = UNSET
        else:
            payment_amount = self.payment_amount

        payment_due_date: None | str | Unset
        if isinstance(self.payment_due_date, Unset):
            payment_due_date = UNSET
        elif isinstance(self.payment_due_date, datetime.date):
            payment_due_date = self.payment_due_date.isoformat()
        else:
            payment_due_date = self.payment_due_date

        amount_paid: float | None | Unset
        if isinstance(self.amount_paid, Unset):
            amount_paid = UNSET
        else:
            amount_paid = self.amount_paid

        payment_id: None | str | Unset
        if isinstance(self.payment_id, Unset):
            payment_id = UNSET
        else:
            payment_id = self.payment_id

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        cancellation_reason: None | str | Unset
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        is_group_appointment: bool | None | Unset
        if isinstance(self.is_group_appointment, Unset):
            is_group_appointment = UNSET
        else:
            is_group_appointment = self.is_group_appointment

        max_participants: int | None | Unset
        if isinstance(self.max_participants, Unset):
            max_participants = UNSET
        else:
            max_participants = self.max_participants

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        recurrence_pattern_id: None | str | Unset
        if isinstance(self.recurrence_pattern_id, Unset):
            recurrence_pattern_id = UNSET
        elif isinstance(self.recurrence_pattern_id, UUID):
            recurrence_pattern_id = str(self.recurrence_pattern_id)
        else:
            recurrence_pattern_id = self.recurrence_pattern_id

        series_id: None | str | Unset
        if isinstance(self.series_id, Unset):
            series_id = UNSET
        elif isinstance(self.series_id, UUID):
            series_id = str(self.series_id)
        else:
            series_id = self.series_id

        series_index: int | None | Unset
        if isinstance(self.series_index, Unset):
            series_index = UNSET
        else:
            series_index = self.series_index

        email_notifications: bool | None | Unset
        if isinstance(self.email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = self.email_notifications

        sms_notifications: bool | None | Unset
        if isinstance(self.sms_notifications, Unset):
            sms_notifications = UNSET
        else:
            sms_notifications = self.sms_notifications

        voice_notifications: bool | None | Unset
        if isinstance(self.voice_notifications, Unset):
            voice_notifications = UNSET
        else:
            voice_notifications = self.voice_notifications

        notes_session_ids: list[str] | Unset = UNSET
        if not isinstance(self.notes_session_ids, Unset):
            notes_session_ids = []
            for notes_session_ids_item_data in self.notes_session_ids:
                notes_session_ids_item = str(notes_session_ids_item_data)
                notes_session_ids.append(notes_session_ids_item)

        class_session_id: None | str | Unset
        if isinstance(self.class_session_id, Unset):
            class_session_id = UNSET
        elif isinstance(self.class_session_id, UUID):
            class_session_id = str(self.class_session_id)
        else:
            class_session_id = self.class_session_id

        self_reschedule_count: int | None | Unset
        if isinstance(self.self_reschedule_count, Unset):
            self_reschedule_count = UNSET
        else:
            self_reschedule_count = self.self_reschedule_count

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        elif isinstance(self.location_id, UUID):
            location_id = str(self.location_id)
        else:
            location_id = self.location_id

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

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
                "status": status,
            }
        )
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if clinician_id is not UNSET:
            field_dict["clinician_id"] = clinician_id
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if venue_type is not UNSET:
            field_dict["venue_type"] = venue_type
        if venue_details is not UNSET:
            field_dict["venue_details"] = venue_details
        if booking_source is not UNSET:
            field_dict["booking_source"] = booking_source
        if patient_notes is not UNSET:
            field_dict["patient_notes"] = patient_notes
        if clinic_notes is not UNSET:
            field_dict["clinic_notes"] = clinic_notes
        if symptoms_description is not UNSET:
            field_dict["symptoms_description"] = symptoms_description
        if urgency_level is not UNSET:
            field_dict["urgency_level"] = urgency_level
        if ai_category is not UNSET:
            field_dict["ai_category"] = ai_category
        if ai_priority_score is not UNSET:
            field_dict["ai_priority_score"] = ai_priority_score
        if ai_suggested_duration is not UNSET:
            field_dict["ai_suggested_duration"] = ai_suggested_duration
        if predicted_show_probability is not UNSET:
            field_dict["predicted_show_probability"] = predicted_show_probability
        if confirmation_sent_at is not UNSET:
            field_dict["confirmation_sent_at"] = confirmation_sent_at
        if confirmation_method is not UNSET:
            field_dict["confirmation_method"] = confirmation_method
        if reminder_sent_at is not UNSET:
            field_dict["reminder_sent_at"] = reminder_sent_at
        if reminder_method is not UNSET:
            field_dict["reminder_method"] = reminder_method
        if reminder_sent is not UNSET:
            field_dict["reminder_sent"] = reminder_sent
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_amount is not UNSET:
            field_dict["payment_amount"] = payment_amount
        if payment_due_date is not UNSET:
            field_dict["payment_due_date"] = payment_due_date
        if amount_paid is not UNSET:
            field_dict["amount_paid"] = amount_paid
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id
        if confirmation_code is not UNSET:
            field_dict["confirmation_code"] = confirmation_code
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if is_group_appointment is not UNSET:
            field_dict["is_group_appointment"] = is_group_appointment
        if max_participants is not UNSET:
            field_dict["max_participants"] = max_participants
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if recurrence_pattern_id is not UNSET:
            field_dict["recurrence_pattern_id"] = recurrence_pattern_id
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if series_index is not UNSET:
            field_dict["series_index"] = series_index
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if sms_notifications is not UNSET:
            field_dict["sms_notifications"] = sms_notifications
        if voice_notifications is not UNSET:
            field_dict["voice_notifications"] = voice_notifications
        if notes_session_ids is not UNSET:
            field_dict["notes_session_ids"] = notes_session_ids
        if class_session_id is not UNSET:
            field_dict["class_session_id"] = class_session_id
        if self_reschedule_count is not UNSET:
            field_dict["self_reschedule_count"] = self_reschedule_count
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if participants is not UNSET:
            field_dict["participants"] = participants
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appointment_participant import AppointmentParticipant  # noqa: PLC0415
        from ..models.appointment_venue_details_type_0 import AppointmentVenueDetailsType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = AppointmentStatus(d.pop("status"))

        def _parse_patient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patient_id_type_0 = UUID(data)

                return patient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        patient_id = _parse_patient_id(d.pop("patient_id", UNSET))

        def _parse_service_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_id_type_0 = UUID(data)

                return service_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        service_id = _parse_service_id(d.pop("service_id", UNSET))

        def _parse_clinician_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinician_id_type_0 = UUID(data)

                return clinician_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clinician_id = _parse_clinician_id(d.pop("clinician_id", UNSET))

        def _parse_start_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_at_type_0 = datetime.datetime.fromisoformat(data)

                return start_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_at = _parse_start_at(d.pop("start_at", UNSET))

        def _parse_end_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = datetime.datetime.fromisoformat(data)

                return end_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_at = _parse_end_at(d.pop("end_at", UNSET))

        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("duration_minutes", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_venue_type(
            data: object,
        ) -> AppointmentVenueTypeType1 | AppointmentVenueTypeType2Type1 | AppointmentVenueTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                venue_type_type_1 = AppointmentVenueTypeType1(data)

                return venue_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                venue_type_type_2_type_1 = AppointmentVenueTypeType2Type1(data)

                return venue_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                venue_type_type_3_type_1 = AppointmentVenueTypeType3Type1(data)

                return venue_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AppointmentVenueTypeType1
                | AppointmentVenueTypeType2Type1
                | AppointmentVenueTypeType3Type1
                | None
                | Unset,
                data,
            )

        venue_type = _parse_venue_type(d.pop("venue_type", UNSET))

        def _parse_venue_details(data: object) -> AppointmentVenueDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                venue_details_type_0 = AppointmentVenueDetailsType0.from_dict(data)

                return venue_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppointmentVenueDetailsType0 | None | Unset, data)

        venue_details = _parse_venue_details(d.pop("venue_details", UNSET))

        def _parse_booking_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_source = _parse_booking_source(d.pop("booking_source", UNSET))

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

        def _parse_urgency_level(
            data: object,
        ) -> (
            AppointmentUrgencyLevelType1
            | AppointmentUrgencyLevelType2Type1
            | AppointmentUrgencyLevelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                urgency_level_type_1 = AppointmentUrgencyLevelType1(data)

                return urgency_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                urgency_level_type_2_type_1 = AppointmentUrgencyLevelType2Type1(data)

                return urgency_level_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                urgency_level_type_3_type_1 = AppointmentUrgencyLevelType3Type1(data)

                return urgency_level_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AppointmentUrgencyLevelType1
                | AppointmentUrgencyLevelType2Type1
                | AppointmentUrgencyLevelType3Type1
                | None
                | Unset,
                data,
            )

        urgency_level = _parse_urgency_level(d.pop("urgency_level", UNSET))

        def _parse_ai_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_category = _parse_ai_category(d.pop("ai_category", UNSET))

        def _parse_ai_priority_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ai_priority_score = _parse_ai_priority_score(d.pop("ai_priority_score", UNSET))

        def _parse_ai_suggested_duration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ai_suggested_duration = _parse_ai_suggested_duration(d.pop("ai_suggested_duration", UNSET))

        def _parse_predicted_show_probability(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        predicted_show_probability = _parse_predicted_show_probability(d.pop("predicted_show_probability", UNSET))

        def _parse_confirmation_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmation_sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return confirmation_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmation_sent_at = _parse_confirmation_sent_at(d.pop("confirmation_sent_at", UNSET))

        def _parse_confirmation_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_method = _parse_confirmation_method(d.pop("confirmation_method", UNSET))

        def _parse_reminder_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reminder_sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return reminder_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reminder_sent_at = _parse_reminder_sent_at(d.pop("reminder_sent_at", UNSET))

        def _parse_reminder_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reminder_method = _parse_reminder_method(d.pop("reminder_method", UNSET))

        def _parse_reminder_sent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reminder_sent = _parse_reminder_sent(d.pop("reminder_sent", UNSET))

        def _parse_payment_status(
            data: object,
        ) -> (
            AppointmentPaymentStatusType1
            | AppointmentPaymentStatusType2Type1
            | AppointmentPaymentStatusType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_status_type_1 = AppointmentPaymentStatusType1(data)

                return payment_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_status_type_2_type_1 = AppointmentPaymentStatusType2Type1(data)

                return payment_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_status_type_3_type_1 = AppointmentPaymentStatusType3Type1(data)

                return payment_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AppointmentPaymentStatusType1
                | AppointmentPaymentStatusType2Type1
                | AppointmentPaymentStatusType3Type1
                | None
                | Unset,
                data,
            )

        payment_status = _parse_payment_status(d.pop("payment_status", UNSET))

        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("payment_method", UNSET))

        def _parse_payment_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payment_amount = _parse_payment_amount(d.pop("payment_amount", UNSET))

        def _parse_payment_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_due_date_type_0 = datetime.date.fromisoformat(data)

                return payment_due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        payment_due_date = _parse_payment_due_date(d.pop("payment_due_date", UNSET))

        def _parse_amount_paid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_paid = _parse_amount_paid(d.pop("amount_paid", UNSET))

        def _parse_payment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_id = _parse_payment_id(d.pop("payment_id", UNSET))

        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmation_code", UNSET))

        def _parse_cancellation_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellation_reason", UNSET))

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

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_is_group_appointment(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_group_appointment = _parse_is_group_appointment(d.pop("is_group_appointment", UNSET))

        def _parse_max_participants(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_participants = _parse_max_participants(d.pop("max_participants", UNSET))

        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("group_name", UNSET))

        def _parse_recurrence_pattern_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recurrence_pattern_id_type_0 = UUID(data)

                return recurrence_pattern_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recurrence_pattern_id = _parse_recurrence_pattern_id(d.pop("recurrence_pattern_id", UNSET))

        def _parse_series_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                series_id_type_0 = UUID(data)

                return series_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        series_id = _parse_series_id(d.pop("series_id", UNSET))

        def _parse_series_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        series_index = _parse_series_index(d.pop("series_index", UNSET))

        def _parse_email_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_notifications = _parse_email_notifications(d.pop("email_notifications", UNSET))

        def _parse_sms_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sms_notifications = _parse_sms_notifications(d.pop("sms_notifications", UNSET))

        def _parse_voice_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        voice_notifications = _parse_voice_notifications(d.pop("voice_notifications", UNSET))

        _notes_session_ids = d.pop("notes_session_ids", UNSET)
        notes_session_ids: list[UUID] | Unset = UNSET
        if _notes_session_ids is not UNSET:
            notes_session_ids = []
            for notes_session_ids_item_data in _notes_session_ids:
                notes_session_ids_item = UUID(notes_session_ids_item_data)

                notes_session_ids.append(notes_session_ids_item)

        def _parse_class_session_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                class_session_id_type_0 = UUID(data)

                return class_session_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        class_session_id = _parse_class_session_id(d.pop("class_session_id", UNSET))

        def _parse_self_reschedule_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        self_reschedule_count = _parse_self_reschedule_count(d.pop("self_reschedule_count", UNSET))

        def _parse_location_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_id_type_0 = UUID(data)

                return location_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        _participants = d.pop("participants", UNSET)
        participants: list[AppointmentParticipant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = AppointmentParticipant.from_dict(participants_item_data)

                participants.append(participants_item)

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

        appointment = cls(
            id=id,
            status=status,
            patient_id=patient_id,
            service_id=service_id,
            clinician_id=clinician_id,
            start_at=start_at,
            end_at=end_at,
            duration_minutes=duration_minutes,
            timezone=timezone,
            venue_type=venue_type,
            venue_details=venue_details,
            booking_source=booking_source,
            patient_notes=patient_notes,
            clinic_notes=clinic_notes,
            symptoms_description=symptoms_description,
            urgency_level=urgency_level,
            ai_category=ai_category,
            ai_priority_score=ai_priority_score,
            ai_suggested_duration=ai_suggested_duration,
            predicted_show_probability=predicted_show_probability,
            confirmation_sent_at=confirmation_sent_at,
            confirmation_method=confirmation_method,
            reminder_sent_at=reminder_sent_at,
            reminder_method=reminder_method,
            reminder_sent=reminder_sent,
            payment_status=payment_status,
            payment_method=payment_method,
            payment_amount=payment_amount,
            payment_due_date=payment_due_date,
            amount_paid=amount_paid,
            payment_id=payment_id,
            confirmation_code=confirmation_code,
            cancellation_reason=cancellation_reason,
            cancelled_at=cancelled_at,
            completed_at=completed_at,
            is_group_appointment=is_group_appointment,
            max_participants=max_participants,
            group_name=group_name,
            recurrence_pattern_id=recurrence_pattern_id,
            series_id=series_id,
            series_index=series_index,
            email_notifications=email_notifications,
            sms_notifications=sms_notifications,
            voice_notifications=voice_notifications,
            notes_session_ids=notes_session_ids,
            class_session_id=class_session_id,
            self_reschedule_count=self_reschedule_count,
            location_id=location_id,
            participants=participants,
            created_at=created_at,
            updated_at=updated_at,
        )

        appointment.additional_properties = d
        return appointment

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
