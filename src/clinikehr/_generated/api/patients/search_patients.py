from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patient_search_request import PatientSearchRequest
from ...models.problem import Problem
from ...models.search_patients_response_200 import SearchPatientsResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: PatientSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/patients/search".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SearchPatientsResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchPatientsResponse200.from_dict(response.json())

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
) -> Response[Problem | SearchPatientsResponse200]:
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
    body: PatientSearchRequest,
) -> Response[Problem | SearchPatientsResponse200]:
    """Exact-match patient search by two or more identifiers. Identifiers in the body, never a URL.

     Never a name-only or partial match; at least two identifiers of DIFFERENT kinds (email, phone, mrn)
    are required, so this cannot be used to iterate one field at a time. Capped at 5 results. "No match"
    and "not permitted" are the identical response — an empty `data` array, never a 404: the query
    itself already excludes anything the caller may not see. For an organization key, results are
    limited to patients LINKED through that connection — today this is moot in practice (patients:read
    is PHI, and the organization patient-data master switch ships false), but the route is built and
    tested as though it were open.

    Args:
        clinic_id (UUID):
        body (PatientSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SearchPatientsResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientSearchRequest,
) -> Problem | SearchPatientsResponse200 | None:
    """Exact-match patient search by two or more identifiers. Identifiers in the body, never a URL.

     Never a name-only or partial match; at least two identifiers of DIFFERENT kinds (email, phone, mrn)
    are required, so this cannot be used to iterate one field at a time. Capped at 5 results. "No match"
    and "not permitted" are the identical response — an empty `data` array, never a 404: the query
    itself already excludes anything the caller may not see. For an organization key, results are
    limited to patients LINKED through that connection — today this is moot in practice (patients:read
    is PHI, and the organization patient-data master switch ships false), but the route is built and
    tested as though it were open.

    Args:
        clinic_id (UUID):
        body (PatientSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SearchPatientsResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientSearchRequest,
) -> Response[Problem | SearchPatientsResponse200]:
    """Exact-match patient search by two or more identifiers. Identifiers in the body, never a URL.

     Never a name-only or partial match; at least two identifiers of DIFFERENT kinds (email, phone, mrn)
    are required, so this cannot be used to iterate one field at a time. Capped at 5 results. "No match"
    and "not permitted" are the identical response — an empty `data` array, never a 404: the query
    itself already excludes anything the caller may not see. For an organization key, results are
    limited to patients LINKED through that connection — today this is moot in practice (patients:read
    is PHI, and the organization patient-data master switch ships false), but the route is built and
    tested as though it were open.

    Args:
        clinic_id (UUID):
        body (PatientSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SearchPatientsResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientSearchRequest,
) -> Problem | SearchPatientsResponse200 | None:
    """Exact-match patient search by two or more identifiers. Identifiers in the body, never a URL.

     Never a name-only or partial match; at least two identifiers of DIFFERENT kinds (email, phone, mrn)
    are required, so this cannot be used to iterate one field at a time. Capped at 5 results. "No match"
    and "not permitted" are the identical response — an empty `data` array, never a 404: the query
    itself already excludes anything the caller may not see. For an organization key, results are
    limited to patients LINKED through that connection — today this is moot in practice (patients:read
    is PHI, and the organization patient-data master switch ships false), but the route is built and
    tested as though it were open.

    Args:
        clinic_id (UUID):
        body (PatientSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SearchPatientsResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
        )
    ).parsed
