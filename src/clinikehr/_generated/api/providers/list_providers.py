from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_providers_response_200 import ListProvidersResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    json_starting_after: str | Unset = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = str(starting_after)
    params["starting_after"] = json_starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/providers".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListProvidersResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListProvidersResponse200.from_dict(response.json())

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
) -> Response[ListProvidersResponse200 | Problem]:
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
    q: str | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListProvidersResponse200 | Problem]:
    """List the clinic's providers (its clinicians).

     The clinic's directory of clinicians: the staff who can author clinical notes, excluding expired
    memberships. It is read only — there is no way to create, change or remove a provider through the
    API. Each provider carries the name, title, role, specialties, department, NPI and licences the
    clinic holds for them; email, phone and every other staff detail are never exposed, and there is no
    verified flag. `q` (at least 2 characters) matches the provider's name. The provider `id` is the
    same id the clinician pickers use. With `Accept: application/fhir+json` the answer is a searchset
    Bundle of FHIR R4 Practitioner resources.

    Args:
        clinic_id (UUID):
        q (str | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProvidersResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        q=q,
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
    q: str | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListProvidersResponse200 | Problem | None:
    """List the clinic's providers (its clinicians).

     The clinic's directory of clinicians: the staff who can author clinical notes, excluding expired
    memberships. It is read only — there is no way to create, change or remove a provider through the
    API. Each provider carries the name, title, role, specialties, department, NPI and licences the
    clinic holds for them; email, phone and every other staff detail are never exposed, and there is no
    verified flag. `q` (at least 2 characters) matches the provider's name. The provider `id` is the
    same id the clinician pickers use. With `Accept: application/fhir+json` the answer is a searchset
    Bundle of FHIR R4 Practitioner resources.

    Args:
        clinic_id (UUID):
        q (str | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProvidersResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        q=q,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListProvidersResponse200 | Problem]:
    """List the clinic's providers (its clinicians).

     The clinic's directory of clinicians: the staff who can author clinical notes, excluding expired
    memberships. It is read only — there is no way to create, change or remove a provider through the
    API. Each provider carries the name, title, role, specialties, department, NPI and licences the
    clinic holds for them; email, phone and every other staff detail are never exposed, and there is no
    verified flag. `q` (at least 2 characters) matches the provider's name. The provider `id` is the
    same id the clinician pickers use. With `Accept: application/fhir+json` the answer is a searchset
    Bundle of FHIR R4 Practitioner resources.

    Args:
        clinic_id (UUID):
        q (str | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProvidersResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        q=q,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListProvidersResponse200 | Problem | None:
    """List the clinic's providers (its clinicians).

     The clinic's directory of clinicians: the staff who can author clinical notes, excluding expired
    memberships. It is read only — there is no way to create, change or remove a provider through the
    API. Each provider carries the name, title, role, specialties, department, NPI and licences the
    clinic holds for them; email, phone and every other staff detail are never exposed, and there is no
    verified flag. `q` (at least 2 characters) matches the provider's name. The provider `id` is the
    same id the clinician pickers use. With `Accept: application/fhir+json` the answer is a searchset
    Bundle of FHIR R4 Practitioner resources.

    Args:
        clinic_id (UUID):
        q (str | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListProvidersResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            q=q,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
