from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.adjudicate_insurance_claim_response_200 import AdjudicateInsuranceClaimResponse200
from ...models.insurance_claim_adjudication import InsuranceClaimAdjudication
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    claim_id: UUID,
    *,
    body: InsuranceClaimAdjudication,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/insurance/claims/{claim_id}/adjudication".format(
            clinic_id=quote(str(clinic_id), safe=""),
            claim_id=quote(str(claim_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdjudicateInsuranceClaimResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = AdjudicateInsuranceClaimResponse200.from_dict(response.json())

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
) -> Response[AdjudicateInsuranceClaimResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    claim_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsuranceClaimAdjudication,
    idempotency_key: str,
) -> Response[AdjudicateInsuranceClaimResponse200 | Problem]:
    """Vet a claim.

     Approve, adjust or decline lines of a claim of the insurer the clinic linked to your organization.
    See the request body for how `decision` and `items` combine. Answers 200 with the claim. It never
    moves money: a claim the clinic has already recorded a payment or write-off against answers 409
    `invalid_status_transition`. A clinic-owned key and an organization with no insurer link are refused
    (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        claim_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimAdjudication): Vet a claim. `decision` sets what EVERY line gets
            (`approved` at billed figures, or `rejected` at zero); `items` overrides individual lines,
            so "approve everything except this line" is `decision: approved` plus one declined line.
            The claim's status follows the lines: all approved as billed - `approved`; all declined -
            `denied`; anything else - `partially_approved`. A rejection needs a `reason`. You can
            never approve more than was billed, and a claim the clinic has already recorded money
            against can no longer be vetted. Nothing here moves money.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjudicateInsuranceClaimResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        claim_id=claim_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    claim_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsuranceClaimAdjudication,
    idempotency_key: str,
) -> AdjudicateInsuranceClaimResponse200 | Problem | None:
    """Vet a claim.

     Approve, adjust or decline lines of a claim of the insurer the clinic linked to your organization.
    See the request body for how `decision` and `items` combine. Answers 200 with the claim. It never
    moves money: a claim the clinic has already recorded a payment or write-off against answers 409
    `invalid_status_transition`. A clinic-owned key and an organization with no insurer link are refused
    (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        claim_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimAdjudication): Vet a claim. `decision` sets what EVERY line gets
            (`approved` at billed figures, or `rejected` at zero); `items` overrides individual lines,
            so "approve everything except this line" is `decision: approved` plus one declined line.
            The claim's status follows the lines: all approved as billed - `approved`; all declined -
            `denied`; anything else - `partially_approved`. A rejection needs a `reason`. You can
            never approve more than was billed, and a claim the clinic has already recorded money
            against can no longer be vetted. Nothing here moves money.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjudicateInsuranceClaimResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        claim_id=claim_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    claim_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsuranceClaimAdjudication,
    idempotency_key: str,
) -> Response[AdjudicateInsuranceClaimResponse200 | Problem]:
    """Vet a claim.

     Approve, adjust or decline lines of a claim of the insurer the clinic linked to your organization.
    See the request body for how `decision` and `items` combine. Answers 200 with the claim. It never
    moves money: a claim the clinic has already recorded a payment or write-off against answers 409
    `invalid_status_transition`. A clinic-owned key and an organization with no insurer link are refused
    (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        claim_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimAdjudication): Vet a claim. `decision` sets what EVERY line gets
            (`approved` at billed figures, or `rejected` at zero); `items` overrides individual lines,
            so "approve everything except this line" is `decision: approved` plus one declined line.
            The claim's status follows the lines: all approved as billed - `approved`; all declined -
            `denied`; anything else - `partially_approved`. A rejection needs a `reason`. You can
            never approve more than was billed, and a claim the clinic has already recorded money
            against can no longer be vetted. Nothing here moves money.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdjudicateInsuranceClaimResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        claim_id=claim_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    claim_id: UUID,
    *,
    client: AuthenticatedClient,
    body: InsuranceClaimAdjudication,
    idempotency_key: str,
) -> AdjudicateInsuranceClaimResponse200 | Problem | None:
    """Vet a claim.

     Approve, adjust or decline lines of a claim of the insurer the clinic linked to your organization.
    See the request body for how `decision` and `items` combine. Answers 200 with the claim. It never
    moves money: a claim the clinic has already recorded a payment or write-off against answers 409
    `invalid_status_transition`. A clinic-owned key and an organization with no insurer link are refused
    (`hmo_not_linked`). The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        claim_id (UUID):
        idempotency_key (str):
        body (InsuranceClaimAdjudication): Vet a claim. `decision` sets what EVERY line gets
            (`approved` at billed figures, or `rejected` at zero); `items` overrides individual lines,
            so "approve everything except this line" is `decision: approved` plus one declined line.
            The claim's status follows the lines: all approved as billed - `approved`; all declined -
            `denied`; anything else - `partially_approved`. A rejection needs a `reason`. You can
            never approve more than was billed, and a claim the clinic has already recorded money
            against can no longer be vetted. Nothing here moves money.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdjudicateInsuranceClaimResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            claim_id=claim_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
