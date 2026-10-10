"""
Retry policy — byte-for-byte the same RULE as the TypeScript SDK's
``retry.ts`` (see that file's header for the full rationale; repeated here
only in outline so this file stands alone):

  - a 429 (``rate_limited``) is ALWAYS retryable.
  - a 5xx or a transport failure is retryable only for a GET/HEAD, or a
    request that carried an ``Idempotency-Key`` (POST, or a DELETE the caller keyed).
  - PATCH is NEVER retried on a 5xx/transport failure, even though it
    carries an ``Idempotency-Key`` (some PATCH routes require one) — a
    stale ``If-Match`` is a different, correct 412, not a transient failure.
  - any other 4xx is never retried.
"""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicyOptions:
    max_attempts: int = 4
    base_delay_ms: int = 500
    max_delay_ms: int = 8_000


DEFAULT_RETRY_OPTIONS = RetryPolicyOptions()


@dataclass(frozen=True)
class RetryDecision:
    should_retry: bool
    delay_ms: float


def _is_repeatable(method: str, has_idempotency_key: bool) -> bool:
    m = method.upper()
    if m in ("GET", "HEAD"):
        return True
    if m == "PATCH":
        return False
    return has_idempotency_key


def _backoff_delay_ms(attempt: int, opts: RetryPolicyOptions) -> float:
    raw = min(opts.max_delay_ms, opts.base_delay_ms * (2**attempt))
    return random.random() * raw


def decide_retry(
    *,
    method: str,
    has_idempotency_key: bool,
    attempt: int,
    status: int | None = None,
    retry_after_seconds: float | None = None,
    options: RetryPolicyOptions = DEFAULT_RETRY_OPTIONS,
) -> RetryDecision:
    if attempt + 1 >= options.max_attempts:
        return RetryDecision(should_retry=False, delay_ms=0)

    is_rate_limited = status == 429
    is_server_error = status is not None and status >= 500
    is_transport_failure = status is None

    if is_rate_limited:
        delay_ms = max(0.0, retry_after_seconds * 1000) if retry_after_seconds is not None else _backoff_delay_ms(attempt, options)
        return RetryDecision(should_retry=True, delay_ms=delay_ms)

    if (is_server_error or is_transport_failure) and _is_repeatable(method, has_idempotency_key):
        return RetryDecision(should_retry=True, delay_ms=_backoff_delay_ms(attempt, options))

    return RetryDecision(should_retry=False, delay_ms=0)
