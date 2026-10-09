from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.coverage_coverage_type_type_1 import CoverageCoverageTypeType1
from ..models.coverage_coverage_type_type_2_type_1 import CoverageCoverageTypeType2Type1
from ..models.coverage_coverage_type_type_3_type_1 import CoverageCoverageTypeType3Type1
from ..models.coverage_network_status_type_1 import CoverageNetworkStatusType1
from ..models.coverage_network_status_type_2_type_1 import CoverageNetworkStatusType2Type1
from ..models.coverage_network_status_type_3_type_1 import CoverageNetworkStatusType3Type1
from ..models.coverage_payment_responsibility_type_1 import CoveragePaymentResponsibilityType1
from ..models.coverage_payment_responsibility_type_2_type_1 import CoveragePaymentResponsibilityType2Type1
from ..models.coverage_payment_responsibility_type_3_type_1 import CoveragePaymentResponsibilityType3Type1
from ..models.coverage_relationship_to_subscriber_type_1 import CoverageRelationshipToSubscriberType1
from ..models.coverage_relationship_to_subscriber_type_2_type_1 import CoverageRelationshipToSubscriberType2Type1
from ..models.coverage_relationship_to_subscriber_type_3_type_1 import CoverageRelationshipToSubscriberType3Type1
from ..models.coverage_source import CoverageSource
from ..models.coverage_verification_status import CoverageVerificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_eligibility import CoverageEligibility
    from ..models.coverage_payer import CoveragePayer
    from ..models.coverage_subscriber import CoverageSubscriber


T = TypeVar("T", bound="Coverage")


