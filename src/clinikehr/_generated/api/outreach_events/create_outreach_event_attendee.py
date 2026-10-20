from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_outreach_event_attendee_response_202 import CreateOutreachEventAttendeeResponse202
from ...models.outreach_attendee_checkin_create import OutreachAttendeeCheckinCreate
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    event_id: UUID,
    *,
    body: OutreachAttendeeCheckinCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/outreach-events/{event_id}/attendees".format(
            clinic_id=quote(str(clinic_id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOutreachEventAttendeeResponse202 | Problem | None:
    if response.status_code == 202:
        response_202 = CreateOutreachEventAttendeeResponse202.from_dict(response.json())

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
) -> Response[CreateOutreachEventAttendeeResponse202 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
    body: OutreachAttendeeCheckinCreate,
    idempotency_key: str,
) -> Response[CreateOutreachEventAttendeeResponse202 | Problem]:
    """Check an existing patient in to an outreach event, for clinician review.

     Create the patient first with `POST /v1/clinics/{clinic_id}/patients`. Held for review and answers
    202 Accepted with a `Location` header pointing at the submission, or immediately confirmed when the
    clinic has chosen automatic acceptance for this key. On confirm, staff run the SAME single write
    path the app's own Check in button uses. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        event_id (UUID):
        idempotency_key (str):
        body (OutreachAttendeeCheckinCreate): A check-in for an EXISTING patient, submitted for
            clinician review. Create the patient first with `POST /v1/clinics/{clinic_id}/patients`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutreachEventAttendeeResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        event_id=event_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
    body: OutreachAttendeeCheckinCreate,
    idempotency_key: str,
) -> CreateOutreachEventAttendeeResponse202 | Problem | None:
    """Check an existing patient in to an outreach event, for clinician review.

     Create the patient first with `POST /v1/clinics/{clinic_id}/patients`. Held for review and answers
    202 Accepted with a `Location` header pointing at the submission, or immediately confirmed when the
    clinic has chosen automatic acceptance for this key. On confirm, staff run the SAME single write
    path the app's own Check in button uses. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        event_id (UUID):
        idempotency_key (str):
        body (OutreachAttendeeCheckinCreate): A check-in for an EXISTING patient, submitted for
            clinician review. Create the patient first with `POST /v1/clinics/{clinic_id}/patients`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutreachEventAttendeeResponse202 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        event_id=event_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
    body: OutreachAttendeeCheckinCreate,
    idempotency_key: str,
) -> Response[CreateOutreachEventAttendeeResponse202 | Problem]:
    """Check an existing patient in to an outreach event, for clinician review.

     Create the patient first with `POST /v1/clinics/{clinic_id}/patients`. Held for review and answers
    202 Accepted with a `Location` header pointing at the submission, or immediately confirmed when the
    clinic has chosen automatic acceptance for this key. On confirm, staff run the SAME single write
    path the app's own Check in button uses. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        event_id (UUID):
        idempotency_key (str):
        body (OutreachAttendeeCheckinCreate): A check-in for an EXISTING patient, submitted for
            clinician review. Create the patient first with `POST /v1/clinics/{clinic_id}/patients`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutreachEventAttendeeResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        event_id=event_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
    body: OutreachAttendeeCheckinCreate,
    idempotency_key: str,
) -> CreateOutreachEventAttendeeResponse202 | Problem | None:
    """Check an existing patient in to an outreach event, for clinician review.

     Create the patient first with `POST /v1/clinics/{clinic_id}/patients`. Held for review and answers
    202 Accepted with a `Location` header pointing at the submission, or immediately confirmed when the
    clinic has chosen automatic acceptance for this key. On confirm, staff run the SAME single write
    path the app's own Check in button uses. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        event_id (UUID):
        idempotency_key (str):
        body (OutreachAttendeeCheckinCreate): A check-in for an EXISTING patient, submitted for
            clinician review. Create the patient first with `POST /v1/clinics/{clinic_id}/patients`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutreachEventAttendeeResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            event_id=event_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
