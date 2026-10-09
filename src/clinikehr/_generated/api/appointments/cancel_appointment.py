from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appointment_cancel_request import AppointmentCancelRequest
from ...models.cancel_appointment_response_200 import CancelAppointmentResponse200
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    body: AppointmentCancelRequest | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/appointments/{appointment_id}/cancel".format(
            clinic_id=quote(str(clinic_id), safe=""),
            appointment_id=quote(str(appointment_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelAppointmentResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = CancelAppointmentResponse200.from_dict(response.json())

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
) -> Response[CancelAppointmentResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentCancelRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[CancelAppointmentResponse200 | Problem]:
    """Cancel an appointment. The only route that may set status=cancelled.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentCancelRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelAppointmentResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentCancelRequest | Unset = UNSET,
    idempotency_key: str,
) -> CancelAppointmentResponse200 | Problem | None:
    """Cancel an appointment. The only route that may set status=cancelled.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentCancelRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelAppointmentResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentCancelRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[CancelAppointmentResponse200 | Problem]:
    """Cancel an appointment. The only route that may set status=cancelled.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentCancelRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelAppointmentResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        appointment_id=appointment_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    appointment_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AppointmentCancelRequest | Unset = UNSET,
    idempotency_key: str,
) -> CancelAppointmentResponse200 | Problem | None:
    """Cancel an appointment. The only route that may set status=cancelled.

    Args:
        clinic_id (UUID):
        appointment_id (UUID):
        idempotency_key (str):
        body (AppointmentCancelRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelAppointmentResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            appointment_id=appointment_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
