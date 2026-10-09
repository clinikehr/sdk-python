from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    care_provider_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/clinics/{clinic_id}/care-providers/{care_provider_id}".format(
            clinic_id=quote(str(clinic_id), safe=""),
            care_provider_id=quote(str(care_provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Problem | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Problem]:
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
) -> Response[Any | Problem]:
    """Remove an outside care provider your app added.

     Answers 204 with no body. Only a contact an app added can be removed, and only by an app of the same
    owner; a contact the clinic added answers 409 `care_provider_clinic_managed`. A contact is a
    reference, not a clinical record, so it is deleted; the removal stays in the clinic's audit trail.
    There is no request body and no `Idempotency-Key`: removing a contact twice answers 404 the second
    time.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
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
) -> Any | Problem | None:
    """Remove an outside care provider your app added.

     Answers 204 with no body. Only a contact an app added can be removed, and only by an app of the same
    owner; a contact the clinic added answers 409 `care_provider_clinic_managed`. A contact is a
    reference, not a clinical record, so it is deleted; the removal stays in the clinic's audit trail.
    There is no request body and no `Idempotency-Key`: removing a contact twice answers 404 the second
    time.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Remove an outside care provider your app added.

     Answers 204 with no body. Only a contact an app added can be removed, and only by an app of the same
    owner; a contact the clinic added answers 409 `care_provider_clinic_managed`. A contact is a
    reference, not a clinical record, so it is deleted; the removal stays in the clinic's audit trail.
    There is no request body and no `Idempotency-Key`: removing a contact twice answers 404 the second
    time.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        care_provider_id=care_provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    care_provider_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Remove an outside care provider your app added.

     Answers 204 with no body. Only a contact an app added can be removed, and only by an app of the same
    owner; a contact the clinic added answers 409 `care_provider_clinic_managed`. A contact is a
    reference, not a clinical record, so it is deleted; the removal stays in the clinic's audit trail.
    There is no request body and no `Idempotency-Key`: removing a contact twice answers 404 the second
    time.

    Args:
        clinic_id (UUID):
        care_provider_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            care_provider_id=care_provider_id,
            client=client,
        )
    ).parsed
