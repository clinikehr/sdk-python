from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.care_provider_create_type import CareProviderCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CareProviderCreate")


@_attrs_define
class CareProviderCreate:
    """An outside care provider to add to a patient. Saved straight away. If `is_primary` is true, the patient's other
    contacts of the same `type` stop being primary. `npi` is ten digits (its shape is checked, not its check digit). The
    clinic's notes on a contact cannot be sent. The `Idempotency-Key` header is REQUIRED.

        Attributes:
            patient_id (UUID):
            name (str):
            type_ (CareProviderCreateType):
            practice_name (str | Unset):
            specialty (str | Unset):
            npi (str | Unset):
            phone (str | Unset):
            fax (str | Unset):
            address (str | Unset):
            is_primary (bool | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    name: str
    type_: CareProviderCreateType
    practice_name: str | Unset = UNSET
    specialty: str | Unset = UNSET
    npi: str | Unset = UNSET
    phone: str | Unset = UNSET
    fax: str | Unset = UNSET
    address: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        name = self.name

        type_ = self.type_.value

        practice_name = self.practice_name

        specialty = self.specialty

        npi = self.npi

        phone = self.phone

        fax = self.fax

        address = self.address

        is_primary = self.is_primary

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "name": name,
                "type": type_,
            }
        )
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
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        name = d.pop("name")

        type_ = CareProviderCreateType(d.pop("type"))

        practice_name = d.pop("practice_name", UNSET)

        specialty = d.pop("specialty", UNSET)

        npi = d.pop("npi", UNSET)

        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        address = d.pop("address", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        care_provider_create = cls(
            patient_id=patient_id,
            name=name,
            type_=type_,
            practice_name=practice_name,
            specialty=specialty,
            npi=npi,
            phone=phone,
            fax=fax,
            address=address,
            is_primary=is_primary,
            origin_assistant_name=origin_assistant_name,
        )

        return care_provider_create
