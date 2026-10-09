from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.coverage_update_coverage_type import CoverageUpdateCoverageType
from ..models.coverage_update_network_status import CoverageUpdateNetworkStatus
from ..models.coverage_update_payment_responsibility import CoverageUpdatePaymentResponsibility
from ..models.coverage_update_relationship_to_subscriber import CoverageUpdateRelationshipToSubscriber
from ..models.coverage_update_subscriber_gender import CoverageUpdateSubscriberGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageUpdate")


@_attrs_define
class CoverageUpdate:
    """A change to an existing coverage. Changing who the coverage is for (`payer_id`, `member_id`, `group_number`,
    `subscriber_member_id`, `relationship_to_subscriber` or the policy holder's name or date of birth) on a confirmed
    coverage sends it back to `unconfirmed` and inactive until staff confirm it again. Other edits keep its status.
    `coverage_active: false` and `termination_date` end a coverage; `coverage_active: true` is refused with
    `activation_requires_staff`. Nothing is ever deleted. Send JSON; a FHIR Coverage body is not accepted.

        Attributes:
            payer_id (UUID | Unset):
            member_id (str | Unset):
            group_number (str | Unset):
            group_name (str | Unset):
            plan_name (str | Unset):
            coverage_type (CoverageUpdateCoverageType | Unset):
            payment_responsibility (CoverageUpdatePaymentResponsibility | Unset):
            relationship_to_subscriber (CoverageUpdateRelationshipToSubscriber | Unset):
            subscriber_first_name (str | Unset):
            subscriber_last_name (str | Unset):
            subscriber_date_of_birth (datetime.date | Unset):
            subscriber_gender (CoverageUpdateSubscriberGender | Unset):
            subscriber_member_id (str | Unset):
            subscriber_address_line1 (str | Unset):
            subscriber_address_city (str | Unset):
            subscriber_address_state (str | Unset):
            subscriber_address_zip (str | Unset):
            coverage_active (bool | Unset): Only `false` is accepted: it ends the coverage. `true` is refused.
            effective_date (datetime.date | Unset):
            termination_date (datetime.date | Unset):
            copay_amount (float | Unset):
            coinsurance_percent (float | Unset):
            deductible_amount (float | Unset):
            out_of_pocket_max (float | Unset):
            pre_authorization_required (bool | Unset):
            network_status (CoverageUpdateNetworkStatus | Unset):
            is_primary (bool | Unset):
    """

    payer_id: UUID | Unset = UNSET
    member_id: str | Unset = UNSET
    group_number: str | Unset = UNSET
    group_name: str | Unset = UNSET
    plan_name: str | Unset = UNSET
    coverage_type: CoverageUpdateCoverageType | Unset = UNSET
    payment_responsibility: CoverageUpdatePaymentResponsibility | Unset = UNSET
    relationship_to_subscriber: CoverageUpdateRelationshipToSubscriber | Unset = UNSET
    subscriber_first_name: str | Unset = UNSET
    subscriber_last_name: str | Unset = UNSET
    subscriber_date_of_birth: datetime.date | Unset = UNSET
    subscriber_gender: CoverageUpdateSubscriberGender | Unset = UNSET
    subscriber_member_id: str | Unset = UNSET
    subscriber_address_line1: str | Unset = UNSET
    subscriber_address_city: str | Unset = UNSET
    subscriber_address_state: str | Unset = UNSET
    subscriber_address_zip: str | Unset = UNSET
    coverage_active: bool | Unset = UNSET
    effective_date: datetime.date | Unset = UNSET
    termination_date: datetime.date | Unset = UNSET
    copay_amount: float | Unset = UNSET
    coinsurance_percent: float | Unset = UNSET
    deductible_amount: float | Unset = UNSET
    out_of_pocket_max: float | Unset = UNSET
    pre_authorization_required: bool | Unset = UNSET
    network_status: CoverageUpdateNetworkStatus | Unset = UNSET
    is_primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payer_id: str | Unset = UNSET
        if not isinstance(self.payer_id, Unset):
            payer_id = str(self.payer_id)

        member_id = self.member_id

        group_number = self.group_number

        group_name = self.group_name

        plan_name = self.plan_name

        coverage_type: str | Unset = UNSET
        if not isinstance(self.coverage_type, Unset):
            coverage_type = self.coverage_type.value

        payment_responsibility: str | Unset = UNSET
        if not isinstance(self.payment_responsibility, Unset):
            payment_responsibility = self.payment_responsibility.value

        relationship_to_subscriber: str | Unset = UNSET
        if not isinstance(self.relationship_to_subscriber, Unset):
            relationship_to_subscriber = self.relationship_to_subscriber.value

        subscriber_first_name = self.subscriber_first_name

        subscriber_last_name = self.subscriber_last_name

        subscriber_date_of_birth: str | Unset = UNSET
        if not isinstance(self.subscriber_date_of_birth, Unset):
            subscriber_date_of_birth = self.subscriber_date_of_birth.isoformat()

        subscriber_gender: str | Unset = UNSET
        if not isinstance(self.subscriber_gender, Unset):
            subscriber_gender = self.subscriber_gender.value

        subscriber_member_id = self.subscriber_member_id

        subscriber_address_line1 = self.subscriber_address_line1

        subscriber_address_city = self.subscriber_address_city

        subscriber_address_state = self.subscriber_address_state

        subscriber_address_zip = self.subscriber_address_zip

        coverage_active = self.coverage_active

        effective_date: str | Unset = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        termination_date: str | Unset = UNSET
        if not isinstance(self.termination_date, Unset):
            termination_date = self.termination_date.isoformat()

        copay_amount = self.copay_amount

        coinsurance_percent = self.coinsurance_percent

        deductible_amount = self.deductible_amount

        out_of_pocket_max = self.out_of_pocket_max

        pre_authorization_required = self.pre_authorization_required

        network_status: str | Unset = UNSET
        if not isinstance(self.network_status, Unset):
            network_status = self.network_status.value

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if group_number is not UNSET:
            field_dict["group_number"] = group_number
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if plan_name is not UNSET:
            field_dict["plan_name"] = plan_name
        if coverage_type is not UNSET:
            field_dict["coverage_type"] = coverage_type
        if payment_responsibility is not UNSET:
            field_dict["payment_responsibility"] = payment_responsibility
        if relationship_to_subscriber is not UNSET:
            field_dict["relationship_to_subscriber"] = relationship_to_subscriber
        if subscriber_first_name is not UNSET:
            field_dict["subscriber_first_name"] = subscriber_first_name
        if subscriber_last_name is not UNSET:
            field_dict["subscriber_last_name"] = subscriber_last_name
        if subscriber_date_of_birth is not UNSET:
            field_dict["subscriber_date_of_birth"] = subscriber_date_of_birth
        if subscriber_gender is not UNSET:
            field_dict["subscriber_gender"] = subscriber_gender
        if subscriber_member_id is not UNSET:
            field_dict["subscriber_member_id"] = subscriber_member_id
        if subscriber_address_line1 is not UNSET:
            field_dict["subscriber_address_line1"] = subscriber_address_line1
        if subscriber_address_city is not UNSET:
            field_dict["subscriber_address_city"] = subscriber_address_city
        if subscriber_address_state is not UNSET:
            field_dict["subscriber_address_state"] = subscriber_address_state
        if subscriber_address_zip is not UNSET:
            field_dict["subscriber_address_zip"] = subscriber_address_zip
        if coverage_active is not UNSET:
            field_dict["coverage_active"] = coverage_active
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if termination_date is not UNSET:
            field_dict["termination_date"] = termination_date
        if copay_amount is not UNSET:
            field_dict["copay_amount"] = copay_amount
        if coinsurance_percent is not UNSET:
            field_dict["coinsurance_percent"] = coinsurance_percent
        if deductible_amount is not UNSET:
            field_dict["deductible_amount"] = deductible_amount
        if out_of_pocket_max is not UNSET:
            field_dict["out_of_pocket_max"] = out_of_pocket_max
        if pre_authorization_required is not UNSET:
            field_dict["pre_authorization_required"] = pre_authorization_required
        if network_status is not UNSET:
            field_dict["network_status"] = network_status
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _payer_id = d.pop("payer_id", UNSET)
        payer_id: UUID | Unset
        if isinstance(_payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = UUID(_payer_id)

        member_id = d.pop("member_id", UNSET)

        group_number = d.pop("group_number", UNSET)

        group_name = d.pop("group_name", UNSET)

        plan_name = d.pop("plan_name", UNSET)

        _coverage_type = d.pop("coverage_type", UNSET)
        coverage_type: CoverageUpdateCoverageType | Unset
        if isinstance(_coverage_type, Unset):
            coverage_type = UNSET
        else:
            coverage_type = CoverageUpdateCoverageType(_coverage_type)

        _payment_responsibility = d.pop("payment_responsibility", UNSET)
        payment_responsibility: CoverageUpdatePaymentResponsibility | Unset
        if isinstance(_payment_responsibility, Unset):
            payment_responsibility = UNSET
        else:
            payment_responsibility = CoverageUpdatePaymentResponsibility(_payment_responsibility)

        _relationship_to_subscriber = d.pop("relationship_to_subscriber", UNSET)
        relationship_to_subscriber: CoverageUpdateRelationshipToSubscriber | Unset
        if isinstance(_relationship_to_subscriber, Unset):
            relationship_to_subscriber = UNSET
        else:
            relationship_to_subscriber = CoverageUpdateRelationshipToSubscriber(_relationship_to_subscriber)

        subscriber_first_name = d.pop("subscriber_first_name", UNSET)

        subscriber_last_name = d.pop("subscriber_last_name", UNSET)

        _subscriber_date_of_birth = d.pop("subscriber_date_of_birth", UNSET)
        subscriber_date_of_birth: datetime.date | Unset
        if isinstance(_subscriber_date_of_birth, Unset):
            subscriber_date_of_birth = UNSET
        else:
            subscriber_date_of_birth = datetime.date.fromisoformat(_subscriber_date_of_birth)

        _subscriber_gender = d.pop("subscriber_gender", UNSET)
        subscriber_gender: CoverageUpdateSubscriberGender | Unset
        if isinstance(_subscriber_gender, Unset):
            subscriber_gender = UNSET
        else:
            subscriber_gender = CoverageUpdateSubscriberGender(_subscriber_gender)

        subscriber_member_id = d.pop("subscriber_member_id", UNSET)

        subscriber_address_line1 = d.pop("subscriber_address_line1", UNSET)

        subscriber_address_city = d.pop("subscriber_address_city", UNSET)

        subscriber_address_state = d.pop("subscriber_address_state", UNSET)

        subscriber_address_zip = d.pop("subscriber_address_zip", UNSET)

        coverage_active = d.pop("coverage_active", UNSET)

        _effective_date = d.pop("effective_date", UNSET)
        effective_date: datetime.date | Unset
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = datetime.date.fromisoformat(_effective_date)

        _termination_date = d.pop("termination_date", UNSET)
        termination_date: datetime.date | Unset
        if isinstance(_termination_date, Unset):
            termination_date = UNSET
        else:
            termination_date = datetime.date.fromisoformat(_termination_date)

        copay_amount = d.pop("copay_amount", UNSET)

        coinsurance_percent = d.pop("coinsurance_percent", UNSET)

        deductible_amount = d.pop("deductible_amount", UNSET)

        out_of_pocket_max = d.pop("out_of_pocket_max", UNSET)

        pre_authorization_required = d.pop("pre_authorization_required", UNSET)

        _network_status = d.pop("network_status", UNSET)
        network_status: CoverageUpdateNetworkStatus | Unset
        if isinstance(_network_status, Unset):
            network_status = UNSET
        else:
            network_status = CoverageUpdateNetworkStatus(_network_status)

        is_primary = d.pop("is_primary", UNSET)

        coverage_update = cls(
            payer_id=payer_id,
            member_id=member_id,
            group_number=group_number,
            group_name=group_name,
            plan_name=plan_name,
            coverage_type=coverage_type,
            payment_responsibility=payment_responsibility,
            relationship_to_subscriber=relationship_to_subscriber,
            subscriber_first_name=subscriber_first_name,
            subscriber_last_name=subscriber_last_name,
            subscriber_date_of_birth=subscriber_date_of_birth,
            subscriber_gender=subscriber_gender,
            subscriber_member_id=subscriber_member_id,
            subscriber_address_line1=subscriber_address_line1,
            subscriber_address_city=subscriber_address_city,
            subscriber_address_state=subscriber_address_state,
            subscriber_address_zip=subscriber_address_zip,
            coverage_active=coverage_active,
            effective_date=effective_date,
            termination_date=termination_date,
            copay_amount=copay_amount,
            coinsurance_percent=coinsurance_percent,
            deductible_amount=deductible_amount,
            out_of_pocket_max=out_of_pocket_max,
            pre_authorization_required=pre_authorization_required,
            network_status=network_status,
            is_primary=is_primary,
        )

        return coverage_update
