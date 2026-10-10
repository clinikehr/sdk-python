from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.insurance_claim_submit_item_item_type import InsuranceClaimSubmitItemItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InsuranceClaimSubmitItem")


@_attrs_define
class InsuranceClaimSubmitItem:
    """
    Attributes:
        description (str):
        unit_price (float):
        item_type (InsuranceClaimSubmitItemItemType | Unset):  Default: InsuranceClaimSubmitItemItemType.SERVICE.
        tariff_code (str | Unset):
        quantity (int | Unset):  Default: 1.
        service_date (datetime.datetime | Unset):
    """

    description: str
    unit_price: float
    item_type: InsuranceClaimSubmitItemItemType | Unset = InsuranceClaimSubmitItemItemType.SERVICE
    tariff_code: str | Unset = UNSET
    quantity: int | Unset = 1
    service_date: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        unit_price = self.unit_price

        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        tariff_code = self.tariff_code

        quantity = self.quantity

        service_date: str | Unset = UNSET
        if not isinstance(self.service_date, Unset):
            service_date = self.service_date.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "unit_price": unit_price,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if tariff_code is not UNSET:
            field_dict["tariff_code"] = tariff_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if service_date is not UNSET:
            field_dict["service_date"] = service_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        unit_price = d.pop("unit_price")

        _item_type = d.pop("item_type", UNSET)
        item_type: InsuranceClaimSubmitItemItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = InsuranceClaimSubmitItemItemType(_item_type)

        tariff_code = d.pop("tariff_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        _service_date = d.pop("service_date", UNSET)
        service_date: datetime.datetime | Unset
        if isinstance(_service_date, Unset):
            service_date = UNSET
        else:
            service_date = datetime.datetime.fromisoformat(_service_date)

        insurance_claim_submit_item = cls(
            description=description,
            unit_price=unit_price,
            item_type=item_type,
            tariff_code=tariff_code,
            quantity=quantity,
            service_date=service_date,
        )

        return insurance_claim_submit_item
