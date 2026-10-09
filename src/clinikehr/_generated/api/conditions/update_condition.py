from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.condition_update import ConditionUpdate
from ...models.problem import Problem
from ...models.update_condition_response_202 import UpdateConditionResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    condition_id: UUID,
    *,
    body: ConditionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/conditions/{condition_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            condition_id=quote(str(condition_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateConditionResponse202 | None:
    if response.status_code == 202:
        response_202 = UpdateConditionResponse202.from_dict(response.json())

        return response_202

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
) -> Response[Problem | UpdateConditionResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    condition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConditionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateConditionResponse202]:
    """Propose a change to a condition, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the problem-list entry is unchanged until then. `clinical_status:
    entered_in_error` proposes a retraction. The `Idempotency-Key` header is optional. Also accepts a
    FHIR R4 Condition body (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        condition_id (UUID):
        idempotency_key (str | Unset):
        body (ConditionUpdate): A proposed change to an existing problem-list entry. It becomes a
            NEW pending submission; the entry itself does not change until a clinician confirms it.
            `clinical_status: entered_in_error` proposes retracting the entry (nothing is ever
            deleted). `code` and `code_system` go together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateConditionResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        condition_id=condition_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    condition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConditionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateConditionResponse202 | None:
    """Propose a change to a condition, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the problem-list entry is unchanged until then. `clinical_status:
    entered_in_error` proposes a retraction. The `Idempotency-Key` header is optional. Also accepts a
    FHIR R4 Condition body (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        condition_id (UUID):
        idempotency_key (str | Unset):
        body (ConditionUpdate): A proposed change to an existing problem-list entry. It becomes a
            NEW pending submission; the entry itself does not change until a clinician confirms it.
            `clinical_status: entered_in_error` proposes retracting the entry (nothing is ever
            deleted). `code` and `code_system` go together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateConditionResponse202
    """

    return sync_detailed(
        clinic_id=clinic_id,
        condition_id=condition_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    condition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConditionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateConditionResponse202]:
    """Propose a change to a condition, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the problem-list entry is unchanged until then. `clinical_status:
    entered_in_error` proposes a retraction. The `Idempotency-Key` header is optional. Also accepts a
    FHIR R4 Condition body (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        condition_id (UUID):
        idempotency_key (str | Unset):
        body (ConditionUpdate): A proposed change to an existing problem-list entry. It becomes a
            NEW pending submission; the entry itself does not change until a clinician confirms it.
            `clinical_status: entered_in_error` proposes retracting the entry (nothing is ever
            deleted). `code` and `code_system` go together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateConditionResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        condition_id=condition_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    condition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ConditionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateConditionResponse202 | None:
    """Propose a change to a condition, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the problem-list entry is unchanged until then. `clinical_status:
    entered_in_error` proposes a retraction. The `Idempotency-Key` header is optional. Also accepts a
    FHIR R4 Condition body (`Content-Type: application/fhir+json`).

    Args:
        clinic_id (UUID):
        condition_id (UUID):
        idempotency_key (str | Unset):
        body (ConditionUpdate): A proposed change to an existing problem-list entry. It becomes a
            NEW pending submission; the entry itself does not change until a clinician confirms it.
            `clinical_status: entered_in_error` proposes retracting the entry (nothing is ever
            deleted). `code` and `code_system` go together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateConditionResponse202
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            condition_id=condition_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