@_attrs_define
class Coverage:
    """A patient's insurance coverage — the exposed-field allow-list, field by field. A coverage that came in through the
    API is saved straight away and visible here, but it is `unconfirmed` and `coverage_active` is `false` until clinic
    staff confirm the payer match; the clinic's own coverages are `confirmed`. Eligibility figures, the clinic's notes
    and the policy holder's address are never exposed.

        Attributes:
            id (UUID):
            patient_id (UUID):
            coverage_active (bool): Always false while `verification_status` is `unconfirmed`.
            verification_status (CoverageVerificationStatus):
            source (CoverageSource): `api` for a coverage that came in through the API.
            payer (CoveragePayer | None | Unset):
            member_id (None | str | Unset):
            group_number (None | str | Unset):
            group_name (None | str | Unset):
            plan_name (None | str | Unset):
            coverage_type (CoverageCoverageTypeType1 | CoverageCoverageTypeType2Type1 | CoverageCoverageTypeType3Type1 |
                None | Unset):
            payment_responsibility (CoveragePaymentResponsibilityType1 | CoveragePaymentResponsibilityType2Type1 |
                CoveragePaymentResponsibilityType3Type1 | None | Unset): P primary, S secondary, T tertiary.
            relationship_to_subscriber (CoverageRelationshipToSubscriberType1 | CoverageRelationshipToSubscriberType2Type1 |
                CoverageRelationshipToSubscriberType3Type1 | None | Unset):
            subscriber (CoverageSubscriber | None | Unset):
            is_primary (bool | None | Unset):
            effective_date (datetime.date | None | Unset):
            termination_date (datetime.date | None | Unset):
            copay_amount (float | None | Unset):
            coinsurance_percent (float | None | Unset):
            deductible_amount (float | None | Unset):
            out_of_pocket_max (float | None | Unset):
            pre_authorization_required (bool | None | Unset):
            network_status (CoverageNetworkStatusType1 | CoverageNetworkStatusType2Type1 | CoverageNetworkStatusType3Type1 |
                None | Unset):
            eligibility (CoverageEligibility | None | Unset):
            origin_assistant_name (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    patient_id: UUID
    coverage_active: bool
    verification_status: CoverageVerificationStatus
    source: CoverageSource
    payer: CoveragePayer | None | Unset = UNSET
    member_id: None | str | Unset = UNSET
    group_number: None | str | Unset = UNSET
    group_name: None | str | Unset = UNSET
    plan_name: None | str | Unset = UNSET
    coverage_type: (
        CoverageCoverageTypeType1 | CoverageCoverageTypeType2Type1 | CoverageCoverageTypeType3Type1 | None | Unset
    ) = UNSET
    payment_responsibility: (
        CoveragePaymentResponsibilityType1
        | CoveragePaymentResponsibilityType2Type1
        | CoveragePaymentResponsibilityType3Type1
        | None
        | Unset
    ) = UNSET
    relationship_to_subscriber: (
        CoverageRelationshipToSubscriberType1
        | CoverageRelationshipToSubscriberType2Type1
        | CoverageRelationshipToSubscriberType3Type1
        | None
        | Unset
    ) = UNSET
    subscriber: CoverageSubscriber | None | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    effective_date: datetime.date | None | Unset = UNSET
    termination_date: datetime.date | None | Unset = UNSET
    copay_amount: float | None | Unset = UNSET
    coinsurance_percent: float | None | Unset = UNSET
    deductible_amount: float | None | Unset = UNSET
    out_of_pocket_max: float | None | Unset = UNSET
    pre_authorization_required: bool | None | Unset = UNSET
    network_status: (
        CoverageNetworkStatusType1 | CoverageNetworkStatusType2Type1 | CoverageNetworkStatusType3Type1 | None | Unset
    ) = UNSET
    eligibility: CoverageEligibility | None | Unset = UNSET
    origin_assistant_name: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.coverage_eligibility import CoverageEligibility  # noqa: PLC0415
        from ..models.coverage_payer import CoveragePayer  # noqa: PLC0415
        from ..models.coverage_subscriber import CoverageSubscriber  # noqa: PLC0415

        id = str(self.id)

        patient_id = str(self.patient_id)

        coverage_active = self.coverage_active

        verification_status = self.verification_status.value

        source = self.source.value

        payer: dict[str, Any] | None | Unset
        if isinstance(self.payer, Unset):
            payer = UNSET
        elif isinstance(self.payer, CoveragePayer):
            payer = self.payer.to_dict()
        else:
            payer = self.payer

        member_id: None | str | Unset
        if isinstance(self.member_id, Unset):
            member_id = UNSET
        else:
            member_id = self.member_id

        group_number: None | str | Unset
        if isinstance(self.group_number, Unset):
            group_number = UNSET
        else:
            group_number = self.group_number

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        plan_name: None | str | Unset
        if isinstance(self.plan_name, Unset):
            plan_name = UNSET
        else:
            plan_name = self.plan_name

        coverage_type: None | str | Unset
        if isinstance(self.coverage_type, Unset):
            coverage_type = UNSET
        elif isinstance(self.coverage_type, CoverageCoverageTypeType1):
            coverage_type = self.coverage_type.value
        elif isinstance(self.coverage_type, CoverageCoverageTypeType2Type1):
            coverage_type = self.coverage_type.value
        elif isinstance(self.coverage_type, CoverageCoverageTypeType3Type1):
            coverage_type = self.coverage_type.value
        else:
            coverage_type = self.coverage_type

        payment_responsibility: None | str | Unset
        if isinstance(self.payment_responsibility, Unset):
            payment_responsibility = UNSET
        elif isinstance(self.payment_responsibility, CoveragePaymentResponsibilityType1):
            payment_responsibility = self.payment_responsibility.value
        elif isinstance(self.payment_responsibility, CoveragePaymentResponsibilityType2Type1):
            payment_responsibility = self.payment_responsibility.value
        elif isinstance(self.payment_responsibility, CoveragePaymentResponsibilityType3Type1):
            payment_responsibility = self.payment_responsibility.value
        else:
            payment_responsibility = self.payment_responsibility

        relationship_to_subscriber: None | str | Unset
        if isinstance(self.relationship_to_subscriber, Unset):
            relationship_to_subscriber = UNSET
        elif isinstance(self.relationship_to_subscriber, CoverageRelationshipToSubscriberType1):
            relationship_to_subscriber = self.relationship_to_subscriber.value
        elif isinstance(self.relationship_to_subscriber, CoverageRelationshipToSubscriberType2Type1):
            relationship_to_subscriber = self.relationship_to_subscriber.value
        elif isinstance(self.relationship_to_subscriber, CoverageRelationshipToSubscriberType3Type1):
            relationship_to_subscriber = self.relationship_to_subscriber.value
        else:
            relationship_to_subscriber = self.relationship_to_subscriber

        subscriber: dict[str, Any] | None | Unset
        if isinstance(self.subscriber, Unset):
            subscriber = UNSET
        elif isinstance(self.subscriber, CoverageSubscriber):
            subscriber = self.subscriber.to_dict()
        else:
            subscriber = self.subscriber

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        effective_date: None | str | Unset
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        elif isinstance(self.effective_date, datetime.date):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        termination_date: None | str | Unset
        if isinstance(self.termination_date, Unset):
            termination_date = UNSET
        elif isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat()
        else:
            termination_date = self.termination_date

        copay_amount: float | None | Unset
        if isinstance(self.copay_amount, Unset):
            copay_amount = UNSET
        else:
            copay_amount = self.copay_amount

        coinsurance_percent: float | None | Unset
        if isinstance(self.coinsurance_percent, Unset):
            coinsurance_percent = UNSET
        else:
            coinsurance_percent = self.coinsurance_percent

        deductible_amount: float | None | Unset
        if isinstance(self.deductible_amount, Unset):
            deductible_amount = UNSET
        else:
            deductible_amount = self.deductible_amount

        out_of_pocket_max: float | None | Unset
        if isinstance(self.out_of_pocket_max, Unset):
            out_of_pocket_max = UNSET
        else:
            out_of_pocket_max = self.out_of_pocket_max

        pre_authorization_required: bool | None | Unset
        if isinstance(self.pre_authorization_required, Unset):
            pre_authorization_required = UNSET
        else:
            pre_authorization_required = self.pre_authorization_required

        network_status: None | str | Unset
        if isinstance(self.network_status, Unset):
            network_status = UNSET
        elif isinstance(self.network_status, CoverageNetworkStatusType1):
            network_status = self.network_status.value
        elif isinstance(self.network_status, CoverageNetworkStatusType2Type1):
            network_status = self.network_status.value
        elif isinstance(self.network_status, CoverageNetworkStatusType3Type1):
            network_status = self.network_status.value
        else:
            network_status = self.network_status

        eligibility: dict[str, Any] | None | Unset
        if isinstance(self.eligibility, Unset):
            eligibility = UNSET
        elif isinstance(self.eligibility, CoverageEligibility):
            eligibility = self.eligibility.to_dict()
        else:
            eligibility = self.eligibility

        origin_assistant_name: None | str | Unset
        if isinstance(self.origin_assistant_name, Unset):
            origin_assistant_name = UNSET
        else:
            origin_assistant_name = self.origin_assistant_name

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "coverage_active": coverage_active,
                "verification_status": verification_status,
                "source": source,
            }
        )
        if payer is not UNSET:
            field_dict["payer"] = payer
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
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
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
        if eligibility is not UNSET:
            field_dict["eligibility"] = eligibility
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_eligibility import CoverageEligibility  # noqa: PLC0415
        from ..models.coverage_payer import CoveragePayer  # noqa: PLC0415
        from ..models.coverage_subscriber import CoverageSubscriber  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        coverage_active = d.pop("coverage_active")

        verification_status = CoverageVerificationStatus(d.pop("verification_status"))

        source = CoverageSource(d.pop("source"))

        def _parse_payer(data: object) -> CoveragePayer | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payer_type_0 = CoveragePayer.from_dict(data)

                return payer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CoveragePayer | None | Unset, data)

        payer = _parse_payer(d.pop("payer", UNSET))

        def _parse_member_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_id = _parse_member_id(d.pop("member_id", UNSET))

        def _parse_group_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_number = _parse_group_number(d.pop("group_number", UNSET))

        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("group_name", UNSET))

        def _parse_plan_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_name = _parse_plan_name(d.pop("plan_name", UNSET))

        def _parse_coverage_type(
            data: object,
        ) -> CoverageCoverageTypeType1 | CoverageCoverageTypeType2Type1 | CoverageCoverageTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_type_type_1 = CoverageCoverageTypeType1(data)

                return coverage_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_type_type_2_type_1 = CoverageCoverageTypeType2Type1(data)

                return coverage_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_type_type_3_type_1 = CoverageCoverageTypeType3Type1(data)

                return coverage_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CoverageCoverageTypeType1
                | CoverageCoverageTypeType2Type1
                | CoverageCoverageTypeType3Type1
                | None
                | Unset,
                data,
            )

        coverage_type = _parse_coverage_type(d.pop("coverage_type", UNSET))

        def _parse_payment_responsibility(
            data: object,
        ) -> (
            CoveragePaymentResponsibilityType1
            | CoveragePaymentResponsibilityType2Type1
            | CoveragePaymentResponsibilityType3Type1
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
                payment_responsibility_type_1 = CoveragePaymentResponsibilityType1(data)

                return payment_responsibility_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_responsibility_type_2_type_1 = CoveragePaymentResponsibilityType2Type1(data)

                return payment_responsibility_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_responsibility_type_3_type_1 = CoveragePaymentResponsibilityType3Type1(data)

                return payment_responsibility_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CoveragePaymentResponsibilityType1
                | CoveragePaymentResponsibilityType2Type1
                | CoveragePaymentResponsibilityType3Type1
                | None
                | Unset,
                data,
            )

        payment_responsibility = _parse_payment_responsibility(d.pop("payment_responsibility", UNSET))

        def _parse_relationship_to_subscriber(
            data: object,
        ) -> (
            CoverageRelationshipToSubscriberType1
            | CoverageRelationshipToSubscriberType2Type1
            | CoverageRelationshipToSubscriberType3Type1
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
                relationship_to_subscriber_type_1 = CoverageRelationshipToSubscriberType1(data)

                return relationship_to_subscriber_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_to_subscriber_type_2_type_1 = CoverageRelationshipToSubscriberType2Type1(data)

                return relationship_to_subscriber_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relationship_to_subscriber_type_3_type_1 = CoverageRelationshipToSubscriberType3Type1(data)

                return relationship_to_subscriber_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CoverageRelationshipToSubscriberType1
                | CoverageRelationshipToSubscriberType2Type1
                | CoverageRelationshipToSubscriberType3Type1
                | None
                | Unset,
                data,
            )

        relationship_to_subscriber = _parse_relationship_to_subscriber(d.pop("relationship_to_subscriber", UNSET))

        def _parse_subscriber(data: object) -> CoverageSubscriber | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscriber_type_0 = CoverageSubscriber.from_dict(data)

                return subscriber_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CoverageSubscriber | None | Unset, data)

        subscriber = _parse_subscriber(d.pop("subscriber", UNSET))

        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("is_primary", UNSET))

        def _parse_effective_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = datetime.date.fromisoformat(data)

                return effective_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_date = _parse_effective_date(d.pop("effective_date", UNSET))

        def _parse_termination_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_date_type_0 = datetime.date.fromisoformat(data)

                return termination_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        termination_date = _parse_termination_date(d.pop("termination_date", UNSET))

        def _parse_copay_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        copay_amount = _parse_copay_amount(d.pop("copay_amount", UNSET))

        def _parse_coinsurance_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coinsurance_percent = _parse_coinsurance_percent(d.pop("coinsurance_percent", UNSET))

        def _parse_deductible_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        deductible_amount = _parse_deductible_amount(d.pop("deductible_amount", UNSET))

        def _parse_out_of_pocket_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        out_of_pocket_max = _parse_out_of_pocket_max(d.pop("out_of_pocket_max", UNSET))

        def _parse_pre_authorization_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pre_authorization_required = _parse_pre_authorization_required(d.pop("pre_authorization_required", UNSET))

        def _parse_network_status(
            data: object,
        ) -> (
            CoverageNetworkStatusType1
            | CoverageNetworkStatusType2Type1
            | CoverageNetworkStatusType3Type1
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
                network_status_type_1 = CoverageNetworkStatusType1(data)

                return network_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                network_status_type_2_type_1 = CoverageNetworkStatusType2Type1(data)

                return network_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                network_status_type_3_type_1 = CoverageNetworkStatusType3Type1(data)

                return network_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CoverageNetworkStatusType1
                | CoverageNetworkStatusType2Type1
                | CoverageNetworkStatusType3Type1
                | None
                | Unset,
                data,
            )

        network_status = _parse_network_status(d.pop("network_status", UNSET))

        def _parse_eligibility(data: object) -> CoverageEligibility | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                eligibility_type_0 = CoverageEligibility.from_dict(data)

                return eligibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CoverageEligibility | None | Unset, data)

        eligibility = _parse_eligibility(d.pop("eligibility", UNSET))

        def _parse_origin_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_assistant_name = _parse_origin_assistant_name(d.pop("origin_assistant_name", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

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

        coverage = cls(
            id=id,
            patient_id=patient_id,
            coverage_active=coverage_active,
            verification_status=verification_status,
            source=source,
            payer=payer,
            member_id=member_id,
            group_number=group_number,
            group_name=group_name,
            plan_name=plan_name,
            coverage_type=coverage_type,
            payment_responsibility=payment_responsibility,
            relationship_to_subscriber=relationship_to_subscriber,
            subscriber=subscriber,
            is_primary=is_primary,
            effective_date=effective_date,
            termination_date=termination_date,
            copay_amount=copay_amount,
            coinsurance_percent=coinsurance_percent,
            deductible_amount=deductible_amount,
            out_of_pocket_max=out_of_pocket_max,
            pre_authorization_required=pre_authorization_required,
            network_status=network_status,
            eligibility=eligibility,
            origin_assistant_name=origin_assistant_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        coverage.additional_properties = d
        return coverage

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
