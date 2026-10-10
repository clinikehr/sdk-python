from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.insurance_pre_authorization_submit_item_item_type import InsurancePreAuthorizationSubmitItemItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InsurancePreAuthorizationSubmitItem")


@_attrs_define
class InsurancePreAuthorizationSubmitItem:
    """
    Attributes:
        description (str):
        unit_cost (float):
        item_type (InsurancePreAuthorizationSubmitItemItemType | Unset):  Default:
            InsurancePreAuthorizationSubmitItemItemType.SERVICE.
        tariff_code (str | Unset):
        quantity (int | Unset):  Default: 1.
        diagnosis (str | Unset):
        icd_cpt_code (str | Unset):
        medical_necessity (str | Unset):
    """

    description: str
    unit_cost: float
    item_type: InsurancePreAuthorizationSubmitItemItemType | Unset = InsurancePreAuthorizationSubmitItemItemType.SERVICE
    tariff_code: str | Unset = UNSET
    quantity: int | Unset = 1
    diagnosis: str | Unset = UNSET
    icd_cpt_code: str | Unset = UNSET
    medical_necessity: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        unit_cost = self.unit_cost

        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        tariff_code = self.tariff_code

        quantity = self.quantity

        diagnosis = self.diagnosis

        icd_cpt_code = self.icd_cpt_code

        medical_necessity = self.medical_necessity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "unit_cost": unit_cost,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if tariff_code is not UNSET:
            field_dict["tariff_code"] = tariff_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if diagnosis is not UNSET:
            field_dict["diagnosis"] = diagnosis
        if icd_cpt_code is not UNSET:
            field_dict["icd_cpt_code"] = icd_cpt_code
        if medical_necessity is not UNSET:
            field_dict["medical_necessity"] = medical_necessity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        unit_cost = d.pop("unit_cost")

        _item_type = d.pop("item_type", UNSET)
        item_type: InsurancePreAuthorizationSubmitItemItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = InsurancePreAuthorizationSubmitItemItemType(_item_type)

        tariff_code = d.pop("tariff_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        diagnosis = d.pop("diagnosis", UNSET)

        icd_cpt_code = d.pop("icd_cpt_code", UNSET)

        medical_necessity = d.pop("medical_necessity", UNSET)

        insurance_pre_authorization_submit_item = cls(
            description=description,
            unit_cost=unit_cost,
            item_type=item_type,
            tariff_code=tariff_code,
            quantity=quantity,
            diagnosis=diagnosis,
            icd_cpt_code=icd_cpt_code,
            medical_necessity=medical_necessity,
        )

        return insurance_pre_authorization_submit_item
