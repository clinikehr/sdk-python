from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insurance_claim_item_hmo_item_status_type_1 import InsuranceClaimItemHmoItemStatusType1
from ..models.insurance_claim_item_hmo_item_status_type_2_type_1 import InsuranceClaimItemHmoItemStatusType2Type1
from ..models.insurance_claim_item_hmo_item_status_type_3_type_1 import InsuranceClaimItemHmoItemStatusType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="InsuranceClaimItem")


@_attrs_define
class InsuranceClaimItem:
    """A line of a claim. `*_billed` is what the clinic billed; `*_approved` is what the insurer approved (null until
    vetted). `hmo_item_status` is `PENDING`, `APPROVED`, `ADJUSTED` or `DECLINED`.

        Attributes:
            id (UUID | Unset):
            item_type (None | str | Unset):
            description (None | str | Unset):
            tariff_code (None | str | Unset):
            service_date (datetime.datetime | None | Unset):
            qty_billed (float | None | Unset):
            unit_price_billed (float | None | Unset):
            sub_total_billed (float | None | Unset):
            qty_approved (float | None | Unset):
            unit_price_approved (float | None | Unset):
            sub_total_approved (float | None | Unset):
            hmo_item_status (InsuranceClaimItemHmoItemStatusType1 | InsuranceClaimItemHmoItemStatusType2Type1 |
                InsuranceClaimItemHmoItemStatusType3Type1 | None | Unset):
            denial_reason (None | str | Unset):
            comments (list[str] | Unset):
            benefit_label (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    item_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tariff_code: None | str | Unset = UNSET
    service_date: datetime.datetime | None | Unset = UNSET
    qty_billed: float | None | Unset = UNSET
    unit_price_billed: float | None | Unset = UNSET
    sub_total_billed: float | None | Unset = UNSET
    qty_approved: float | None | Unset = UNSET
    unit_price_approved: float | None | Unset = UNSET
    sub_total_approved: float | None | Unset = UNSET
    hmo_item_status: (
        InsuranceClaimItemHmoItemStatusType1
        | InsuranceClaimItemHmoItemStatusType2Type1
        | InsuranceClaimItemHmoItemStatusType3Type1
        | None
        | Unset
    ) = UNSET
    denial_reason: None | str | Unset = UNSET
    comments: list[str] | Unset = UNSET
    benefit_label: None | str | Unset = UNSET
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

        service_date: None | str | Unset
        if isinstance(self.service_date, Unset):
            service_date = UNSET
        elif isinstance(self.service_date, datetime.datetime):
            service_date = self.service_date.isoformat()
        else:
            service_date = self.service_date

        qty_billed: float | None | Unset
        if isinstance(self.qty_billed, Unset):
            qty_billed = UNSET
        else:
            qty_billed = self.qty_billed

        unit_price_billed: float | None | Unset
        if isinstance(self.unit_price_billed, Unset):
            unit_price_billed = UNSET
        else:
            unit_price_billed = self.unit_price_billed

        sub_total_billed: float | None | Unset
        if isinstance(self.sub_total_billed, Unset):
            sub_total_billed = UNSET
        else:
            sub_total_billed = self.sub_total_billed

        qty_approved: float | None | Unset
        if isinstance(self.qty_approved, Unset):
            qty_approved = UNSET
        else:
            qty_approved = self.qty_approved

        unit_price_approved: float | None | Unset
        if isinstance(self.unit_price_approved, Unset):
            unit_price_approved = UNSET
        else:
            unit_price_approved = self.unit_price_approved

        sub_total_approved: float | None | Unset
        if isinstance(self.sub_total_approved, Unset):
            sub_total_approved = UNSET
        else:
            sub_total_approved = self.sub_total_approved

        hmo_item_status: None | str | Unset
        if isinstance(self.hmo_item_status, Unset):
            hmo_item_status = UNSET
        elif isinstance(self.hmo_item_status, InsuranceClaimItemHmoItemStatusType1):
            hmo_item_status = self.hmo_item_status.value
        elif isinstance(self.hmo_item_status, InsuranceClaimItemHmoItemStatusType2Type1):
            hmo_item_status = self.hmo_item_status.value
        elif isinstance(self.hmo_item_status, InsuranceClaimItemHmoItemStatusType3Type1):
            hmo_item_status = self.hmo_item_status.value
        else:
            hmo_item_status = self.hmo_item_status

        denial_reason: None | str | Unset
        if isinstance(self.denial_reason, Unset):
            denial_reason = UNSET
        else:
            denial_reason = self.denial_reason

        comments: list[str] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments

        benefit_label: None | str | Unset
        if isinstance(self.benefit_label, Unset):
            benefit_label = UNSET
        else:
            benefit_label = self.benefit_label

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
        if service_date is not UNSET:
            field_dict["service_date"] = service_date
        if qty_billed is not UNSET:
            field_dict["qty_billed"] = qty_billed
        if unit_price_billed is not UNSET:
            field_dict["unit_price_billed"] = unit_price_billed
        if sub_total_billed is not UNSET:
            field_dict["sub_total_billed"] = sub_total_billed
        if qty_approved is not UNSET:
            field_dict["qty_approved"] = qty_approved
        if unit_price_approved is not UNSET:
            field_dict["unit_price_approved"] = unit_price_approved
        if sub_total_approved is not UNSET:
            field_dict["sub_total_approved"] = sub_total_approved
        if hmo_item_status is not UNSET:
            field_dict["hmo_item_status"] = hmo_item_status
        if denial_reason is not UNSET:
            field_dict["denial_reason"] = denial_reason
        if comments is not UNSET:
            field_dict["comments"] = comments
        if benefit_label is not UNSET:
            field_dict["benefit_label"] = benefit_label

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

        def _parse_service_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_date_type_0 = datetime.datetime.fromisoformat(data)

                return service_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        service_date = _parse_service_date(d.pop("service_date", UNSET))

        def _parse_qty_billed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qty_billed = _parse_qty_billed(d.pop("qty_billed", UNSET))

        def _parse_unit_price_billed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price_billed = _parse_unit_price_billed(d.pop("unit_price_billed", UNSET))

        def _parse_sub_total_billed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sub_total_billed = _parse_sub_total_billed(d.pop("sub_total_billed", UNSET))

        def _parse_qty_approved(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qty_approved = _parse_qty_approved(d.pop("qty_approved", UNSET))

        def _parse_unit_price_approved(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price_approved = _parse_unit_price_approved(d.pop("unit_price_approved", UNSET))

        def _parse_sub_total_approved(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sub_total_approved = _parse_sub_total_approved(d.pop("sub_total_approved", UNSET))

        def _parse_hmo_item_status(
            data: object,
        ) -> (
            InsuranceClaimItemHmoItemStatusType1
            | InsuranceClaimItemHmoItemStatusType2Type1
            | InsuranceClaimItemHmoItemStatusType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_item_status_type_1 = InsuranceClaimItemHmoItemStatusType1(data)

                return hmo_item_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_item_status_type_2_type_1 = InsuranceClaimItemHmoItemStatusType2Type1(data)

                return hmo_item_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hmo_item_status_type_3_type_1 = InsuranceClaimItemHmoItemStatusType3Type1(data)

                return hmo_item_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InsuranceClaimItemHmoItemStatusType1
                | InsuranceClaimItemHmoItemStatusType2Type1
                | InsuranceClaimItemHmoItemStatusType3Type1
                | None
                | Unset,
                data,
            )

        hmo_item_status = _parse_hmo_item_status(d.pop("hmo_item_status", UNSET))

        def _parse_denial_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        denial_reason = _parse_denial_reason(d.pop("denial_reason", UNSET))

        comments = cast(list[str], d.pop("comments", UNSET))

        def _parse_benefit_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        benefit_label = _parse_benefit_label(d.pop("benefit_label", UNSET))

        insurance_claim_item = cls(
            id=id,
            item_type=item_type,
            description=description,
            tariff_code=tariff_code,
            service_date=service_date,
            qty_billed=qty_billed,
            unit_price_billed=unit_price_billed,
            sub_total_billed=sub_total_billed,
            qty_approved=qty_approved,
            unit_price_approved=unit_price_approved,
            sub_total_approved=sub_total_approved,
            hmo_item_status=hmo_item_status,
            denial_reason=denial_reason,
            comments=comments,
            benefit_label=benefit_label,
        )

        insurance_claim_item.additional_properties = d
        return insurance_claim_item

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
