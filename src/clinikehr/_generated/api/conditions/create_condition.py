from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.condition_create import ConditionCreate
from ...models.create_condition_response_202 import CreateConditionResponse202
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: ConditionCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/conditions".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateConditionResponse202 | Problem | None:
    if response.status_code == 202:
        response_202 = CreateConditionResponse202.from_dict(response.json())

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
) -> Response[CreateConditionResponse202 | Problem]:
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
    body: ConditionCreate,
    idempotency_key: str,
) -> Response[CreateConditionResponse202 | Problem]:
    """Submit a condition for a clinician to confirm.

     The condition is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not in the problem list until a clinician confirms it. The `Idempotency-Key`
    header is REQUIRED — a retry with the same key returns the original submission, never a second one.
    Send `client_reference` to tie the record to your own id. Also accepts a FHIR R4 Condition body
    (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (ConditionCreate): An outside condition, submitted for a clinician to confirm. It
            does not enter the problem list until then. `code` and `code_system` go together.
            `client_reference` (your own id for the record, up to 200 characters) makes a second
            submission of the same record with different content a `client_reference_conflict`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConditionResponse202 | Problem]
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
    body: ConditionCreate,
    idempotency_key: str,
) -> CreateConditionResponse202 | Problem | None:
    """Submit a condition for a clinician to confirm.

     The condition is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not in the problem list until a clinician confirms it. The `Idempotency-Key`
    header is REQUIRED — a retry with the same key returns the original submission, never a second one.
    Send `client_reference` to tie the record to your own id. Also accepts a FHIR R4 Condition body
    (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (ConditionCreate): An outside condition, submitted for a clinician to confirm. It
            does not enter the problem list until then. `code` and `code_system` go together.
            `client_reference` (your own id for the record, up to 200 characters) makes a second
            submission of the same record with different content a `client_reference_conflict`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConditionResponse202 | Problem
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
    body: ConditionCreate,
    idempotency_key: str,
) -> Response[CreateConditionResponse202 | Problem]:
    """Submit a condition for a clinician to confirm.

     The condition is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not in the problem list until a clinician confirms it. The `Idempotency-Key`
    header is REQUIRED — a retry with the same key returns the original submission, never a second one.
    Send `client_reference` to tie the record to your own id. Also accepts a FHIR R4 Condition body
    (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (ConditionCreate): An outside condition, submitted for a clinician to confirm. It
            does not enter the problem list until then. `code` and `code_system` go together.
            `client_reference` (your own id for the record, up to 200 characters) makes a second
            submission of the same record with different content a `client_reference_conflict`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConditionResponse202 | Problem]
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
    body: ConditionCreate,
    idempotency_key: str,
) -> CreateConditionResponse202 | Problem | None:
    """Submit a condition for a clinician to confirm.

     The condition is held for review and answers 202 Accepted with a `Location` header pointing at the
    submission; it is not in the problem list until a clinician confirms it. The `Idempotency-Key`
    header is REQUIRED — a retry with the same key returns the original submission, never a second one.
    Send `client_reference` to tie the record to your own id. Also accepts a FHIR R4 Condition body
    (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (ConditionCreate): An outside condition, submitted for a clinician to confirm. It
            does not enter the problem list until then. `code` and `code_system` go together.
            `client_reference` (your own id for the record, up to 200 characters) makes a second
            submission of the same record with different content a `client_reference_conflict`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConditionResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
