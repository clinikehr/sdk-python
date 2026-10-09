from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.run_valid_patient_import_rows_response_200 import RunValidPatientImportRowsResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    job_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/patient-imports/{job_id}/run-valid".format(
            clinic_id=quote(str(clinic_id), safe=""),
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RunValidPatientImportRowsResponse200 | None:
    if response.status_code == 200:
        response_200 = RunValidPatientImportRowsResponse200.from_dict(response.json())

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

    if response.status_code == 410:
        response_410 = Problem.from_dict(response.json())

        return response_410

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | RunValidPatientImportRowsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | RunValidPatientImportRowsResponse200]:
    """Import only the rows that passed, for a job waiting for review.

     An explicit, recorded choice — the key that made it is stored on the job. Only a job in
    `needs_review` whose file is still held (files are deleted after 7 days) can be run this way;
    anything else is `invalid_status_transition` (409) or `file_expired` (410). Rows that failed stay in
    `row_errors` for reference and are not imported. The response is the finished job.

    Args:
        clinic_id (UUID):
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RunValidPatientImportRowsResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Problem | RunValidPatientImportRowsResponse200 | None:
    """Import only the rows that passed, for a job waiting for review.

     An explicit, recorded choice — the key that made it is stored on the job. Only a job in
    `needs_review` whose file is still held (files are deleted after 7 days) can be run this way;
    anything else is `invalid_status_transition` (409) or `file_expired` (410). Rows that failed stay in
    `row_errors` for reference and are not imported. The response is the finished job.

    Args:
        clinic_id (UUID):
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RunValidPatientImportRowsResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | RunValidPatientImportRowsResponse200]:
    """Import only the rows that passed, for a job waiting for review.

     An explicit, recorded choice — the key that made it is stored on the job. Only a job in
    `needs_review` whose file is still held (files are deleted after 7 days) can be run this way;
    anything else is `invalid_status_transition` (409) or `file_expired` (410). Rows that failed stay in
    `row_errors` for reference and are not imported. The response is the finished job.

    Args:
        clinic_id (UUID):
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RunValidPatientImportRowsResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    job_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Problem | RunValidPatientImportRowsResponse200 | None:
    """Import only the rows that passed, for a job waiting for review.

     An explicit, recorded choice — the key that made it is stored on the job. Only a job in
    `needs_review` whose file is still held (files are deleted after 7 days) can be run this way;
    anything else is `invalid_status_transition` (409) or `file_expired` (410). Rows that failed stay in
    `row_errors` for reference and are not imported. The response is the finished job.

    Args:
        clinic_id (UUID):
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RunValidPatientImportRowsResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
