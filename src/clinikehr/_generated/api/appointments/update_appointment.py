from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appointment_update_request import AppointmentUpdateRequest
from ...models.problem import Problem
from ...models.update_appointment_response_200 import UpdateAppointmentResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    body: AppointmentUpdateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/appointments/{appointment_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            appointment_id=quote(str(appointment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateAppointmentResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAppointmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UpdateAppointmentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentUpdateRequest,
    idempotency_key: str,
) -> Response[Problem | UpdateAppointmentResponse200]:
    """Reschedule or update an appointment. Immutable after create — patient_id, service_id, location_id,
    every payment field — are refused if sent.

     A new `start_at` or `clinician_id` is checked exactly as a new booking is (the slot must be free and
    the clinician bookable). Other fields are plain edits; an absent field is unchanged. `status` may
    only move to `confirmed` here; use the cancel route to cancel. A cancelled, completed or no-show
    appointment cannot be changed. With a test key, rescheduling is not available: cancel the sandbox
    appointment and book a new one.

    Who is told. For a live (non-test) appointment that is still booked and in the future, changing
    `start_at`, `clinician_id` or `venue_type` emails the patient and any participants: a new time is a
    reschedule notice, a new clinician or venue is an "Appointment updated" notice. The clinicians
    involved are told in the app and by email: the new clinician that a visit was added, the previous
    clinician that it was removed, or the current clinician that it moved. This follows the clinic's
    appointment notification setting and each clinician's own email setting. With `email_notifications`
    false on the appointment the patient is not emailed, but the clinicians still are. Each later change
    sends its own notice, and the patient's reminder is re-armed for the new time. Test-key appointments
    never send email.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentUpdateRequest): Immutable after create, and refused if sent: patient_id,
            service_id, location_id, every payment field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateAppointmentResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentUpdateRequest,
    idempotency_key: str,
) -> Problem | UpdateAppointmentResponse200 | None:
    """Reschedule or update an appointment. Immutable after create — patient_id, service_id, location_id,
    every payment field — are refused if sent.

     A new `start_at` or `clinician_id` is checked exactly as a new booking is (the slot must be free and
    the clinician bookable). Other fields are plain edits; an absent field is unchanged. `status` may
    only move to `confirmed` here; use the cancel route to cancel. A cancelled, completed or no-show
    appointment cannot be changed. With a test key, rescheduling is not available: cancel the sandbox
    appointment and book a new one.

    Who is told. For a live (non-test) appointment that is still booked and in the future, changing
    `start_at`, `clinician_id` or `venue_type` emails the patient and any participants: a new time is a
    reschedule notice, a new clinician or venue is an "Appointment updated" notice. The clinicians
    involved are told in the app and by email: the new clinician that a visit was added, the previous
    clinician that it was removed, or the current clinician that it moved. This follows the clinic's
    appointment notification setting and each clinician's own email setting. With `email_notifications`
    false on the appointment the patient is not emailed, but the clinicians still are. Each later change
    sends its own notice, and the patient's reminder is re-armed for the new time. Test-key appointments
    never send email.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentUpdateRequest): Immutable after create, and refused if sent: patient_id,
            service_id, location_id, every payment field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateAppointmentResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentUpdateRequest,
    idempotency_key: str,
) -> Response[Problem | UpdateAppointmentResponse200]:
    """Reschedule or update an appointment. Immutable after create — patient_id, service_id, location_id,
    every payment field — are refused if sent.

     A new `start_at` or `clinician_id` is checked exactly as a new booking is (the slot must be free and
    the clinician bookable). Other fields are plain edits; an absent field is unchanged. `status` may
    only move to `confirmed` here; use the cancel route to cancel. A cancelled, completed or no-show
    appointment cannot be changed. With a test key, rescheduling is not available: cancel the sandbox
    appointment and book a new one.

    Who is told. For a live (non-test) appointment that is still booked and in the future, changing
    `start_at`, `clinician_id` or `venue_type` emails the patient and any participants: a new time is a
    reschedule notice, a new clinician or venue is an "Appointment updated" notice. The clinicians
    involved are told in the app and by email: the new clinician that a visit was added, the previous
    clinician that it was removed, or the current clinician that it moved. This follows the clinic's
    appointment notification setting and each clinician's own email setting. With `email_notifications`
    false on the appointment the patient is not emailed, but the clinicians still are. Each later change
    sends its own notice, and the patient's reminder is re-armed for the new time. Test-key appointments
    never send email.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentUpdateRequest): Immutable after create, and refused if sent: patient_id,
            service_id, location_id, every payment field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateAppointmentResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentUpdateRequest,
    idempotency_key: str,
) -> Problem | UpdateAppointmentResponse200 | None:
    """Reschedule or update an appointment. Immutable after create — patient_id, service_id, location_id,
    every payment field — are refused if sent.

     A new `start_at` or `clinician_id` is checked exactly as a new booking is (the slot must be free and
    the clinician bookable). Other fields are plain edits; an absent field is unchanged. `status` may
    only move to `confirmed` here; use the cancel route to cancel. A cancelled, completed or no-show
    appointment cannot be changed. With a test key, rescheduling is not available: cancel the sandbox
    appointment and book a new one.

    Who is told. For a live (non-test) appointment that is still booked and in the future, changing
    `start_at`, `clinician_id` or `venue_type` emails the patient and any participants: a new time is a
    reschedule notice, a new clinician or venue is an "Appointment updated" notice. The clinicians
    involved are told in the app and by email: the new clinician that a visit was added, the previous
    clinician that it was removed, or the current clinician that it moved. This follows the clinic's
    appointment notification setting and each clinician's own email setting. With `email_notifications`
    false on the appointment the patient is not emailed, but the clinicians still are. Each later change
    sends its own notice, and the patient's reminder is re-armed for the new time. Test-key appointments
    never send email.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentUpdateRequest): Immutable after create, and refused if sent: patient_id,
            service_id, location_id, every payment field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateAppointmentResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            appointment_id=appointment_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
