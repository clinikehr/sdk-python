from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_drug_request_substitution_response_200 import ConfirmDrugRequestSubstitutionResponse200
from ...models.drug_request_confirm_substitution_request import DrugRequestConfirmSubstitutionRequest
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    request_id: UUID,
    *,
    body: DrugRequestConfirmSubstitutionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/drug_requests/{request_id}/confirm_substitution".format(
            clinic_id=quote(str(clinic_id), safe=""),
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfirmDrugRequestSubstitutionResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ConfirmDrugRequestSubstitutionResponse200.from_dict(response.json())

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
) -> Response[ConfirmDrugRequestSubstitutionResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DrugRequestConfirmSubstitutionRequest,
) -> Response[ConfirmDrugRequestSubstitutionResponse200 | Problem]:
    """Accept or decline a pharmacist-proposed substitute. Only valid from status=substituted.

     Declining ends the whole request (declined) — the requester may submit a new request rather than
    looping back to submitted.

    Args:
        clinic_id (UUID):
        request_id (UUID):
        body (DrugRequestConfirmSubstitutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmDrugRequestSubstitutionResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DrugRequestConfirmSubstitutionRequest,
) -> ConfirmDrugRequestSubstitutionResponse200 | Problem | None:
    """Accept or decline a pharmacist-proposed substitute. Only valid from status=substituted.

     Declining ends the whole request (declined) — the requester may submit a new request rather than
    looping back to submitted.

    Args:
        clinic_id (UUID):
        request_id (UUID):
        body (DrugRequestConfirmSubstitutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmDrugRequestSubstitutionResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DrugRequestConfirmSubstitutionRequest,
) -> Response[ConfirmDrugRequestSubstitutionResponse200 | Problem]:
    """Accept or decline a pharmacist-proposed substitute. Only valid from status=substituted.

     Declining ends the whole request (declined) — the requester may submit a new request rather than
    looping back to submitted.

    Args:
        clinic_id (UUID):
        request_id (UUID):
        body (DrugRequestConfirmSubstitutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmDrugRequestSubstitutionResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: DrugRequestConfirmSubstitutionRequest,
) -> ConfirmDrugRequestSubstitutionResponse200 | Problem | None:
    """Accept or decline a pharmacist-proposed substitute. Only valid from status=substituted.

     Declining ends the whole request (declined) — the requester may submit a new request rather than
    looping back to submitted.

    Args:
        clinic_id (UUID):
        request_id (UUID):
        body (DrugRequestConfirmSubstitutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmDrugRequestSubstitutionResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
