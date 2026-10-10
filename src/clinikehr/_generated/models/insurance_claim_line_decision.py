from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.insurance_claim_line_decision_status import InsuranceClaimLineDecisionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="InsuranceClaimLineDecision")


@_attrs_define
class InsuranceClaimLineDecision:
    """
    Attributes:
        item_id (UUID):
        status (InsuranceClaimLineDecisionStatus): `adjusted` approves less than was billed (set `qty_approved` and/or
            `unit_price_approved`); `approved` is exactly as billed.
        qty_approved (int | Unset):
        unit_price_approved (float | Unset):
        reason (str | Unset): Required for `declined` unless the body has a top-level `reason`.
        comment (str | Unset):
    """

    item_id: UUID
    status: InsuranceClaimLineDecisionStatus
    qty_approved: int | Unset = UNSET
    unit_price_approved: float | Unset = UNSET
    reason: str | Unset = UNSET
    comment: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        status = self.status.value

        qty_approved = self.qty_approved

        unit_price_approved = self.unit_price_approved

        reason = self.reason

        comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item_id": item_id,
                "status": status,
            }
        )
        if qty_approved is not UNSET:
            field_dict["qty_approved"] = qty_approved
        if unit_price_approved is not UNSET:
            field_dict["unit_price_approved"] = unit_price_approved
        if reason is not UNSET:
            field_dict["reason"] = reason
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        status = InsuranceClaimLineDecisionStatus(d.pop("status"))

        qty_approved = d.pop("qty_approved", UNSET)

        unit_price_approved = d.pop("unit_price_approved", UNSET)

        reason = d.pop("reason", UNSET)

        comment = d.pop("comment", UNSET)

        insurance_claim_line_decision = cls(
            item_id=item_id,
            status=status,
            qty_approved=qty_approved,
            unit_price_approved=unit_price_approved,
            reason=reason,
            comment=comment,
        )

        return insurance_claim_line_decision
