from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_stock_batch_status_status import ExternalStockBatchStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalStockBatchStatus")


@_attrs_define
class ExternalStockBatchStatus:
    """
    Attributes:
        batch_id (UUID):
        status (ExternalStockBatchStatusStatus):
        feed_source (None | str | Unset):
        as_of (datetime.datetime | None | Unset):
        item_count (int | None | Unset):
        matched_count (int | None | Unset):
        unmatched_count (int | None | Unset):
        rejected_reason (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    batch_id: UUID
    status: ExternalStockBatchStatusStatus
    feed_source: None | str | Unset = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
    item_count: int | None | Unset = UNSET
    matched_count: int | None | Unset = UNSET
    unmatched_count: int | None | Unset = UNSET
    rejected_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = str(self.batch_id)

        status = self.status.value

        feed_source: None | str | Unset
        if isinstance(self.feed_source, Unset):
            feed_source = UNSET
        else:
            feed_source = self.feed_source

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        item_count: int | None | Unset
        if isinstance(self.item_count, Unset):
            item_count = UNSET
        else:
            item_count = self.item_count

        matched_count: int | None | Unset
        if isinstance(self.matched_count, Unset):
            matched_count = UNSET
        else:
            matched_count = self.matched_count

        unmatched_count: int | None | Unset
        if isinstance(self.unmatched_count, Unset):
            unmatched_count = UNSET
        else:
            unmatched_count = self.unmatched_count

        rejected_reason: None | str | Unset
        if isinstance(self.rejected_reason, Unset):
            rejected_reason = UNSET
        else:
            rejected_reason = self.rejected_reason

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_id": batch_id,
                "status": status,
            }
        )
        if feed_source is not UNSET:
            field_dict["feed_source"] = feed_source
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if matched_count is not UNSET:
            field_dict["matched_count"] = matched_count
        if unmatched_count is not UNSET:
            field_dict["unmatched_count"] = unmatched_count
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_id = UUID(d.pop("batch_id"))

        status = ExternalStockBatchStatusStatus(d.pop("status"))

        def _parse_feed_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feed_source = _parse_feed_source(d.pop("feed_source", UNSET))

        def _parse_as_of(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        as_of = _parse_as_of(d.pop("as_of", UNSET))

        def _parse_item_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item_count = _parse_item_count(d.pop("item_count", UNSET))

        def _parse_matched_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        matched_count = _parse_matched_count(d.pop("matched_count", UNSET))

        def _parse_unmatched_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unmatched_count = _parse_unmatched_count(d.pop("unmatched_count", UNSET))

        def _parse_rejected_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejected_reason = _parse_rejected_reason(d.pop("rejected_reason", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        external_stock_batch_status = cls(
            batch_id=batch_id,
            status=status,
            feed_source=feed_source,
            as_of=as_of,
            item_count=item_count,
            matched_count=matched_count,
            unmatched_count=unmatched_count,
            rejected_reason=rejected_reason,
            created_at=created_at,
        )

        external_stock_batch_status.additional_properties = d
        return external_stock_batch_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
