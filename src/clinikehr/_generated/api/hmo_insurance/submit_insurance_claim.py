from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insurance_claim_submit import InsuranceClaimSubmit
from ...models.problem import Problem
from ...models.submit_insurance_claim_response_201 import SubmitInsuranceClaimResponse201
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: InsuranceClaimSubmit,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/insurance/claims".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SubmitInsuranceClaimResponse201 | None:
    if response.status_code == 201:
        response_201 = SubmitInsuranceClaimResponse201.from_dict(response.json())

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
) -> Response[Problem | SubmitInsuranceClaimResponse201]:
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
    body: InsuranceClaimSubmit,
    idempotency_key: str,
) -> Response[Problem | SubmitInsuranceClaimResponse201]:
    """Submit a claim to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link (a developer). An organization
    linked to an insurer is refused (`role_required`): an insurer does not submit claims to itself. The
    claim is saved as `submitted`, answers 201 with the claim and its lines, and carries no money. The
    `Idempotency-Key` header is REQUIRED - a retry with the same key returns the original claim, never a
    second one.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimSubmit): A claim to submit to one of the clinic's insurers for a
            patient. It is saved as `submitted` with no money on it. `patient_id` must be a patient
            your organization is linked to (a clinic-owned key may use any of its clinic's patients).
            There is no field for a paid or written-off amount; sending one is refused as an unknown
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SubmitInsuranceClaimResponse201]
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
    body: InsuranceClaimSubmit,
    idempotency_key: str,
) -> Problem | SubmitInsuranceClaimResponse201 | None:
    """Submit a claim to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link (a developer). An organization
    linked to an insurer is refused (`role_required`): an insurer does not submit claims to itself. The
    claim is saved as `submitted`, answers 201 with the claim and its lines, and carries no money. The
    `Idempotency-Key` header is REQUIRED - a retry with the same key returns the original claim, never a
    second one.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimSubmit): A claim to submit to one of the clinic's insurers for a
            patient. It is saved as `submitted` with no money on it. `patient_id` must be a patient
            your organization is linked to (a clinic-owned key may use any of its clinic's patients).
            There is no field for a paid or written-off amount; sending one is refused as an unknown
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SubmitInsuranceClaimResponse201
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
    body: InsuranceClaimSubmit,
    idempotency_key: str,
) -> Response[Problem | SubmitInsuranceClaimResponse201]:
    """Submit a claim to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link (a developer). An organization
    linked to an insurer is refused (`role_required`): an insurer does not submit claims to itself. The
    claim is saved as `submitted`, answers 201 with the claim and its lines, and carries no money. The
    `Idempotency-Key` header is REQUIRED - a retry with the same key returns the original claim, never a
    second one.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimSubmit): A claim to submit to one of the clinic's insurers for a
            patient. It is saved as `submitted` with no money on it. `patient_id` must be a patient
            your organization is linked to (a clinic-owned key may use any of its clinic's patients).
            There is no field for a paid or written-off amount; sending one is refused as an unknown
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SubmitInsuranceClaimResponse201]
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
    body: InsuranceClaimSubmit,
    idempotency_key: str,
) -> Problem | SubmitInsuranceClaimResponse201 | None:
    """Submit a claim to one of the clinic's insurers.

     For a clinic-owned key, or an organization with NO insurer link (a developer). An organization
    linked to an insurer is refused (`role_required`): an insurer does not submit claims to itself. The
    claim is saved as `submitted`, answers 201 with the claim and its lines, and carries no money. The
    `Idempotency-Key` header is REQUIRED - a retry with the same key returns the original claim, never a
    second one.

    Args:
        clinic_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimSubmit): A claim to submit to one of the clinic's insurers for a
            patient. It is saved as `submitted` with no money on it. `patient_id` must be a patient
            your organization is linked to (a clinic-owned key may use any of its clinic's patients).
            There is no field for a paid or written-off amount; sending one is refused as an unknown
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SubmitInsuranceClaimResponse201
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
