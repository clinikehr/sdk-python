from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_connections_response_200 import ListConnectionsResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListConnectionsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListConnectionsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[ListConnectionsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListConnectionsResponse200 | Problem]:
    """Clinics this key can reach, and the scopes granted to it.

     For a workspace TEST key this is always one entry — the workspace's own sandbox, marked sandbox:
    true. For a LIVE workspace key this lists every clinic with an ACTIVE, non-expired connection that
    also still has API access switched on — the same set the key could actually reach on the next call,
    never a stale or pending one. An unverified workspace, or one with no connections yet, gets an empty
    list. A clinic-owned key gets exactly one entry, for its own clinic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectionsResponse200 | Problem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ListConnectionsResponse200 | Problem | None:
    """Clinics this key can reach, and the scopes granted to it.

     For a workspace TEST key this is always one entry — the workspace's own sandbox, marked sandbox:
    true. For a LIVE workspace key this lists every clinic with an ACTIVE, non-expired connection that
    also still has API access switched on — the same set the key could actually reach on the next call,
    never a stale or pending one. An unverified workspace, or one with no connections yet, gets an empty
    list. A clinic-owned key gets exactly one entry, for its own clinic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectionsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListConnectionsResponse200 | Problem]:
    """Clinics this key can reach, and the scopes granted to it.

     For a workspace TEST key this is always one entry — the workspace's own sandbox, marked sandbox:
    true. For a LIVE workspace key this lists every clinic with an ACTIVE, non-expired connection that
    also still has API access switched on — the same set the key could actually reach on the next call,
    never a stale or pending one. An unverified workspace, or one with no connections yet, gets an empty
    list. A clinic-owned key gets exactly one entry, for its own clinic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectionsResponse200 | Problem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ListConnectionsResponse200 | Problem | None:
    """Clinics this key can reach, and the scopes granted to it.

     For a workspace TEST key this is always one entry — the workspace's own sandbox, marked sandbox:
    true. For a LIVE workspace key this lists every clinic with an ACTIVE, non-expired connection that
    also still has API access switched on — the same set the key could actually reach on the next call,
    never a stale or pending one. An unverified workspace, or one with no connections yet, gets an empty
    list. A clinic-owned key gets exactly one entry, for its own clinic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectionsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
