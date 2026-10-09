from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prescription import Prescription


T = TypeVar("T", bound="GetPrescriptionResponse200")


@_attrs_define
class GetPrescriptionResponse200:
    """
    Attributes:
        data (Prescription): A prescription, read only and deliberately minimal: the drug, the dose, the frequency, the
            status and when it was written. Nothing about dispensing, payment, scheduling, the prescriber or notes ever
            leaves the clinic. There is no way to create or change a prescription through the API. `source` is `eprescribe`
            for a prescription sent through the clinic's e-prescribing connection and `clinic` otherwise. `status: unknown`
            appears only on an `eprescribe` prescription whose status the e-prescribing service reports in a form the
            platform does not recognise.
    """

    data: Prescription
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
        from ..models.prescription import Prescription  # noqa: PLC0415

        d = dict(src_dict)
        data = Prescription.from_dict(d.pop("data"))

        get_prescription_response_200 = cls(
            data=data,
        )

        get_prescription_response_200.additional_properties = d
        return get_prescription_response_200

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
