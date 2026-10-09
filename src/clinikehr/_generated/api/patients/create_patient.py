from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_patient_response_200 import CreatePatientResponse200
from ...models.patient_create_request import PatientCreateRequest
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: PatientCreateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/patients".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatePatientResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = CreatePatientResponse200.from_dict(response.json())

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
) -> Response[CreatePatientResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientCreateRequest,
    idempotency_key: str,
) -> Response[CreatePatientResponse200 | Problem]:
    """Create a patient. Possible duplicates are flagged for staff review, never silently merged or
    refused.

     run_automations defaults false, suppressing the patient.created Agent Studio dispatch.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (PatientCreateRequest): Unknown top-level fields, and every named read-only field
            (mrn, portal_access_enabled, admission_status, client_status, insurance, pharmacies,
            care_providers, couple, profile_image, notification_settings — the last refused with the
            distinct code notification_settings_not_writable), are refused BY NAME, never silently
            dropped — enforced by the database, not this schema. `allergies`, `current_medications`
            and `chronic_conditions` are not accepted here either: they are the clinic's reviewed
            clinical record, so they are refused by name. Send allergies to `createAllergy` and
            conditions to `createCondition`; each is held for a clinician to confirm. They are still
            returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePatientResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientCreateRequest,
    idempotency_key: str,
) -> CreatePatientResponse200 | Problem | None:
    """Create a patient. Possible duplicates are flagged for staff review, never silently merged or
    refused.

     run_automations defaults false, suppressing the patient.created Agent Studio dispatch.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (PatientCreateRequest): Unknown top-level fields, and every named read-only field
            (mrn, portal_access_enabled, admission_status, client_status, insurance, pharmacies,
            care_providers, couple, profile_image, notification_settings — the last refused with the
            distinct code notification_settings_not_writable), are refused BY NAME, never silently
            dropped — enforced by the database, not this schema. `allergies`, `current_medications`
            and `chronic_conditions` are not accepted here either: they are the clinic's reviewed
            clinical record, so they are refused by name. Send allergies to `createAllergy` and
            conditions to `createCondition`; each is held for a clinician to confirm. They are still
            returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePatientResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientCreateRequest,
    idempotency_key: str,
) -> Response[CreatePatientResponse200 | Problem]:
    """Create a patient. Possible duplicates are flagged for staff review, never silently merged or
    refused.

     run_automations defaults false, suppressing the patient.created Agent Studio dispatch.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (PatientCreateRequest): Unknown top-level fields, and every named read-only field
            (mrn, portal_access_enabled, admission_status, client_status, insurance, pharmacies,
            care_providers, couple, profile_image, notification_settings — the last refused with the
            distinct code notification_settings_not_writable), are refused BY NAME, never silently
            dropped — enforced by the database, not this schema. `allergies`, `current_medications`
            and `chronic_conditions` are not accepted here either: they are the clinic's reviewed
            clinical record, so they are refused by name. Send allergies to `createAllergy` and
            conditions to `createCondition`; each is held for a clinician to confirm. They are still
            returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePatientResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientCreateRequest,
    idempotency_key: str,
) -> CreatePatientResponse200 | Problem | None:
    """Create a patient. Possible duplicates are flagged for staff review, never silently merged or
    refused.

     run_automations defaults false, suppressing the patient.created Agent Studio dispatch.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (PatientCreateRequest): Unknown top-level fields, and every named read-only field
            (mrn, portal_access_enabled, admission_status, client_status, insurance, pharmacies,
            care_providers, couple, profile_image, notification_settings — the last refused with the
            distinct code notification_settings_not_writable), are refused BY NAME, never silently
            dropped — enforced by the database, not this schema. `allergies`, `current_medications`
            and `chronic_conditions` are not accepted here either: they are the clinic's reviewed
            clinical record, so they are refused by name. Send allergies to `createAllergy` and
            conditions to `createCondition`; each is held for a clinician to confirm. They are still
            returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePatientResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
