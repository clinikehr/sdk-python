from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_service_code_system import ReferralServiceCodeSystem

T = TypeVar("T", bound="ReferralServiceCode")


@_attrs_define
class ReferralServiceCode:
    """A coded service. `system` is `snomed-ct` (a SNOMED CT concept id, 6 to 18 digits; the platform holds no SNOMED
    corpus, so only its shape is checked) or `local` (your own code, never mapped to a standard).

        Attributes:
            system (ReferralServiceCodeSystem):
            code (str):
    """

    system: ReferralServiceCodeSystem
    code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        system = ReferralServiceCodeSystem(d.pop("system"))

        code = d.pop("code")

        referral_service_code = cls(
            system=system,
            code=code,
        )

        referral_service_code.additional_properties = d
        return referral_service_code

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
