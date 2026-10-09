from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patient_import_request import PatientImportRequest
from ...models.problem import Problem
from ...models.start_patient_import_response_200 import StartPatientImportResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: PatientImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/patient-imports".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | StartPatientImportResponse200 | None:
    if response.status_code == 200:
        response_200 = StartPatientImportResponse200.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | StartPatientImportResponse200]:
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
    body: PatientImportRequest,
) -> Response[Problem | StartPatientImportResponse200]:
    """Import up to 100 patients from a FHIR Bundle, NDJSON, or a JSON array. Nothing is written unless
    every row is valid.

     The same import the app's Patients screen offers, for the clinic's OWN key. The file is checked in
    full before anything is written: every row goes through the same validation a real create does. If
    EVERY row is valid the import runs at once and the response is the finished job (`status:
    succeeded`). If ANY row fails, nothing is written and the response is the job with `status:
    needs_review` and a `row_errors` list — row number, field and reason for each, never the value that
    failed. Fix the file and send it again, or call `runValidPatientImportRows` to import only the rows
    that passed. A file with exactly the same content that has already been imported is refused
    `already_imported`, so retrying a timed-out call is safe; no Idempotency-Key is needed or read. An
    import contacts no patient and starts no automation. A possible duplicate is still created and
    counted in `flagged_duplicate`, for staff to review. Limits: 100 rows and 10 MiB, refused before any
    row is read. Needs `patients:write`, the API add-on and the accepted API data agreement. Only a
    clinic's own key may import — an organization connected to the clinic may not, whatever it was
    granted (`not_found`).

    Args:
        clinic_id (UUID):
        body (PatientImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StartPatientImportResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientImportRequest,
) -> Problem | StartPatientImportResponse200 | None:
    """Import up to 100 patients from a FHIR Bundle, NDJSON, or a JSON array. Nothing is written unless
    every row is valid.

     The same import the app's Patients screen offers, for the clinic's OWN key. The file is checked in
    full before anything is written: every row goes through the same validation a real create does. If
    EVERY row is valid the import runs at once and the response is the finished job (`status:
    succeeded`). If ANY row fails, nothing is written and the response is the job with `status:
    needs_review` and a `row_errors` list — row number, field and reason for each, never the value that
    failed. Fix the file and send it again, or call `runValidPatientImportRows` to import only the rows
    that passed. A file with exactly the same content that has already been imported is refused
    `already_imported`, so retrying a timed-out call is safe; no Idempotency-Key is needed or read. An
    import contacts no patient and starts no automation. A possible duplicate is still created and
    counted in `flagged_duplicate`, for staff to review. Limits: 100 rows and 10 MiB, refused before any
    row is read. Needs `patients:write`, the API add-on and the accepted API data agreement. Only a
    clinic's own key may import — an organization connected to the clinic may not, whatever it was
    granted (`not_found`).

    Args:
        clinic_id (UUID):
        body (PatientImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StartPatientImportResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientImportRequest,
) -> Response[Problem | StartPatientImportResponse200]:
    """Import up to 100 patients from a FHIR Bundle, NDJSON, or a JSON array. Nothing is written unless
    every row is valid.

     The same import the app's Patients screen offers, for the clinic's OWN key. The file is checked in
    full before anything is written: every row goes through the same validation a real create does. If
    EVERY row is valid the import runs at once and the response is the finished job (`status:
    succeeded`). If ANY row fails, nothing is written and the response is the job with `status:
    needs_review` and a `row_errors` list — row number, field and reason for each, never the value that
    failed. Fix the file and send it again, or call `runValidPatientImportRows` to import only the rows
    that passed. A file with exactly the same content that has already been imported is refused
    `already_imported`, so retrying a timed-out call is safe; no Idempotency-Key is needed or read. An
    import contacts no patient and starts no automation. A possible duplicate is still created and
    counted in `flagged_duplicate`, for staff to review. Limits: 100 rows and 10 MiB, refused before any
    row is read. Needs `patients:write`, the API add-on and the accepted API data agreement. Only a
    clinic's own key may import — an organization connected to the clinic may not, whatever it was
    granted (`not_found`).

    Args:
        clinic_id (UUID):
        body (PatientImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StartPatientImportResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatientImportRequest,
) -> Problem | StartPatientImportResponse200 | None:
    """Import up to 100 patients from a FHIR Bundle, NDJSON, or a JSON array. Nothing is written unless
    every row is valid.

     The same import the app's Patients screen offers, for the clinic's OWN key. The file is checked in
    full before anything is written: every row goes through the same validation a real create does. If
    EVERY row is valid the import runs at once and the response is the finished job (`status:
    succeeded`). If ANY row fails, nothing is written and the response is the job with `status:
    needs_review` and a `row_errors` list — row number, field and reason for each, never the value that
    failed. Fix the file and send it again, or call `runValidPatientImportRows` to import only the rows
    that passed. A file with exactly the same content that has already been imported is refused
    `already_imported`, so retrying a timed-out call is safe; no Idempotency-Key is needed or read. An
    import contacts no patient and starts no automation. A possible duplicate is still created and
    counted in `flagged_duplicate`, for staff to review. Limits: 100 rows and 10 MiB, refused before any
    row is read. Needs `patients:write`, the API add-on and the accepted API data agreement. Only a
    clinic's own key may import — an organization connected to the clinic may not, whatever it was
    granted (`not_found`).

    Args:
        clinic_id (UUID):
        body (PatientImportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StartPatientImportResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
        )
    ).parsed
