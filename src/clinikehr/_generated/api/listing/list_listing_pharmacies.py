from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_listing_pharmacies_response_200 import ListListingPharmaciesResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["starting_after"] = starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/pharmacies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListListingPharmaciesResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListListingPharmaciesResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListListingPharmaciesResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> Response[ListListingPharmaciesResponse200 | Problem]:
    """Every pharmacy this key's workspace can reach through an active listing connection.

     No clinic in the path — the calling key's organization must hold an ACTIVE connection granting
    listing.profile:read to each returned clinic; a clinic-owned key always gets an empty page. For a
    workspace TEST key this reads the workspace's own seeded fictional pharmacies instead — the same
    shape either way. Never an exact quantity; profile fields only.

    Args:
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListListingPharmaciesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        starting_after=starting_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> ListListingPharmaciesResponse200 | Problem | None:
    """Every pharmacy this key's workspace can reach through an active listing connection.

     No clinic in the path — the calling key's organization must hold an ACTIVE connection granting
    listing.profile:read to each returned clinic; a clinic-owned key always gets an empty page. For a
    workspace TEST key this reads the workspace's own seeded fictional pharmacies instead — the same
    shape either way. Never an exact quantity; profile fields only.

    Args:
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListListingPharmaciesResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> Response[ListListingPharmaciesResponse200 | Problem]:
    """Every pharmacy this key's workspace can reach through an active listing connection.

     No clinic in the path — the calling key's organization must hold an ACTIVE connection granting
    listing.profile:read to each returned clinic; a clinic-owned key always gets an empty page. For a
    workspace TEST key this reads the workspace's own seeded fictional pharmacies instead — the same
    shape either way. Never an exact quantity; profile fields only.

    Args:
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListListingPharmaciesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
) -> ListListingPharmaciesResponse200 | Problem | None:
    """Every pharmacy this key's workspace can reach through an active listing connection.

     No clinic in the path — the calling key's organization must hold an ACTIVE connection granting
    listing.profile:read to each returned clinic; a clinic-owned key always gets an empty page. For a
    workspace TEST key this reads the workspace's own seeded fictional pharmacies instead — the same
    shape either way. Never an exact quantity; profile fields only.

    Args:
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListListingPharmaciesResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
