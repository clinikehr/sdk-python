from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.allergy_create import AllergyCreate
from ...models.create_allergy_response_202 import CreateAllergyResponse202
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: AllergyCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/allergies".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAllergyResponse202 | Problem | None:
    if response.status_code == 202:
        response_202 = CreateAllergyResponse202.from_dict(response.json())

        return response_202

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
) -> Response[CreateAllergyResponse202 | Problem]:
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
    body: AllergyCreate,
    idempotency_key: str,
) -> Response[CreateAllergyResponse202 | Problem]:
    """Submit an allergy for a clinician to confirm.

     The allergy is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not on the chart until a clinician confirms it. The `Idempotency-Key` header is
    REQUIRED - a retry with the same key returns the original submission, never a second one. An allergy
    the patient already has is not refused: it is held for a clinician like any other, who rejects the
    duplicate. JSON only: a FHIR AllergyIntolerance body is not accepted.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (AllergyCreate): An outside allergy, or a "no known allergies" statement, submitted
            for a clinician to confirm. It does not enter the chart until then. To record that the
            patient has no known allergies, send `no_known_allergies: true` INSTEAD of a substance
            (the two cannot be combined); it is also held for a clinician to confirm. Sending `none`
            or similar as a substance is refused. `client_reference` (your own id, up to 200
            characters) makes a second submission of the same record with different content a
            `client_reference_conflict`. An allergy the patient already has is not refused: it is held
            for a clinician like any other.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAllergyResponse202 | Problem]
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
    body: AllergyCreate,
    idempotency_key: str,
) -> CreateAllergyResponse202 | Problem | None:
    """Submit an allergy for a clinician to confirm.

     The allergy is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not on the chart until a clinician confirms it. The `Idempotency-Key` header is
    REQUIRED - a retry with the same key returns the original submission, never a second one. An allergy
    the patient already has is not refused: it is held for a clinician like any other, who rejects the
    duplicate. JSON only: a FHIR AllergyIntolerance body is not accepted.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (AllergyCreate): An outside allergy, or a "no known allergies" statement, submitted
            for a clinician to confirm. It does not enter the chart until then. To record that the
            patient has no known allergies, send `no_known_allergies: true` INSTEAD of a substance
            (the two cannot be combined); it is also held for a clinician to confirm. Sending `none`
            or similar as a substance is refused. `client_reference` (your own id, up to 200
            characters) makes a second submission of the same record with different content a
            `client_reference_conflict`. An allergy the patient already has is not refused: it is held
            for a clinician like any other.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAllergyResponse202 | Problem
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
    body: AllergyCreate,
    idempotency_key: str,
) -> Response[CreateAllergyResponse202 | Problem]:
    """Submit an allergy for a clinician to confirm.

     The allergy is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not on the chart until a clinician confirms it. The `Idempotency-Key` header is
    REQUIRED - a retry with the same key returns the original submission, never a second one. An allergy
    the patient already has is not refused: it is held for a clinician like any other, who rejects the
    duplicate. JSON only: a FHIR AllergyIntolerance body is not accepted.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (AllergyCreate): An outside allergy, or a "no known allergies" statement, submitted
            for a clinician to confirm. It does not enter the chart until then. To record that the
            patient has no known allergies, send `no_known_allergies: true` INSTEAD of a substance
            (the two cannot be combined); it is also held for a clinician to confirm. Sending `none`
            or similar as a substance is refused. `client_reference` (your own id, up to 200
            characters) makes a second submission of the same record with different content a
            `client_reference_conflict`. An allergy the patient already has is not refused: it is held
            for a clinician like any other.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAllergyResponse202 | Problem]
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
    body: AllergyCreate,
    idempotency_key: str,
) -> CreateAllergyResponse202 | Problem | None:
    """Submit an allergy for a clinician to confirm.

     The allergy is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not on the chart until a clinician confirms it. The `Idempotency-Key` header is
    REQUIRED - a retry with the same key returns the original submission, never a second one. An allergy
    the patient already has is not refused: it is held for a clinician like any other, who rejects the
    duplicate. JSON only: a FHIR AllergyIntolerance body is not accepted.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (AllergyCreate): An outside allergy, or a "no known allergies" statement, submitted
            for a clinician to confirm. It does not enter the chart until then. To record that the
            patient has no known allergies, send `no_known_allergies: true` INSTEAD of a substance
            (the two cannot be combined); it is also held for a clinician to confirm. Sending `none`
            or similar as a substance is refused. `client_reference` (your own id, up to 200
            characters) makes a second submission of the same record with different content a
            `client_reference_conflict`. An allergy the patient already has is not refused: it is held
            for a clinician like any other.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAllergyResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
