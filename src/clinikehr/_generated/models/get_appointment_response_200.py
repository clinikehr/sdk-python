from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.appointment import Appointment


T = TypeVar("T", bound="GetAppointmentResponse200")


@_attrs_define
class GetAppointmentResponse200:
    """
    Attributes:
        data (Appointment): Never present here, by name: client_appointment_date/client_start_time/
            client_end_time/client_timezone, form_data, custom_color, provider_user_id, time_range,
            excluded_from_overlap_check, booking_identity_review, provider_busy_minutes, out_of_office_confirmed_at,
            booking_confirmation_deferred, clinic_id.
    """

    data: Appointment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appointment import Appointment  # noqa: PLC0415

        d = dict(src_dict)
        data = Appointment.from_dict(d.pop("data"))

        get_appointment_response_200 = cls(
            data=data,
        )

        get_appointment_response_200.additional_properties = d
        return get_appointment_response_200

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
