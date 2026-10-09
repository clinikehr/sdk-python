from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listing_search_request import ListingSearchRequest
from ...models.post_listing_search_response_200 import PostListingSearchResponse200
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: ListingSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostListingSearchResponse200 | Problem | None:
    if response.status_code == 200:
        response_200 = PostListingSearchResponse200.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostListingSearchResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListingSearchRequest,
) -> Response[PostListingSearchResponse200 | Problem]:
    """Search by medicine identity across every listed pharmacy this key's workspace can reach.

     A clinic-owned key always gets an empty result. For a workspace TEST key this searches the
    workspace's own seeded fictional items instead. Fail-closed allow-list — an unlinked or excluded
    item never appears, code or text search alike. Never an exact quantity; band only. Capped at 50
    results.

    Args:
        body (ListingSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostListingSearchResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ListingSearchRequest,
) -> PostListingSearchResponse200 | Problem | None:
    """Search by medicine identity across every listed pharmacy this key's workspace can reach.

     A clinic-owned key always gets an empty result. For a workspace TEST key this searches the
    workspace's own seeded fictional items instead. Fail-closed allow-list — an unlinked or excluded
    item never appears, code or text search alike. Never an exact quantity; band only. Capped at 50
    results.

    Args:
        body (ListingSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostListingSearchResponse200 | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListingSearchRequest,
) -> Response[PostListingSearchResponse200 | Problem]:
    """Search by medicine identity across every listed pharmacy this key's workspace can reach.

     A clinic-owned key always gets an empty result. For a workspace TEST key this searches the
    workspace's own seeded fictional items instead. Fail-closed allow-list — an unlinked or excluded
    item never appears, code or text search alike. Never an exact quantity; band only. Capped at 50
    results.

    Args:
        body (ListingSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostListingSearchResponse200 | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListingSearchRequest,
) -> PostListingSearchResponse200 | Problem | None:
    """Search by medicine identity across every listed pharmacy this key's workspace can reach.

     A clinic-owned key always gets an empty result. For a workspace TEST key this searches the
    workspace's own seeded fictional items instead. Fail-closed allow-list — an unlinked or excluded
    item never appears, code or text search alike. Never an exact quantity; band only. Capped at 50
    results.

    Args:
        body (ListingSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostListingSearchResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
