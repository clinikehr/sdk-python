from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.coverage_update import CoverageUpdate
from ...models.problem import Problem
from ...models.update_coverage_response_200 import UpdateCoverageResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    coverage_id: UUID,
    *,
    body: CoverageUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/coverages/{coverage_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            coverage_id=quote(str(coverage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateCoverageResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateCoverageResponse200.from_dict(response.json())

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
) -> Response[Problem | UpdateCoverageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    coverage_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoverageUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateCoverageResponse200]:
    """Change a coverage, or end it.

     Answers 200 with the coverage. Changing who the coverage is for on a confirmed coverage sends it
    back to unconfirmed and inactive for staff to confirm again. `coverage_active: false` and
    `termination_date` end a coverage; `coverage_active: true` is refused (`activation_requires_staff`).
    The `Idempotency-Key` header is optional. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        coverage_id (UUID):
        idempotency_key (str | Unset):
        body (CoverageUpdate): A change to an existing coverage. Changing who the coverage is for
            (`payer_id`, `member_id`, `group_number`, `subscriber_member_id`,
            `relationship_to_subscriber` or the policy holder's name or date of birth) on a confirmed
            coverage sends it back to `unconfirmed` and inactive until staff confirm it again. Other
            edits keep its status. `coverage_active: false` and `termination_date` end a coverage;
            `coverage_active: true` is refused with `activation_requires_staff`. Nothing is ever
            deleted. Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCoverageResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        coverage_id=coverage_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    coverage_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoverageUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateCoverageResponse200 | None:
    """Change a coverage, or end it.

     Answers 200 with the coverage. Changing who the coverage is for on a confirmed coverage sends it
    back to unconfirmed and inactive for staff to confirm again. `coverage_active: false` and
    `termination_date` end a coverage; `coverage_active: true` is refused (`activation_requires_staff`).
    The `Idempotency-Key` header is optional. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        coverage_id (UUID):
        idempotency_key (str | Unset):
        body (CoverageUpdate): A change to an existing coverage. Changing who the coverage is for
            (`payer_id`, `member_id`, `group_number`, `subscriber_member_id`,
            `relationship_to_subscriber` or the policy holder's name or date of birth) on a confirmed
            coverage sends it back to `unconfirmed` and inactive until staff confirm it again. Other
            edits keep its status. `coverage_active: false` and `termination_date` end a coverage;
            `coverage_active: true` is refused with `activation_requires_staff`. Nothing is ever
            deleted. Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCoverageResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        coverage_id=coverage_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    coverage_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoverageUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateCoverageResponse200]:
    """Change a coverage, or end it.

     Answers 200 with the coverage. Changing who the coverage is for on a confirmed coverage sends it
    back to unconfirmed and inactive for staff to confirm again. `coverage_active: false` and
    `termination_date` end a coverage; `coverage_active: true` is refused (`activation_requires_staff`).
    The `Idempotency-Key` header is optional. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        coverage_id (UUID):
        idempotency_key (str | Unset):
        body (CoverageUpdate): A change to an existing coverage. Changing who the coverage is for
            (`payer_id`, `member_id`, `group_number`, `subscriber_member_id`,
            `relationship_to_subscriber` or the policy holder's name or date of birth) on a confirmed
            coverage sends it back to `unconfirmed` and inactive until staff confirm it again. Other
            edits keep its status. `coverage_active: false` and `termination_date` end a coverage;
            `coverage_active: true` is refused with `activation_requires_staff`. Nothing is ever
            deleted. Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCoverageResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        coverage_id=coverage_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    coverage_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CoverageUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateCoverageResponse200 | None:
    """Change a coverage, or end it.

     Answers 200 with the coverage. Changing who the coverage is for on a confirmed coverage sends it
    back to unconfirmed and inactive for staff to confirm again. `coverage_active: false` and
    `termination_date` end a coverage; `coverage_active: true` is refused (`activation_requires_staff`).
    The `Idempotency-Key` header is optional. Send JSON; a FHIR Coverage body is refused.

    Args:
        clinic_id (UUID):
        coverage_id (UUID):
        idempotency_key (str | Unset):
        body (CoverageUpdate): A change to an existing coverage. Changing who the coverage is for
            (`payer_id`, `member_id`, `group_number`, `subscriber_member_id`,
            `relationship_to_subscriber` or the policy holder's name or date of birth) on a confirmed
            coverage sends it back to `unconfirmed` and inactive until staff confirm it again. Other
            edits keep its status. `coverage_active: false` and `termination_date` end a coverage;
            `coverage_active: true` is refused with `activation_requires_staff`. Nothing is ever
            deleted. Send JSON; a FHIR Coverage body is not accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCoverageResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            coverage_id=coverage_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
