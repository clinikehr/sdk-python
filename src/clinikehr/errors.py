"""
Typed errors from the API's RFC 9457 ``application/problem+json`` shape.
Mirrors the API's error body field-for-field — this module types the shape
the API actually returns, and does not invent a second one. Same fields, same names, as the
TypeScript SDK's ``errors.ts``, for parity between the two languages.
"""

from __future__ import annotations

from typing import Any


class ClinikEHRApiError(Exception):
    """
    Raised for every request that reached the server and got back a
    ``problem+json`` error. Never raised for a network-level failure: that surfaces as ``httpx``'s own
    exception (``httpx.ConnectError``, ``httpx.TimeoutException``, ...) once the retry policy has run out.
    """

    def __init__(
        self,
        *,
        status: int,
        code: str,
        title: str,
        request_id: str,
        detail: str | None = None,
        errors: list[dict[str, Any]] | None = None,
        retry_after_seconds: float | None = None,
        raw: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(detail or title)
        self.status = status
        self.code = code
        self.title = title
        self.request_id = request_id
        self.detail = detail
        self.errors = errors or []
        self.retry_after_seconds = retry_after_seconds
        self.raw = raw or {}

    @property
    def is_retryable(self) -> bool:
        """``True`` for a 429 (``rate_limited``) or any 5xx."""
        return self.status == 429 or self.status >= 500

    @classmethod
    def from_problem_dict(cls, problem: dict[str, Any], *, retry_after_seconds: float | None = None) -> ClinikEHRApiError:
        return cls(
            status=int(problem.get("status", 0)),
            code=str(problem.get("code", "unknown_error")),
            title=str(problem.get("title", "Error")),
            request_id=str(problem.get("request_id", "")),
            detail=problem.get("detail"),
            errors=problem.get("errors"),
            retry_after_seconds=retry_after_seconds,
            raw=problem,
        )

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"ClinikEHRApiError(status={self.status!r}, code={self.code!r}, request_id={self.request_id!r})"


class TransportError(Exception):
    """Reserved for a network-level failure (DNS, TCP, TLS, a timeout). Not raised by 0.1.x: today such a
    failure surfaces as ``httpx``'s own exception, as the README says. Exported so code can name it once it is."""

    def __init__(self, message: str, *, cause: BaseException | None = None) -> None:
        super().__init__(message)
        self.__cause__ = cause


class WebhookVerificationError(Exception):
    """Raised by :func:`clinikehr.webhooks.verify_webhook` — never a returned ``False``."""
