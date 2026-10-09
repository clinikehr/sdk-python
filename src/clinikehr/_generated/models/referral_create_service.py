from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_create_service_code import ReferralCreateServiceCode


T = TypeVar("T", bound="ReferralCreateService")


@_attrs_define
class ReferralCreateService:
    """
    Attributes:
        text (str):
        code (ReferralCreateServiceCode | Unset):
    """

    text: str
    code: ReferralCreateServiceCode | Unset = UNSET

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
        from ..models.referral_create_service_code import ReferralCreateServiceCode  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        _code = d.pop("code", UNSET)
        code: ReferralCreateServiceCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = ReferralCreateServiceCode.from_dict(_code)

        referral_create_service = cls(
            text=text,
            code=code,
        )

        return referral_create_service
