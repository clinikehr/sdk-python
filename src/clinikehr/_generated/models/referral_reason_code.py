from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_reason_code_system import ReferralReasonCodeSystem

T = TypeVar("T", bound="ReferralReasonCode")


@_attrs_define
class ReferralReasonCode:
    """A coded reason. `system` is `icd-10-cm` or `icd-10` (checked against the platform's own diagnosis codes and stored
    in canonical form; an unrecognised code is refused), `snomed-ct` (6 to 18 digits, shape only) or `local` (your own
    code, never mapped to a standard).

        Attributes:
            system (ReferralReasonCodeSystem):
            code (str):
    """

    system: ReferralReasonCodeSystem
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
        system = ReferralReasonCodeSystem(d.pop("system"))

        code = d.pop("code")

        referral_reason_code = cls(
            system=system,
            code=code,
        )

        referral_reason_code.additional_properties = d
        return referral_reason_code

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
