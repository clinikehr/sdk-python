from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.inventory_lot_write_off_request import InventoryLotWriteOffRequest
from ...models.problem import Problem
from ...models.write_off_inventory_lot_response_200 import WriteOffInventoryLotResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    lot_id: UUID,
    *,
    body: InventoryLotWriteOffRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/inventory/lots/{lot_id}/write-off".format(
            clinic_id=quote(str(clinic_id), safe=""),
            lot_id=quote(str(lot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WriteOffInventoryLotResponse200 | None:
    if response.status_code == 200:
        response_200 = WriteOffInventoryLotResponse200.from_dict(response.json())

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
) -> Response[Problem | WriteOffInventoryLotResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    lot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryLotWriteOffRequest,
    idempotency_key: str,
) -> Response[Problem | WriteOffInventoryLotResponse200]:
    """Write off the remaining stock of one lot, through the ledger. A reason is required.

     Records the lot's remaining quantity as wasted at every location where it is held, then archives the
    lot. The ledger keeps the movement; the lot and its history are never deleted. Send the `reason` in
    the body and an `Idempotency-Key` header. A controlled drug is refused with
    `controlled_drug_not_api_movable` — an API key has no witness identity to offer.

    Args:
        clinic_id (UUID):
        lot_id (UUID):
        idempotency_key (str):
        body (InventoryLotWriteOffRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WriteOffInventoryLotResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        lot_id=lot_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    lot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryLotWriteOffRequest,
    idempotency_key: str,
) -> Problem | WriteOffInventoryLotResponse200 | None:
    """Write off the remaining stock of one lot, through the ledger. A reason is required.

     Records the lot's remaining quantity as wasted at every location where it is held, then archives the
    lot. The ledger keeps the movement; the lot and its history are never deleted. Send the `reason` in
    the body and an `Idempotency-Key` header. A controlled drug is refused with
    `controlled_drug_not_api_movable` — an API key has no witness identity to offer.

    Args:
        clinic_id (UUID):
        lot_id (UUID):
        idempotency_key (str):
        body (InventoryLotWriteOffRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WriteOffInventoryLotResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        lot_id=lot_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    lot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryLotWriteOffRequest,
    idempotency_key: str,
) -> Response[Problem | WriteOffInventoryLotResponse200]:
    """Write off the remaining stock of one lot, through the ledger. A reason is required.

     Records the lot's remaining quantity as wasted at every location where it is held, then archives the
    lot. The ledger keeps the movement; the lot and its history are never deleted. Send the `reason` in
    the body and an `Idempotency-Key` header. A controlled drug is refused with
    `controlled_drug_not_api_movable` — an API key has no witness identity to offer.

    Args:
        clinic_id (UUID):
        lot_id (UUID):
        idempotency_key (str):
        body (InventoryLotWriteOffRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WriteOffInventoryLotResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        lot_id=lot_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    lot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryLotWriteOffRequest,
    idempotency_key: str,
) -> Problem | WriteOffInventoryLotResponse200 | None:
    """Write off the remaining stock of one lot, through the ledger. A reason is required.

     Records the lot's remaining quantity as wasted at every location where it is held, then archives the
    lot. The ledger keeps the movement; the lot and its history are never deleted. Send the `reason` in
    the body and an `Idempotency-Key` header. A controlled drug is refused with
    `controlled_drug_not_api_movable` — an API key has no witness identity to offer.

    Args:
        clinic_id (UUID):
        lot_id (UUID):
        idempotency_key (str):
        body (InventoryLotWriteOffRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WriteOffInventoryLotResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            lot_id=lot_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
