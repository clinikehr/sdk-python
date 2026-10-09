import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_care_providers_response_200 import ListCareProvidersResponse200
from ...models.list_care_providers_type import ListCareProvidersType
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    patient_id: UUID,
    type_: ListCareProvidersType | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_patient_id = str(patient_id)
    params["patient_id"] = json_patient_id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

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
        "url": "/v1/clinics/{clinic_id}/care-providers".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCareProvidersResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = ListCareProvidersResponse200.from_dict(response.json())

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
) -> Response[ListCareProvidersResponse200 | Problem]:
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
    type_: ListCareProvidersType | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListCareProvidersResponse200 | Problem]:
    """List one patient's outside care providers.

     The clinicians outside the clinic that a patient names: their own doctor, a referring doctor, a
    specialist. `patient_id` is required. `type` filters to one kind. Every contact on the patient's
    record is listed, whoever added it; `source` says whether the clinic or an app did, and `editable`
    says whether this key's app may change or remove it. A restricted patient's contacts are never
    returned. Outside care providers are JSON only — there is no FHIR representation.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        type_ (ListCareProvidersType | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCareProvidersResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        type_=type_,
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
    type_: ListCareProvidersType | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListCareProvidersResponse200 | Problem | None:
    """List one patient's outside care providers.

     The clinicians outside the clinic that a patient names: their own doctor, a referring doctor, a
    specialist. `patient_id` is required. `type` filters to one kind. Every contact on the patient's
    record is listed, whoever added it; `source` says whether the clinic or an app did, and `editable`
    says whether this key's app may change or remove it. A restricted patient's contacts are never
    returned. Outside care providers are JSON only — there is no FHIR representation.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        type_ (ListCareProvidersType | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCareProvidersResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        patient_id=patient_id,
        type_=type_,
        updated_since=updated_since,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    patient_id: UUID,
    type_: ListCareProvidersType | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> Response[ListCareProvidersResponse200 | Problem]:
    """List one patient's outside care providers.

     The clinicians outside the clinic that a patient names: their own doctor, a referring doctor, a
    specialist. `patient_id` is required. `type` filters to one kind. Every contact on the patient's
    record is listed, whoever added it; `source` says whether the clinic or an app did, and `editable`
    says whether this key's app may change or remove it. A restricted patient's contacts are never
    returned. Outside care providers are JSON only — there is no FHIR representation.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        type_ (ListCareProvidersType | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCareProvidersResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        patient_id=patient_id,
        type_=type_,
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
    type_: ListCareProvidersType | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 25,
    starting_after: UUID | Unset = UNSET,
) -> ListCareProvidersResponse200 | Problem | None:
    """List one patient's outside care providers.

     The clinicians outside the clinic that a patient names: their own doctor, a referring doctor, a
    specialist. `patient_id` is required. `type` filters to one kind. Every contact on the patient's
    record is listed, whoever added it; `source` says whether the clinic or an app did, and `editable`
    says whether this key's app may change or remove it. A restricted patient's contacts are never
    returned. Outside care providers are JSON only — there is no FHIR representation.

    Args:
        clinic_id (UUID):
        patient_id (UUID):
        type_ (ListCareProvidersType | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 25.
        starting_after (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCareProvidersResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            patient_id=patient_id,
            type_=type_,
            updated_since=updated_since,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed
