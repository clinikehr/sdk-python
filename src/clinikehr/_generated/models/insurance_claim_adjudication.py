from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.insurance_claim_adjudication_decision import InsuranceClaimAdjudicationDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_claim_line_decision import InsuranceClaimLineDecision


T = TypeVar("T", bound="InsuranceClaimAdjudication")


@_attrs_define
class InsuranceClaimAdjudication:
    """Vet a claim. `decision` sets what EVERY line gets (`approved` at billed figures, or `rejected` at zero); `items`
    overrides individual lines, so "approve everything except this line" is `decision: approved` plus one declined line.
    The claim's status follows the lines: all approved as billed - `approved`; all declined - `denied`; anything else -
    `partially_approved`. A rejection needs a `reason`. You can never approve more than was billed, and a claim the
    clinic has already recorded money against can no longer be vetted. Nothing here moves money.

        Attributes:
            decision (InsuranceClaimAdjudicationDecision):
            reason (str | Unset):
            pa_code (str | Unset): The authorization code the claim is matched to, if any.
            items (list[InsuranceClaimLineDecision] | Unset):
    """

    decision: InsuranceClaimAdjudicationDecision
    reason: str | Unset = UNSET
    pa_code: str | Unset = UNSET
    items: list[InsuranceClaimLineDecision] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        reason = self.reason

        pa_code = self.pa_code

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
        if reason is not UNSET:
            field_dict["reason"] = reason
        if pa_code is not UNSET:
            field_dict["pa_code"] = pa_code
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_claim_line_decision import InsuranceClaimLineDecision  # noqa: PLC0415

        d = dict(src_dict)
        decision = InsuranceClaimAdjudicationDecision(d.pop("decision"))

        reason = d.pop("reason", UNSET)

        pa_code = d.pop("pa_code", UNSET)

        _items = d.pop("items", UNSET)
        items: list[InsuranceClaimLineDecision] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = InsuranceClaimLineDecision.from_dict(items_item_data)

                items.append(items_item)

        insurance_claim_adjudication = cls(
            decision=decision,
            reason=reason,
            pa_code=pa_code,
            items=items,
        )

        return insurance_claim_adjudication
