from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_outreach_events_response_200 import ListOutreachEventsResponse200
from ...models.list_outreach_events_status import ListOutreachEventsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    status: ListOutreachEventsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    json_starting_after: str | Unset = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = str(starting_after)
    params["starting_after"] = json_starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/outreach-events".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListOutreachEventsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListOutreachEventsResponse200.from_dict(response.json())

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
) -> Response[ListOutreachEventsResponse200 | Problem]:
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
    status: ListOutreachEventsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListOutreachEventsResponse200 | Problem]:
    """List this clinic's outreach (screening-day) events.

     Events and stations carry no patient data.

    Args:
        clinic_id (UUID):
        status (ListOutreachEventsStatus | Unset):
        limit (int | Unset):  Default: 50.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOutreachEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        status=status,
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
    status: ListOutreachEventsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    starting_after: UUID | Unset = UNSET,
) -> ListOutreachEventsResponse200 | Problem | None:
    """List this clinic's outreach (screening-day) events.

     Events and stations carry no patient data.

    Args:
        clinic_id (UUID):
        status (ListOutreachEventsStatus | Unset):
        limit (int | Unset):  Default: 50.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOutreachEventsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        status=status,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    status: ListOutreachEventsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListOutreachEventsResponse200 | Problem]:
    """List this clinic's outreach (screening-day) events.

     Events and stations carry no patient data.

    Args:
        clinic_id (UUID):
        status (ListOutreachEventsStatus | Unset):
        limit (int | Unset):  Default: 50.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOutreachEventsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        status=status,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    status: ListOutreachEventsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    starting_after: UUID | Unset = UNSET,
) -> ListOutreachEventsResponse200 | Problem | None:
    """List this clinic's outreach (screening-day) events.

     Events and stations carry no patient data.

    Args:
        clinic_id (UUID):
        status (ListOutreachEventsStatus | Unset):
        limit (int | Unset):  Default: 50.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOutreachEventsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            status=status,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
