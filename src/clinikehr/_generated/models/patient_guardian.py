from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_guardian_relationship_type_1 import PatientGuardianRelationshipType1
from ..models.patient_guardian_relationship_type_2_type_1 import PatientGuardianRelationshipType2Type1
from ..models.patient_guardian_relationship_type_3_type_1 import PatientGuardianRelationshipType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientGuardian")


@_attrs_define
class PatientGuardian:
    """
    Attributes:
        guardian_id (None | Unset | UUID):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        email (None | str | Unset):
        phone (None | str | Unset):
        relationship (None | PatientGuardianRelationshipType1 | PatientGuardianRelationshipType2Type1 |
            PatientGuardianRelationshipType3Type1 | Unset):
        is_responsible_for_billing (bool | Unset):  Default: False.
        is_primary (bool | Unset):  Default: False.
        can_access_records (bool | Unset):  Default: False.
        is_emergency_contact (bool | Unset):  Default: True.
        can_schedule_appointments (bool | Unset):  Default: False.
        notes (None | str | Unset):
    """

    guardian_id: None | Unset | UUID = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    relationship: (
        None
        | PatientGuardianRelationshipType1
        | PatientGuardianRelationshipType2Type1
        | PatientGuardianRelationshipType3Type1
        | Unset
    ) = UNSET
    is_responsible_for_billing: bool | Unset = False
    is_primary: bool | Unset = False
    can_access_records: bool | Unset = False
    is_emergency_contact: bool | Unset = True
    can_schedule_appointments: bool | Unset = False
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guardian_id: None | str | Unset
        if isinstance(self.guardian_id, Unset):
            guardian_id = UNSET
        elif isinstance(self.guardian_id, UUID):
            guardian_id = str(self.guardian_id)
        else:
            guardian_id = self.guardian_id

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        relationship: None | str | Unset
        if isinstance(self.relationship, Unset):
            relationship = UNSET
        elif isinstance(self.relationship, PatientGuardianRelationshipType1):
            relationship = self.relationship.value
        elif isinstance(self.relationship, PatientGuardianRelationshipType2Type1):
            relationship = self.relationship.value
        elif isinstance(self.relationship, PatientGuardianRelationshipType3Type1):
            relationship = self.relationship.value
        else:
            relationship = self.relationship

        is_responsible_for_billing = self.is_responsible_for_billing

        is_primary = self.is_primary

        can_access_records = self.can_access_records

        is_emergency_contact = self.is_emergency_contact

        can_schedule_appointments = self.can_schedule_appointments

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guardian_id is not UNSET:
            field_dict["guardian_id"] = guardian_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if is_responsible_for_billing is not UNSET:
            field_dict["is_responsible_for_billing"] = is_responsible_for_billing
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if can_access_records is not UNSET:
            field_dict["can_access_records"] = can_access_records
        if is_emergency_contact is not UNSET:
            field_dict["is_emergency_contact"] = is_emergency_contact
        if can_schedule_appointments is not UNSET:
            field_dict["can_schedule_appointments"] = can_schedule_appointments
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_guardian_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                guardian_id_type_0 = UUID(data)

                return guardian_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        guardian_id = _parse_guardian_id(d.pop("guardian_id", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_relationship(
            data: object,
        ) -> (
            None
            | PatientGuardianRelationshipType1
            | PatientGuardianRelationshipType2Type1
            | PatientGuardianRelationshipType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_type_1 = PatientGuardianRelationshipType1(data)

                return relationship_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_type_2_type_1 = PatientGuardianRelationshipType2Type1(data)

                return relationship_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_type_3_type_1 = PatientGuardianRelationshipType3Type1(data)

                return relationship_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientGuardianRelationshipType1
                | PatientGuardianRelationshipType2Type1
                | PatientGuardianRelationshipType3Type1
                | Unset,
                data,
            )

        relationship = _parse_relationship(d.pop("relationship", UNSET))

        is_responsible_for_billing = d.pop("is_responsible_for_billing", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        can_access_records = d.pop("can_access_records", UNSET)

        is_emergency_contact = d.pop("is_emergency_contact", UNSET)

        can_schedule_appointments = d.pop("can_schedule_appointments", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        patient_guardian = cls(
            guardian_id=guardian_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            relationship=relationship,
            is_responsible_for_billing=is_responsible_for_billing,
            is_primary=is_primary,
            can_access_records=can_access_records,
            is_emergency_contact=is_emergency_contact,
            can_schedule_appointments=can_schedule_appointments,
            notes=notes,
        )

        patient_guardian.additional_properties = d
        return patient_guardian

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
