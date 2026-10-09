from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crm_contact_update_request import CrmContactUpdateRequest
from ...models.problem import Problem
from ...models.update_crm_contact_response_200 import UpdateCrmContactResponse200
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    contact_id: UUID,
    *,
    body: CrmContactUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/crm/contacts/{contact_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateCrmContactResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateCrmContactResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UpdateCrmContactResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    contact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrmContactUpdateRequest,
) -> Response[Problem | UpdateCrmContactResponse200]:
    """Update a CRM contact. Absent fields are unchanged; JSON null clears a nullable field.

     status/score/do_not_contact/unsubscribed_at/converted_patient_id/ converted_at/lost_reason are never
    writable here.

    Args:
        clinic_id (UUID):
        contact_id (UUID):
        body (CrmContactUpdateRequest): Absent fields are unchanged. Every property is optional;
            only present keys are patched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCrmContactResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        contact_id=contact_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    contact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrmContactUpdateRequest,
) -> Problem | UpdateCrmContactResponse200 | None:
    """Update a CRM contact. Absent fields are unchanged; JSON null clears a nullable field.

     status/score/do_not_contact/unsubscribed_at/converted_patient_id/ converted_at/lost_reason are never
    writable here.

    Args:
        clinic_id (UUID):
        contact_id (UUID):
        body (CrmContactUpdateRequest): Absent fields are unchanged. Every property is optional;
            only present keys are patched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCrmContactResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        contact_id=contact_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    contact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrmContactUpdateRequest,
) -> Response[Problem | UpdateCrmContactResponse200]:
    """Update a CRM contact. Absent fields are unchanged; JSON null clears a nullable field.

     status/score/do_not_contact/unsubscribed_at/converted_patient_id/ converted_at/lost_reason are never
    writable here.

    Args:
        clinic_id (UUID):
        contact_id (UUID):
        body (CrmContactUpdateRequest): Absent fields are unchanged. Every property is optional;
            only present keys are patched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCrmContactResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        contact_id=contact_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    contact_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrmContactUpdateRequest,
) -> Problem | UpdateCrmContactResponse200 | None:
    """Update a CRM contact. Absent fields are unchanged; JSON null clears a nullable field.

     status/score/do_not_contact/unsubscribed_at/converted_patient_id/ converted_at/lost_reason are never
    writable here.

    Args:
        clinic_id (UUID):
        contact_id (UUID):
        body (CrmContactUpdateRequest): Absent fields are unchanged. Every property is optional;
            only present keys are patched.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCrmContactResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            contact_id=contact_id,
            client=client,
            body=body,
        )
    ).parsed
