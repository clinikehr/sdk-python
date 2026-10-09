from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.referral_update import ReferralUpdate
from ...models.update_referral_response_202 import UpdateReferralResponse202
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    referral_id: UUID,
    *,
    body: ReferralUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/referrals/{referral_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            referral_id=quote(str(referral_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateReferralResponse202 | None:
    if response.status_code == 202:
        response_202 = UpdateReferralResponse202.from_dict(response.json())

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
) -> Response[Problem | UpdateReferralResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    referral_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReferralUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateReferralResponse202]:
    """Propose a change to a referral you sent, or retract it.

     The change is held for clinic staff to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the referral is unchanged until then. You can change a referral only
    while the clinic has not acted on it (`status: received`); after staff accept, decline, schedule,
    complete or cancel it, the request is refused with a 400 saying the clinic has already actioned it.
    `status: entered_in_error` proposes a retraction, also only while `received`. A sender cannot
    accept, decline, schedule, complete or cancel a referral. The service cannot be changed. The
    `Idempotency-Key` header is optional. JSON only: a FHIR ServiceRequest body is not accepted.

    Args:
        clinic_id (UUID):
        referral_id (UUID):
        idempotency_key (str | Unset):
        body (ReferralUpdate): A proposed change to a referral, or a retraction. It becomes a NEW
            pending submission; the referral does not change until clinic staff confirm it. A change
            is always reviewed, even when the clinic accepts new referrals automatically. You can
            change a referral only while the clinic has not acted on it: once staff have accepted,
            declined, scheduled, completed or cancelled it, the change is refused. The service can
            never be changed (a different service is a new referral). `status` accepts only
            `entered_in_error`, which proposes retracting the referral as sent in error and cannot be
            combined with other changes. A sender cannot accept, decline, schedule, complete or cancel
            a referral.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateReferralResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        referral_id=referral_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    referral_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReferralUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateReferralResponse202 | None:
    """Propose a change to a referral you sent, or retract it.

     The change is held for clinic staff to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the referral is unchanged until then. You can change a referral only
    while the clinic has not acted on it (`status: received`); after staff accept, decline, schedule,
    complete or cancel it, the request is refused with a 400 saying the clinic has already actioned it.
    `status: entered_in_error` proposes a retraction, also only while `received`. A sender cannot
    accept, decline, schedule, complete or cancel a referral. The service cannot be changed. The
    `Idempotency-Key` header is optional. JSON only: a FHIR ServiceRequest body is not accepted.

    Args:
        clinic_id (UUID):
        referral_id (UUID):
        idempotency_key (str | Unset):
        body (ReferralUpdate): A proposed change to a referral, or a retraction. It becomes a NEW
            pending submission; the referral does not change until clinic staff confirm it. A change
            is always reviewed, even when the clinic accepts new referrals automatically. You can
            change a referral only while the clinic has not acted on it: once staff have accepted,
            declined, scheduled, completed or cancelled it, the change is refused. The service can
            never be changed (a different service is a new referral). `status` accepts only
            `entered_in_error`, which proposes retracting the referral as sent in error and cannot be
            combined with other changes. A sender cannot accept, decline, schedule, complete or cancel
            a referral.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateReferralResponse202
    """

    return sync_detailed(
        clinic_id=clinic_id,
        referral_id=referral_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    referral_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReferralUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateReferralResponse202]:
    """Propose a change to a referral you sent, or retract it.

     The change is held for clinic staff to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the referral is unchanged until then. You can change a referral only
    while the clinic has not acted on it (`status: received`); after staff accept, decline, schedule,
    complete or cancel it, the request is refused with a 400 saying the clinic has already actioned it.
    `status: entered_in_error` proposes a retraction, also only while `received`. A sender cannot
    accept, decline, schedule, complete or cancel a referral. The service cannot be changed. The
    `Idempotency-Key` header is optional. JSON only: a FHIR ServiceRequest body is not accepted.

    Args:
        clinic_id (UUID):
        referral_id (UUID):
        idempotency_key (str | Unset):
        body (ReferralUpdate): A proposed change to a referral, or a retraction. It becomes a NEW
            pending submission; the referral does not change until clinic staff confirm it. A change
            is always reviewed, even when the clinic accepts new referrals automatically. You can
            change a referral only while the clinic has not acted on it: once staff have accepted,
            declined, scheduled, completed or cancelled it, the change is refused. The service can
            never be changed (a different service is a new referral). `status` accepts only
            `entered_in_error`, which proposes retracting the referral as sent in error and cannot be
            combined with other changes. A sender cannot accept, decline, schedule, complete or cancel
            a referral.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateReferralResponse202]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        referral_id=referral_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    referral_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReferralUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateReferralResponse202 | None:
    """Propose a change to a referral you sent, or retract it.

     The change is held for clinic staff to confirm and answers 202 Accepted with a `Location` header
    pointing at the new submission; the referral is unchanged until then. You can change a referral only
    while the clinic has not acted on it (`status: received`); after staff accept, decline, schedule,
    complete or cancel it, the request is refused with a 400 saying the clinic has already actioned it.
    `status: entered_in_error` proposes a retraction, also only while `received`. A sender cannot
    accept, decline, schedule, complete or cancel a referral. The service cannot be changed. The
    `Idempotency-Key` header is optional. JSON only: a FHIR ServiceRequest body is not accepted.

    Args:
        clinic_id (UUID):
        referral_id (UUID):
        idempotency_key (str | Unset):
        body (ReferralUpdate): A proposed change to a referral, or a retraction. It becomes a NEW
            pending submission; the referral does not change until clinic staff confirm it. A change
            is always reviewed, even when the clinic accepts new referrals automatically. You can
            change a referral only while the clinic has not acted on it: once staff have accepted,
            declined, scheduled, completed or cancelled it, the change is refused. The service can
            never be changed (a different service is a new referral). `status` accepts only
            `entered_in_error`, which proposes retracting the referral as sent in error and cannot be
            combined with other changes. A sender cannot accept, decline, schedule, complete or cancel
            a referral.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateReferralResponse202
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            referral_id=referral_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
