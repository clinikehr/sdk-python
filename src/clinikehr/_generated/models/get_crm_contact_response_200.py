from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.crm_contact import CrmContact


T = TypeVar("T", bound="GetCrmContactResponse200")


@_attrs_define
class GetCrmContactResponse200:
    """
    Attributes:
        data (CrmContact): Withheld, by NAME: clinic_id (implicit in the path), unsubscribe_token,
            migrated_from_patient_id, custom_color, created_by, confirmed_opt_in_at, marketing_authorization_id.
    """

    data: CrmContact
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
        from ..models.crm_contact import CrmContact  # noqa: PLC0415

        d = dict(src_dict)
        data = CrmContact.from_dict(d.pop("data"))

        get_crm_contact_response_200 = cls(
            data=data,
        )

        get_crm_contact_response_200.additional_properties = d
        return get_crm_contact_response_200

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
