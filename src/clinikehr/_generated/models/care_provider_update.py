from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.care_provider_update_type import CareProviderUpdateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CareProviderUpdate")


@_attrs_define
class CareProviderUpdate:
    """A change to an outside care provider your app added. The patient cannot be changed. `is_primary: true` makes the
    patient's other contacts of the same `type` non-primary.

        Attributes:
            name (str | Unset):
            type_ (CareProviderUpdateType | Unset):
            practice_name (str | Unset):
            specialty (str | Unset):
            npi (str | Unset):
            phone (str | Unset):
            fax (str | Unset):
            address (str | Unset):
            is_primary (bool | Unset):
    """

    name: str | Unset = UNSET
    type_: CareProviderUpdateType | Unset = UNSET
    practice_name: str | Unset = UNSET
    specialty: str | Unset = UNSET
    npi: str | Unset = UNSET
    phone: str | Unset = UNSET
    fax: str | Unset = UNSET
    address: str | Unset = UNSET
    is_primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        practice_name = self.practice_name

        specialty = self.specialty

        npi = self.npi

        phone = self.phone

        fax = self.fax

        address = self.address

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if practice_name is not UNSET:
            field_dict["practice_name"] = practice_name
        if specialty is not UNSET:
            field_dict["specialty"] = specialty
        if npi is not UNSET:
            field_dict["npi"] = npi
        if phone is not UNSET:
            field_dict["phone"] = phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if address is not UNSET:
            field_dict["address"] = address
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CareProviderUpdateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CareProviderUpdateType(_type_)

        practice_name = d.pop("practice_name", UNSET)

        specialty = d.pop("specialty", UNSET)

        npi = d.pop("npi", UNSET)

        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        address = d.pop("address", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        care_provider_update = cls(
            name=name,
            type_=type_,
            practice_name=practice_name,
            specialty=specialty,
            npi=npi,
            phone=phone,
            fax=fax,
            address=address,
            is_primary=is_primary,
        )

        return care_provider_update
