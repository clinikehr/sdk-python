from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.referral_create_service_code_system import ReferralCreateServiceCodeSystem

T = TypeVar("T", bound="ReferralCreateServiceCode")


@_attrs_define
class ReferralCreateServiceCode:
    """
    Attributes:
        system (ReferralCreateServiceCodeSystem):
        code (str): A `snomed-ct` code is 6 to 18 digits.
    """

    system: ReferralCreateServiceCodeSystem
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
        system = ReferralCreateServiceCodeSystem(d.pop("system"))

        code = d.pop("code")

        referral_create_service_code = cls(
            system=system,
            code=code,
        )

        return referral_create_service_code
