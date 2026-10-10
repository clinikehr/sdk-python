from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="InsurancePaymentAdviceAllocation")


@_attrs_define
class InsurancePaymentAdviceAllocation:
    """
    Attributes:
        claim_id (UUID):
        amount (float):
    """

    claim_id: UUID
    amount: float

    def to_dict(self) -> dict[str, Any]:
        claim_id = str(self.claim_id)

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "claim_id": claim_id,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim_id = UUID(d.pop("claim_id"))

        amount = d.pop("amount")

        insurance_payment_advice_allocation = cls(
            claim_id=claim_id,
            amount=amount,
        )

        return insurance_payment_advice_allocation
