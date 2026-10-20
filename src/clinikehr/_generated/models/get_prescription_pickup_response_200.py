from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pickup import Pickup


T = TypeVar("T", bound="GetPrescriptionPickupResponse200")


@_attrs_define
class GetPrescriptionPickupResponse200:
    """
    Attributes:
        data (Pickup): One prescription-pickup handover. Signatures are never returned — `has_signature` only.
            `agent_name` is never shown to an organization connection (only `agent_relationship` is). `pos_sale_id` is set,
            and `lines` carry `pos_sale_item_id` instead of `prescription_id`, for a Pharmacy-edition till sale's pickup;
            otherwise both are null.
    """

    data: Pickup
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
        from ..models.pickup import Pickup  # noqa: PLC0415

        d = dict(src_dict)
        data = Pickup.from_dict(d.pop("data"))

        get_prescription_pickup_response_200 = cls(
            data=data,
        )

        get_prescription_pickup_response_200.additional_properties = d
        return get_prescription_pickup_response_200

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
