"""Official Python client for the ClinikEHR API (api.clinikehr.com)."""

from .client import create_client, raise_for_response
from .errors import ClinikEHRApiError, TransportError, WebhookVerificationError
from .pagination import CursorPage, paginate
from .retry import DEFAULT_RETRY_OPTIONS, RetryPolicyOptions, decide_retry
from .webhooks import WebhookHeaders, verify_webhook

# The generated core — full typed access to every operation and model is at
# `clinikehr._generated.api.<tag>.<operation>` / `clinikehr._generated.models.*`.
# The leading underscore names it as this package's own implementation detail
# (never hand-edit it; regenerate with `ehr-api-generate-sdks.mjs --py-only`),
# not that it is unusable — a Python package attribute alias (`generated = ...`)
# cannot make `from clinikehr.generated.api.x import y` resolve (Python's
# import machinery needs a REAL module at that dotted path, not merely an
# attribute equal to one), so this SDK does not pretend otherwise with a
# broken shortcut. Import the real path directly; see the README.

__all__ = (
    "create_client",
    "raise_for_response",
    "ClinikEHRApiError",
    "TransportError",
    "WebhookVerificationError",
    "CursorPage",
    "paginate",
    "DEFAULT_RETRY_OPTIONS",
    "RetryPolicyOptions",
    "decide_retry",
    "WebhookHeaders",
    "verify_webhook",
)

__version__ = "0.2.0"
