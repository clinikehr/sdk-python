from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.care_provider_source import CareProviderSource
from ..models.care_provider_type import CareProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CareProvider")


@_attrs_define
class CareProvider:
    """An outside clinician a patient names (their own doctor, a referring doctor, a specialist) — the exposed-field allow-
    list, field by field. `source` is `clinic` for a contact the clinic recorded (including one taken from an intake
    form) and `api` for one an app added. `editable` is true only when this key's app added the contact, so it may
    change or remove it; every other contact is read only to apps. The clinic's own notes on a contact are never
    exposed.

        Attributes:
            id (UUID):
            patient_id (UUID):
            type_ (CareProviderType):
            name (str):
            is_primary (bool):
            source (CareProviderSource):
            editable (bool): True only when this key's app added the contact.
            practice_name (None | str | Unset):
            specialty (None | str | Unset):
            npi (None | str | Unset):
            phone (None | str | Unset):
            fax (None | str | Unset):
            address (None | str | Unset):
            origin_assistant_name (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    patient_id: UUID
    type_: CareProviderType
    name: str
    is_primary: bool
    source: CareProviderSource
    editable: bool
    practice_name: None | str | Unset = UNSET
    specialty: None | str | Unset = UNSET
    npi: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        patient_id = str(self.patient_id)

        type_ = self.type_.value

        name = self.name

        is_primary = self.is_primary

        source = self.source.value

        editable = self.editable

        practice_name: None | str | Unset
        if isinstance(self.practice_name, Unset):
            practice_name = UNSET
        else:
            practice_name = self.practice_name

        specialty: None | str | Unset
        if isinstance(self.specialty, Unset):
            specialty = UNSET
        else:
            specialty = self.specialty

        npi: None | str | Unset
        if isinstance(self.npi, Unset):
            npi = UNSET
        else:
            npi = self.npi

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "type": type_,
                "name": name,
                "is_primary": is_primary,
                "source": source,
                "editable": editable,
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
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        type_ = CareProviderType(d.pop("type"))

        name = d.pop("name")

        is_primary = d.pop("is_primary")

        source = CareProviderSource(d.pop("source"))

        editable = d.pop("editable")

        def _parse_practice_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        practice_name = _parse_practice_name(d.pop("practice_name", UNSET))

        def _parse_specialty(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        specialty = _parse_specialty(d.pop("specialty", UNSET))

        def _parse_npi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        npi = _parse_npi(d.pop("npi", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        care_provider = cls(
            id=id,
            patient_id=patient_id,
            type_=type_,
            name=name,
            is_primary=is_primary,
            source=source,
            editable=editable,
            practice_name=practice_name,
            specialty=specialty,
            npi=npi,
            phone=phone,
            fax=fax,
            address=address,
            origin_assistant_name=origin_assistant_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        care_provider.additional_properties = d
        return care_provider

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
