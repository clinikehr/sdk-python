from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_inventory_item_response_200 import DeleteInventoryItemResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    item_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/clinics/{clinic_id}/inventory/items/{item_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteInventoryItemResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = DeleteInventoryItemResponse200.from_dict(response.json())

        return response_200

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
) -> Response[DeleteInventoryItemResponse200 | Problem]:
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
) -> Response[DeleteInventoryItemResponse200 | Problem]:
    """Permanently delete an item that has never been used. Anything with history is refused — archive it
    instead.

     Deleting is permanent and only possible for an item that has never been used: no stock, no stock
    history, and not part of any order, count, recipe or dispense. Anything else is refused with
    `item_has_history` (409) — archive the item instead; archiving is reversible and keeps the history.
    No Idempotency-Key is needed: sending the same delete twice returns `404` the second time.

    Args:
        clinic_id (UUID):
        item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInventoryItemResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        item_id=item_id,
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
) -> DeleteInventoryItemResponse200 | Problem | None:
    """Permanently delete an item that has never been used. Anything with history is refused — archive it
    instead.

     Deleting is permanent and only possible for an item that has never been used: no stock, no stock
    history, and not part of any order, count, recipe or dispense. Anything else is refused with
    `item_has_history` (409) — archive the item instead; archiving is reversible and keeps the history.
    No Idempotency-Key is needed: sending the same delete twice returns `404` the second time.

    Args:
        clinic_id (UUID):
        item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInventoryItemResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteInventoryItemResponse200 | Problem]:
    """Permanently delete an item that has never been used. Anything with history is refused — archive it
    instead.

     Deleting is permanent and only possible for an item that has never been used: no stock, no stock
    history, and not part of any order, count, recipe or dispense. Anything else is refused with
    `item_has_history` (409) — archive the item instead; archiving is reversible and keeps the history.
    No Idempotency-Key is needed: sending the same delete twice returns `404` the second time.

    Args:
        clinic_id (UUID):
        item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInventoryItemResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    item_id: UUID,
    *,
    client: AuthenticatedClient,
) -> DeleteInventoryItemResponse200 | Problem | None:
    """Permanently delete an item that has never been used. Anything with history is refused — archive it
    instead.

     Deleting is permanent and only possible for an item that has never been used: no stock, no stock
    history, and not part of any order, count, recipe or dispense. Anything else is refused with
    `item_has_history` (409) — archive the item instead; archiving is reversible and keeps the history.
    No Idempotency-Key is needed: sending the same delete twice returns `404` the second time.

    Args:
        clinic_id (UUID):
        item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInventoryItemResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
