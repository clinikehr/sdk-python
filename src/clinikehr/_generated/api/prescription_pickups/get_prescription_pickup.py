from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_prescription_pickup_response_200 import GetPrescriptionPickupResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    pickup_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/prescription-pickups/{pickup_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            pickup_id=quote(str(pickup_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPrescriptionPickupResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetPrescriptionPickupResponse200.from_dict(response.json())

        return response_200

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
) -> Response[GetPrescriptionPickupResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetPrescriptionPickupResponse200 | Problem]:
    """Read one prescription pickup.

     Absent and not-permitted answer the same 404.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrescriptionPickupResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetPrescriptionPickupResponse200 | Problem | None:
    """Read one prescription pickup.

     Absent and not-permitted answer the same 404.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrescriptionPickupResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetPrescriptionPickupResponse200 | Problem]:
    """Read one prescription pickup.

     Absent and not-permitted answer the same 404.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrescriptionPickupResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetPrescriptionPickupResponse200 | Problem | None:
    """Read one prescription pickup.

     Absent and not-permitted answer the same 404.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrescriptionPickupResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            pickup_id=pickup_id,
            client=client,
        )
    ).parsed
