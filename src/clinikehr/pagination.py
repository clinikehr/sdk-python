"""
Cursor pagination: ``{ data: [], has_more: true, next_cursor: "…" }``,
cursors opaque and signed, no offset, no total count.
"""

from __future__ import annotations

from collections.abc import Callable, Generator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class CursorPage(Generic[T]):
    data: list[T]
    has_more: bool
    next_cursor: str | None


def paginate(fetch_page: Callable[[str | None], CursorPage[T]]) -> Generator[T, None, None]:
    """
    Lazily yields every row across every page. ``fetch_page`` is called with
    ``None`` for the first page, then with each page's own ``next_cursor``.
    Fetches ONE page ahead only when the previous page's rows are exhausted —
    a caller that stops iterating early never triggers a page it never asked
    to see.
    """
    cursor: str | None = None
    while True:
        page = fetch_page(cursor)
        yield from page.data
        if not page.has_more or not page.next_cursor:
            return
        cursor = page.next_cursor


# Async pagination is intentionally NOT a separate generator here: the
# generated client's `asyncio`/`asyncio_detailed` functions are already
# coroutines, and an async generator wrapping them is a two-line
# `async for` loop at the call site — see the README's "Pagination (async)"
# section. A second, parallel iterator implementation for a two-line
# difference was judged not worth the duplicate surface to maintain.
