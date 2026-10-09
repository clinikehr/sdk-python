from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.medication_statement_update import MedicationStatementUpdate
from ...models.problem import Problem
from ...models.update_medication_statement_response_202 import UpdateMedicationStatementResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    medication_statement_id: UUID,
    *,
    body: MedicationStatementUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/medication-statements/{medication_statement_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            medication_statement_id=quote(str(medication_statement_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateMedicationStatementResponse202 | None:
    if response.status_code == 202:
        response_202 = UpdateMedicationStatementResponse202.from_dict(response.json())

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
) -> Response[Problem | UpdateMedicationStatementResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    medication_statement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MedicationStatementUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateMedicationStatementResponse202]:
    """Propose a change to a reported medicine, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the statement is unchanged until then. A change is always reviewed
    by a clinician, even when the clinic accepts new reported medicines automatically. `status:
    entered_in_error` proposes a retraction. The medicine cannot be changed. The `Idempotency-Key`
    header is optional. JSON only: a FHIR MedicationStatement body is not accepted.

    Args:
        clinic_id (UUID):
        medication_statement_id (UUID):
        idempotency_key (str | Unset):
        body (MedicationStatementUpdate): A proposed change to a reported medicine. It becomes a
            NEW pending submission; the statement does not change until a clinician confirms it. The
            medicine itself can never be changed (a different medicine is a new statement). `status:
            entered_in_error` proposes retracting the statement and cannot be combined with other
            changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateMedicationStatementResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        medication_statement_id=medication_statement_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    medication_statement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MedicationStatementUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateMedicationStatementResponse202 | None:
    """Propose a change to a reported medicine, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the statement is unchanged until then. A change is always reviewed
    by a clinician, even when the clinic accepts new reported medicines automatically. `status:
    entered_in_error` proposes a retraction. The medicine cannot be changed. The `Idempotency-Key`
    header is optional. JSON only: a FHIR MedicationStatement body is not accepted.

    Args:
        clinic_id (UUID):
        medication_statement_id (UUID):
        idempotency_key (str | Unset):
        body (MedicationStatementUpdate): A proposed change to a reported medicine. It becomes a
            NEW pending submission; the statement does not change until a clinician confirms it. The
            medicine itself can never be changed (a different medicine is a new statement). `status:
            entered_in_error` proposes retracting the statement and cannot be combined with other
            changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateMedicationStatementResponse202
    """

    return sync_detailed(
        clinic_id=clinic_id,
        medication_statement_id=medication_statement_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    medication_statement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MedicationStatementUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateMedicationStatementResponse202]:
    """Propose a change to a reported medicine, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the statement is unchanged until then. A change is always reviewed
    by a clinician, even when the clinic accepts new reported medicines automatically. `status:
    entered_in_error` proposes a retraction. The medicine cannot be changed. The `Idempotency-Key`
    header is optional. JSON only: a FHIR MedicationStatement body is not accepted.

    Args:
        clinic_id (UUID):
        medication_statement_id (UUID):
        idempotency_key (str | Unset):
        body (MedicationStatementUpdate): A proposed change to a reported medicine. It becomes a
            NEW pending submission; the statement does not change until a clinician confirms it. The
            medicine itself can never be changed (a different medicine is a new statement). `status:
            entered_in_error` proposes retracting the statement and cannot be combined with other
            changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateMedicationStatementResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        medication_statement_id=medication_statement_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    medication_statement_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MedicationStatementUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateMedicationStatementResponse202 | None:
    """Propose a change to a reported medicine, or retract it.

     The change is held for a clinician to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the statement is unchanged until then. A change is always reviewed
    by a clinician, even when the clinic accepts new reported medicines automatically. `status:
    entered_in_error` proposes a retraction. The medicine cannot be changed. The `Idempotency-Key`
    header is optional. JSON only: a FHIR MedicationStatement body is not accepted.

    Args:
        clinic_id (UUID):
        medication_statement_id (UUID):
        idempotency_key (str | Unset):
        body (MedicationStatementUpdate): A proposed change to a reported medicine. It becomes a
            NEW pending submission; the statement does not change until a clinician confirms it. The
            medicine itself can never be changed (a different medicine is a new statement). `status:
            entered_in_error` proposes retracting the statement and cannot be combined with other
            changes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateMedicationStatementResponse202
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            medication_statement_id=medication_statement_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
