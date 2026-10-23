from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_prescription_pickup_collection_response_202 import CreatePrescriptionPickupCollectionResponse202
from ...models.pickup_collection_create import PickupCollectionCreate
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    body: PickupCollectionCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clinics/{clinic_id}/prescription-pickups/{pickup_id}/collection".format(
            clinic_id=quote(str(clinic_id), safe=""),
            pickup_id=quote(str(pickup_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatePrescriptionPickupCollectionResponse202 | Problem | None:
    if response.status_code == 202:
        response_202 = CreatePrescriptionPickupCollectionResponse202.from_dict(response.json())

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
) -> Response[CreatePrescriptionPickupCollectionResponse202 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PickupCollectionCreate,
    idempotency_key: str,
) -> Response[CreatePrescriptionPickupCollectionResponse202 | Problem]:
    """Submit a prescription pickup collection for clinician review.

     Held for review and answers 202 Accepted with a `Location` header pointing at the submission; the
    pickup stays `awaiting` until a clinician confirms it in ClinikEHR, or the clinic has chosen
    automatic acceptance for this key — then it is confirmed immediately and the body already shows
    `review_status: confirmed`. On confirm, staff run the SAME single write path the pharmacy counter
    uses — never a parallel write. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):
        idempotency_key (str):
        body (PickupCollectionCreate): A collection, submitted for clinician review — it never
            writes the pickup directly. `signature_data` follows the clinic's own **Require a
            signature at pickup** setting, which the server reads: when the clinic requires a
            signature, a request without one is refused with `400 signature_required`; when the clinic
            has switched it off, `signature_data` may be omitted and the pickup is recorded unsigned
            (`has_signature: false`). A signature you do send is always checked (PNG data URL, under
            64 KB). To hand over only some lines, list their `line_id` values in `line_ids`; the lines
            left behind stay on a new awaiting pickup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePrescriptionPickupCollectionResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PickupCollectionCreate,
    idempotency_key: str,
) -> CreatePrescriptionPickupCollectionResponse202 | Problem | None:
    """Submit a prescription pickup collection for clinician review.

     Held for review and answers 202 Accepted with a `Location` header pointing at the submission; the
    pickup stays `awaiting` until a clinician confirms it in ClinikEHR, or the clinic has chosen
    automatic acceptance for this key — then it is confirmed immediately and the body already shows
    `review_status: confirmed`. On confirm, staff run the SAME single write path the pharmacy counter
    uses — never a parallel write. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):
        idempotency_key (str):
        body (PickupCollectionCreate): A collection, submitted for clinician review — it never
            writes the pickup directly. `signature_data` follows the clinic's own **Require a
            signature at pickup** setting, which the server reads: when the clinic requires a
            signature, a request without one is refused with `400 signature_required`; when the clinic
            has switched it off, `signature_data` may be omitted and the pickup is recorded unsigned
            (`has_signature: false`). A signature you do send is always checked (PNG data URL, under
            64 KB). To hand over only some lines, list their `line_id` values in `line_ids`; the lines
            left behind stay on a new awaiting pickup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePrescriptionPickupCollectionResponse202 | Problem
    """

    return sync_detailed(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PickupCollectionCreate,
    idempotency_key: str,
) -> Response[CreatePrescriptionPickupCollectionResponse202 | Problem]:
    """Submit a prescription pickup collection for clinician review.

     Held for review and answers 202 Accepted with a `Location` header pointing at the submission; the
    pickup stays `awaiting` until a clinician confirms it in ClinikEHR, or the clinic has chosen
    automatic acceptance for this key — then it is confirmed immediately and the body already shows
    `review_status: confirmed`. On confirm, staff run the SAME single write path the pharmacy counter
    uses — never a parallel write. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):
        idempotency_key (str):
        body (PickupCollectionCreate): A collection, submitted for clinician review — it never
            writes the pickup directly. `signature_data` follows the clinic's own **Require a
            signature at pickup** setting, which the server reads: when the clinic requires a
            signature, a request without one is refused with `400 signature_required`; when the clinic
            has switched it off, `signature_data` may be omitted and the pickup is recorded unsigned
            (`has_signature: false`). A signature you do send is always checked (PNG data URL, under
            64 KB). To hand over only some lines, list their `line_id` values in `line_ids`; the lines
            left behind stay on a new awaiting pickup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePrescriptionPickupCollectionResponse202 | Problem]
    """

    kwargs = _get_kwargs(
        clinic_id=clinic_id,
        pickup_id=pickup_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clinic_id: UUID,
    pickup_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PickupCollectionCreate,
    idempotency_key: str,
) -> CreatePrescriptionPickupCollectionResponse202 | Problem | None:
    """Submit a prescription pickup collection for clinician review.

     Held for review and answers 202 Accepted with a `Location` header pointing at the submission; the
    pickup stays `awaiting` until a clinician confirms it in ClinikEHR, or the clinic has chosen
    automatic acceptance for this key — then it is confirmed immediately and the body already shows
    `review_status: confirmed`. On confirm, staff run the SAME single write path the pharmacy counter
    uses — never a parallel write. The `Idempotency-Key` header is REQUIRED.

    Args:
        clinic_id (UUID):
        pickup_id (UUID):
        idempotency_key (str):
        body (PickupCollectionCreate): A collection, submitted for clinician review — it never
            writes the pickup directly. `signature_data` follows the clinic's own **Require a
            signature at pickup** setting, which the server reads: when the clinic requires a
            signature, a request without one is refused with `400 signature_required`; when the clinic
            has switched it off, `signature_data` may be omitted and the pickup is recorded unsigned
            (`has_signature: false`). A signature you do send is always checked (PNG data URL, under
            64 KB). To hand over only some lines, list their `line_id` values in `line_ids`; the lines
            left behind stay on a new awaiting pickup.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePrescriptionPickupCollectionResponse202 | Problem
    """

    return (
        await asyncio_detailed(
            clinic_id=clinic_id,
            pickup_id=pickup_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
