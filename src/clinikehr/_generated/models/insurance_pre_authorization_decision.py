from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.insurance_pre_authorization_decision_decision import InsurancePreAuthorizationDecisionDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_pre_authorization_line_decision import InsurancePreAuthorizationLineDecision


T = TypeVar("T", bound="InsurancePreAuthorizationDecision")


@_attrs_define
class InsurancePreAuthorizationDecision:
    """Decide a request that is `sent_for_authorization`. An approval needs `pa_code`; a denial needs `reason`.
    `approved_amount` (approval only) defaults to the estimated cost and may not exceed it. Lines you do not list follow
    the decision. A decided request cannot be decided again.

        Attributes:
            decision (InsurancePreAuthorizationDecisionDecision):
            pa_code (str | Unset):
            approved_amount (float | Unset):
            reason (str | Unset):
            items (list[InsurancePreAuthorizationLineDecision] | Unset):
    """

    decision: InsurancePreAuthorizationDecisionDecision
    pa_code: str | Unset = UNSET
    approved_amount: float | Unset = UNSET
    reason: str | Unset = UNSET
    items: list[InsurancePreAuthorizationLineDecision] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        pa_code = self.pa_code

        approved_amount = self.approved_amount

        reason = self.reason

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decision": decision,
            }
        )
        if pa_code is not UNSET:
            field_dict["pa_code"] = pa_code
        if approved_amount is not UNSET:
            field_dict["approved_amount"] = approved_amount
        if reason is not UNSET:
            field_dict["reason"] = reason
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_pre_authorization_line_decision import (
            InsurancePreAuthorizationLineDecision,  # noqa: PLC0415
        )

        d = dict(src_dict)
        decision = InsurancePreAuthorizationDecisionDecision(d.pop("decision"))

        pa_code = d.pop("pa_code", UNSET)

        approved_amount = d.pop("approved_amount", UNSET)

        reason = d.pop("reason", UNSET)

        _items = d.pop("items", UNSET)
        items: list[InsurancePreAuthorizationLineDecision] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = InsurancePreAuthorizationLineDecision.from_dict(items_item_data)

                items.append(items_item)

        insurance_pre_authorization_decision = cls(
            decision=decision,
            pa_code=pa_code,
            approved_amount=approved_amount,
            reason=reason,
            items=items,
        )

        return insurance_pre_authorization_decision
