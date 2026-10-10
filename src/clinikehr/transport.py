"""
The httpx transport that implements retry + automatic Idempotency-Key.

Both live at the TRANSPORT layer (below every generated ``api.*`` call) so
they apply uniformly to EVERY operation without a per-endpoint wrapper —
mirroring the TypeScript SDK's approach of wrapping ``openapi-fetch``'s
generated, typed methods rather than hand-writing one function per route.

Idempotency-Key generation happens in an httpx REQUEST EVENT HOOK, which
fires exactly once per logical call, before this transport's retry loop
starts resending the SAME ``httpx.Request`` object — so the key is generated
once and naturally reused on every retry of that call, never regenerated.
"""

from __future__ import annotations

import asyncio
import time
import uuid
from collections.abc import Awaitable, Callable

import httpx

from .retry import RetryPolicyOptions, decide_retry


def ensure_idempotency_key(request: httpx.Request) -> None:
    """Request event hook: generates an ``Idempotency-Key`` for a POST or PATCH with none, in place (several PATCH routes require one). A caller who set their own is never overridden; DELETE carries one only when the caller sets it; PATCH is still never retried."""
    if request.method.upper() in ("POST", "PATCH") and "idempotency-key" not in {k.lower() for k in request.headers}:
        request.headers["Idempotency-Key"] = str(uuid.uuid4())


class RetryTransport(httpx.BaseTransport):
    """
    Wraps an inner ``httpx.BaseTransport`` and retries a request per
    :func:`clinikehr.retry.decide_retry` — see that module for the exact
    rule (429 always; 5xx/transport only for GET/HEAD or a request already
    carrying ``Idempotency-Key``; PATCH never).
    """

    def __init__(self, inner: httpx.BaseTransport, *, options: RetryPolicyOptions | None = None, sleep: Callable[[float], None] = time.sleep) -> None:
        self._inner = inner
        self._options = options or RetryPolicyOptions()
        self._sleep = sleep

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        has_idempotency_key = "idempotency-key" in {k.lower() for k in request.headers}
        attempt = 0
        while True:
            try:
                response = self._inner.handle_request(request)
            except httpx.HTTPError as exc:
                decision = decide_retry(method=request.method, has_idempotency_key=has_idempotency_key, attempt=attempt, options=self._options)
                if not decision.should_retry:
                    raise
                self._sleep(decision.delay_ms / 1000)
                attempt += 1
                continue

            if response.status_code < 400:
                return response

            retry_after_seconds: float | None = None
            retry_after_header = response.headers.get("retry-after")
            if retry_after_header is not None:
                try:
                    retry_after_seconds = float(retry_after_header)
                except ValueError:
                    retry_after_seconds = None

            decision = decide_retry(
                method=request.method,
                has_idempotency_key=has_idempotency_key,
                attempt=attempt,
                status=response.status_code,
                retry_after_seconds=retry_after_seconds,
                options=self._options,
            )
            if not decision.should_retry:
                return response
            response.close()
            self._sleep(decision.delay_ms / 1000)
            attempt += 1

    def close(self) -> None:
        self._inner.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """The ``asyncio`` twin of :class:`RetryTransport` — same rule, same decision function, `await`ed."""

    def __init__(
        self,
        inner: httpx.AsyncBaseTransport,
        *,
        options: RetryPolicyOptions | None = None,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self._inner = inner
        self._options = options or RetryPolicyOptions()
        self._sleep = sleep

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        has_idempotency_key = "idempotency-key" in {k.lower() for k in request.headers}
        attempt = 0
        while True:
            try:
                response = await self._inner.handle_async_request(request)
            except httpx.HTTPError as exc:
                decision = decide_retry(method=request.method, has_idempotency_key=has_idempotency_key, attempt=attempt, options=self._options)
                if not decision.should_retry:
                    raise
                await self._sleep(decision.delay_ms / 1000)
                attempt += 1
                continue

            if response.status_code < 400:
                return response

            retry_after_seconds: float | None = None
            retry_after_header = response.headers.get("retry-after")
            if retry_after_header is not None:
                try:
                    retry_after_seconds = float(retry_after_header)
                except ValueError:
                    retry_after_seconds = None

            decision = decide_retry(
                method=request.method,
                has_idempotency_key=has_idempotency_key,
                attempt=attempt,
                status=response.status_code,
                retry_after_seconds=retry_after_seconds,
                options=self._options,
            )
            if not decision.should_retry:
                return response
            await response.aclose()
            await self._sleep(decision.delay_ms / 1000)
            attempt += 1

    async def aclose(self) -> None:
        await self._inner.aclose()
