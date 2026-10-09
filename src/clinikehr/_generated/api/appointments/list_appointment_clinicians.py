from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_appointment_clinicians_response_200 import ListAppointmentCliniciansResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    service_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_service_id: str | Unset = UNSET
    if not isinstance(service_id, Unset):
        json_service_id = str(service_id)
    params["service_id"] = json_service_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/appointments/clinicians".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListAppointmentCliniciansResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListAppointmentCliniciansResponse200.from_dict(response.json())

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
) -> Response[ListAppointmentCliniciansResponse200 | Problem]:
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
    service_id: UUID | Unset = UNSET,
) -> Response[ListAppointmentCliniciansResponse200 | Problem]:
    """Clinicians, optionally filtered to those offering one service — discovery, non-PHI.

    Args:
        clinic_id (UUID):
        service_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAppointmentCliniciansResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    service_id: UUID | Unset = UNSET,
) -> ListAppointmentCliniciansResponse200 | Problem | None:
    """Clinicians, optionally filtered to those offering one service — discovery, non-PHI.

    Args:
        clinic_id (UUID):
        service_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAppointmentCliniciansResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        service_id=service_id,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    service_id: UUID | Unset = UNSET,
) -> Response[ListAppointmentCliniciansResponse200 | Problem]:
    """Clinicians, optionally filtered to those offering one service — discovery, non-PHI.

    Args:
        clinic_id (UUID):
        service_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAppointmentCliniciansResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    service_id: UUID | Unset = UNSET,
) -> ListAppointmentCliniciansResponse200 | Problem | None:
    """Clinicians, optionally filtered to those offering one service — discovery, non-PHI.

    Args:
        clinic_id (UUID):
        service_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAppointmentCliniciansResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            service_id=service_id,
        )
    ).parsed
