from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.me_environment import MeEnvironment

T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        key_id (str):
        clinic_id (None | UUID):
        environment (MeEnvironment):
        scopes (list[str]):
        org_id (None | UUID):
        sandbox (bool): True when clinic_id above is this key's workspace's synthetic sandbox clinic, not a real one.
            Always false for a clinic-owned key.
    """

    key_id: str
    clinic_id: None | UUID
    environment: MeEnvironment
    scopes: list[str]
    org_id: None | UUID
    sandbox: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = self.key_id

        clinic_id: None | str
        if isinstance(self.clinic_id, UUID):
            clinic_id = str(self.clinic_id)
        else:
            clinic_id = self.clinic_id

        environment = self.environment.value

        scopes = self.scopes

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        sandbox = self.sandbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "clinic_id": clinic_id,
                "environment": environment,
                "scopes": scopes,
                "org_id": org_id,
                "sandbox": sandbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = d.pop("key_id")

        def _parse_clinic_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinic_id_type_0 = UUID(data)

                return clinic_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        clinic_id = _parse_clinic_id(d.pop("clinic_id"))

        environment = MeEnvironment(d.pop("environment"))

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        sandbox = d.pop("sandbox")

        me = cls(
            key_id=key_id,
            clinic_id=clinic_id,
            environment=environment,
            scopes=scopes,
            org_id=org_id,
            sandbox=sandbox,
        )

        me.additional_properties = d
        return me

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
