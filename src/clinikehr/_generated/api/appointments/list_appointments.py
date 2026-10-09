import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_appointments_response_200 import ListAppointmentsResponse200
from ...models.list_appointments_status import ListAppointmentsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    patient_id: UUID | Unset = UNSET,
    clinician_id: UUID | Unset = UNSET,
    status: ListAppointmentsStatus | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["starting_after"] = starting_after

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    json_patient_id: str | Unset = UNSET
    if not isinstance(patient_id, Unset):
        json_patient_id = str(patient_id)
    params["patient_id"] = json_patient_id

    json_clinician_id: str | Unset = UNSET
    if not isinstance(clinician_id, Unset):
        json_clinician_id = str(clinician_id)
    params["clinician_id"] = json_clinician_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/appointments".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAppointmentsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListAppointmentsResponse200.from_dict(response.json())

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
) -> Response[ListAppointmentsResponse200 | Problem]:
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
    patient_id: UUID | Unset = UNSET,
    clinician_id: UUID | Unset = UNSET,
    status: ListAppointmentsStatus | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[ListAppointmentsResponse200 | Problem]:
    """List appointments.

     A restricted patient's appointment is excluded. Date range clamped to 366 days.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        patient_id (UUID | Unset):
        clinician_id (UUID | Unset):
        status (ListAppointmentsStatus | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAppointmentsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        patient_id=patient_id,
        clinician_id=clinician_id,
        status=status,
        from_=from_,
        to=to,
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
    patient_id: UUID | Unset = UNSET,
    clinician_id: UUID | Unset = UNSET,
    status: ListAppointmentsStatus | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> ListAppointmentsResponse200 | Problem | None:
    """List appointments.

     A restricted patient's appointment is excluded. Date range clamped to 366 days.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        patient_id (UUID | Unset):
        clinician_id (UUID | Unset):
        status (ListAppointmentsStatus | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAppointmentsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        patient_id=patient_id,
        clinician_id=clinician_id,
        status=status,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    starting_after: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    patient_id: UUID | Unset = UNSET,
    clinician_id: UUID | Unset = UNSET,
    status: ListAppointmentsStatus | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[ListAppointmentsResponse200 | Problem]:
    """List appointments.

     A restricted patient's appointment is excluded. Date range clamped to 366 days.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        patient_id (UUID | Unset):
        clinician_id (UUID | Unset):
        status (ListAppointmentsStatus | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAppointmentsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        limit=limit,
        starting_after=starting_after,
        updated_since=updated_since,
        patient_id=patient_id,
        clinician_id=clinician_id,
        status=status,
        from_=from_,
        to=to,
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
    patient_id: UUID | Unset = UNSET,
    clinician_id: UUID | Unset = UNSET,
    status: ListAppointmentsStatus | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> ListAppointmentsResponse200 | Problem | None:
    """List appointments.

     A restricted patient's appointment is excluded. Date range clamped to 366 days.

    Args:
        clinic_id (UUID):
        limit (int | Unset):  Default: 25.
        starting_after (str | Unset):
        updated_since (datetime.datetime | Unset):
        patient_id (UUID | Unset):
        clinician_id (UUID | Unset):
        status (ListAppointmentsStatus | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAppointmentsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            limit=limit,
            starting_after=starting_after,
            updated_since=updated_since,
            patient_id=patient_id,
            clinician_id=clinician_id,
            status=status,
            from_=from_,
            to=to,
        )
    ).parsed
