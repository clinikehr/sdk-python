from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.care_provider import CareProvider


T = TypeVar("T", bound="GetCareProviderResponse200")


@_attrs_define
class GetCareProviderResponse200:
    """
    Attributes:
        data (CareProvider): An outside clinician a patient names (their own doctor, a referring doctor, a specialist) —
            the exposed-field allow-list, field by field. `source` is `clinic` for a contact the clinic recorded (including
            one taken from an intake form) and `api` for one an app added. `editable` is true only when this key's app added
            the contact, so it may change or remove it; every other contact is read only to apps. The clinic's own notes on
            a contact are never exposed.
    """

    data: CareProvider
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
        from ..models.care_provider import CareProvider  # noqa: PLC0415

        d = dict(src_dict)
        data = CareProvider.from_dict(d.pop("data"))

        get_care_provider_response_200 = cls(
            data=data,
        )

        get_care_provider_response_200.additional_properties = d
        return get_care_provider_response_200

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
