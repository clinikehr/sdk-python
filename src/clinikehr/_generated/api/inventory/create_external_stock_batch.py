from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_stock_batch_create_request import ExternalStockBatchCreateRequest
from ...models.external_stock_batch_result import ExternalStockBatchResult
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: ExternalStockBatchCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/inventory/external-stock/batches".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExternalStockBatchResult | Problem | None:
    if response.status_code == 200:
        response_200 = ExternalStockBatchResult.from_dict(response.json())

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
) -> Response[ExternalStockBatchResult | Problem]:
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
    body: ExternalStockBatchCreateRequest,
) -> Response[ExternalStockBatchResult | Problem]:
    """Upload a batch of external stock quantities/bands for a pharmacy selling through another till.

     Clinic-owned key only — an organization never pushes a clinic's own stock. batch_id doubles as the
    idempotency key (a replay of an already-processed batch returns the stored result, never
    reprocesses). Unmatched rows are counted, never guessed at, never written. A structurally invalid or
    suspiciously-shrunk batch is rejected (409) — nothing is written to the mirror.

    Args:
        clinic_id (UUID):
        body (ExternalStockBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalStockBatchResult | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExternalStockBatchCreateRequest,
) -> ExternalStockBatchResult | Problem | None:
    """Upload a batch of external stock quantities/bands for a pharmacy selling through another till.

     Clinic-owned key only — an organization never pushes a clinic's own stock. batch_id doubles as the
    idempotency key (a replay of an already-processed batch returns the stored result, never
    reprocesses). Unmatched rows are counted, never guessed at, never written. A structurally invalid or
    suspiciously-shrunk batch is rejected (409) — nothing is written to the mirror.

    Args:
        clinic_id (UUID):
        body (ExternalStockBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalStockBatchResult | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExternalStockBatchCreateRequest,
) -> Response[ExternalStockBatchResult | Problem]:
    """Upload a batch of external stock quantities/bands for a pharmacy selling through another till.

     Clinic-owned key only — an organization never pushes a clinic's own stock. batch_id doubles as the
    idempotency key (a replay of an already-processed batch returns the stored result, never
    reprocesses). Unmatched rows are counted, never guessed at, never written. A structurally invalid or
    suspiciously-shrunk batch is rejected (409) — nothing is written to the mirror.

    Args:
        clinic_id (UUID):
        body (ExternalStockBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalStockBatchResult | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ExternalStockBatchCreateRequest,
) -> ExternalStockBatchResult | Problem | None:
    """Upload a batch of external stock quantities/bands for a pharmacy selling through another till.

     Clinic-owned key only — an organization never pushes a clinic's own stock. batch_id doubles as the
    idempotency key (a replay of an already-processed batch returns the stored result, never
    reprocesses). Unmatched rows are counted, never guessed at, never written. A structurally invalid or
    suspiciously-shrunk batch is rejected (409) — nothing is written to the mirror.

    Args:
        clinic_id (UUID):
        body (ExternalStockBatchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalStockBatchResult | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
        )
    ).parsed
