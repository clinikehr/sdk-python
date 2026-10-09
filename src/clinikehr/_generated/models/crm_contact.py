from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crm_contact_lifecycle_stage_type_1 import CrmContactLifecycleStageType1
from ..models.crm_contact_lifecycle_stage_type_2_type_1 import CrmContactLifecycleStageType2Type1
from ..models.crm_contact_lifecycle_stage_type_3_type_1 import CrmContactLifecycleStageType3Type1
from ..models.crm_contact_priority_type_1 import CrmContactPriorityType1
from ..models.crm_contact_priority_type_2_type_1 import CrmContactPriorityType2Type1
from ..models.crm_contact_priority_type_3_type_1 import CrmContactPriorityType3Type1
from ..models.crm_contact_record_type_type_1 import CrmContactRecordTypeType1
from ..models.crm_contact_record_type_type_2_type_1 import CrmContactRecordTypeType2Type1
from ..models.crm_contact_record_type_type_3_type_1 import CrmContactRecordTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crm_contact_custom_fields import CrmContactCustomFields


T = TypeVar("T", bound="CrmContact")


@_attrs_define
class CrmContact:
    """Withheld, by NAME: clinic_id (implicit in the path), unsubscribe_token, migrated_from_patient_id, custom_color,
    created_by, confirmed_opt_in_at, marketing_authorization_id.

        Attributes:
            id (UUID):
            owner_staff_id (None | Unset | UUID):
            record_type (CrmContactRecordTypeType1 | CrmContactRecordTypeType2Type1 | CrmContactRecordTypeType3Type1 | None
                | Unset):
            first_name (None | str | Unset):
            last_name (None | str | Unset):
            email (None | str | Unset):
            phone (None | str | Unset):
            company (None | str | Unset):
            lifecycle_stage (CrmContactLifecycleStageType1 | CrmContactLifecycleStageType2Type1 |
                CrmContactLifecycleStageType3Type1 | None | Unset):
            pipeline_id (None | Unset | UUID):
            stage_id (None | Unset | UUID):
            status (None | str | Unset):
            source (None | str | Unset):
            referral_source_id (None | Unset | UUID):
            referred_by_contact_id (None | Unset | UUID):
            interest (None | str | Unset):
            desired_service_id (None | Unset | UUID):
            desired_provider_id (None | Unset | UUID):
            estimated_value_cents (int | None | Unset):
            currency (None | str | Unset):
            priority (CrmContactPriorityType1 | CrmContactPriorityType2Type1 | CrmContactPriorityType3Type1 | None | Unset):
            score (int | None | Unset):
            marketing_opt_in (bool | None | Unset):
            sms_opt_in (bool | None | Unset):
            consent_at (datetime.datetime | None | Unset):
            consent_source (None | str | Unset):
            do_not_contact (bool | None | Unset):
            unsubscribed_at (datetime.datetime | None | Unset):
            tags (list[str] | Unset):
            custom_fields (CrmContactCustomFields | Unset):
            converted_patient_id (None | Unset | UUID):
            converted_at (datetime.datetime | None | Unset):
            lost_reason (None | str | Unset):
            last_activity_at (datetime.datetime | None | Unset):
            next_task_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    owner_staff_id: None | Unset | UUID = UNSET
    record_type: (
        CrmContactRecordTypeType1 | CrmContactRecordTypeType2Type1 | CrmContactRecordTypeType3Type1 | None | Unset
    ) = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    lifecycle_stage: (
        CrmContactLifecycleStageType1
        | CrmContactLifecycleStageType2Type1
        | CrmContactLifecycleStageType3Type1
        | None
        | Unset
    ) = UNSET
    pipeline_id: None | Unset | UUID = UNSET
    stage_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    referral_source_id: None | Unset | UUID = UNSET
    referred_by_contact_id: None | Unset | UUID = UNSET
    interest: None | str | Unset = UNSET
    desired_service_id: None | Unset | UUID = UNSET
    desired_provider_id: None | Unset | UUID = UNSET
    estimated_value_cents: int | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    priority: CrmContactPriorityType1 | CrmContactPriorityType2Type1 | CrmContactPriorityType3Type1 | None | Unset = (
        UNSET
    )
    score: int | None | Unset = UNSET
    marketing_opt_in: bool | None | Unset = UNSET
    sms_opt_in: bool | None | Unset = UNSET
    consent_at: datetime.datetime | None | Unset = UNSET
    consent_source: None | str | Unset = UNSET
    do_not_contact: bool | None | Unset = UNSET
    unsubscribed_at: datetime.datetime | None | Unset = UNSET
    tags: list[str] | Unset = UNSET
    custom_fields: CrmContactCustomFields | Unset = UNSET
    converted_patient_id: None | Unset | UUID = UNSET
    converted_at: datetime.datetime | None | Unset = UNSET
    lost_reason: None | str | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    next_task_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        owner_staff_id: None | str | Unset
        if isinstance(self.owner_staff_id, Unset):
            owner_staff_id = UNSET
        elif isinstance(self.owner_staff_id, UUID):
            owner_staff_id = str(self.owner_staff_id)
        else:
            owner_staff_id = self.owner_staff_id

        record_type: None | str | Unset
        if isinstance(self.record_type, Unset):
            record_type = UNSET
        elif isinstance(self.record_type, CrmContactRecordTypeType1):
            record_type = self.record_type.value
        elif isinstance(self.record_type, CrmContactRecordTypeType2Type1):
            record_type = self.record_type.value
        elif isinstance(self.record_type, CrmContactRecordTypeType3Type1):
            record_type = self.record_type.value
        else:
            record_type = self.record_type

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        lifecycle_stage: None | str | Unset
        if isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        elif isinstance(self.lifecycle_stage, CrmContactLifecycleStageType1):
            lifecycle_stage = self.lifecycle_stage.value
        elif isinstance(self.lifecycle_stage, CrmContactLifecycleStageType2Type1):
            lifecycle_stage = self.lifecycle_stage.value
        elif isinstance(self.lifecycle_stage, CrmContactLifecycleStageType3Type1):
            lifecycle_stage = self.lifecycle_stage.value
        else:
            lifecycle_stage = self.lifecycle_stage

        pipeline_id: None | str | Unset
        if isinstance(self.pipeline_id, Unset):
            pipeline_id = UNSET
        elif isinstance(self.pipeline_id, UUID):
            pipeline_id = str(self.pipeline_id)
        else:
            pipeline_id = self.pipeline_id

        stage_id: None | str | Unset
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        elif isinstance(self.stage_id, UUID):
            stage_id = str(self.stage_id)
        else:
            stage_id = self.stage_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        referral_source_id: None | str | Unset
        if isinstance(self.referral_source_id, Unset):
            referral_source_id = UNSET
        elif isinstance(self.referral_source_id, UUID):
            referral_source_id = str(self.referral_source_id)
        else:
            referral_source_id = self.referral_source_id

        referred_by_contact_id: None | str | Unset
        if isinstance(self.referred_by_contact_id, Unset):
            referred_by_contact_id = UNSET
        elif isinstance(self.referred_by_contact_id, UUID):
            referred_by_contact_id = str(self.referred_by_contact_id)
        else:
            referred_by_contact_id = self.referred_by_contact_id

        interest: None | str | Unset
        if isinstance(self.interest, Unset):
            interest = UNSET
        else:
            interest = self.interest

        desired_service_id: None | str | Unset
        if isinstance(self.desired_service_id, Unset):
            desired_service_id = UNSET
        elif isinstance(self.desired_service_id, UUID):
            desired_service_id = str(self.desired_service_id)
        else:
            desired_service_id = self.desired_service_id

        desired_provider_id: None | str | Unset
        if isinstance(self.desired_provider_id, Unset):
            desired_provider_id = UNSET
        elif isinstance(self.desired_provider_id, UUID):
            desired_provider_id = str(self.desired_provider_id)
        else:
            desired_provider_id = self.desired_provider_id

        estimated_value_cents: int | None | Unset
        if isinstance(self.estimated_value_cents, Unset):
            estimated_value_cents = UNSET
        else:
            estimated_value_cents = self.estimated_value_cents

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, CrmContactPriorityType1):
            priority = self.priority.value
        elif isinstance(self.priority, CrmContactPriorityType2Type1):
            priority = self.priority.value
        elif isinstance(self.priority, CrmContactPriorityType3Type1):
            priority = self.priority.value
        else:
            priority = self.priority

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        marketing_opt_in: bool | None | Unset
        if isinstance(self.marketing_opt_in, Unset):
            marketing_opt_in = UNSET
        else:
            marketing_opt_in = self.marketing_opt_in

        sms_opt_in: bool | None | Unset
        if isinstance(self.sms_opt_in, Unset):
            sms_opt_in = UNSET
        else:
            sms_opt_in = self.sms_opt_in

        consent_at: None | str | Unset
        if isinstance(self.consent_at, Unset):
            consent_at = UNSET
        elif isinstance(self.consent_at, datetime.datetime):
            consent_at = self.consent_at.isoformat()
        else:
            consent_at = self.consent_at

        consent_source: None | str | Unset
        if isinstance(self.consent_source, Unset):
            consent_source = UNSET
        else:
            consent_source = self.consent_source

        do_not_contact: bool | None | Unset
        if isinstance(self.do_not_contact, Unset):
            do_not_contact = UNSET
        else:
            do_not_contact = self.do_not_contact

        unsubscribed_at: None | str | Unset
        if isinstance(self.unsubscribed_at, Unset):
            unsubscribed_at = UNSET
        elif isinstance(self.unsubscribed_at, datetime.datetime):
            unsubscribed_at = self.unsubscribed_at.isoformat()
        else:
            unsubscribed_at = self.unsubscribed_at

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        custom_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        converted_patient_id: None | str | Unset
        if isinstance(self.converted_patient_id, Unset):
            converted_patient_id = UNSET
        elif isinstance(self.converted_patient_id, UUID):
            converted_patient_id = str(self.converted_patient_id)
        else:
            converted_patient_id = self.converted_patient_id

        converted_at: None | str | Unset
        if isinstance(self.converted_at, Unset):
            converted_at = UNSET
        elif isinstance(self.converted_at, datetime.datetime):
            converted_at = self.converted_at.isoformat()
        else:
            converted_at = self.converted_at

        lost_reason: None | str | Unset
        if isinstance(self.lost_reason, Unset):
            lost_reason = UNSET
        else:
            lost_reason = self.lost_reason

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        next_task_at: None | str | Unset
        if isinstance(self.next_task_at, Unset):
            next_task_at = UNSET
        elif isinstance(self.next_task_at, datetime.datetime):
            next_task_at = self.next_task_at.isoformat()
        else:
            next_task_at = self.next_task_at

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
            }
        )
        if owner_staff_id is not UNSET:
            field_dict["owner_staff_id"] = owner_staff_id
        if record_type is not UNSET:
            field_dict["record_type"] = record_type
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if company is not UNSET:
            field_dict["company"] = company
        if lifecycle_stage is not UNSET:
            field_dict["lifecycle_stage"] = lifecycle_stage
        if pipeline_id is not UNSET:
            field_dict["pipeline_id"] = pipeline_id
        if stage_id is not UNSET:
            field_dict["stage_id"] = stage_id
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if referral_source_id is not UNSET:
            field_dict["referral_source_id"] = referral_source_id
        if referred_by_contact_id is not UNSET:
            field_dict["referred_by_contact_id"] = referred_by_contact_id
        if interest is not UNSET:
            field_dict["interest"] = interest
        if desired_service_id is not UNSET:
            field_dict["desired_service_id"] = desired_service_id
        if desired_provider_id is not UNSET:
            field_dict["desired_provider_id"] = desired_provider_id
        if estimated_value_cents is not UNSET:
            field_dict["estimated_value_cents"] = estimated_value_cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if priority is not UNSET:
            field_dict["priority"] = priority
        if score is not UNSET:
            field_dict["score"] = score
        if marketing_opt_in is not UNSET:
            field_dict["marketing_opt_in"] = marketing_opt_in
        if sms_opt_in is not UNSET:
            field_dict["sms_opt_in"] = sms_opt_in
        if consent_at is not UNSET:
            field_dict["consent_at"] = consent_at
        if consent_source is not UNSET:
            field_dict["consent_source"] = consent_source
        if do_not_contact is not UNSET:
            field_dict["do_not_contact"] = do_not_contact
        if unsubscribed_at is not UNSET:
            field_dict["unsubscribed_at"] = unsubscribed_at
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if converted_patient_id is not UNSET:
            field_dict["converted_patient_id"] = converted_patient_id
        if converted_at is not UNSET:
            field_dict["converted_at"] = converted_at
        if lost_reason is not UNSET:
            field_dict["lost_reason"] = lost_reason
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if next_task_at is not UNSET:
            field_dict["next_task_at"] = next_task_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crm_contact_custom_fields import CrmContactCustomFields  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_owner_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_staff_id_type_0 = UUID(data)

                return owner_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_staff_id = _parse_owner_staff_id(d.pop("owner_staff_id", UNSET))

        def _parse_record_type(
            data: object,
        ) -> CrmContactRecordTypeType1 | CrmContactRecordTypeType2Type1 | CrmContactRecordTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_type_type_1 = CrmContactRecordTypeType1(data)

                return record_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_type_type_2_type_1 = CrmContactRecordTypeType2Type1(data)

                return record_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_type_type_3_type_1 = CrmContactRecordTypeType3Type1(data)

                return record_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CrmContactRecordTypeType1
                | CrmContactRecordTypeType2Type1
                | CrmContactRecordTypeType3Type1
                | None
                | Unset,
                data,
            )

        record_type = _parse_record_type(d.pop("record_type", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_lifecycle_stage(
            data: object,
        ) -> (
            CrmContactLifecycleStageType1
            | CrmContactLifecycleStageType2Type1
            | CrmContactLifecycleStageType3Type1
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
                lifecycle_stage_type_1 = CrmContactLifecycleStageType1(data)

                return lifecycle_stage_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_stage_type_2_type_1 = CrmContactLifecycleStageType2Type1(data)

                return lifecycle_stage_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_stage_type_3_type_1 = CrmContactLifecycleStageType3Type1(data)

                return lifecycle_stage_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CrmContactLifecycleStageType1
                | CrmContactLifecycleStageType2Type1
                | CrmContactLifecycleStageType3Type1
                | None
                | Unset,
                data,
            )

        lifecycle_stage = _parse_lifecycle_stage(d.pop("lifecycle_stage", UNSET))

        def _parse_pipeline_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipeline_id_type_0 = UUID(data)

                return pipeline_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pipeline_id = _parse_pipeline_id(d.pop("pipeline_id", UNSET))

        def _parse_stage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_id_type_0 = UUID(data)

                return stage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        stage_id = _parse_stage_id(d.pop("stage_id", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_referral_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                referral_source_id_type_0 = UUID(data)

                return referral_source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        referral_source_id = _parse_referral_source_id(d.pop("referral_source_id", UNSET))

        def _parse_referred_by_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                referred_by_contact_id_type_0 = UUID(data)

                return referred_by_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        referred_by_contact_id = _parse_referred_by_contact_id(d.pop("referred_by_contact_id", UNSET))

        def _parse_interest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interest = _parse_interest(d.pop("interest", UNSET))

        def _parse_desired_service_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_service_id_type_0 = UUID(data)

                return desired_service_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        desired_service_id = _parse_desired_service_id(d.pop("desired_service_id", UNSET))

        def _parse_desired_provider_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                desired_provider_id_type_0 = UUID(data)

                return desired_provider_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        desired_provider_id = _parse_desired_provider_id(d.pop("desired_provider_id", UNSET))

        def _parse_estimated_value_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_value_cents = _parse_estimated_value_cents(d.pop("estimated_value_cents", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_priority(
            data: object,
        ) -> CrmContactPriorityType1 | CrmContactPriorityType2Type1 | CrmContactPriorityType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_1 = CrmContactPriorityType1(data)

                return priority_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_2_type_1 = CrmContactPriorityType2Type1(data)

                return priority_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_3_type_1 = CrmContactPriorityType3Type1(data)

                return priority_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CrmContactPriorityType1 | CrmContactPriorityType2Type1 | CrmContactPriorityType3Type1 | None | Unset,
                data,
            )

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_marketing_opt_in(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        marketing_opt_in = _parse_marketing_opt_in(d.pop("marketing_opt_in", UNSET))

        def _parse_sms_opt_in(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sms_opt_in = _parse_sms_opt_in(d.pop("sms_opt_in", UNSET))

        def _parse_consent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                consent_at_type_0 = datetime.datetime.fromisoformat(data)

                return consent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        consent_at = _parse_consent_at(d.pop("consent_at", UNSET))

        def _parse_consent_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consent_source = _parse_consent_source(d.pop("consent_source", UNSET))

        def _parse_do_not_contact(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_contact = _parse_do_not_contact(d.pop("do_not_contact", UNSET))

        def _parse_unsubscribed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unsubscribed_at_type_0 = datetime.datetime.fromisoformat(data)

                return unsubscribed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        unsubscribed_at = _parse_unsubscribed_at(d.pop("unsubscribed_at", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: CrmContactCustomFields | Unset
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CrmContactCustomFields.from_dict(_custom_fields)

        def _parse_converted_patient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                converted_patient_id_type_0 = UUID(data)

                return converted_patient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        converted_patient_id = _parse_converted_patient_id(d.pop("converted_patient_id", UNSET))

        def _parse_converted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                converted_at_type_0 = datetime.datetime.fromisoformat(data)

                return converted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        converted_at = _parse_converted_at(d.pop("converted_at", UNSET))

        def _parse_lost_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lost_reason = _parse_lost_reason(d.pop("lost_reason", UNSET))

        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("last_activity_at", UNSET))

        def _parse_next_task_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_task_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_task_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_task_at = _parse_next_task_at(d.pop("next_task_at", UNSET))

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

        crm_contact = cls(
            id=id,
            owner_staff_id=owner_staff_id,
            record_type=record_type,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            company=company,
            lifecycle_stage=lifecycle_stage,
            pipeline_id=pipeline_id,
            stage_id=stage_id,
            status=status,
            source=source,
            referral_source_id=referral_source_id,
            referred_by_contact_id=referred_by_contact_id,
            interest=interest,
            desired_service_id=desired_service_id,
            desired_provider_id=desired_provider_id,
            estimated_value_cents=estimated_value_cents,
            currency=currency,
            priority=priority,
            score=score,
            marketing_opt_in=marketing_opt_in,
            sms_opt_in=sms_opt_in,
            consent_at=consent_at,
            consent_source=consent_source,
            do_not_contact=do_not_contact,
            unsubscribed_at=unsubscribed_at,
            tags=tags,
            custom_fields=custom_fields,
            converted_patient_id=converted_patient_id,
            converted_at=converted_at,
            lost_reason=lost_reason,
            last_activity_at=last_activity_at,
            next_task_at=next_task_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        crm_contact.additional_properties = d
        return crm_contact

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
