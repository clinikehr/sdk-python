from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insurance_pre_authorization_submit import InsurancePreAuthorizationSubmit
from ...models.problem import Problem
from ...models.submit_insurance_pre_authorization_response_201 import SubmitInsurancePreAuthorizationResponse201
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: InsurancePreAuthorizationSubmit,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/insurance/pre-authorizations".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SubmitInsurancePreAuthorizationResponse201 | None:
    if response.status_code == 201:
        response_201 = SubmitInsurancePreAuthorizationResponse201.from_dict(response.json())

        return response_201

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
) -> Response[Problem | SubmitInsurancePreAuthorizationResponse201]:
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
    body: InsurancePreAuthorizationSubmit,
    idempotency_key: str,
) -> Response[Problem | SubmitInsurancePreAuthorizationResponse201]:
    """Send a pre-authorization request to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link. Saved as `sent_for_authorization`;
    answers 201 with the request. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationSubmit): A pre-authorization request to send to one of the
            clinic's insurers. It is saved as `sent_for_authorization`. `patient_id` must be a patient
            your organization is linked to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SubmitInsurancePreAuthorizationResponse201]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationSubmit,
    idempotency_key: str,
) -> Problem | SubmitInsurancePreAuthorizationResponse201 | None:
    """Send a pre-authorization request to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link. Saved as `sent_for_authorization`;
    answers 201 with the request. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationSubmit): A pre-authorization request to send to one of the
            clinic's insurers. It is saved as `sent_for_authorization`. `patient_id` must be a patient
            your organization is linked to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SubmitInsurancePreAuthorizationResponse201
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationSubmit,
    idempotency_key: str,
) -> Response[Problem | SubmitInsurancePreAuthorizationResponse201]:
    """Send a pre-authorization request to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link. Saved as `sent_for_authorization`;
    answers 201 with the request. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationSubmit): A pre-authorization request to send to one of the
            clinic's insurers. It is saved as `sent_for_authorization`. `patient_id` must be a patient
            your organization is linked to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SubmitInsurancePreAuthorizationResponse201]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationSubmit,
    idempotency_key: str,
) -> Problem | SubmitInsurancePreAuthorizationResponse201 | None:
    """Send a pre-authorization request to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link. Saved as `sent_for_authorization`;
    answers 201 with the request. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationSubmit): A pre-authorization request to send to one of the
            clinic's insurers. It is saved as `sent_for_authorization`. `patient_id` must be a patient
            your organization is linked to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SubmitInsurancePreAuthorizationResponse201
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
