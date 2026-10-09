from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.coverage_create_coverage_type import CoverageCreateCoverageType
from ..models.coverage_create_network_status import CoverageCreateNetworkStatus
from ..models.coverage_create_payment_responsibility import CoverageCreatePaymentResponsibility
from ..models.coverage_create_relationship_to_subscriber import CoverageCreateRelationshipToSubscriber
from ..models.coverage_create_subscriber_gender import CoverageCreateSubscriberGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageCreate")


@_attrs_define
class CoverageCreate:
    """A coverage to record for a patient. It is saved straight away, but as `unconfirmed` with `coverage_active: false`;
    clinic staff confirm the payer match before it counts. `payer_id` must be a payer the clinic has enabled in Settings
    → Insurance (see `GET …/payers`), otherwise `payer_not_enabled`; a patient can hold one coverage per payer
    (`coverage_exists`). `coverage_active: true` is refused with `activation_requires_staff`. The clinic's notes, the
    deductible and out-of-pocket amounts met and every eligibility field cannot be sent. The `Idempotency-Key` header is
    REQUIRED. Send JSON; a FHIR Coverage body is not accepted.

        Attributes:
            patient_id (UUID):
            payer_id (UUID):
            member_id (str | Unset):
            group_number (str | Unset):
            group_name (str | Unset):
            plan_name (str | Unset):
            coverage_type (CoverageCreateCoverageType | Unset):
            payment_responsibility (CoverageCreatePaymentResponsibility | Unset):
            relationship_to_subscriber (CoverageCreateRelationshipToSubscriber | Unset):
            subscriber_first_name (str | Unset):
            subscriber_last_name (str | Unset):
            subscriber_date_of_birth (datetime.date | Unset):
            subscriber_gender (CoverageCreateSubscriberGender | Unset):
            subscriber_member_id (str | Unset):
            subscriber_address_line1 (str | Unset):
            subscriber_address_city (str | Unset):
            subscriber_address_state (str | Unset):
            subscriber_address_zip (str | Unset):
            coverage_active (bool | Unset): Send `false` or omit it. `true` is refused: only clinic staff activate a
                coverage.
            effective_date (datetime.date | Unset):
            termination_date (datetime.date | Unset):
            copay_amount (float | Unset):
            coinsurance_percent (float | Unset):
            deductible_amount (float | Unset):
            out_of_pocket_max (float | Unset):
            pre_authorization_required (bool | Unset):
            network_status (CoverageCreateNetworkStatus | Unset):
            is_primary (bool | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    payer_id: UUID
    member_id: str | Unset = UNSET
    group_number: str | Unset = UNSET
    group_name: str | Unset = UNSET
    plan_name: str | Unset = UNSET
    coverage_type: CoverageCreateCoverageType | Unset = UNSET
    payment_responsibility: CoverageCreatePaymentResponsibility | Unset = UNSET
    relationship_to_subscriber: CoverageCreateRelationshipToSubscriber | Unset = UNSET
    subscriber_first_name: str | Unset = UNSET
    subscriber_last_name: str | Unset = UNSET
    subscriber_date_of_birth: datetime.date | Unset = UNSET
    subscriber_gender: CoverageCreateSubscriberGender | Unset = UNSET
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
    network_status: CoverageCreateNetworkStatus | Unset = UNSET
    is_primary: bool | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

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

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
                "payer_id": payer_id,
            }
        )
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
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        payer_id = UUID(d.pop("payer_id"))

        member_id = d.pop("member_id", UNSET)

        group_number = d.pop("group_number", UNSET)

        group_name = d.pop("group_name", UNSET)

        plan_name = d.pop("plan_name", UNSET)

        _coverage_type = d.pop("coverage_type", UNSET)
        coverage_type: CoverageCreateCoverageType | Unset
        if isinstance(_coverage_type, Unset):
            coverage_type = UNSET
        else:
            coverage_type = CoverageCreateCoverageType(_coverage_type)

        _payment_responsibility = d.pop("payment_responsibility", UNSET)
        payment_responsibility: CoverageCreatePaymentResponsibility | Unset
        if isinstance(_payment_responsibility, Unset):
            payment_responsibility = UNSET
        else:
            payment_responsibility = CoverageCreatePaymentResponsibility(_payment_responsibility)

        _relationship_to_subscriber = d.pop("relationship_to_subscriber", UNSET)
        relationship_to_subscriber: CoverageCreateRelationshipToSubscriber | Unset
        if isinstance(_relationship_to_subscriber, Unset):
            relationship_to_subscriber = UNSET
        else:
            relationship_to_subscriber = CoverageCreateRelationshipToSubscriber(_relationship_to_subscriber)

        subscriber_first_name = d.pop("subscriber_first_name", UNSET)

        subscriber_last_name = d.pop("subscriber_last_name", UNSET)

        _subscriber_date_of_birth = d.pop("subscriber_date_of_birth", UNSET)
        subscriber_date_of_birth: datetime.date | Unset
        if isinstance(_subscriber_date_of_birth, Unset):
            subscriber_date_of_birth = UNSET
        else:
            subscriber_date_of_birth = datetime.date.fromisoformat(_subscriber_date_of_birth)

        _subscriber_gender = d.pop("subscriber_gender", UNSET)
        subscriber_gender: CoverageCreateSubscriberGender | Unset
        if isinstance(_subscriber_gender, Unset):
            subscriber_gender = UNSET
        else:
            subscriber_gender = CoverageCreateSubscriberGender(_subscriber_gender)

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
        network_status: CoverageCreateNetworkStatus | Unset
        if isinstance(_network_status, Unset):
            network_status = UNSET
        else:
            network_status = CoverageCreateNetworkStatus(_network_status)

        is_primary = d.pop("is_primary", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        coverage_create = cls(
            patient_id=patient_id,
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
            origin_assistant_name=origin_assistant_name,
        )

        return coverage_create
