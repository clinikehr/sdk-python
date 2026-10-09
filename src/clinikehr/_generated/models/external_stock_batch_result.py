from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_stock_batch_result_rejected_reason_type_1 import ExternalStockBatchResultRejectedReasonType1
from ..models.external_stock_batch_result_rejected_reason_type_2_type_1 import (
    ExternalStockBatchResultRejectedReasonType2Type1,
)
from ..models.external_stock_batch_result_rejected_reason_type_3_type_1 import (
    ExternalStockBatchResultRejectedReasonType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalStockBatchResult")


@_attrs_define
class ExternalStockBatchResult:
    """
    Attributes:
        ok (bool):
        batch_id (UUID):
        item_count (int | None | Unset):
        matched_count (int | None | Unset):
        unmatched_count (int | None | Unset):
        rejected (bool | None | Unset):
        rejected_reason (ExternalStockBatchResultRejectedReasonType1 | ExternalStockBatchResultRejectedReasonType2Type1
            | ExternalStockBatchResultRejectedReasonType3Type1 | None | Unset):
        replayed (bool | None | Unset):
    """

    ok: bool
    batch_id: UUID
    item_count: int | None | Unset = UNSET
    matched_count: int | None | Unset = UNSET
    unmatched_count: int | None | Unset = UNSET
    rejected: bool | None | Unset = UNSET
    rejected_reason: (
        ExternalStockBatchResultRejectedReasonType1
        | ExternalStockBatchResultRejectedReasonType2Type1
        | ExternalStockBatchResultRejectedReasonType3Type1
        | None
        | Unset
    ) = UNSET
    replayed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        batch_id = str(self.batch_id)

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

        rejected: bool | None | Unset
        if isinstance(self.rejected, Unset):
            rejected = UNSET
        else:
            rejected = self.rejected

        rejected_reason: None | str | Unset
        if isinstance(self.rejected_reason, Unset):
            rejected_reason = UNSET
        elif isinstance(self.rejected_reason, ExternalStockBatchResultRejectedReasonType1):
            rejected_reason = self.rejected_reason.value
        elif isinstance(self.rejected_reason, ExternalStockBatchResultRejectedReasonType2Type1):
            rejected_reason = self.rejected_reason.value
        elif isinstance(self.rejected_reason, ExternalStockBatchResultRejectedReasonType3Type1):
            rejected_reason = self.rejected_reason.value
        else:
            rejected_reason = self.rejected_reason

        replayed: bool | None | Unset
        if isinstance(self.replayed, Unset):
            replayed = UNSET
        else:
            replayed = self.replayed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ok": ok,
                "batch_id": batch_id,
            }
        )
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if matched_count is not UNSET:
            field_dict["matched_count"] = matched_count
        if unmatched_count is not UNSET:
            field_dict["unmatched_count"] = unmatched_count
        if rejected is not UNSET:
            field_dict["rejected"] = rejected
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if replayed is not UNSET:
            field_dict["replayed"] = replayed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        batch_id = UUID(d.pop("batch_id"))

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

        def _parse_rejected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rejected = _parse_rejected(d.pop("rejected", UNSET))

        def _parse_rejected_reason(
            data: object,
        ) -> (
            ExternalStockBatchResultRejectedReasonType1
            | ExternalStockBatchResultRejectedReasonType2Type1
            | ExternalStockBatchResultRejectedReasonType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_reason_type_1 = ExternalStockBatchResultRejectedReasonType1(data)

                return rejected_reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_reason_type_2_type_1 = ExternalStockBatchResultRejectedReasonType2Type1(data)

                return rejected_reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_reason_type_3_type_1 = ExternalStockBatchResultRejectedReasonType3Type1(data)

                return rejected_reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ExternalStockBatchResultRejectedReasonType1
                | ExternalStockBatchResultRejectedReasonType2Type1
                | ExternalStockBatchResultRejectedReasonType3Type1
                | None
                | Unset,
                data,
            )

        rejected_reason = _parse_rejected_reason(d.pop("rejected_reason", UNSET))

        def _parse_replayed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        replayed = _parse_replayed(d.pop("replayed", UNSET))

        external_stock_batch_result = cls(
            ok=ok,
            batch_id=batch_id,
            item_count=item_count,
            matched_count=matched_count,
            unmatched_count=unmatched_count,
            rejected=rejected,
            rejected_reason=rejected_reason,
            replayed=replayed,
        )

        external_stock_batch_result.additional_properties = d
        return external_stock_batch_result

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
