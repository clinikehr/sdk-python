"""
Standard Webhooks verifier. It mirrors the API's webhook signing scheme
exactly (same secret-decoding rule, same signed string, same header shape);
the test vectors in ``tests/fixtures/webhook-signing-vectors.json`` were
produced by the API's own signer, not re-derived here.

During a secret rotation the API sends two signatures for an overlap window.
Consumers should reject timestamps older than 5 minutes and dedupe on
`webhook-id`. Deduping is the caller's own idempotent-handler job — this
module checks the signature and the timestamp tolerance only.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import re
import time
from dataclasses import dataclass

from .errors import WebhookVerificationError

_HEX_RE = re.compile(r"^[0-9a-f]+$", re.IGNORECASE)


def _secret_key_bytes(whsec: str) -> bytes:
    """Byte-for-byte the same rule as signing.ts's secretKeyBytes: hex-decode
    an even-length hex remainder, else treat as literal UTF-8 key material."""
    raw = whsec[len("whsec_") :] if whsec.startswith("whsec_") else whsec
    if _HEX_RE.match(raw) and len(raw) % 2 == 0:
        return bytes.fromhex(raw)
    return raw.encode("utf-8")


def _hmac_sha256_base64(key: bytes, message: str) -> str:
    digest = hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


@dataclass(frozen=True)
class WebhookHeaders:
    webhook_id: str
    webhook_timestamp: str
    webhook_signature: str

    @classmethod
    def from_mapping(cls, headers: dict) -> "WebhookHeaders":
        """Accepts either underscore or hyphen header names (a caller reading
        raw HTTP headers has hyphens; one building this from a dict of kwargs
        may have underscores) — case-insensitive on the hyphen form."""
        lower = {str(k).lower(): v for k, v in headers.items()}
        return cls(
            webhook_id=str(lower.get("webhook-id") or lower.get("webhook_id") or ""),
            webhook_timestamp=str(lower.get("webhook-timestamp") or lower.get("webhook_timestamp") or ""),
            webhook_signature=str(lower.get("webhook-signature") or lower.get("webhook_signature") or ""),
        )


def verify_webhook(
    headers: dict | WebhookHeaders,
    raw_body: str,
    *,
    secrets: list[str],
    tolerance_seconds: float = 300,
    now: float | None = None,
) -> None:
    """
    Verifies a webhook delivery. Raises :class:`WebhookVerificationError`
    (never returns ``False``) when the timestamp is missing/stale, or no
    signature term matches any provided secret. Returns nothing on success.

    :param secrets: one or two ``whsec_…`` values — pass BOTH during a
        rotation's overlap window (current, previous).
    :param now: epoch SECONDS to compare against (defaults to ``time.time()``);
        injectable for tests.
    """
    h = headers if isinstance(headers, WebhookHeaders) else WebhookHeaders.from_mapping(headers)

    try:
        timestamp = int(h.webhook_timestamp)
    except (TypeError, ValueError):
        raise WebhookVerificationError("webhook-timestamp is missing or not a valid integer.") from None

    current = now if now is not None else time.time()
    age_seconds = abs(current - timestamp)
    if age_seconds > tolerance_seconds:
        raise WebhookVerificationError(f"webhook-timestamp is outside the {tolerance_seconds}s tolerance (age {age_seconds:.0f}s).")

    if not h.webhook_id:
        raise WebhookVerificationError("webhook-id is missing.")

    presented = [term.strip() for term in (h.webhook_signature or "").split(" ") if term.strip()]
    if not presented:
        raise WebhookVerificationError("webhook-signature is missing.")

    to_sign = f"{h.webhook_id}.{h.webhook_timestamp}.{raw_body}"
    expected = [f"v1,{_hmac_sha256_base64(_secret_key_bytes(secret), to_sign)}" for secret in secrets if secret]

    matched = any(hmac.compare_digest(term, exp) for term in presented for exp in expected)
    if not matched:
        raise WebhookVerificationError("No signature in webhook-signature matched any provided secret.")
