from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_create_reason_code import ReferralCreateReasonCode


T = TypeVar("T", bound="ReferralCreateReason")


@_attrs_define
class ReferralCreateReason:
    """
    Attributes:
        text (str):
        code (ReferralCreateReasonCode | Unset):
    """

    text: str
    code: ReferralCreateReasonCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_create_reason_code import ReferralCreateReasonCode  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        _code = d.pop("code", UNSET)
        code: ReferralCreateReasonCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = ReferralCreateReasonCode.from_dict(_code)

        referral_create_reason = cls(
            text=text,
            code=code,
        )

        return referral_create_reason
