from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.referral_update_reason_code_system import ReferralUpdateReasonCodeSystem

T = TypeVar("T", bound="ReferralUpdateReasonCode")


@_attrs_define
class ReferralUpdateReasonCode:
    """
    Attributes:
        system (ReferralUpdateReasonCodeSystem):
        code (str):
    """

    system: ReferralUpdateReasonCodeSystem
    code: str

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "system": system,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = ReferralUpdateReasonCodeSystem(d.pop("system"))

        code = d.pop("code")

        referral_update_reason_code = cls(
            system=system,
            code=code,
        )

        return referral_update_reason_code
