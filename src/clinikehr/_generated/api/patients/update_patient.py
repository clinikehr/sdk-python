from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patient_update_request import PatientUpdateRequest
from ...models.problem import Problem
from ...models.update_patient_response_200 import UpdatePatientResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    patient_id: UUID,
    *,
    body: PatientUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/patients/{patient_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            patient_id=quote(str(patient_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdatePatientResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdatePatientResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UpdatePatientResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    patient_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientUpdateRequest,
) -> Response[Problem | UpdatePatientResponse200]:
    """Update a patient. Absent fields are unchanged; JSON null clears a nullable field.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        body (PatientUpdateRequest): A key ABSENT from the body leaves that field unchanged; a key
            present with JSON null clears it where the column allows null, refused (naming the field)
            where it does not (first_name/last_name can never be cleared). Nested objects
            (next_of_kin/employment/billing) replace as a whole when present. Arrays
            (emails/phones/guardians) replace the set when present. `allergies`, `current_medications`
            and `chronic_conditions` cannot be changed here: they are refused by name. Use
            `createAllergy` / `updateAllergy` and `createCondition` / `updateCondition`, which a
            clinician confirms. They are still returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdatePatientResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    patient_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientUpdateRequest,
) -> Problem | UpdatePatientResponse200 | None:
    """Update a patient. Absent fields are unchanged; JSON null clears a nullable field.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        body (PatientUpdateRequest): A key ABSENT from the body leaves that field unchanged; a key
            present with JSON null clears it where the column allows null, refused (naming the field)
            where it does not (first_name/last_name can never be cleared). Nested objects
            (next_of_kin/employment/billing) replace as a whole when present. Arrays
            (emails/phones/guardians) replace the set when present. `allergies`, `current_medications`
            and `chronic_conditions` cannot be changed here: they are refused by name. Use
            `createAllergy` / `updateAllergy` and `createCondition` / `updateCondition`, which a
            clinician confirms. They are still returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdatePatientResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        patient_id=patient_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    patient_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientUpdateRequest,
) -> Response[Problem | UpdatePatientResponse200]:
    """Update a patient. Absent fields are unchanged; JSON null clears a nullable field.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        body (PatientUpdateRequest): A key ABSENT from the body leaves that field unchanged; a key
            present with JSON null clears it where the column allows null, refused (naming the field)
            where it does not (first_name/last_name can never be cleared). Nested objects
            (next_of_kin/employment/billing) replace as a whole when present. Arrays
            (emails/phones/guardians) replace the set when present. `allergies`, `current_medications`
            and `chronic_conditions` cannot be changed here: they are refused by name. Use
            `createAllergy` / `updateAllergy` and `createCondition` / `updateCondition`, which a
            clinician confirms. They are still returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdatePatientResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    patient_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientUpdateRequest,
) -> Problem | UpdatePatientResponse200 | None:
    """Update a patient. Absent fields are unchanged; JSON null clears a nullable field.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        body (PatientUpdateRequest): A key ABSENT from the body leaves that field unchanged; a key
            present with JSON null clears it where the column allows null, refused (naming the field)
            where it does not (first_name/last_name can never be cleared). Nested objects
            (next_of_kin/employment/billing) replace as a whole when present. Arrays
            (emails/phones/guardians) replace the set when present. `allergies`, `current_medications`
            and `chronic_conditions` cannot be changed here: they are refused by name. Use
            `createAllergy` / `updateAllergy` and `createCondition` / `updateCondition`, which a
            clinician confirms. They are still returned when you read a patient.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdatePatientResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            patient_id=patient_id,
            client=client,
            body=body,
        )
    ).parsed
