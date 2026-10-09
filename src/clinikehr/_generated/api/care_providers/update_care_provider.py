from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.care_provider_update import CareProviderUpdate
from ...models.problem import Problem
from ...models.update_care_provider_response_200 import UpdateCareProviderResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    body: CareProviderUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/clinics/{clinic_id}/care-providers/{care_provider_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            care_provider_id=quote(str(care_provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpdateCareProviderResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateCareProviderResponse200.from_dict(response.json())

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
) -> Response[Problem | UpdateCareProviderResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CareProviderUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateCareProviderResponse200]:
    """Change an outside care provider your app added.

     Answers 200 with the contact. Only a contact an app added can be changed, and only by an app of the
    same owner; a contact the clinic added (`editable: false`) answers 409
    `care_provider_clinic_managed`. The patient cannot be changed. The `Idempotency-Key` header is
    optional.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):
        idempotency_key (str | Unset):
        body (CareProviderUpdate): A change to an outside care provider your app added. The
            patient cannot be changed. `is_primary: true` makes the patient's other contacts of the
            same `type` non-primary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCareProviderResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CareProviderUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateCareProviderResponse200 | None:
    """Change an outside care provider your app added.

     Answers 200 with the contact. Only a contact an app added can be changed, and only by an app of the
    same owner; a contact the clinic added (`editable: false`) answers 409
    `care_provider_clinic_managed`. The patient cannot be changed. The `Idempotency-Key` header is
    optional.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):
        idempotency_key (str | Unset):
        body (CareProviderUpdate): A change to an outside care provider your app added. The
            patient cannot be changed. `is_primary: true` makes the patient's other contacts of the
            same `type` non-primary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCareProviderResponse200
    """

    return sync_detailed(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CareProviderUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | UpdateCareProviderResponse200]:
    """Change an outside care provider your app added.

     Answers 200 with the contact. Only a contact an app added can be changed, and only by an app of the
    same owner; a contact the clinic added (`editable: false`) answers 409
    `care_provider_clinic_managed`. The patient cannot be changed. The `Idempotency-Key` header is
    optional.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):
        idempotency_key (str | Unset):
        body (CareProviderUpdate): A change to an outside care provider your app added. The
            patient cannot be changed. `is_primary: true` makes the patient's other contacts of the
            same `type` non-primary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpdateCareProviderResponse200]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CareProviderUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | UpdateCareProviderResponse200 | None:
    """Change an outside care provider your app added.

     Answers 200 with the contact. Only a contact an app added can be changed, and only by an app of the
    same owner; a contact the clinic added (`editable: false`) answers 409
    `care_provider_clinic_managed`. The patient cannot be changed. The `Idempotency-Key` header is
    optional.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):
        idempotency_key (str | Unset):
        body (CareProviderUpdate): A change to an outside care provider your app added. The
            patient cannot be changed. `is_primary: true` makes the patient's other contacts of the
            same `type` non-primary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpdateCareProviderResponse200
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            care_provider_id=care_provider_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
