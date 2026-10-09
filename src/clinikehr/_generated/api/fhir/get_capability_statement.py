from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_capability_statement_response_200 import GetCapabilityStatementResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCapabilityStatementResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCapabilityStatementResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCapabilityStatementResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCapabilityStatementResponse200]:
    """FHIR R4 CapabilityStatement — exactly what this gateway supports, nothing more.

     No bearer key required (this is the same discovery document for every caller); Content-Type is
    application/fhir+json, not the {data} envelope. Lists ONLY the resources/interactions this gateway
    actually serves — Patient, Appointment, DocumentReference (notes), Condition, AllergyIntolerance,
    MedicationStatement, MedicationRequest, Practitioner (providers), Coverage, Organization (insurance
    payers) and MedicationKnowledge (inventory items), search parameters limited to the query filters
    the plain JSON routes already accept. There is no _include/_revinclude and no general /fhir
    passthrough — see the developer guide (api-docs/fhir.mdx) for what a partner will not find.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCapabilityStatementResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetCapabilityStatementResponse200 | None:
    """FHIR R4 CapabilityStatement — exactly what this gateway supports, nothing more.

     No bearer key required (this is the same discovery document for every caller); Content-Type is
    application/fhir+json, not the {data} envelope. Lists ONLY the resources/interactions this gateway
    actually serves — Patient, Appointment, DocumentReference (notes), Condition, AllergyIntolerance,
    MedicationStatement, MedicationRequest, Practitioner (providers), Coverage, Organization (insurance
    payers) and MedicationKnowledge (inventory items), search parameters limited to the query filters
    the plain JSON routes already accept. There is no _include/_revinclude and no general /fhir
    passthrough — see the developer guide (api-docs/fhir.mdx) for what a partner will not find.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCapabilityStatementResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCapabilityStatementResponse200]:
    """FHIR R4 CapabilityStatement — exactly what this gateway supports, nothing more.

     No bearer key required (this is the same discovery document for every caller); Content-Type is
    application/fhir+json, not the {data} envelope. Lists ONLY the resources/interactions this gateway
    actually serves — Patient, Appointment, DocumentReference (notes), Condition, AllergyIntolerance,
    MedicationStatement, MedicationRequest, Practitioner (providers), Coverage, Organization (insurance
    payers) and MedicationKnowledge (inventory items), search parameters limited to the query filters
    the plain JSON routes already accept. There is no _include/_revinclude and no general /fhir
    passthrough — see the developer guide (api-docs/fhir.mdx) for what a partner will not find.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCapabilityStatementResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetCapabilityStatementResponse200 | None:
    """FHIR R4 CapabilityStatement — exactly what this gateway supports, nothing more.

     No bearer key required (this is the same discovery document for every caller); Content-Type is
    application/fhir+json, not the {data} envelope. Lists ONLY the resources/interactions this gateway
    actually serves — Patient, Appointment, DocumentReference (notes), Condition, AllergyIntolerance,
    MedicationStatement, MedicationRequest, Practitioner (providers), Coverage, Organization (insurance
    payers) and MedicationKnowledge (inventory items), search parameters limited to the query filters
    the plain JSON routes already accept. There is no _include/_revinclude and no general /fhir
    passthrough — see the developer guide (api-docs/fhir.mdx) for what a partner will not find.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCapabilityStatementResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
