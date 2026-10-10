from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.insurance_payment_advice_create_method import InsurancePaymentAdviceCreateMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_payment_advice_allocation import InsurancePaymentAdviceAllocation


T = TypeVar("T", bound="InsurancePaymentAdviceCreate")


@_attrs_define
class InsurancePaymentAdviceCreate:
    """A payment advice. Each allocation names a claim of that insurer that is awaiting payment and an amount no larger
    than what the claim still owes; the allocations may not add up to more than `amount`. `currency`, if sent, must be
    the clinic's currency.

        Attributes:
            insurance_company_id (UUID):
            paid_on (datetime.date):
            amount (float):
            method (InsurancePaymentAdviceCreateMethod):
            currency (str | Unset):
            reference (str | Unset):
            allocations (list[InsurancePaymentAdviceAllocation] | Unset):
    """

    insurance_company_id: UUID
    paid_on: datetime.date
    amount: float
    method: InsurancePaymentAdviceCreateMethod
    currency: str | Unset = UNSET
    reference: str | Unset = UNSET
    allocations: list[InsurancePaymentAdviceAllocation] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        insurance_company_id = str(self.insurance_company_id)

        paid_on = self.paid_on.isoformat()

        amount = self.amount

        method = self.method.value

        currency = self.currency

        reference = self.reference

        allocations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "insurance_company_id": insurance_company_id,
                "paid_on": paid_on,
                "amount": amount,
                "method": method,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if reference is not UNSET:
            field_dict["reference"] = reference
        if allocations is not UNSET:
            field_dict["allocations"] = allocations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_payment_advice_allocation import InsurancePaymentAdviceAllocation  # noqa: PLC0415

        d = dict(src_dict)
        insurance_company_id = UUID(d.pop("insurance_company_id"))

        paid_on = datetime.date.fromisoformat(d.pop("paid_on"))

        amount = d.pop("amount")

        method = InsurancePaymentAdviceCreateMethod(d.pop("method"))

        currency = d.pop("currency", UNSET)

        reference = d.pop("reference", UNSET)

        _allocations = d.pop("allocations", UNSET)
        allocations: list[InsurancePaymentAdviceAllocation] | Unset = UNSET
        if _allocations is not UNSET:
            allocations = []
            for allocations_item_data in _allocations:
                allocations_item = InsurancePaymentAdviceAllocation.from_dict(allocations_item_data)

                allocations.append(allocations_item)

        insurance_payment_advice_create = cls(
            insurance_company_id=insurance_company_id,
            paid_on=paid_on,
            amount=amount,
            method=method,
            currency=currency,
            reference=reference,
            allocations=allocations,
        )

        return insurance_payment_advice_create
