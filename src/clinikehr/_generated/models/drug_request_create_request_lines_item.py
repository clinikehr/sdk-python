from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.drug_request_create_request_lines_item_code_system import DrugRequestCreateRequestLinesItemCodeSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="DrugRequestCreateRequestLinesItem")


@_attrs_define
class DrugRequestCreateRequestLinesItem:
    """
    Attributes:
        quantity (float):
        code_system (DrugRequestCreateRequestLinesItemCodeSystem | Unset):
        code_value (str | Unset):
        description (str | Unset):
        directions (str | Unset):
    """

    quantity: float
    code_system: DrugRequestCreateRequestLinesItemCodeSystem | Unset = UNSET
    code_value: str | Unset = UNSET
    description: str | Unset = UNSET
    directions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        code_system: str | Unset = UNSET
        if not isinstance(self.code_system, Unset):
            code_system = self.code_system.value

        code_value = self.code_value

        description = self.description

        directions = self.directions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
            }
        )
        if code_system is not UNSET:
            field_dict["code_system"] = code_system
        if code_value is not UNSET:
            field_dict["code_value"] = code_value
        if description is not UNSET:
            field_dict["description"] = description
        if directions is not UNSET:
            field_dict["directions"] = directions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        _code_system = d.pop("code_system", UNSET)
        code_system: DrugRequestCreateRequestLinesItemCodeSystem | Unset
        if isinstance(_code_system, Unset):
            code_system = UNSET
        else:
            code_system = DrugRequestCreateRequestLinesItemCodeSystem(_code_system)

        code_value = d.pop("code_value", UNSET)

        description = d.pop("description", UNSET)

        directions = d.pop("directions", UNSET)

        drug_request_create_request_lines_item = cls(
            quantity=quantity,
            code_system=code_system,
            code_value=code_value,
            description=description,
            directions=directions,
        )

        drug_request_create_request_lines_item.additional_properties = d
        return drug_request_create_request_lines_item

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
