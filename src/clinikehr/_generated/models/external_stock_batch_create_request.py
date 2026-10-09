from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.external_stock_batch_row import ExternalStockBatchRow


T = TypeVar("T", bound="ExternalStockBatchCreateRequest")


@_attrs_define
class ExternalStockBatchCreateRequest:
    """
    Attributes:
        batch_id (UUID): Client-generated. Doubles as the idempotency key — a replay returns the stored result, never
            reprocesses.
        as_of (datetime.datetime): Clamped server-side to [now-30d, now].
        feed_source (str):
        rows (list[ExternalStockBatchRow]):
    """

    batch_id: UUID
    as_of: datetime.datetime
    feed_source: str
    rows: list[ExternalStockBatchRow]

    def to_dict(self) -> dict[str, Any]:
        batch_id = str(self.batch_id)

        as_of = self.as_of.isoformat()

        feed_source = self.feed_source

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "batch_id": batch_id,
                "as_of": as_of,
                "feed_source": feed_source,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_stock_batch_row import ExternalStockBatchRow  # noqa: PLC0415

        d = dict(src_dict)
        batch_id = UUID(d.pop("batch_id"))

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        feed_source = d.pop("feed_source")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ExternalStockBatchRow.from_dict(rows_item_data)

            rows.append(rows_item)

        external_stock_batch_create_request = cls(
            batch_id=batch_id,
            as_of=as_of,
            feed_source=feed_source,
            rows=rows,
        )

        return external_stock_batch_create_request
