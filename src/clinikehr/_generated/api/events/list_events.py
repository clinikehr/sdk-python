from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_events_response_200 import ListEventsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    after_seq: int | Unset = 0,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["after_seq"] = after_seq

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/events".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListEventsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListEventsResponse200.from_dict(response.json())

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
) -> Response[ListEventsResponse200 | Problem]:
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
    after_seq: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[ListEventsResponse200 | Problem]:
    """The clinic's own change feed — catch-up for a partner whose webhook endpoint was down.

     Needs no scope of its own: any valid key that can reach the clinic may read the feed. The feed is
    filtered to event types whose required_scope the key's CURRENT scopes cover.

    Args:
        clinic_id (UUID):
        after_seq (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        after_seq=after_seq,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    after_seq: int | Unset = 0,
    limit: int | Unset = 50,
) -> ListEventsResponse200 | Problem | None:
    """The clinic's own change feed — catch-up for a partner whose webhook endpoint was down.

     Needs no scope of its own: any valid key that can reach the clinic may read the feed. The feed is
    filtered to event types whose required_scope the key's CURRENT scopes cover.

    Args:
        clinic_id (UUID):
        after_seq (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        after_seq=after_seq,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    after_seq: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[ListEventsResponse200 | Problem]:
    """The clinic's own change feed — catch-up for a partner whose webhook endpoint was down.

     Needs no scope of its own: any valid key that can reach the clinic may read the feed. The feed is
    filtered to event types whose required_scope the key's CURRENT scopes cover.

    Args:
        clinic_id (UUID):
        after_seq (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        after_seq=after_seq,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    after_seq: int | Unset = 0,
    limit: int | Unset = 50,
) -> ListEventsResponse200 | Problem | None:
    """The clinic's own change feed — catch-up for a partner whose webhook endpoint was down.

     Needs no scope of its own: any valid key that can reach the clinic may read the feed. The feed is
    filtered to event types whose required_scope the key's CURRENT scopes cover.

    Args:
        clinic_id (UUID):
        after_seq (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            after_seq=after_seq,
            limit=limit,
        )
    ).parsed
