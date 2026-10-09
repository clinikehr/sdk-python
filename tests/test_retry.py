from clinikehr.retry import DEFAULT_RETRY_OPTIONS, RetryPolicyOptions, decide_retry


def test_429_always_retryable_any_method():
    for method in ("GET", "POST", "PATCH", "DELETE"):
        d = decide_retry(method=method, has_idempotency_key=False, attempt=0, status=429)
        assert d.should_retry is True


def test_429_honours_retry_after_in_milliseconds():
    d = decide_retry(method="GET", has_idempotency_key=False, attempt=0, status=429, retry_after_seconds=3)
    assert d.delay_ms == 3000


def test_5xx_on_get_is_retryable():
    d = decide_retry(method="GET", has_idempotency_key=False, attempt=0, status=503)
    assert d.should_retry is True


def test_5xx_on_post_without_idempotency_key_is_never_retried():
    d = decide_retry(method="POST", has_idempotency_key=False, attempt=0, status=503)
    assert d.should_retry is False


def test_5xx_on_post_with_idempotency_key_is_retried():
    d = decide_retry(method="POST", has_idempotency_key=True, attempt=0, status=503)
    assert d.should_retry is True


def test_5xx_on_patch_is_never_retried_even_with_idempotency_key_claimed():
    d = decide_retry(method="PATCH", has_idempotency_key=True, attempt=0, status=503)
    assert d.should_retry is False


def test_transport_failure_follows_repeatability_rule():
    assert decide_retry(method="GET", has_idempotency_key=False, attempt=0).should_retry is True
    assert decide_retry(method="POST", has_idempotency_key=False, attempt=0).should_retry is False


def test_plain_4xx_never_retried():
    for status in (400, 401, 403, 404, 409, 412, 422):
        assert decide_retry(method="GET", has_idempotency_key=False, attempt=0, status=status).should_retry is False


def test_stops_after_max_attempts():
    opts = RetryPolicyOptions(max_attempts=2, base_delay_ms=1, max_delay_ms=2)
    assert decide_retry(method="GET", has_idempotency_key=False, attempt=0, status=429, options=opts).should_retry is True
    assert decide_retry(method="GET", has_idempotency_key=False, attempt=1, status=429, options=opts).should_retry is False


def test_backoff_delay_never_exceeds_max_delay_ms():
    opts = RetryPolicyOptions(max_attempts=10, base_delay_ms=500, max_delay_ms=1000)
    for attempt in range(8):
        d = decide_retry(method="GET", has_idempotency_key=False, attempt=attempt, status=503, options=opts)
        assert 0 <= d.delay_ms <= 1000
