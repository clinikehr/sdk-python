from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.drug_request_confirm_substitution_request_decision import DrugRequestConfirmSubstitutionRequestDecision

T = TypeVar("T", bound="DrugRequestConfirmSubstitutionRequest")


@_attrs_define
class DrugRequestConfirmSubstitutionRequest:
    """
    Attributes:
        decision (DrugRequestConfirmSubstitutionRequestDecision):
    """

    decision: DrugRequestConfirmSubstitutionRequestDecision

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decision": decision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decision = DrugRequestConfirmSubstitutionRequestDecision(d.pop("decision"))

        drug_request_confirm_substitution_request = cls(
            decision=decision,
        )

        return drug_request_confirm_substitution_request
