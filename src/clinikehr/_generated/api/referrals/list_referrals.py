import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_referrals_response_200 import ListReferralsResponse200
from ...models.list_referrals_review_status import ListReferralsReviewStatus
from ...models.list_referrals_status import ListReferralsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    patient_id: UUID,
    review_status: ListReferralsReviewStatus | Unset = ListReferralsReviewStatus.CONFIRMED,
    status: ListReferralsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_patient_id = str(patient_id)
    params["patient_id"] = json_patient_id

    json_review_status: str | Unset = UNSET
    if not isinstance(review_status, Unset):
        json_review_status = review_status.value

    params["review_status"] = json_review_status

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["limit"] = limit

    json_starting_after: str | Unset = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = str(starting_after)
    params["starting_after"] = json_starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clinics/{clinic_id}/referrals".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListReferralsResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListReferralsResponse200.from_dict(response.json())

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
) -> Response[ListReferralsResponse200 | Problem]:
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
    patient_id: UUID,
    review_status: ListReferralsReviewStatus | Unset = ListReferralsReviewStatus.CONFIRMED,
    status: ListReferralsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListReferralsResponse200 | Problem]:
    """List one patient's clinical referrals (the clinic's list, or what this key submitted).

     `patient_id` is required. `review_status` picks the view: `confirmed` (default) is the clinic's own
    referral list for the patient, whoever sent each referral; `pending` is this key's own submissions
    still waiting for clinic staff (and those staff rejected); `all` is both. `status` filters confirmed
    referrals by the clinic's workflow state. These are clinical referrals to the clinic; they are not
    the clinic referral programme. A restricted patient's referrals are never returned. With `Accept:
    application/fhir+json` the answer is a searchset Bundle of FHIR R4 ServiceRequest resources.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        review_status (ListReferralsReviewStatus | Unset):  Default:
            ListReferralsReviewStatus.CONFIRMED.
        status (ListReferralsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReferralsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        review_status=review_status,
        status=status,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    patient_id: UUID,
    review_status: ListReferralsReviewStatus | Unset = ListReferralsReviewStatus.CONFIRMED,
    status: ListReferralsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListReferralsResponse200 | Problem | None:
    """List one patient's clinical referrals (the clinic's list, or what this key submitted).

     `patient_id` is required. `review_status` picks the view: `confirmed` (default) is the clinic's own
    referral list for the patient, whoever sent each referral; `pending` is this key's own submissions
    still waiting for clinic staff (and those staff rejected); `all` is both. `status` filters confirmed
    referrals by the clinic's workflow state. These are clinical referrals to the clinic; they are not
    the clinic referral programme. A restricted patient's referrals are never returned. With `Accept:
    application/fhir+json` the answer is a searchset Bundle of FHIR R4 ServiceRequest resources.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        review_status (ListReferralsReviewStatus | Unset):  Default:
            ListReferralsReviewStatus.CONFIRMED.
        status (ListReferralsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReferralsResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        patient_id=patient_id,
        review_status=review_status,
        status=status,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    patient_id: UUID,
    review_status: ListReferralsReviewStatus | Unset = ListReferralsReviewStatus.CONFIRMED,
    status: ListReferralsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListReferralsResponse200 | Problem]:
    """List one patient's clinical referrals (the clinic's list, or what this key submitted).

     `patient_id` is required. `review_status` picks the view: `confirmed` (default) is the clinic's own
    referral list for the patient, whoever sent each referral; `pending` is this key's own submissions
    still waiting for clinic staff (and those staff rejected); `all` is both. `status` filters confirmed
    referrals by the clinic's workflow state. These are clinical referrals to the clinic; they are not
    the clinic referral programme. A restricted patient's referrals are never returned. With `Accept:
    application/fhir+json` the answer is a searchset Bundle of FHIR R4 ServiceRequest resources.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        review_status (ListReferralsReviewStatus | Unset):  Default:
            ListReferralsReviewStatus.CONFIRMED.
        status (ListReferralsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReferralsResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        review_status=review_status,
        status=status,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    patient_id: UUID,
    review_status: ListReferralsReviewStatus | Unset = ListReferralsReviewStatus.CONFIRMED,
    status: ListReferralsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListReferralsResponse200 | Problem | None:
    """List one patient's clinical referrals (the clinic's list, or what this key submitted).

     `patient_id` is required. `review_status` picks the view: `confirmed` (default) is the clinic's own
    referral list for the patient, whoever sent each referral; `pending` is this key's own submissions
    still waiting for clinic staff (and those staff rejected); `all` is both. `status` filters confirmed
    referrals by the clinic's workflow state. These are clinical referrals to the clinic; they are not
    the clinic referral programme. A restricted patient's referrals are never returned. With `Accept:
    application/fhir+json` the answer is a searchset Bundle of FHIR R4 ServiceRequest resources.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        review_status (ListReferralsReviewStatus | Unset):  Default:
            ListReferralsReviewStatus.CONFIRMED.
        status (ListReferralsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReferralsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            patient_id=patient_id,
            review_status=review_status,
            status=status,
            updated_since=updated_since,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
