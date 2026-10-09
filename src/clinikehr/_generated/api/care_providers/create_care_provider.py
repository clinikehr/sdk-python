from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.care_provider_create import CareProviderCreate
from ...models.create_care_provider_response_201 import CreateCareProviderResponse201
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: CareProviderCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/care-providers".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateCareProviderResponse201 | Problem | None:
    if response.status_code == 201:
        response_201 = CreateCareProviderResponse201.from_dict(response.json())

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
) -> Response[CreateCareProviderResponse201 | Problem]:
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
    body: CareProviderCreate,
    idempotency_key: str,
) -> Response[CreateCareProviderResponse201 | Problem]:
    """Add an outside care provider to a patient.

     Saved straight away and visible on the patient's record: answers 201 Created with the contact. If
    `is_primary` is true, the patient's other contacts of the same `type` stop being primary. The
    `Idempotency-Key` header is REQUIRED — a retry with the same key returns the original contact, never
    a second one. Contact notes cannot be sent. Only the contacts an app adds can later be changed or
    removed by that app.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CareProviderCreate): An outside care provider to add to a patient. Saved straight
            away. If `is_primary` is true, the patient's other contacts of the same `type` stop being
            primary. `npi` is ten digits (its shape is checked, not its check digit). The clinic's
            notes on a contact cannot be sent. The `Idempotency-Key` header is REQUIRED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCareProviderResponse201 | Problem]
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
    body: CareProviderCreate,
    idempotency_key: str,
) -> CreateCareProviderResponse201 | Problem | None:
    """Add an outside care provider to a patient.

     Saved straight away and visible on the patient's record: answers 201 Created with the contact. If
    `is_primary` is true, the patient's other contacts of the same `type` stop being primary. The
    `Idempotency-Key` header is REQUIRED — a retry with the same key returns the original contact, never
    a second one. Contact notes cannot be sent. Only the contacts an app adds can later be changed or
    removed by that app.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CareProviderCreate): An outside care provider to add to a patient. Saved straight
            away. If `is_primary` is true, the patient's other contacts of the same `type` stop being
            primary. `npi` is ten digits (its shape is checked, not its check digit). The clinic's
            notes on a contact cannot be sent. The `Idempotency-Key` header is REQUIRED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCareProviderResponse201 | Problem
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
    body: CareProviderCreate,
    idempotency_key: str,
) -> Response[CreateCareProviderResponse201 | Problem]:
    """Add an outside care provider to a patient.

     Saved straight away and visible on the patient's record: answers 201 Created with the contact. If
    `is_primary` is true, the patient's other contacts of the same `type` stop being primary. The
    `Idempotency-Key` header is REQUIRED — a retry with the same key returns the original contact, never
    a second one. Contact notes cannot be sent. Only the contacts an app adds can later be changed or
    removed by that app.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CareProviderCreate): An outside care provider to add to a patient. Saved straight
            away. If `is_primary` is true, the patient's other contacts of the same `type` stop being
            primary. `npi` is ten digits (its shape is checked, not its check digit). The clinic's
            notes on a contact cannot be sent. The `Idempotency-Key` header is REQUIRED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCareProviderResponse201 | Problem]
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
    body: CareProviderCreate,
    idempotency_key: str,
) -> CreateCareProviderResponse201 | Problem | None:
    """Add an outside care provider to a patient.

     Saved straight away and visible on the patient's record: answers 201 Created with the contact. If
    `is_primary` is true, the patient's other contacts of the same `type` stop being primary. The
    `Idempotency-Key` header is REQUIRED — a retry with the same key returns the original contact, never
    a second one. Contact notes cannot be sent. Only the contacts an app adds can later be changed or
    removed by that app.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (CareProviderCreate): An outside care provider to add to a patient. Saved straight
            away. If `is_primary` is true, the patient's other contacts of the same `type` stop being
            primary. `npi` is ten digits (its shape is checked, not its check digit). The clinic's
            notes on a contact cannot be sent. The `Idempotency-Key` header is REQUIRED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCareProviderResponse201 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
