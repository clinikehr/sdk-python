from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_prescription_response_200 import GetPrescriptionResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    prescription_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/prescriptions/{prescription_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            prescription_id=quote(str(prescription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPrescriptionResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = GetPrescriptionResponse200.from_dict(response.json())

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
) -> Response[GetPrescriptionResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    prescription_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetPrescriptionResponse200 | Problem]:
    """Get one prescription (read only).

     The same minimal fields as the list. With `Accept: application/fhir+json` the answer is a FHIR R4
    MedicationRequest.

    Args:
        clinic_id (UUID):
        prescription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrescriptionResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        prescription_id=prescription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    prescription_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetPrescriptionResponse200 | Problem | None:
    """Get one prescription (read only).

     The same minimal fields as the list. With `Accept: application/fhir+json` the answer is a FHIR R4
    MedicationRequest.

    Args:
        clinic_id (UUID):
        prescription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrescriptionResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        prescription_id=prescription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    prescription_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[GetPrescriptionResponse200 | Problem]:
    """Get one prescription (read only).

     The same minimal fields as the list. With `Accept: application/fhir+json` the answer is a FHIR R4
    MedicationRequest.

    Args:
        clinic_id (UUID):
        prescription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrescriptionResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        prescription_id=prescription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    prescription_id: UUID,
    *,
    client: AuthenticatedClient,
) -> GetPrescriptionResponse200 | Problem | None:
    """Get one prescription (read only).

     The same minimal fields as the list. With `Accept: application/fhir+json` the answer is a FHIR R4
    MedicationRequest.

    Args:
        clinic_id (UUID):
        prescription_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrescriptionResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            prescription_id=prescription_id,
            client=client,
        )
    ).parsed
