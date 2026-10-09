from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.crm_contact_create_request_lifecycle_stage import CrmContactCreateRequestLifecycleStage
from ..models.crm_contact_create_request_priority import CrmContactCreateRequestPriority
from ..models.crm_contact_create_request_record_type import CrmContactCreateRequestRecordType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crm_contact_create_request_custom_fields import CrmContactCreateRequestCustomFields


T = TypeVar("T", bound="CrmContactCreateRequest")


@_attrs_define
class CrmContactCreateRequest:
    """
    Attributes:
        owner_staff_id (None | Unset | UUID):
        record_type (CrmContactCreateRequestRecordType | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        email (None | str | Unset):
        phone (None | str | Unset):
        company (None | str | Unset):
        lifecycle_stage (CrmContactCreateRequestLifecycleStage | Unset):
        pipeline_id (None | Unset | UUID):
        stage_id (None | Unset | UUID):
        source (str | Unset):
        referral_source_id (None | Unset | UUID):
        interest (None | str | Unset):
        desired_service_id (None | Unset | UUID):
        desired_provider_id (None | Unset | UUID):
        estimated_value_cents (int | None | Unset):
        priority (CrmContactCreateRequestPriority | Unset):
        marketing_opt_in (bool | Unset):
        sms_opt_in (bool | Unset):
        tags (list[str] | Unset):
        custom_fields (CrmContactCreateRequestCustomFields | Unset):
    """

    owner_staff_id: None | Unset | UUID = UNSET
    record_type: CrmContactCreateRequestRecordType | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    lifecycle_stage: CrmContactCreateRequestLifecycleStage | Unset = UNSET
    pipeline_id: None | Unset | UUID = UNSET
    stage_id: None | Unset | UUID = UNSET
    source: str | Unset = UNSET
    referral_source_id: None | Unset | UUID = UNSET
    interest: None | str | Unset = UNSET
    desired_service_id: None | Unset | UUID = UNSET
    desired_provider_id: None | Unset | UUID = UNSET
    estimated_value_cents: int | None | Unset = UNSET
    priority: CrmContactCreateRequestPriority | Unset = UNSET
    marketing_opt_in: bool | Unset = UNSET
    sms_opt_in: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    custom_fields: CrmContactCreateRequestCustomFields | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        owner_staff_id: None | str | Unset
        if isinstance(self.owner_staff_id, Unset):
            owner_staff_id = UNSET
        elif isinstance(self.owner_staff_id, UUID):
            owner_staff_id = str(self.owner_staff_id)
        else:
            owner_staff_id = self.owner_staff_id

        record_type: str | Unset = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.value

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

        lifecycle_stage: str | Unset = UNSET
        if not isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = self.lifecycle_stage.value

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

        source = self.source

        referral_source_id: None | str | Unset
        if isinstance(self.referral_source_id, Unset):
            referral_source_id = UNSET
        elif isinstance(self.referral_source_id, UUID):
            referral_source_id = str(self.referral_source_id)
        else:
            referral_source_id = self.referral_source_id

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

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        marketing_opt_in = self.marketing_opt_in

        sms_opt_in = self.sms_opt_in

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        custom_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        if source is not UNSET:
            field_dict["source"] = source
        if referral_source_id is not UNSET:
            field_dict["referral_source_id"] = referral_source_id
        if interest is not UNSET:
            field_dict["interest"] = interest
        if desired_service_id is not UNSET:
            field_dict["desired_service_id"] = desired_service_id
        if desired_provider_id is not UNSET:
            field_dict["desired_provider_id"] = desired_provider_id
        if estimated_value_cents is not UNSET:
            field_dict["estimated_value_cents"] = estimated_value_cents
        if priority is not UNSET:
            field_dict["priority"] = priority
        if marketing_opt_in is not UNSET:
            field_dict["marketing_opt_in"] = marketing_opt_in
        if sms_opt_in is not UNSET:
            field_dict["sms_opt_in"] = sms_opt_in
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crm_contact_create_request_custom_fields import (
            CrmContactCreateRequestCustomFields,  # noqa: PLC0415
        )

        d = dict(src_dict)

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

        _record_type = d.pop("record_type", UNSET)
        record_type: CrmContactCreateRequestRecordType | Unset
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = CrmContactCreateRequestRecordType(_record_type)

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

        _lifecycle_stage = d.pop("lifecycle_stage", UNSET)
        lifecycle_stage: CrmContactCreateRequestLifecycleStage | Unset
        if isinstance(_lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        else:
            lifecycle_stage = CrmContactCreateRequestLifecycleStage(_lifecycle_stage)

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

        source = d.pop("source", UNSET)

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

        _priority = d.pop("priority", UNSET)
        priority: CrmContactCreateRequestPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CrmContactCreateRequestPriority(_priority)

        marketing_opt_in = d.pop("marketing_opt_in", UNSET)

        sms_opt_in = d.pop("sms_opt_in", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: CrmContactCreateRequestCustomFields | Unset
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CrmContactCreateRequestCustomFields.from_dict(_custom_fields)

        crm_contact_create_request = cls(
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
            source=source,
            referral_source_id=referral_source_id,
            interest=interest,
            desired_service_id=desired_service_id,
            desired_provider_id=desired_provider_id,
            estimated_value_cents=estimated_value_cents,
            priority=priority,
            marketing_opt_in=marketing_opt_in,
            sms_opt_in=sms_opt_in,
            tags=tags,
            custom_fields=custom_fields,
        )

        return crm_contact_create_request
