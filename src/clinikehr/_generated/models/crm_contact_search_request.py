from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmContactSearchRequest")


@_attrs_define
class CrmContactSearchRequest:
    """Exact match only. email or phone — at least one is required.

    Attributes:
        email (str | Unset):
        phone (str | Unset):
    """

    email: str | Unset = UNSET
    phone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        phone = self.phone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        crm_contact_search_request = cls(
            email=email,
            phone=phone,
        )

        return crm_contact_search_request
