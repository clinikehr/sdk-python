from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_phone_permission_type_1 import PatientPhonePermissionType1
from ..models.patient_phone_permission_type_2_type_1 import PatientPhonePermissionType2Type1
from ..models.patient_phone_permission_type_3_type_1 import PatientPhonePermissionType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientPhone")


@_attrs_define
class PatientPhone:
    """
    Attributes:
        phone_number (str):
        type_ (None | str | Unset):
        permission (None | PatientPhonePermissionType1 | PatientPhonePermissionType2Type1 |
            PatientPhonePermissionType3Type1 | Unset):
        is_primary (bool | Unset):  Default: False.
    """

    phone_number: str
    type_: None | str | Unset = UNSET
    permission: (
        None | PatientPhonePermissionType1 | PatientPhonePermissionType2Type1 | PatientPhonePermissionType3Type1 | Unset
    ) = UNSET
    is_primary: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        permission: None | str | Unset
        if isinstance(self.permission, Unset):
            permission = UNSET
        elif isinstance(self.permission, PatientPhonePermissionType1):
            permission = self.permission.value
        elif isinstance(self.permission, PatientPhonePermissionType2Type1):
            permission = self.permission.value
        elif isinstance(self.permission, PatientPhonePermissionType3Type1):
            permission = self.permission.value
        else:
            permission = self.permission

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if permission is not UNSET:
            field_dict["permission"] = permission
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_number = d.pop("phone_number")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_permission(
            data: object,
        ) -> (
            None
            | PatientPhonePermissionType1
            | PatientPhonePermissionType2Type1
            | PatientPhonePermissionType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permission_type_1 = PatientPhonePermissionType1(data)

                return permission_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permission_type_2_type_1 = PatientPhonePermissionType2Type1(data)

                return permission_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permission_type_3_type_1 = PatientPhonePermissionType3Type1(data)

                return permission_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientPhonePermissionType1
                | PatientPhonePermissionType2Type1
                | PatientPhonePermissionType3Type1
                | Unset,
                data,
            )

        permission = _parse_permission(d.pop("permission", UNSET))

        is_primary = d.pop("is_primary", UNSET)

        patient_phone = cls(
            phone_number=phone_number,
            type_=type_,
            permission=permission,
            is_primary=is_primary,
        )

        patient_phone.additional_properties = d
        return patient_phone

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
