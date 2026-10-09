from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_encounter_response_201 import CreateEncounterResponse201
from ...models.encounter_create import EncounterCreate
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: EncounterCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/encounters".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateEncounterResponse201 | Problem | None:
    if response.status_code == 201:
        response_201 = CreateEncounterResponse201.from_dict(response.json())

        return response_201

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
) -> Response[CreateEncounterResponse201 | Problem]:
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
    body: EncounterCreate,
    idempotency_key: str,
) -> Response[CreateEncounterResponse201 | Problem]:
    """Open a visit as a draft note.

     Opens a visit for a patient as a DRAFT note a clinician completes, and answers 201 Created with the
    encounter (`status: draft`, `review_status: pending`). Nothing is ordered, prescribed, signed,
    locked or billed, and no note text can be sent; the draft appears in the clinic's consultation list
    for a clinician to finish. A restricted patient is a 404. The `Idempotency-Key` header is REQUIRED —
    a retry with the same key returns the original encounter, never a second draft. Send JSON; a FHIR
    Encounter body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (EncounterCreate): A visit to open for a patient. It opens a DRAFT note for a
            clinician to complete: nothing is ordered, prescribed, signed, locked or billed, and no
            note text can be sent (there is no field for it). The draft appears in the clinic's
            consultation list for the clinician to finish. `clinician_id` must be a clinician the
            clinic lists (see `GET …/note-clinicians`). The `Idempotency-Key` header is REQUIRED. Send
            JSON; a FHIR Encounter body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEncounterResponse201 | Problem]
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
    body: EncounterCreate,
    idempotency_key: str,
) -> CreateEncounterResponse201 | Problem | None:
    """Open a visit as a draft note.

     Opens a visit for a patient as a DRAFT note a clinician completes, and answers 201 Created with the
    encounter (`status: draft`, `review_status: pending`). Nothing is ordered, prescribed, signed,
    locked or billed, and no note text can be sent; the draft appears in the clinic's consultation list
    for a clinician to finish. A restricted patient is a 404. The `Idempotency-Key` header is REQUIRED —
    a retry with the same key returns the original encounter, never a second draft. Send JSON; a FHIR
    Encounter body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (EncounterCreate): A visit to open for a patient. It opens a DRAFT note for a
            clinician to complete: nothing is ordered, prescribed, signed, locked or billed, and no
            note text can be sent (there is no field for it). The draft appears in the clinic's
            consultation list for the clinician to finish. `clinician_id` must be a clinician the
            clinic lists (see `GET …/note-clinicians`). The `Idempotency-Key` header is REQUIRED. Send
            JSON; a FHIR Encounter body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEncounterResponse201 | Problem
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
    body: EncounterCreate,
    idempotency_key: str,
) -> Response[CreateEncounterResponse201 | Problem]:
    """Open a visit as a draft note.

     Opens a visit for a patient as a DRAFT note a clinician completes, and answers 201 Created with the
    encounter (`status: draft`, `review_status: pending`). Nothing is ordered, prescribed, signed,
    locked or billed, and no note text can be sent; the draft appears in the clinic's consultation list
    for a clinician to finish. A restricted patient is a 404. The `Idempotency-Key` header is REQUIRED —
    a retry with the same key returns the original encounter, never a second draft. Send JSON; a FHIR
    Encounter body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (EncounterCreate): A visit to open for a patient. It opens a DRAFT note for a
            clinician to complete: nothing is ordered, prescribed, signed, locked or billed, and no
            note text can be sent (there is no field for it). The draft appears in the clinic's
            consultation list for the clinician to finish. `clinician_id` must be a clinician the
            clinic lists (see `GET …/note-clinicians`). The `Idempotency-Key` header is REQUIRED. Send
            JSON; a FHIR Encounter body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEncounterResponse201 | Problem]
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
    body: EncounterCreate,
    idempotency_key: str,
) -> CreateEncounterResponse201 | Problem | None:
    """Open a visit as a draft note.

     Opens a visit for a patient as a DRAFT note a clinician completes, and answers 201 Created with the
    encounter (`status: draft`, `review_status: pending`). Nothing is ordered, prescribed, signed,
    locked or billed, and no note text can be sent; the draft appears in the clinic's consultation list
    for a clinician to finish. A restricted patient is a 404. The `Idempotency-Key` header is REQUIRED —
    a retry with the same key returns the original encounter, never a second draft. Send JSON; a FHIR
    Encounter body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (EncounterCreate): A visit to open for a patient. It opens a DRAFT note for a
            clinician to complete: nothing is ordered, prescribed, signed, locked or billed, and no
            note text can be sent (there is no field for it). The draft appears in the clinic's
            consultation list for the clinician to finish. `clinician_id` must be a clinician the
            clinic lists (see `GET …/note-clinicians`). The `Idempotency-Key` header is REQUIRED. Send
            JSON; a FHIR Encounter body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEncounterResponse201 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
