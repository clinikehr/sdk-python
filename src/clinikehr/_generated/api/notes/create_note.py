from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_note_response_200 import CreateNoteResponse200
from ...models.note_create_request import NoteCreateRequest
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clinic_id: UUID,
    *,
    body: NoteCreateRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/notes".format(
            clinic_id=quote(str(clinic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateNoteResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = CreateNoteResponse200.from_dict(response.json())

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
) -> Response[CreateNoteResponse200 | Problem]:
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
    body: NoteCreateRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateNoteResponse200 | Problem]:
    """Create a DRAFT note. Always status=draft — this route can never sign, lock, finalize or co-sign.

     Unknown content keys are refused (unknown_field) naming both the offending keys and the full valid
    list for whichever template note_type/custom_template_id resolves to. The answer is the full note,
    the same object `GET …/notes/{note_id}` returns: its details plus `content` and `citations`. A
    citation's `url`, when given, must be an `http://` or `https://` address; anything else is refused
    with a 400 naming `/citations/N/url`.

    Args:
        clinic_id (UUID):
        idempotency_key (str | Unset):
        body (NoteCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNoteResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: NoteCreateRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateNoteResponse200 | Problem | None:
    """Create a DRAFT note. Always status=draft — this route can never sign, lock, finalize or co-sign.

     Unknown content keys are refused (unknown_field) naming both the offending keys and the full valid
    list for whichever template note_type/custom_template_id resolves to. The answer is the full note,
    the same object `GET …/notes/{note_id}` returns: its details plus `content` and `citations`. A
    citation's `url`, when given, must be an `http://` or `https://` address; anything else is refused
    with a 400 naming `/citations/N/url`.

    Args:
        clinic_id (UUID):
        idempotency_key (str | Unset):
        body (NoteCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNoteResponse200 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: NoteCreateRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateNoteResponse200 | Problem]:
    """Create a DRAFT note. Always status=draft — this route can never sign, lock, finalize or co-sign.

     Unknown content keys are refused (unknown_field) naming both the offending keys and the full valid
    list for whichever template note_type/custom_template_id resolves to. The answer is the full note,
    the same object `GET …/notes/{note_id}` returns: its details plus `content` and `citations`. A
    citation's `url`, when given, must be an `http://` or `https://` address; anything else is refused
    with a 400 naming `/citations/N/url`.

    Args:
        clinic_id (UUID):
        idempotency_key (str | Unset):
        body (NoteCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNoteResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    *,
    client: AuthenticatedClient,
    body: NoteCreateRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateNoteResponse200 | Problem | None:
    """Create a DRAFT note. Always status=draft — this route can never sign, lock, finalize or co-sign.

     Unknown content keys are refused (unknown_field) naming both the offending keys and the full valid
    list for whichever template note_type/custom_template_id resolves to. The answer is the full note,
    the same object `GET …/notes/{note_id}` returns: its details plus `content` and `citations`. A
    citation's `url`, when given, must be an `http://` or `https://` address; anything else is refused
    with a 400 naming `/citations/N/url`.

    Args:
        clinic_id (UUID):
        idempotency_key (str | Unset):
        body (NoteCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNoteResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
