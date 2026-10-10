from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_plan_benefit import InsurancePlanBenefit


T = TypeVar("T", bound="InsurancePlan")


@_attrs_define
class InsurancePlan:
    """A plan of an insurer the clinic linked to your organization. The list omits `benefits`; the single-plan read carries
    them (up to 500).

        Attributes:
            id (UUID):
            insurance_company_id (UUID):
            name (str):
            code (None | str | Unset):
            id_from_hmo (None | str | Unset): The insurer's own identifier for the plan.
            plan_type (None | str | Unset):
            coverage_type (None | str | Unset):
            description (None | str | Unset):
            amount_limit (float | None | Unset):
            co_payment_value (float | None | Unset):
            cover_dependants (bool | None | Unset):
            dependant_limit (float | None | Unset):
            pre_authorization_required (bool | None | Unset):
            network_type (None | str | Unset):
            waiting_period_days (float | None | Unset):
            active (bool | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            benefits (list[InsurancePlanBenefit] | Unset): Present on the single-plan read only.
    """

    id: UUID
    insurance_company_id: UUID
    name: str
    code: None | str | Unset = UNSET
    id_from_hmo: None | str | Unset = UNSET
    plan_type: None | str | Unset = UNSET
    coverage_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    amount_limit: float | None | Unset = UNSET
    co_payment_value: float | None | Unset = UNSET
    cover_dependants: bool | None | Unset = UNSET
    dependant_limit: float | None | Unset = UNSET
    pre_authorization_required: bool | None | Unset = UNSET
    network_type: None | str | Unset = UNSET
    waiting_period_days: float | None | Unset = UNSET
    active: bool | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    benefits: list[InsurancePlanBenefit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        insurance_company_id = str(self.insurance_company_id)

        name = self.name

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        id_from_hmo: None | str | Unset
        if isinstance(self.id_from_hmo, Unset):
            id_from_hmo = UNSET
        else:
            id_from_hmo = self.id_from_hmo

        plan_type: None | str | Unset
        if isinstance(self.plan_type, Unset):
            plan_type = UNSET
        else:
            plan_type = self.plan_type

        coverage_type: None | str | Unset
        if isinstance(self.coverage_type, Unset):
            coverage_type = UNSET
        else:
            coverage_type = self.coverage_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        amount_limit: float | None | Unset
        if isinstance(self.amount_limit, Unset):
            amount_limit = UNSET
        else:
            amount_limit = self.amount_limit

        co_payment_value: float | None | Unset
        if isinstance(self.co_payment_value, Unset):
            co_payment_value = UNSET
        else:
            co_payment_value = self.co_payment_value

        cover_dependants: bool | None | Unset
        if isinstance(self.cover_dependants, Unset):
            cover_dependants = UNSET
        else:
            cover_dependants = self.cover_dependants

        dependant_limit: float | None | Unset
        if isinstance(self.dependant_limit, Unset):
            dependant_limit = UNSET
        else:
            dependant_limit = self.dependant_limit

        pre_authorization_required: bool | None | Unset
        if isinstance(self.pre_authorization_required, Unset):
            pre_authorization_required = UNSET
        else:
            pre_authorization_required = self.pre_authorization_required

        network_type: None | str | Unset
        if isinstance(self.network_type, Unset):
            network_type = UNSET
        else:
            network_type = self.network_type

        waiting_period_days: float | None | Unset
        if isinstance(self.waiting_period_days, Unset):
            waiting_period_days = UNSET
        else:
            waiting_period_days = self.waiting_period_days

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        benefits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefits, Unset):
            benefits = []
            for benefits_item_data in self.benefits:
                benefits_item = benefits_item_data.to_dict()
                benefits.append(benefits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "insurance_company_id": insurance_company_id,
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if id_from_hmo is not UNSET:
            field_dict["id_from_hmo"] = id_from_hmo
        if plan_type is not UNSET:
            field_dict["plan_type"] = plan_type
        if coverage_type is not UNSET:
            field_dict["coverage_type"] = coverage_type
        if description is not UNSET:
            field_dict["description"] = description
        if amount_limit is not UNSET:
            field_dict["amount_limit"] = amount_limit
        if co_payment_value is not UNSET:
            field_dict["co_payment_value"] = co_payment_value
        if cover_dependants is not UNSET:
            field_dict["cover_dependants"] = cover_dependants
        if dependant_limit is not UNSET:
            field_dict["dependant_limit"] = dependant_limit
        if pre_authorization_required is not UNSET:
            field_dict["pre_authorization_required"] = pre_authorization_required
        if network_type is not UNSET:
            field_dict["network_type"] = network_type
        if waiting_period_days is not UNSET:
            field_dict["waiting_period_days"] = waiting_period_days
        if active is not UNSET:
            field_dict["active"] = active
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if benefits is not UNSET:
            field_dict["benefits"] = benefits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_plan_benefit import InsurancePlanBenefit  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        name = d.pop("name")

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_id_from_hmo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id_from_hmo = _parse_id_from_hmo(d.pop("id_from_hmo", UNSET))

        def _parse_plan_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_type = _parse_plan_type(d.pop("plan_type", UNSET))

        def _parse_coverage_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coverage_type = _parse_coverage_type(d.pop("coverage_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_amount_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_limit = _parse_amount_limit(d.pop("amount_limit", UNSET))

        def _parse_co_payment_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        co_payment_value = _parse_co_payment_value(d.pop("co_payment_value", UNSET))

        def _parse_cover_dependants(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cover_dependants = _parse_cover_dependants(d.pop("cover_dependants", UNSET))

        def _parse_dependant_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dependant_limit = _parse_dependant_limit(d.pop("dependant_limit", UNSET))

        def _parse_pre_authorization_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pre_authorization_required = _parse_pre_authorization_required(d.pop("pre_authorization_required", UNSET))

        def _parse_network_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_type = _parse_network_type(d.pop("network_type", UNSET))

        def _parse_waiting_period_days(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        waiting_period_days = _parse_waiting_period_days(d.pop("waiting_period_days", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        _benefits = d.pop("benefits", UNSET)
        benefits: list[InsurancePlanBenefit] | Unset = UNSET
        if _benefits is not UNSET:
            benefits = []
            for benefits_item_data in _benefits:
                benefits_item = InsurancePlanBenefit.from_dict(benefits_item_data)

                benefits.append(benefits_item)

        insurance_plan = cls(
            id=id,
            insurance_company_id=insurance_company_id,
            name=name,
            code=code,
            id_from_hmo=id_from_hmo,
            plan_type=plan_type,
            coverage_type=coverage_type,
            description=description,
            amount_limit=amount_limit,
            co_payment_value=co_payment_value,
            cover_dependants=cover_dependants,
            dependant_limit=dependant_limit,
            pre_authorization_required=pre_authorization_required,
            network_type=network_type,
            waiting_period_days=waiting_period_days,
            active=active,
            updated_at=updated_at,
            benefits=benefits,
        )

        insurance_plan.additional_properties = d
        return insurance_plan

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
