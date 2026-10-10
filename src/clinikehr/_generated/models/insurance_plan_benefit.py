from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsurancePlanBenefit")


@_attrs_define
class InsurancePlanBenefit:
    """One benefit line of a plan - what is covered, at what percentage, with what limit.

    Attributes:
        id (UUID | Unset):
        name (None | str | Unset):
        coverage_type (None | str | Unset):
        claim_category (None | str | Unset):
        covered (bool | None | Unset):
        coverage_percentage (float | None | Unset):
        co_payment_value (float | None | Unset):
        limit_type (None | str | Unset):
        limit_value (float | None | Unset):
        max_amount (float | None | Unset):
        waiting_period (float | None | Unset):
        enrollee_type (None | str | Unset):
        gender (None | str | Unset):
        active (bool | None | Unset):
    """

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    coverage_type: None | str | Unset = UNSET
    claim_category: None | str | Unset = UNSET
    covered: bool | None | Unset = UNSET
    coverage_percentage: float | None | Unset = UNSET
    co_payment_value: float | None | Unset = UNSET
    limit_type: None | str | Unset = UNSET
    limit_value: float | None | Unset = UNSET
    max_amount: float | None | Unset = UNSET
    waiting_period: float | None | Unset = UNSET
    enrollee_type: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        coverage_type: None | str | Unset
        if isinstance(self.coverage_type, Unset):
            coverage_type = UNSET
        else:
            coverage_type = self.coverage_type

        claim_category: None | str | Unset
        if isinstance(self.claim_category, Unset):
            claim_category = UNSET
        else:
            claim_category = self.claim_category

        covered: bool | None | Unset
        if isinstance(self.covered, Unset):
            covered = UNSET
        else:
            covered = self.covered

        coverage_percentage: float | None | Unset
        if isinstance(self.coverage_percentage, Unset):
            coverage_percentage = UNSET
        else:
            coverage_percentage = self.coverage_percentage

        co_payment_value: float | None | Unset
        if isinstance(self.co_payment_value, Unset):
            co_payment_value = UNSET
        else:
            co_payment_value = self.co_payment_value

        limit_type: None | str | Unset
        if isinstance(self.limit_type, Unset):
            limit_type = UNSET
        else:
            limit_type = self.limit_type

        limit_value: float | None | Unset
        if isinstance(self.limit_value, Unset):
            limit_value = UNSET
        else:
            limit_value = self.limit_value

        max_amount: float | None | Unset
        if isinstance(self.max_amount, Unset):
            max_amount = UNSET
        else:
            max_amount = self.max_amount

        waiting_period: float | None | Unset
        if isinstance(self.waiting_period, Unset):
            waiting_period = UNSET
        else:
            waiting_period = self.waiting_period

        enrollee_type: None | str | Unset
        if isinstance(self.enrollee_type, Unset):
            enrollee_type = UNSET
        else:
            enrollee_type = self.enrollee_type

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if coverage_type is not UNSET:
            field_dict["coverage_type"] = coverage_type
        if claim_category is not UNSET:
            field_dict["claim_category"] = claim_category
        if covered is not UNSET:
            field_dict["covered"] = covered
        if coverage_percentage is not UNSET:
            field_dict["coverage_percentage"] = coverage_percentage
        if co_payment_value is not UNSET:
            field_dict["co_payment_value"] = co_payment_value
        if limit_type is not UNSET:
            field_dict["limit_type"] = limit_type
        if limit_value is not UNSET:
            field_dict["limit_value"] = limit_value
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount
        if waiting_period is not UNSET:
            field_dict["waiting_period"] = waiting_period
        if enrollee_type is not UNSET:
            field_dict["enrollee_type"] = enrollee_type
        if gender is not UNSET:
            field_dict["gender"] = gender
        if active is not UNSET:
            field_dict["active"] = active

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_coverage_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coverage_type = _parse_coverage_type(d.pop("coverage_type", UNSET))

        def _parse_claim_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_category = _parse_claim_category(d.pop("claim_category", UNSET))

        def _parse_covered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        covered = _parse_covered(d.pop("covered", UNSET))

        def _parse_coverage_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coverage_percentage = _parse_coverage_percentage(d.pop("coverage_percentage", UNSET))

        def _parse_co_payment_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        co_payment_value = _parse_co_payment_value(d.pop("co_payment_value", UNSET))

        def _parse_limit_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        limit_type = _parse_limit_type(d.pop("limit_type", UNSET))

        def _parse_limit_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        limit_value = _parse_limit_value(d.pop("limit_value", UNSET))

        def _parse_max_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_amount = _parse_max_amount(d.pop("max_amount", UNSET))

        def _parse_waiting_period(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        waiting_period = _parse_waiting_period(d.pop("waiting_period", UNSET))

        def _parse_enrollee_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enrollee_type = _parse_enrollee_type(d.pop("enrollee_type", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        insurance_plan_benefit = cls(
            id=id,
            name=name,
            coverage_type=coverage_type,
            claim_category=claim_category,
            covered=covered,
            coverage_percentage=coverage_percentage,
            co_payment_value=co_payment_value,
            limit_type=limit_type,
            limit_value=limit_value,
            max_amount=max_amount,
            waiting_period=waiting_period,
            enrollee_type=enrollee_type,
            gender=gender,
            active=active,
        )

        insurance_plan_benefit.additional_properties = d
        return insurance_plan_benefit

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
