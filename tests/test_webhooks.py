"""
Vectors produced by running the API's own webhook signer under Deno — not
re-derived by this test file. If this verifier disagrees with these vectors,
the verifier is wrong; the signer is the source of truth.
"""

import json
from pathlib import Path

import pytest

from clinikehr.errors import WebhookVerificationError
from clinikehr.webhooks import verify_webhook

VECTORS_PATH = Path(__file__).resolve().parent / "fixtures" / "webhook-signing-vectors.json"
VECTORS = json.loads(VECTORS_PATH.read_text())["vectors"]

TEN_YEARS = 10 * 365 * 24 * 3600


def _now_for(vector) -> float:
    return float(vector["headers"]["webhook-timestamp"]) + 30


@pytest.mark.parametrize("vector", VECTORS, ids=[v["name"] for v in VECTORS])
def test_verifies_against_its_own_secrets(vector):
    verify_webhook(vector["headers"], vector["body"], secrets=vector["secrets"], tolerance_seconds=TEN_YEARS, now=_now_for(vector))


def test_rotation_overlap_verifies_against_either_secret_alone():
    vector = next(v for v in VECTORS if v["name"] == "two_secrets_rotation_overlap")
    verify_webhook(vector["headers"], vector["body"], secrets=[vector["secrets"][0]], tolerance_seconds=TEN_YEARS, now=_now_for(vector))
    verify_webhook(vector["headers"], vector["body"], secrets=[vector["secrets"][1]], tolerance_seconds=TEN_YEARS, now=_now_for(vector))


def test_fails_with_the_wrong_secret():
    vector = next(v for v in VECTORS if v["name"] == "single_secret_simple_body")
    with pytest.raises(WebhookVerificationError):
        verify_webhook(vector["headers"], vector["body"], secrets=["whsec_" + "ff" * 24], tolerance_seconds=TEN_YEARS, now=_now_for(vector))


def test_fails_if_the_body_was_tampered_with():
    vector = next(v for v in VECTORS if v["name"] == "single_secret_simple_body")
    tampered = vector["body"].replace("stock_changed", "stock_change_")
    with pytest.raises(WebhookVerificationError):
        verify_webhook(vector["headers"], tampered, secrets=vector["secrets"], tolerance_seconds=TEN_YEARS, now=_now_for(vector))


def test_fails_outside_timestamp_tolerance():
    vector = next(v for v in VECTORS if v["name"] == "single_secret_simple_body")
    with pytest.raises(WebhookVerificationError):
        # `now` defaults to time.time() — the vector's timestamp is years in the past.
        verify_webhook(vector["headers"], vector["body"], secrets=vector["secrets"], tolerance_seconds=300)


def test_passes_within_default_five_minute_tolerance():
    vector = next(v for v in VECTORS if v["name"] == "single_secret_simple_body")
    now = float(vector["headers"]["webhook-timestamp"]) + 60
    verify_webhook(vector["headers"], vector["body"], secrets=vector["secrets"], now=now)


def test_throws_never_returns_false_on_missing_signature_header():
    vector = next(v for v in VECTORS if v["name"] == "single_secret_simple_body")
    headers = {**vector["headers"], "webhook-signature": ""}
    with pytest.raises(WebhookVerificationError):
        verify_webhook(headers, vector["body"], secrets=vector["secrets"], tolerance_seconds=TEN_YEARS, now=_now_for(vector))
