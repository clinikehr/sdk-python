import json

import httpx
import pytest

from clinikehr import create_client, raise_for_response
from clinikehr._generated.api.me import get_me
from clinikehr.errors import ClinikEHRApiError
from clinikehr.transport import AsyncRetryTransport, RetryTransport


def _mock_client(handler) -> httpx.Client:
    """A plain httpx.Client over a MockTransport — used to test the GENERATED call + raise_for_response integration without going through create_client's real network transport."""
    from clinikehr._generated import AuthenticatedClient

    ac = AuthenticatedClient(base_url="https://example.test/v1", token="ehr_test_fakekey")
    ac.set_httpx_client(
        httpx.Client(
            base_url="https://example.test/v1",
            headers={"Authorization": "Bearer ehr_test_fakekey"},
            transport=httpx.MockTransport(handler),
        )
    )
    return ac


def test_generated_call_sends_bearer_auth_and_parses_a_success_response():
    seen_auth = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen_auth["value"] = request.headers.get("authorization")
        return httpx.Response(
            200,
            json={"key_id": "k1", "clinic_id": None, "environment": "test", "scopes": [], "org_id": None, "sandbox": False},
        )

    client = _mock_client(handler)
    response = get_me.sync_detailed(client=client)
    assert seen_auth["value"] == "Bearer ehr_test_fakekey"
    me = raise_for_response(response)
    assert me.key_id == "k1"


def test_raise_for_response_raises_clinikehr_api_error_on_a_problem_response():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            403,
            json={"type": "https://developer.clinikehr.com/errors/scope_missing", "title": "Scope missing", "status": 403, "code": "scope_missing", "request_id": "req-1"},
        )

    client = _mock_client(handler)
    response = get_me.sync_detailed(client=client)
    with pytest.raises(ClinikEHRApiError) as excinfo:
        raise_for_response(response)
    assert excinfo.value.status == 403
    assert excinfo.value.code == "scope_missing"
    assert excinfo.value.request_id == "req-1"


def test_raise_for_response_carries_retry_after_on_429():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429,
            headers={"retry-after": "9"},
            json={"type": "https://developer.clinikehr.com/errors/rate_limited", "title": "Rate limited", "status": 429, "code": "rate_limited", "request_id": "req-2"},
        )

    client = _mock_client(handler)
    response = get_me.sync_detailed(client=client)
    with pytest.raises(ClinikEHRApiError) as excinfo:
        raise_for_response(response)
    assert excinfo.value.retry_after_seconds == 9
    assert excinfo.value.is_retryable is True


class TestCreateClient:
    def test_requires_api_key(self):
        with pytest.raises(ValueError):
            create_client("")

    def test_installs_a_retry_transport_on_the_sync_client(self):
        client = create_client("ehr_test_fakekey", base_url="https://example.test/v1")
        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client._transport, RetryTransport)

    def test_installs_an_async_retry_transport_on_the_async_client(self):
        client = create_client("ehr_test_fakekey", base_url="https://example.test/v1")
        async_httpx_client = client.get_async_httpx_client()
        assert isinstance(async_httpx_client._transport, AsyncRetryTransport)

    def test_fhir_flag_sets_accept_header(self):
        client = create_client("ehr_test_fakekey", base_url="https://example.test/v1", fhir=True)
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers.get("accept") == "application/fhir+json"

    def test_no_fhir_by_default(self):
        client = create_client("ehr_test_fakekey", base_url="https://example.test/v1")
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers.get("accept") != "application/fhir+json"


class TestTheUrlActuallyRequested:
    """0.1.0 requested /v1/v1/... (the base repeated /v1) and every call was a 404. Assert the real URL."""

    def _url(self, **kwargs) -> str:
        client = create_client("ehr_test_fakekey", **kwargs)
        return str(client.get_httpx_client().build_request("GET", "/v1/me").url)

    def test_default_reaches_exactly_one_v1(self):
        assert self._url() == "https://api.clinikehr.com/v1/me"

    def test_a_base_ending_in_v1_is_not_doubled(self):
        assert self._url(base_url="https://api.clinikehr.com/v1") == "https://api.clinikehr.com/v1/me"
        assert self._url(base_url="https://api.clinikehr.com/v1/") == "https://api.clinikehr.com/v1/me"
        assert self._url(base_url="https://proxy.example.com") == "https://proxy.example.com/v1/me"

    def test_the_async_client_uses_the_same_base(self):
        client = create_client("ehr_test_fakekey")
        assert str(client.get_async_httpx_client().build_request("GET", "/v1/me").url) == "https://api.clinikehr.com/v1/me"
