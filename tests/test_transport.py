import asyncio

import httpx
import pytest

from clinikehr.retry import RetryPolicyOptions
from clinikehr.transport import AsyncRetryTransport, RetryTransport, ensure_idempotency_key


class _StubTransport(httpx.BaseTransport):
    """Returns a scripted sequence of responses/exceptions, one per call."""

    def __init__(self, script):
        self.script = list(script)
        self.calls: list[httpx.Request] = []

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.calls.append(request)
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


class _AsyncStubTransport(httpx.AsyncBaseTransport):
    def __init__(self, script):
        self.script = list(script)
        self.calls: list[httpx.Request] = []

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.calls.append(request)
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


def _resp(status: int, headers: dict | None = None) -> httpx.Response:
    return httpx.Response(status_code=status, headers=headers or {}, content=b"{}")


def test_retries_5xx_on_get_and_returns_eventual_success():
    stub = _StubTransport([_resp(503), _resp(200)])
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: None)
    request = httpx.Request("GET", "https://example.test/v1/me")
    response = transport.handle_request(request)
    assert response.status_code == 200
    assert len(stub.calls) == 2


def test_never_retries_5xx_on_post_without_idempotency_key():
    stub = _StubTransport([_resp(503), _resp(200)])
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: None)
    request = httpx.Request("POST", "https://example.test/v1/clinics/x/inventory/items", json={})
    response = transport.handle_request(request)
    assert response.status_code == 503
    assert len(stub.calls) == 1


def test_ensure_idempotency_key_hook_sets_one_uuid_reused_across_retries():
    request = httpx.Request("POST", "https://example.test/v1/x", json={})
    ensure_idempotency_key(request)
    key1 = request.headers["idempotency-key"]

    stub = _StubTransport([_resp(503), _resp(503), _resp(201)])
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=4, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: None)
    response = transport.handle_request(request)
    assert response.status_code == 201
    assert len(stub.calls) == 3
    # The SAME header value on every attempt — the hook ran once, before the retry loop.
    assert all(call.headers["idempotency-key"] == key1 for call in stub.calls)


def test_hook_never_overrides_a_caller_supplied_key():
    request = httpx.Request("POST", "https://example.test/v1/x", json={}, headers={"Idempotency-Key": "caller-chosen"})
    ensure_idempotency_key(request)
    assert request.headers["idempotency-key"] == "caller-chosen"


def test_hook_never_touches_get():
    request = httpx.Request("GET", "https://example.test/v1/me")
    ensure_idempotency_key(request)
    assert "idempotency-key" not in {k.lower() for k in request.headers}


def test_429_honours_retry_after():
    stub = _StubTransport([_resp(429, {"retry-after": "0"}), _resp(200)])
    slept = []
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: slept.append(s))
    request = httpx.Request("GET", "https://example.test/v1/me")
    response = transport.handle_request(request)
    assert response.status_code == 200
    assert slept == [0.0]


def test_transport_failure_on_get_is_retried_and_recovers():
    stub = _StubTransport([httpx.ConnectError("boom"), _resp(200)])
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: None)
    request = httpx.Request("GET", "https://example.test/v1/me")
    response = transport.handle_request(request)
    assert response.status_code == 200


def test_transport_failure_on_post_without_idempotency_key_raises():
    stub = _StubTransport([httpx.ConnectError("boom")])
    transport = RetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: None)
    request = httpx.Request("POST", "https://example.test/v1/x", json={})
    with pytest.raises(httpx.ConnectError):
        transport.handle_request(request)


def test_async_retry_transport_retries_5xx_on_get():
    async def run():
        stub = _AsyncStubTransport([_resp(503), _resp(200)])
        transport = AsyncRetryTransport(stub, options=RetryPolicyOptions(max_attempts=3, base_delay_ms=1, max_delay_ms=2), sleep=lambda s: asyncio.sleep(0))
        request = httpx.Request("GET", "https://example.test/v1/me")
        response = await transport.handle_async_request(request)
        assert response.status_code == 200
        assert len(stub.calls) == 2

    asyncio.run(run())


def test_ensure_idempotency_key_on_patch_but_not_get_or_unkeyed_delete():
    # 0.1.0 keyed POST only, so a PATCH route that requires the header answered 400.
    patch = httpx.Request("PATCH", "https://example.test/v1/x", json={})
    ensure_idempotency_key(patch)
    assert len(patch.headers["Idempotency-Key"]) == 36
    for method in ("GET", "DELETE"):
        r = httpx.Request(method, "https://example.test/v1/x")
        ensure_idempotency_key(r)
        assert "idempotency-key" not in {k.lower() for k in r.headers}
