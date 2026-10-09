from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.coverage_create import CoverageCreate
from ...models.create_coverage_response_201 import CreateCoverageResponse201
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: CoverageCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/coverages".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateCoverageResponse201 | Problem | None:
    if response.status_code == 201:
        response_201 = CreateCoverageResponse201.from_dict(response.json())

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
) -> Response[CreateCoverageResponse201 | Problem]:
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
    body: CoverageCreate,
    idempotency_key: str,
) -> Response[CreateCoverageResponse201 | Problem]:
    """Record a patient's insurance coverage.

     The coverage is saved and visible straight away, answers 201 Created with the coverage, and is
    `unconfirmed` with `coverage_active: false` until clinic staff confirm the payer match. The payer
    must be one the clinic has enabled (`payer_not_enabled` otherwise). A patient can hold one coverage
    per payer (`coverage_exists`). The `Idempotency-Key` header is REQUIRED — a retry with the same key
    returns the original coverage, never a second one. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CoverageCreate): A coverage to record for a patient. It is saved straight away, but
            as `unconfirmed` with `coverage_active: false`; clinic staff confirm the payer match
            before it counts. `payer_id` must be a payer the clinic has enabled in Settings →
            Insurance (see `GET …/payers`), otherwise `payer_not_enabled`; a patient can hold one
            coverage per payer (`coverage_exists`). `coverage_active: true` is refused with
            `activation_requires_staff`. The clinic's notes, the deductible and out-of-pocket amounts
            met and every eligibility field cannot be sent. The `Idempotency-Key` header is REQUIRED.
            Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCoverageResponse201 | Problem]
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
    body: CoverageCreate,
    idempotency_key: str,
) -> CreateCoverageResponse201 | Problem | None:
    """Record a patient's insurance coverage.

     The coverage is saved and visible straight away, answers 201 Created with the coverage, and is
    `unconfirmed` with `coverage_active: false` until clinic staff confirm the payer match. The payer
    must be one the clinic has enabled (`payer_not_enabled` otherwise). A patient can hold one coverage
    per payer (`coverage_exists`). The `Idempotency-Key` header is REQUIRED — a retry with the same key
    returns the original coverage, never a second one. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CoverageCreate): A coverage to record for a patient. It is saved straight away, but
            as `unconfirmed` with `coverage_active: false`; clinic staff confirm the payer match
            before it counts. `payer_id` must be a payer the clinic has enabled in Settings →
            Insurance (see `GET …/payers`), otherwise `payer_not_enabled`; a patient can hold one
            coverage per payer (`coverage_exists`). `coverage_active: true` is refused with
            `activation_requires_staff`. The clinic's notes, the deductible and out-of-pocket amounts
            met and every eligibility field cannot be sent. The `Idempotency-Key` header is REQUIRED.
            Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCoverageResponse201 | Problem
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
    body: CoverageCreate,
    idempotency_key: str,
) -> Response[CreateCoverageResponse201 | Problem]:
    """Record a patient's insurance coverage.

     The coverage is saved and visible straight away, answers 201 Created with the coverage, and is
    `unconfirmed` with `coverage_active: false` until clinic staff confirm the payer match. The payer
    must be one the clinic has enabled (`payer_not_enabled` otherwise). A patient can hold one coverage
    per payer (`coverage_exists`). The `Idempotency-Key` header is REQUIRED — a retry with the same key
    returns the original coverage, never a second one. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CoverageCreate): A coverage to record for a patient. It is saved straight away, but
            as `unconfirmed` with `coverage_active: false`; clinic staff confirm the payer match
            before it counts. `payer_id` must be a payer the clinic has enabled in Settings →
            Insurance (see `GET …/payers`), otherwise `payer_not_enabled`; a patient can hold one
            coverage per payer (`coverage_exists`). `coverage_active: true` is refused with
            `activation_requires_staff`. The clinic's notes, the deductible and out-of-pocket amounts
            met and every eligibility field cannot be sent. The `Idempotency-Key` header is REQUIRED.
            Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCoverageResponse201 | Problem]
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
    body: CoverageCreate,
    idempotency_key: str,
) -> CreateCoverageResponse201 | Problem | None:
    """Record a patient's insurance coverage.

     The coverage is saved and visible straight away, answers 201 Created with the coverage, and is
    `unconfirmed` with `coverage_active: false` until clinic staff confirm the payer match. The payer
    must be one the clinic has enabled (`payer_not_enabled` otherwise). A patient can hold one coverage
    per payer (`coverage_exists`). The `Idempotency-Key` header is REQUIRED — a retry with the same key
    returns the original coverage, never a second one. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CoverageCreate): A coverage to record for a patient. It is saved straight away, but
            as `unconfirmed` with `coverage_active: false`; clinic staff confirm the payer match
            before it counts. `payer_id` must be a payer the clinic has enabled in Settings →
            Insurance (see `GET …/payers`), otherwise `payer_not_enabled`; a patient can hold one
            coverage per payer (`coverage_exists`). `coverage_active: true` is refused with
            `activation_requires_staff`. The clinic's notes, the deductible and out-of-pocket amounts
            met and every eligibility field cannot be sent. The `Idempotency-Key` header is REQUIRED.
            Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCoverageResponse201 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
