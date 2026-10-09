"""
``create_client()`` — the ONE hand-written entry point around the generated
core (``clinikehr._generated``). It builds the generated ``AuthenticatedClient``
(bearer-token support, per-operation typed calls) and installs, on BOTH its
sync and async httpx clients independently: automatic ``Idempotency-Key``
on every POST, and the shared retry policy (``clinikehr.retry``).

Every generated operation module still works exactly as
`openapi-python-client`'s own docs describe — this file changes nothing
about how ``clinikehr._generated.api.me.get_me.sync_detailed(client=client)``
is called. It only arranges for the ``client`` you pass to already carry
auth, retry and idempotency.
"""

from __future__ import annotations

from typing import Any

import httpx

from ._generated import AuthenticatedClient
from ._generated.models.problem import Problem
from ._generated.types import Response
from .errors import ClinikEHRApiError
from .retry import DEFAULT_RETRY_OPTIONS, RetryPolicyOptions
from .transport import AsyncRetryTransport, RetryTransport, ensure_idempotency_key

DEFAULT_BASE_URL = "https://api.clinikehr.com/v1"


def create_client(
    api_key: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    fhir: bool = False,
    timeout: httpx.Timeout | float | None = None,
    retry_options: RetryPolicyOptions = DEFAULT_RETRY_OPTIONS,
) -> AuthenticatedClient:
    """
    Builds a generated :class:`AuthenticatedClient`, ready to use with any
    function under ``clinikehr._generated.api.*``.

    :param api_key: ``ehr_live_…`` or ``ehr_test_…``. Read it from your own
        secret store — never hardcode a live key.
    :param fhir: when true, sends ``Accept: application/fhir+json`` (and, on
        a write call whose body you supply, ``Content-Type:
        application/fhir+json``) by default on every request. FHIR content
        types on writes are per-call, since the generated body-serializing
        code sets ``Content-Type: application/json`` itself — see the
        README's FHIR section for the exact override.
    """
    if not api_key:
        raise ValueError("create_client(api_key=...) — api_key is required.")

    headers: dict[str, str] = {}
    if fhir:
        headers["Accept"] = "application/fhir+json"

    client = AuthenticatedClient(base_url=base_url, token=api_key, headers=headers, timeout=timeout)

    # Independent sync/async httpx clients, each with its own typed
    # transport — httpx.Client wants a BaseTransport, httpx.AsyncClient
    # wants an AsyncBaseTransport, and the generated client's shared
    # `httpx_args` dict cannot hold two different transport types for the
    # two constructors it feeds, so this SDK sets each one explicitly
    # instead of routing through `httpx_args`.
    sync_httpx_client = httpx.Client(
        base_url=base_url,
        headers=headers | {"Authorization": f"Bearer {api_key}"},
        timeout=timeout,
        follow_redirects=False,
        transport=RetryTransport(httpx.HTTPTransport(), options=retry_options),
        event_hooks={"request": [ensure_idempotency_key]},
    )
    client.set_httpx_client(sync_httpx_client)

    async_httpx_client = httpx.AsyncClient(
        base_url=base_url,
        headers=headers | {"Authorization": f"Bearer {api_key}"},
        timeout=timeout,
        follow_redirects=False,
        transport=AsyncRetryTransport(httpx.AsyncHTTPTransport(), options=retry_options),
        event_hooks={"request": [ensure_idempotency_key]},
    )
    client.set_async_httpx_client(async_httpx_client)

    return client


def raise_for_response(response: Response[Any]) -> Any:
    """
    Call this with the ``Response`` object any generated
    ``*.sync_detailed()``/``*.asyncio_detailed()`` function returns. Returns
    ``response.parsed`` on success (status < 400); raises
    :class:`ClinikEHRApiError` — built from the parsed ``Problem`` model, or
    a raw JSON fallback if parsing failed for some reason — otherwise.
    """
    if response.status_code < 400:
        return response.parsed

    problem_dict: dict[str, Any] = {}
    if isinstance(response.parsed, Problem):
        problem_dict = response.parsed.to_dict()
    if not problem_dict:
        import json

        try:
            problem_dict = json.loads(response.content)
        except Exception:  # noqa: BLE001 - genuinely anything could go wrong parsing an unknown body
            problem_dict = {}

    retry_after_header = response.headers.get("retry-after")
    retry_after_seconds = None
    if retry_after_header is not None:
        try:
            retry_after_seconds = float(retry_after_header)
        except ValueError:
            retry_after_seconds = None

    if not problem_dict:
        problem_dict = {
            "type": "about:blank",
            "title": "Error",
            "status": int(response.status_code),
            "code": "unknown_error",
            "request_id": response.headers.get("x-request-id", ""),
        }

    raise ClinikEHRApiError.from_problem_dict(problem_dict, retry_after_seconds=retry_after_seconds)
