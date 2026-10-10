from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsurancePreAuthorizationLineDecision")


@_attrs_define
class InsurancePreAuthorizationLineDecision:
    """
    Attributes:
        item_id (UUID):
        approved (bool):
        reason (str | Unset):
    """

    item_id: UUID
    approved: bool
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_id = str(self.item_id)

        approved = self.approved

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item_id": item_id,
                "approved": approved,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = UUID(d.pop("item_id"))

        approved = d.pop("approved")

        reason = d.pop("reason", UNSET)

        insurance_pre_authorization_line_decision = cls(
            item_id=item_id,
            approved=approved,
            reason=reason,
        )

        return insurance_pre_authorization_line_decision
