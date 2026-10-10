from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insurance_payment_advice_method import InsurancePaymentAdviceMethod
from ..models.insurance_payment_advice_status import InsurancePaymentAdviceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_payment_advice_allocations_item import InsurancePaymentAdviceAllocationsItem


T = TypeVar("T", bound="InsurancePaymentAdvice")


@_attrs_define
class InsurancePaymentAdvice:
    """What an insurer says it paid the clinic. It is an ADVICE for clinic staff to reconcile: it never changes a claim,
    the clinic's payments or its books. `status` is `advised` until staff act on it.

        Attributes:
            id (UUID):
            insurance_company_id (UUID):
            amount (float):
            status (InsurancePaymentAdviceStatus):
            paid_on (datetime.date | Unset):
            currency (str | Unset):
            method (InsurancePaymentAdviceMethod | Unset):
            reference (None | str | Unset):
            created_at (datetime.datetime | Unset):
            allocations (list[InsurancePaymentAdviceAllocationsItem] | Unset):
    """

    id: UUID
    insurance_company_id: UUID
    amount: float
    status: InsurancePaymentAdviceStatus
    paid_on: datetime.date | Unset = UNSET
    currency: str | Unset = UNSET
    method: InsurancePaymentAdviceMethod | Unset = UNSET
    reference: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    allocations: list[InsurancePaymentAdviceAllocationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        insurance_company_id = str(self.insurance_company_id)

        amount = self.amount

        status = self.status.value

        paid_on: str | Unset = UNSET
        if not isinstance(self.paid_on, Unset):
            paid_on = self.paid_on.isoformat()

        currency = self.currency

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        allocations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "insurance_company_id": insurance_company_id,
                "amount": amount,
                "status": status,
            }
        )
        if paid_on is not UNSET:
            field_dict["paid_on"] = paid_on
        if currency is not UNSET:
            field_dict["currency"] = currency
        if method is not UNSET:
            field_dict["method"] = method
        if reference is not UNSET:
            field_dict["reference"] = reference
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if allocations is not UNSET:
            field_dict["allocations"] = allocations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_payment_advice_allocations_item import InsurancePaymentAdviceAllocationsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        amount = d.pop("amount")

        status = InsurancePaymentAdviceStatus(d.pop("status"))

        _paid_on = d.pop("paid_on", UNSET)
        paid_on: datetime.date | Unset
        if isinstance(_paid_on, Unset):
            paid_on = UNSET
        else:
            paid_on = datetime.date.fromisoformat(_paid_on)

        currency = d.pop("currency", UNSET)

        _method = d.pop("method", UNSET)
        method: InsurancePaymentAdviceMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = InsurancePaymentAdviceMethod(_method)

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _allocations = d.pop("allocations", UNSET)
        allocations: list[InsurancePaymentAdviceAllocationsItem] | Unset = UNSET
        if _allocations is not UNSET:
            allocations = []
            for allocations_item_data in _allocations:
                allocations_item = InsurancePaymentAdviceAllocationsItem.from_dict(allocations_item_data)

                allocations.append(allocations_item)

        insurance_payment_advice = cls(
            id=id,
            insurance_company_id=insurance_company_id,
            amount=amount,
            status=status,
            paid_on=paid_on,
            currency=currency,
            method=method,
            reference=reference,
            created_at=created_at,
            allocations=allocations,
        )

        insurance_payment_advice.additional_properties = d
        return insurance_payment_advice

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
