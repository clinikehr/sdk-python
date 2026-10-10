from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decide_insurance_pre_authorization_response_200 import DecideInsurancePreAuthorizationResponse200
from ...models.insurance_pre_authorization_decision import InsurancePreAuthorizationDecision
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    pa_id: UUID,
    *,
    body: InsurancePreAuthorizationDecision,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/insurance/pre-authorizations/{pa_id}/decision".format(
            clinic_id=quote(str(clinic_id), safe=""),
            pa_id=quote(str(pa_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DecideInsurancePreAuthorizationResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = DecideInsurancePreAuthorizationResponse200.from_dict(response.json())

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
) -> Response[DecideInsurancePreAuthorizationResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    pa_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationDecision,
    idempotency_key: str,
) -> Response[DecideInsurancePreAuthorizationResponse200 | Problem]:
    """Approve or deny a pre-authorization request.

     For the insurer the clinic linked to your organization. Only a request that is
    `sent_for_authorization` can be decided, once; a decided request answers 409
    `invalid_status_transition`. Answers 200 with the request. A clinic-owned key and an organization
    with no insurer link are refused (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pa_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationDecision): Decide a request that is
            `sent_for_authorization`. An approval needs `pa_code`; a denial needs `reason`.
            `approved_amount` (approval only) defaults to the estimated cost and may not exceed it.
            Lines you do not list follow the decision. A decided request cannot be decided again.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecideInsurancePreAuthorizationResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pa_id=pa_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    pa_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationDecision,
    idempotency_key: str,
) -> DecideInsurancePreAuthorizationResponse200 | Problem | None:
    """Approve or deny a pre-authorization request.

     For the insurer the clinic linked to your organization. Only a request that is
    `sent_for_authorization` can be decided, once; a decided request answers 409
    `invalid_status_transition`. Answers 200 with the request. A clinic-owned key and an organization
    with no insurer link are refused (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pa_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationDecision): Decide a request that is
            `sent_for_authorization`. An approval needs `pa_code`; a denial needs `reason`.
            `approved_amount` (approval only) defaults to the estimated cost and may not exceed it.
            Lines you do not list follow the decision. A decided request cannot be decided again.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecideInsurancePreAuthorizationResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        pa_id=pa_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    pa_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationDecision,
    idempotency_key: str,
) -> Response[DecideInsurancePreAuthorizationResponse200 | Problem]:
    """Approve or deny a pre-authorization request.

     For the insurer the clinic linked to your organization. Only a request that is
    `sent_for_authorization` can be decided, once; a decided request answers 409
    `invalid_status_transition`. Answers 200 with the request. A clinic-owned key and an organization
    with no insurer link are refused (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pa_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationDecision): Decide a request that is
            `sent_for_authorization`. An approval needs `pa_code`; a denial needs `reason`.
            `approved_amount` (approval only) defaults to the estimated cost and may not exceed it.
            Lines you do not list follow the decision. A decided request cannot be decided again.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecideInsurancePreAuthorizationResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pa_id=pa_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    pa_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsurancePreAuthorizationDecision,
    idempotency_key: str,
) -> DecideInsurancePreAuthorizationResponse200 | Problem | None:
    """Approve or deny a pre-authorization request.

     For the insurer the clinic linked to your organization. Only a request that is
    `sent_for_authorization` can be decided, once; a decided request answers 409
    `invalid_status_transition`. Answers 200 with the request. A clinic-owned key and an organization
    with no insurer link are refused (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pa_id (UUID):
        idempotency_key (str):
        body (InsurancePreAuthorizationDecision): Decide a request that is
            `sent_for_authorization`. An approval needs `pa_code`; a denial needs `reason`.
            `approved_amount` (approval only) defaults to the estimated cost and may not exceed it.
            Lines you do not list follow the decision. A decided request cannot be decided again.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecideInsurancePreAuthorizationResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            pa_id=pa_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
