from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_summary_environment import ConnectionSummaryEnvironment

T = TypeVar("T", bound="ConnectionSummary")


@_attrs_define
class ConnectionSummary:
    """
    Attributes:
        clinic_id (UUID):
        clinic_name (None | str): The clinic's display name — null for the synthetic sandbox (there is no real clinic
            behind it).
        environment (ConnectionSummaryEnvironment):
        granted_scopes (list[str]):
        connected_at (datetime.datetime | None): When the connection was approved. Null for a clinic-owned key's
            implicit self-connection and for the sandbox entry — neither is a consent-model connection row.
        expires_at (datetime.datetime | None): When a PHI-scoped connection must be re-attested. Null for a non-PHI-only
            connection, a clinic-owned key, and the sandbox entry.
        sandbox (bool): True when this entry IS the workspace's synthetic sandbox, not a real clinic.
    """

    clinic_id: UUID
    clinic_name: None | str
    environment: ConnectionSummaryEnvironment
    granted_scopes: list[str]
    connected_at: datetime.datetime | None
    expires_at: datetime.datetime | None
    sandbox: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clinic_id = str(self.clinic_id)

        clinic_name: None | str
        clinic_name = self.clinic_name

        environment = self.environment.value

        granted_scopes = self.granted_scopes

        connected_at: None | str
        if isinstance(self.connected_at, datetime.datetime):
            connected_at = self.connected_at.isoformat()
        else:
            connected_at = self.connected_at

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        sandbox = self.sandbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clinic_id": clinic_id,
                "clinic_name": clinic_name,
                "environment": environment,
                "granted_scopes": granted_scopes,
                "connected_at": connected_at,
                "expires_at": expires_at,
                "sandbox": sandbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clinic_id = UUID(d.pop("clinic_id"))

        def _parse_clinic_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        clinic_name = _parse_clinic_name(d.pop("clinic_name"))

        environment = ConnectionSummaryEnvironment(d.pop("environment"))

        granted_scopes = cast(list[str], d.pop("granted_scopes"))

        def _parse_connected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connected_at_type_0 = datetime.datetime.fromisoformat(data)

                return connected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        connected_at = _parse_connected_at(d.pop("connected_at"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        sandbox = d.pop("sandbox")

        connection_summary = cls(
            clinic_id=clinic_id,
            clinic_name=clinic_name,
            environment=environment,
            granted_scopes=granted_scopes,
            connected_at=connected_at,
            expires_at=expires_at,
            sandbox=sandbox,
        )

        connection_summary.additional_properties = d
        return connection_summary

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
