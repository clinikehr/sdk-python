import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_insurance_enrollees_response_200 import ListInsuranceEnrolleesResponse200
from ...models.list_insurance_enrollees_status import ListInsuranceEnrolleesStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    insurance_company_id: UUID | Unset = UNSET,
    insurance_no: str | Unset = UNSET,
    status: ListInsuranceEnrolleesStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_insurance_company_id: str | Unset = UNSET
    if not isinstance(insurance_company_id, Unset):
        json_insurance_company_id = str(insurance_company_id)
    params["insurance_company_id"] = json_insurance_company_id

    params["insurance_no"] = insurance_no

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

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
        "url": "/v1/clinics/{clinic_id}/insurance/enrollees".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListInsuranceEnrolleesResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListInsuranceEnrolleesResponse200.from_dict(response.json())

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
) -> Response[ListInsuranceEnrolleesResponse200 | Problem]:
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
    insurance_no: str | Unset = UNSET,
    status: ListInsuranceEnrolleesStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListInsuranceEnrolleesResponse200 | Problem]:
    """List the enrollees of your insurer.

     For an organization the clinic linked to an insurer: that insurer's enrollees at this clinic. To
    verify an enrollee, send `insurance_no` (it also matches the alternate number). A clinic-owned key
    sees every insurer's enrollees. An organization with no insurer link is refused (`hmo_not_linked`);
    a clinic on the US insurance setup is refused (`insurance_region_unsupported`). A restricted
    patient's enrollee record is never returned.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        insurance_no (str | Unset):
        status (ListInsuranceEnrolleesStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInsuranceEnrolleesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        insurance_company_id=insurance_company_id,
        insurance_no=insurance_no,
        status=status,
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
    insurance_no: str | Unset = UNSET,
    status: ListInsuranceEnrolleesStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListInsuranceEnrolleesResponse200 | Problem | None:
    """List the enrollees of your insurer.

     For an organization the clinic linked to an insurer: that insurer's enrollees at this clinic. To
    verify an enrollee, send `insurance_no` (it also matches the alternate number). A clinic-owned key
    sees every insurer's enrollees. An organization with no insurer link is refused (`hmo_not_linked`);
    a clinic on the US insurance setup is refused (`insurance_region_unsupported`). A restricted
    patient's enrollee record is never returned.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        insurance_no (str | Unset):
        status (ListInsuranceEnrolleesStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInsuranceEnrolleesResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        insurance_company_id=insurance_company_id,
        insurance_no=insurance_no,
        status=status,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    insurance_company_id: UUID | Unset = UNSET,
    insurance_no: str | Unset = UNSET,
    status: ListInsuranceEnrolleesStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListInsuranceEnrolleesResponse200 | Problem]:
    """List the enrollees of your insurer.

     For an organization the clinic linked to an insurer: that insurer's enrollees at this clinic. To
    verify an enrollee, send `insurance_no` (it also matches the alternate number). A clinic-owned key
    sees every insurer's enrollees. An organization with no insurer link is refused (`hmo_not_linked`);
    a clinic on the US insurance setup is refused (`insurance_region_unsupported`). A restricted
    patient's enrollee record is never returned.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        insurance_no (str | Unset):
        status (ListInsuranceEnrolleesStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInsuranceEnrolleesResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        insurance_company_id=insurance_company_id,
        insurance_no=insurance_no,
        status=status,
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
    insurance_no: str | Unset = UNSET,
    status: ListInsuranceEnrolleesStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListInsuranceEnrolleesResponse200 | Problem | None:
    """List the enrollees of your insurer.

     For an organization the clinic linked to an insurer: that insurer's enrollees at this clinic. To
    verify an enrollee, send `insurance_no` (it also matches the alternate number). A clinic-owned key
    sees every insurer's enrollees. An organization with no insurer link is refused (`hmo_not_linked`);
    a clinic on the US insurance setup is refused (`insurance_region_unsupported`). A restricted
    patient's enrollee record is never returned.

    Args:
        clinic_id (UUID):
        insurance_company_id (UUID | Unset):
        insurance_no (str | Unset):
        status (ListInsuranceEnrolleesStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInsuranceEnrolleesResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            insurance_company_id=insurance_company_id,
            insurance_no=insurance_no,
            status=status,
            updated_since=updated_since,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
