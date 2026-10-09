from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralUpdateRequester")


@_attrs_define
class ReferralUpdateRequester:
    """
    Attributes:
        name (str | Unset):
        organization (str | Unset):
        npi (str | Unset):
    """

    name: str | Unset = UNSET
    organization: str | Unset = UNSET
    npi: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization = self.organization

        npi = self.npi

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if npi is not UNSET:
            field_dict["npi"] = npi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        organization = d.pop("organization", UNSET)

        npi = d.pop("npi", UNSET)

        referral_update_requester = cls(
            name=name,
            organization=organization,
            npi=npi,
        )

        return referral_update_requester
