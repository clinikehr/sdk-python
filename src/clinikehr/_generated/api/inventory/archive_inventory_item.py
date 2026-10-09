from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_inventory_item_response_200 import ArchiveInventoryItemResponse200
from ...models.inventory_item_archive_request import InventoryItemArchiveRequest
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    item_id: UUID,
    *,
    body: InventoryItemArchiveRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/inventory/items/{item_id}/archive".format(
            clinic_id=quote(str(clinic_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveInventoryItemResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ArchiveInventoryItemResponse200.from_dict(response.json())

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
) -> Response[ArchiveInventoryItemResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryItemArchiveRequest | Unset = UNSET,
) -> Response[ArchiveInventoryItemResponse200 | Problem]:
    """Archive an item. Reversible — refused (item_has_stock) while any stock remains.

     Hides the item from sale and dispensing without erasing anything; use the restore route to bring it
    back. An item that still has stock on hand is refused with `item_has_stock` — move or write off the
    stock first. Archiving an item that is already archived succeeds and changes nothing. An optional
    `reason` is kept with the item. No Idempotency-Key is needed.

    Args:
        clinic_id (UUID):
        item_id (UUID):
        body (InventoryItemArchiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveInventoryItemResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryItemArchiveRequest | Unset = UNSET,
) -> ArchiveInventoryItemResponse200 | Problem | None:
    """Archive an item. Reversible — refused (item_has_stock) while any stock remains.

     Hides the item from sale and dispensing without erasing anything; use the restore route to bring it
    back. An item that still has stock on hand is refused with `item_has_stock` — move or write off the
    stock first. Archiving an item that is already archived succeeds and changes nothing. An optional
    `reason` is kept with the item. No Idempotency-Key is needed.

    Args:
        clinic_id (UUID):
        item_id (UUID):
        body (InventoryItemArchiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveInventoryItemResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryItemArchiveRequest | Unset = UNSET,
) -> Response[ArchiveInventoryItemResponse200 | Problem]:
    """Archive an item. Reversible — refused (item_has_stock) while any stock remains.

     Hides the item from sale and dispensing without erasing anything; use the restore route to bring it
    back. An item that still has stock on hand is refused with `item_has_stock` — move or write off the
    stock first. Archiving an item that is already archived succeeds and changes nothing. An optional
    `reason` is kept with the item. No Idempotency-Key is needed.

    Args:
        clinic_id (UUID):
        item_id (UUID):
        body (InventoryItemArchiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveInventoryItemResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InventoryItemArchiveRequest | Unset = UNSET,
) -> ArchiveInventoryItemResponse200 | Problem | None:
    """Archive an item. Reversible — refused (item_has_stock) while any stock remains.

     Hides the item from sale and dispensing without erasing anything; use the restore route to bring it
    back. An item that still has stock on hand is refused with `item_has_stock` — move or write off the
    stock first. Archiving an item that is already archived succeeds and changes nothing. An optional
    `reason` is kept with the item. No Idempotency-Key is needed.

    Args:
        clinic_id (UUID):
        item_id (UUID):
        body (InventoryItemArchiveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveInventoryItemResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
