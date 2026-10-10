from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsurancePreAuthorizationItem")


@_attrs_define
class InsurancePreAuthorizationItem:
    """
    Attributes:
        id (UUID | Unset):
        item_type (None | str | Unset):
        description (None | str | Unset):
        tariff_code (None | str | Unset):
        quantity (float | None | Unset):
        unit_cost (float | None | Unset):
        total_cost (float | None | Unset):
        diagnosis (None | str | Unset):
        icd_cpt_code (None | str | Unset):
        medical_necessity (None | str | Unset):
        approval_status (None | str | Unset):
        is_approved (bool | None | Unset):
        reject_reason (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    item_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tariff_code: None | str | Unset = UNSET
    quantity: float | None | Unset = UNSET
    unit_cost: float | None | Unset = UNSET
    total_cost: float | None | Unset = UNSET
    diagnosis: None | str | Unset = UNSET
    icd_cpt_code: None | str | Unset = UNSET
    medical_necessity: None | str | Unset = UNSET
    approval_status: None | str | Unset = UNSET
    is_approved: bool | None | Unset = UNSET
    reject_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        item_type: None | str | Unset
        if isinstance(self.item_type, Unset):
            item_type = UNSET
        else:
            item_type = self.item_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tariff_code: None | str | Unset
        if isinstance(self.tariff_code, Unset):
            tariff_code = UNSET
        else:
            tariff_code = self.tariff_code

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        unit_cost: float | None | Unset
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        total_cost: float | None | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        diagnosis: None | str | Unset
        if isinstance(self.diagnosis, Unset):
            diagnosis = UNSET
        else:
            diagnosis = self.diagnosis

        icd_cpt_code: None | str | Unset
        if isinstance(self.icd_cpt_code, Unset):
            icd_cpt_code = UNSET
        else:
            icd_cpt_code = self.icd_cpt_code

        medical_necessity: None | str | Unset
        if isinstance(self.medical_necessity, Unset):
            medical_necessity = UNSET
        else:
            medical_necessity = self.medical_necessity

        approval_status: None | str | Unset
        if isinstance(self.approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = self.approval_status

        is_approved: bool | None | Unset
        if isinstance(self.is_approved, Unset):
            is_approved = UNSET
        else:
            is_approved = self.is_approved

        reject_reason: None | str | Unset
        if isinstance(self.reject_reason, Unset):
            reject_reason = UNSET
        else:
            reject_reason = self.reject_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if description is not UNSET:
            field_dict["description"] = description
        if tariff_code is not UNSET:
            field_dict["tariff_code"] = tariff_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_cost is not UNSET:
            field_dict["unit_cost"] = unit_cost
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost
        if diagnosis is not UNSET:
            field_dict["diagnosis"] = diagnosis
        if icd_cpt_code is not UNSET:
            field_dict["icd_cpt_code"] = icd_cpt_code
        if medical_necessity is not UNSET:
            field_dict["medical_necessity"] = medical_necessity
        if approval_status is not UNSET:
            field_dict["approval_status"] = approval_status
        if is_approved is not UNSET:
            field_dict["is_approved"] = is_approved
        if reject_reason is not UNSET:
            field_dict["reject_reason"] = reject_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_item_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_type = _parse_item_type(d.pop("item_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tariff_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tariff_code = _parse_tariff_code(d.pop("tariff_code", UNSET))

        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_unit_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_cost = _parse_unit_cost(d.pop("unit_cost", UNSET))

        def _parse_total_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_cost = _parse_total_cost(d.pop("total_cost", UNSET))

        def _parse_diagnosis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diagnosis = _parse_diagnosis(d.pop("diagnosis", UNSET))

        def _parse_icd_cpt_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icd_cpt_code = _parse_icd_cpt_code(d.pop("icd_cpt_code", UNSET))

        def _parse_medical_necessity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medical_necessity = _parse_medical_necessity(d.pop("medical_necessity", UNSET))

        def _parse_approval_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_status = _parse_approval_status(d.pop("approval_status", UNSET))

        def _parse_is_approved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_approved = _parse_is_approved(d.pop("is_approved", UNSET))

        def _parse_reject_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reject_reason = _parse_reject_reason(d.pop("reject_reason", UNSET))

        insurance_pre_authorization_item = cls(
            id=id,
            item_type=item_type,
            description=description,
            tariff_code=tariff_code,
            quantity=quantity,
            unit_cost=unit_cost,
            total_cost=total_cost,
            diagnosis=diagnosis,
            icd_cpt_code=icd_cpt_code,
            medical_necessity=medical_necessity,
            approval_status=approval_status,
            is_approved=is_approved,
            reject_reason=reject_reason,
        )

        insurance_pre_authorization_item.additional_properties = d
        return insurance_pre_authorization_item

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
