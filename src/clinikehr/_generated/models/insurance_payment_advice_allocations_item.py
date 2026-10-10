from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsurancePaymentAdviceAllocationsItem")


@_attrs_define
class InsurancePaymentAdviceAllocationsItem:
    """
    Attributes:
        claim_id (UUID | Unset):
        amount (float | Unset):
    """

    claim_id: UUID | Unset = UNSET
    amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim_id: str | Unset = UNSET
        if not isinstance(self.claim_id, Unset):
            claim_id = str(self.claim_id)

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim_id is not UNSET:
            field_dict["claim_id"] = claim_id
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _claim_id = d.pop("claim_id", UNSET)
        claim_id: UUID | Unset
        if isinstance(_claim_id, Unset):
            claim_id = UNSET
        else:
            claim_id = UUID(_claim_id)

        amount = d.pop("amount", UNSET)

        insurance_payment_advice_allocations_item = cls(
            claim_id=claim_id,
            amount=amount,
        )

        insurance_payment_advice_allocations_item.additional_properties = d
        return insurance_payment_advice_allocations_item

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
