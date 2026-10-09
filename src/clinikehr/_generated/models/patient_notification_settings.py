from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientNotificationSettings")


@_attrs_define
class PatientNotificationSettings:
    """Read-only — refused (notification_settings_not_writable) if sent on a write.

    Attributes:
        upcoming_appointments_enabled (bool | None | Unset):
        upcoming_appointments_email_option (None | str | Unset):
        upcoming_appointments_phone_option (None | str | Unset):
        incomplete_documents_enabled (bool | None | Unset):
        incomplete_documents_email_option (None | str | Unset):
        incomplete_documents_phone_option (None | str | Unset):
        cancellations_enabled (bool | None | Unset):
        cancellations_email_option (None | str | Unset):
        cancellations_phone_option (None | str | Unset):
    """

    upcoming_appointments_enabled: bool | None | Unset = UNSET
    upcoming_appointments_email_option: None | str | Unset = UNSET
    upcoming_appointments_phone_option: None | str | Unset = UNSET
    incomplete_documents_enabled: bool | None | Unset = UNSET
    incomplete_documents_email_option: None | str | Unset = UNSET
    incomplete_documents_phone_option: None | str | Unset = UNSET
    cancellations_enabled: bool | None | Unset = UNSET
    cancellations_email_option: None | str | Unset = UNSET
    cancellations_phone_option: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upcoming_appointments_enabled: bool | None | Unset
        if isinstance(self.upcoming_appointments_enabled, Unset):
            upcoming_appointments_enabled = UNSET
        else:
            upcoming_appointments_enabled = self.upcoming_appointments_enabled

        upcoming_appointments_email_option: None | str | Unset
        if isinstance(self.upcoming_appointments_email_option, Unset):
            upcoming_appointments_email_option = UNSET
        else:
            upcoming_appointments_email_option = self.upcoming_appointments_email_option

        upcoming_appointments_phone_option: None | str | Unset
        if isinstance(self.upcoming_appointments_phone_option, Unset):
            upcoming_appointments_phone_option = UNSET
        else:
            upcoming_appointments_phone_option = self.upcoming_appointments_phone_option

        incomplete_documents_enabled: bool | None | Unset
        if isinstance(self.incomplete_documents_enabled, Unset):
            incomplete_documents_enabled = UNSET
        else:
            incomplete_documents_enabled = self.incomplete_documents_enabled

        incomplete_documents_email_option: None | str | Unset
        if isinstance(self.incomplete_documents_email_option, Unset):
            incomplete_documents_email_option = UNSET
        else:
            incomplete_documents_email_option = self.incomplete_documents_email_option

        incomplete_documents_phone_option: None | str | Unset
        if isinstance(self.incomplete_documents_phone_option, Unset):
            incomplete_documents_phone_option = UNSET
        else:
            incomplete_documents_phone_option = self.incomplete_documents_phone_option

        cancellations_enabled: bool | None | Unset
        if isinstance(self.cancellations_enabled, Unset):
            cancellations_enabled = UNSET
        else:
            cancellations_enabled = self.cancellations_enabled

        cancellations_email_option: None | str | Unset
        if isinstance(self.cancellations_email_option, Unset):
            cancellations_email_option = UNSET
        else:
            cancellations_email_option = self.cancellations_email_option

        cancellations_phone_option: None | str | Unset
        if isinstance(self.cancellations_phone_option, Unset):
            cancellations_phone_option = UNSET
        else:
            cancellations_phone_option = self.cancellations_phone_option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upcoming_appointments_enabled is not UNSET:
            field_dict["upcoming_appointments_enabled"] = upcoming_appointments_enabled
        if upcoming_appointments_email_option is not UNSET:
            field_dict["upcoming_appointments_email_option"] = upcoming_appointments_email_option
        if upcoming_appointments_phone_option is not UNSET:
            field_dict["upcoming_appointments_phone_option"] = upcoming_appointments_phone_option
        if incomplete_documents_enabled is not UNSET:
            field_dict["incomplete_documents_enabled"] = incomplete_documents_enabled
        if incomplete_documents_email_option is not UNSET:
            field_dict["incomplete_documents_email_option"] = incomplete_documents_email_option
        if incomplete_documents_phone_option is not UNSET:
            field_dict["incomplete_documents_phone_option"] = incomplete_documents_phone_option
        if cancellations_enabled is not UNSET:
            field_dict["cancellations_enabled"] = cancellations_enabled
        if cancellations_email_option is not UNSET:
            field_dict["cancellations_email_option"] = cancellations_email_option
        if cancellations_phone_option is not UNSET:
            field_dict["cancellations_phone_option"] = cancellations_phone_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_upcoming_appointments_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upcoming_appointments_enabled = _parse_upcoming_appointments_enabled(
            d.pop("upcoming_appointments_enabled", UNSET)
        )

        def _parse_upcoming_appointments_email_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upcoming_appointments_email_option = _parse_upcoming_appointments_email_option(
            d.pop("upcoming_appointments_email_option", UNSET)
        )

        def _parse_upcoming_appointments_phone_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upcoming_appointments_phone_option = _parse_upcoming_appointments_phone_option(
            d.pop("upcoming_appointments_phone_option", UNSET)
        )

        def _parse_incomplete_documents_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        incomplete_documents_enabled = _parse_incomplete_documents_enabled(d.pop("incomplete_documents_enabled", UNSET))

        def _parse_incomplete_documents_email_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incomplete_documents_email_option = _parse_incomplete_documents_email_option(
            d.pop("incomplete_documents_email_option", UNSET)
        )

        def _parse_incomplete_documents_phone_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incomplete_documents_phone_option = _parse_incomplete_documents_phone_option(
            d.pop("incomplete_documents_phone_option", UNSET)
        )

        def _parse_cancellations_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cancellations_enabled = _parse_cancellations_enabled(d.pop("cancellations_enabled", UNSET))

        def _parse_cancellations_email_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellations_email_option = _parse_cancellations_email_option(d.pop("cancellations_email_option", UNSET))

        def _parse_cancellations_phone_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellations_phone_option = _parse_cancellations_phone_option(d.pop("cancellations_phone_option", UNSET))

        patient_notification_settings = cls(
            upcoming_appointments_enabled=upcoming_appointments_enabled,
            upcoming_appointments_email_option=upcoming_appointments_email_option,
            upcoming_appointments_phone_option=upcoming_appointments_phone_option,
            incomplete_documents_enabled=incomplete_documents_enabled,
            incomplete_documents_email_option=incomplete_documents_email_option,
            incomplete_documents_phone_option=incomplete_documents_phone_option,
            cancellations_enabled=cancellations_enabled,
            cancellations_email_option=cancellations_email_option,
            cancellations_phone_option=cancellations_phone_option,
        )

        patient_notification_settings.additional_properties = d
        return patient_notification_settings

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
