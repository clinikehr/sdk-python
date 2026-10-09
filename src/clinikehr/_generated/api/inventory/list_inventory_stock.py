import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_inventory_stock_response_200 import ListInventoryStockResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    location_id: UUID | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    expiring_before: datetime.date | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_location_id: str | Unset = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = str(location_id)
    params["location_id"] = json_location_id

    json_item_id: str | Unset = UNSET
    if not isinstance(item_id, Unset):
        json_item_id = str(item_id)
    params["item_id"] = json_item_id

    json_expiring_before: str | Unset = UNSET
    if not isinstance(expiring_before, Unset):
        json_expiring_before = expiring_before.isoformat()
    params["expiring_before"] = json_expiring_before

    params["limit"] = limit

    params["starting_after"] = starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/inventory/stock".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListInventoryStockResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListInventoryStockResponse200.from_dict(response.json())

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
) -> Response[ListInventoryStockResponse200 | Problem]:
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
    location_id: UUID | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    expiring_before: datetime.date | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> Response[ListInventoryStockResponse200 | Problem]:
    """Exact quantities per location and lot.

     For a workspace TEST key this reads the workspace's seeded synthetic sandbox stock, never a real
    clinic's — same shape either way.

    Args:
        clinic_id (UUID):
        location_id (UUID | Unset):
        item_id (UUID | Unset):
        expiring_before (datetime.date | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInventoryStockResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        location_id=location_id,
        item_id=item_id,
        expiring_before=expiring_before,
        limit=limit,
        starting_after=starting_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    location_id: UUID | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    expiring_before: datetime.date | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> ListInventoryStockResponse200 | Problem | None:
    """Exact quantities per location and lot.

     For a workspace TEST key this reads the workspace's seeded synthetic sandbox stock, never a real
    clinic's — same shape either way.

    Args:
        clinic_id (UUID):
        location_id (UUID | Unset):
        item_id (UUID | Unset):
        expiring_before (datetime.date | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInventoryStockResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        location_id=location_id,
        item_id=item_id,
        expiring_before=expiring_before,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    location_id: UUID | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    expiring_before: datetime.date | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> Response[ListInventoryStockResponse200 | Problem]:
    """Exact quantities per location and lot.

     For a workspace TEST key this reads the workspace's seeded synthetic sandbox stock, never a real
    clinic's — same shape either way.

    Args:
        clinic_id (UUID):
        location_id (UUID | Unset):
        item_id (UUID | Unset):
        expiring_before (datetime.date | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInventoryStockResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        location_id=location_id,
        item_id=item_id,
        expiring_before=expiring_before,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    location_id: UUID | Unset = UNSET,
    item_id: UUID | Unset = UNSET,
    expiring_before: datetime.date | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> ListInventoryStockResponse200 | Problem | None:
    """Exact quantities per location and lot.

     For a workspace TEST key this reads the workspace's seeded synthetic sandbox stock, never a real
    clinic's — same shape either way.

    Args:
        clinic_id (UUID):
        location_id (UUID | Unset):
        item_id (UUID | Unset):
        expiring_before (datetime.date | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInventoryStockResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            location_id=location_id,
            item_id=item_id,
            expiring_before=expiring_before,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
