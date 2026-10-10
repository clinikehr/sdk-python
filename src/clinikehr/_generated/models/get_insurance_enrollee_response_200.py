from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.insurance_enrollee import InsuranceEnrollee


T = TypeVar("T", bound="GetInsuranceEnrolleeResponse200")


@_attrs_define
class GetInsuranceEnrolleeResponse200:
    """
    Attributes:
        data (InsuranceEnrollee): A person an insurer covers at this clinic, as the clinic holds them. `insurance_no` is
            the number an enrollee is verified by. Only enrollees of an insurer the clinic linked to your organization are
            returned. Verification metadata and the clinic's internal notes are never exposed.
    """

    data: InsuranceEnrollee
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
        from ..models.insurance_enrollee import InsuranceEnrollee  # noqa: PLC0415

        d = dict(src_dict)
        data = InsuranceEnrollee.from_dict(d.pop("data"))

        get_insurance_enrollee_response_200 = cls(
            data=data,
        )

        get_insurance_enrollee_response_200.additional_properties = d
        return get_insurance_enrollee_response_200

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
