import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_patients_response_200 import ListPatientsResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    mrn: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["starting_after"] = starting_after

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["email"] = email

    params["phone"] = phone

    params["mrn"] = mrn

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/patients".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListPatientsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListPatientsResponse200.from_dict(response.json())

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
) -> Response[ListPatientsResponse200 | Problem]:
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
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    mrn: str | Unset = UNSET,
) -> Response[ListPatientsResponse200 | Problem]:
    """List patients in scope for this key's connection.

     Restricted/access-controlled patients never appear.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        email (str | Unset):
        phone (str | Unset):
        mrn (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPatientsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        email=email,
        phone=phone,
        mrn=mrn,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    mrn: str | Unset = UNSET,
) -> ListPatientsResponse200 | Problem | None:
    """List patients in scope for this key's connection.

     Restricted/access-controlled patients never appear.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        email (str | Unset):
        phone (str | Unset):
        mrn (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPatientsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        email=email,
        phone=phone,
        mrn=mrn,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    mrn: str | Unset = UNSET,
) -> Response[ListPatientsResponse200 | Problem]:
    """List patients in scope for this key's connection.

     Restricted/access-controlled patients never appear.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        email (str | Unset):
        phone (str | Unset):
        mrn (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPatientsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        email=email,
        phone=phone,
        mrn=mrn,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    email: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    mrn: str | Unset = UNSET,
) -> ListPatientsResponse200 | Problem | None:
    """List patients in scope for this key's connection.

     Restricted/access-controlled patients never appear.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        email (str | Unset):
        phone (str | Unset):
        mrn (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPatientsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            limit=limit,
            starting_after=starting_after,
            updated_since=updated_since,
            email=email,
            phone=phone,
            mrn=mrn,
        )
    ).parsed
