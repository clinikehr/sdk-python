import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_insurance_claims_hmo_status import ListInsuranceClaimsHmoStatus
from ...models.list_insurance_claims_response_200 import ListInsuranceClaimsResponse200
from ...models.list_insurance_claims_status import ListInsuranceClaimsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    insurance_company_id: UUID | Unset = UNSET,
    status: ListInsuranceClaimsStatus | Unset = UNSET,
    hmo_status: ListInsuranceClaimsHmoStatus | Unset = UNSET,
    enrollee_id: UUID | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_insurance_company_id: str | Unset = UNSET
    if not isinstance(insurance_company_id, Unset):
        json_insurance_company_id = str(insurance_company_id)
    params["insurance_company_id"] = json_insurance_company_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_hmo_status: str | Unset = UNSET
    if not isinstance(hmo_status, Unset):
        json_hmo_status = hmo_status.value

    params["hmo_status"] = json_hmo_status

    json_enrollee_id: str | Unset = UNSET
    if not isinstance(enrollee_id, Unset):
        json_enrollee_id = str(enrollee_id)
    params["enrollee_id"] = json_enrollee_id

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["limit"] = limit

    json_starting_after: str | Unset = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = str(starting_after)
    params["starting_after"] = json_starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/insurance/claims".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListInsuranceClaimsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListInsuranceClaimsResponse200.from_dict(response.json())

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
) -> Response[ListInsuranceClaimsResponse200 | Problem]:
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
    insurance_company_id: UUID | Unset = UNSET,
    status: ListInsuranceClaimsStatus | Unset = UNSET,
    hmo_status: ListInsuranceClaimsHmoStatus | Unset = UNSET,
    enrollee_id: UUID | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListInsuranceClaimsResponse200 | Problem]:
    """List claims submitted to your insurer.

     For an organization the clinic linked to an insurer: that insurer's claims that the clinic has
    submitted. Claims still in the clinic's draft stages are never shown to an insurer. A clinic-owned
    key sees all of its clinic's claims. Lines, diagnoses and documents are on the single-claim read.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        status (ListInsuranceClaimsStatus | Unset):
        hmo_status (ListInsuranceClaimsHmoStatus | Unset):
        enrollee_id (UUID | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInsuranceClaimsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        insurance_company_id=insurance_company_id,
        status=status,
        hmo_status=hmo_status,
        enrollee_id=enrollee_id,
        updated_since=updated_since,
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
    insurance_company_id: UUID | Unset = UNSET,
    status: ListInsuranceClaimsStatus | Unset = UNSET,
    hmo_status: ListInsuranceClaimsHmoStatus | Unset = UNSET,
    enrollee_id: UUID | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListInsuranceClaimsResponse200 | Problem | None:
    """List claims submitted to your insurer.

     For an organization the clinic linked to an insurer: that insurer's claims that the clinic has
    submitted. Claims still in the clinic's draft stages are never shown to an insurer. A clinic-owned
    key sees all of its clinic's claims. Lines, diagnoses and documents are on the single-claim read.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        status (ListInsuranceClaimsStatus | Unset):
        hmo_status (ListInsuranceClaimsHmoStatus | Unset):
        enrollee_id (UUID | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInsuranceClaimsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        insurance_company_id=insurance_company_id,
        status=status,
        hmo_status=hmo_status,
        enrollee_id=enrollee_id,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    insurance_company_id: UUID | Unset = UNSET,
    status: ListInsuranceClaimsStatus | Unset = UNSET,
    hmo_status: ListInsuranceClaimsHmoStatus | Unset = UNSET,
    enrollee_id: UUID | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListInsuranceClaimsResponse200 | Problem]:
    """List claims submitted to your insurer.

     For an organization the clinic linked to an insurer: that insurer's claims that the clinic has
    submitted. Claims still in the clinic's draft stages are never shown to an insurer. A clinic-owned
    key sees all of its clinic's claims. Lines, diagnoses and documents are on the single-claim read.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        status (ListInsuranceClaimsStatus | Unset):
        hmo_status (ListInsuranceClaimsHmoStatus | Unset):
        enrollee_id (UUID | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInsuranceClaimsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        insurance_company_id=insurance_company_id,
        status=status,
        hmo_status=hmo_status,
        enrollee_id=enrollee_id,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    insurance_company_id: UUID | Unset = UNSET,
    status: ListInsuranceClaimsStatus | Unset = UNSET,
    hmo_status: ListInsuranceClaimsHmoStatus | Unset = UNSET,
    enrollee_id: UUID | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListInsuranceClaimsResponse200 | Problem | None:
    """List claims submitted to your insurer.

     For an organization the clinic linked to an insurer: that insurer's claims that the clinic has
    submitted. Claims still in the clinic's draft stages are never shown to an insurer. A clinic-owned
    key sees all of its clinic's claims. Lines, diagnoses and documents are on the single-claim read.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        status (ListInsuranceClaimsStatus | Unset):
        hmo_status (ListInsuranceClaimsHmoStatus | Unset):
        enrollee_id (UUID | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInsuranceClaimsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            insurance_company_id=insurance_company_id,
            status=status,
            hmo_status=hmo_status,
            enrollee_id=enrollee_id,
            updated_since=updated_since,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
