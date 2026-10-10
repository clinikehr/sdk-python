from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insurance_enrollee_status import InsuranceEnrolleeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_enrollee_plan import InsuranceEnrolleePlan


T = TypeVar("T", bound="InsuranceEnrollee")


@_attrs_define
class InsuranceEnrollee:
    """A person an insurer covers at this clinic, as the clinic holds them. `insurance_no` is the number an enrollee is
    verified by. Only enrollees of an insurer the clinic linked to your organization are returned. Verification metadata
    and the clinic's internal notes are never exposed.

        Attributes:
            id (UUID):
            insurance_company_id (UUID):
            insurance_no (str):
            status (InsuranceEnrolleeStatus): Curacel enrollee status codes: AA active, IA inactive, SX suspended, XX
                cancelled, PP pending, WP waiting period.
            patient_id (None | Unset | UUID): The clinic's own patient id; null for a floating enrollee not yet matched to a
                patient.
            alternate_insurance_no (None | str | Unset):
            firstname (None | str | Unset):
            middlename (None | str | Unset):
            lastname (None | str | Unset):
            sex (None | str | Unset):
            birthdate (datetime.date | None | Unset):
            status_effective_from (datetime.date | None | Unset):
            valid_until (datetime.date | None | Unset):
            plan (InsuranceEnrolleePlan | None | Unset):
            parent_enrollee_id (None | Unset | UUID):
            parent_relationship (None | str | Unset):
            staff_number (None | str | Unset):
            primary_provider_code (None | str | Unset):
            is_floating (bool | None | Unset):
            verified_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    insurance_company_id: UUID
    insurance_no: str
    status: InsuranceEnrolleeStatus
    patient_id: None | Unset | UUID = UNSET
    alternate_insurance_no: None | str | Unset = UNSET
    firstname: None | str | Unset = UNSET
    middlename: None | str | Unset = UNSET
    lastname: None | str | Unset = UNSET
    sex: None | str | Unset = UNSET
    birthdate: datetime.date | None | Unset = UNSET
    status_effective_from: datetime.date | None | Unset = UNSET
    valid_until: datetime.date | None | Unset = UNSET
    plan: InsuranceEnrolleePlan | None | Unset = UNSET
    parent_enrollee_id: None | Unset | UUID = UNSET
    parent_relationship: None | str | Unset = UNSET
    staff_number: None | str | Unset = UNSET
    primary_provider_code: None | str | Unset = UNSET
    is_floating: bool | None | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.insurance_enrollee_plan import InsuranceEnrolleePlan  # noqa: PLC0415

        id = str(self.id)

        insurance_company_id = str(self.insurance_company_id)

        insurance_no = self.insurance_no

        status = self.status.value

        patient_id: None | str | Unset
        if isinstance(self.patient_id, Unset):
            patient_id = UNSET
        elif isinstance(self.patient_id, UUID):
            patient_id = str(self.patient_id)
        else:
            patient_id = self.patient_id

        alternate_insurance_no: None | str | Unset
        if isinstance(self.alternate_insurance_no, Unset):
            alternate_insurance_no = UNSET
        else:
            alternate_insurance_no = self.alternate_insurance_no

        firstname: None | str | Unset
        if isinstance(self.firstname, Unset):
            firstname = UNSET
        else:
            firstname = self.firstname

        middlename: None | str | Unset
        if isinstance(self.middlename, Unset):
            middlename = UNSET
        else:
            middlename = self.middlename

        lastname: None | str | Unset
        if isinstance(self.lastname, Unset):
            lastname = UNSET
        else:
            lastname = self.lastname

        sex: None | str | Unset
        if isinstance(self.sex, Unset):
            sex = UNSET
        else:
            sex = self.sex

        birthdate: None | str | Unset
        if isinstance(self.birthdate, Unset):
            birthdate = UNSET
        elif isinstance(self.birthdate, datetime.date):
            birthdate = self.birthdate.isoformat()
        else:
            birthdate = self.birthdate

        status_effective_from: None | str | Unset
        if isinstance(self.status_effective_from, Unset):
            status_effective_from = UNSET
        elif isinstance(self.status_effective_from, datetime.date):
            status_effective_from = self.status_effective_from.isoformat()
        else:
            status_effective_from = self.status_effective_from

        valid_until: None | str | Unset
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.date):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        plan: dict[str, Any] | None | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        elif isinstance(self.plan, InsuranceEnrolleePlan):
            plan = self.plan.to_dict()
        else:
            plan = self.plan

        parent_enrollee_id: None | str | Unset
        if isinstance(self.parent_enrollee_id, Unset):
            parent_enrollee_id = UNSET
        elif isinstance(self.parent_enrollee_id, UUID):
            parent_enrollee_id = str(self.parent_enrollee_id)
        else:
            parent_enrollee_id = self.parent_enrollee_id

        parent_relationship: None | str | Unset
        if isinstance(self.parent_relationship, Unset):
            parent_relationship = UNSET
        else:
            parent_relationship = self.parent_relationship

        staff_number: None | str | Unset
        if isinstance(self.staff_number, Unset):
            staff_number = UNSET
        else:
            staff_number = self.staff_number

        primary_provider_code: None | str | Unset
        if isinstance(self.primary_provider_code, Unset):
            primary_provider_code = UNSET
        else:
            primary_provider_code = self.primary_provider_code

        is_floating: bool | None | Unset
        if isinstance(self.is_floating, Unset):
            is_floating = UNSET
        else:
            is_floating = self.is_floating

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

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
                "insurance_company_id": insurance_company_id,
                "insurance_no": insurance_no,
                "status": status,
            }
        )
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if alternate_insurance_no is not UNSET:
            field_dict["alternate_insurance_no"] = alternate_insurance_no
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if middlename is not UNSET:
            field_dict["middlename"] = middlename
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if sex is not UNSET:
            field_dict["sex"] = sex
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if status_effective_from is not UNSET:
            field_dict["status_effective_from"] = status_effective_from
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until
        if plan is not UNSET:
            field_dict["plan"] = plan
        if parent_enrollee_id is not UNSET:
            field_dict["parent_enrollee_id"] = parent_enrollee_id
        if parent_relationship is not UNSET:
            field_dict["parent_relationship"] = parent_relationship
        if staff_number is not UNSET:
            field_dict["staff_number"] = staff_number
        if primary_provider_code is not UNSET:
            field_dict["primary_provider_code"] = primary_provider_code
        if is_floating is not UNSET:
            field_dict["is_floating"] = is_floating
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_enrollee_plan import InsuranceEnrolleePlan  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        insurance_company_id = UUID(d.pop("insurance_company_id"))

        insurance_no = d.pop("insurance_no")

        status = InsuranceEnrolleeStatus(d.pop("status"))

        def _parse_patient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patient_id_type_0 = UUID(data)

                return patient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        patient_id = _parse_patient_id(d.pop("patient_id", UNSET))

        def _parse_alternate_insurance_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alternate_insurance_no = _parse_alternate_insurance_no(d.pop("alternate_insurance_no", UNSET))

        def _parse_firstname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        firstname = _parse_firstname(d.pop("firstname", UNSET))

        def _parse_middlename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middlename = _parse_middlename(d.pop("middlename", UNSET))

        def _parse_lastname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lastname = _parse_lastname(d.pop("lastname", UNSET))

        def _parse_sex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sex = _parse_sex(d.pop("sex", UNSET))

        def _parse_birthdate(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birthdate_type_0 = datetime.date.fromisoformat(data)

                return birthdate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        birthdate = _parse_birthdate(d.pop("birthdate", UNSET))

        def _parse_status_effective_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_effective_from_type_0 = datetime.date.fromisoformat(data)

                return status_effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        status_effective_from = _parse_status_effective_from(d.pop("status_effective_from", UNSET))

        def _parse_valid_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = datetime.date.fromisoformat(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        valid_until = _parse_valid_until(d.pop("valid_until", UNSET))

        def _parse_plan(data: object) -> InsuranceEnrolleePlan | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plan_type_0 = InsuranceEnrolleePlan.from_dict(data)

                return plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InsuranceEnrolleePlan | None | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        def _parse_parent_enrollee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_enrollee_id_type_0 = UUID(data)

                return parent_enrollee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_enrollee_id = _parse_parent_enrollee_id(d.pop("parent_enrollee_id", UNSET))

        def _parse_parent_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_relationship = _parse_parent_relationship(d.pop("parent_relationship", UNSET))

        def _parse_staff_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staff_number = _parse_staff_number(d.pop("staff_number", UNSET))

        def _parse_primary_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_provider_code = _parse_primary_provider_code(d.pop("primary_provider_code", UNSET))

        def _parse_is_floating(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_floating = _parse_is_floating(d.pop("is_floating", UNSET))

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

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

        insurance_enrollee = cls(
            id=id,
            insurance_company_id=insurance_company_id,
            insurance_no=insurance_no,
            status=status,
            patient_id=patient_id,
            alternate_insurance_no=alternate_insurance_no,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            sex=sex,
            birthdate=birthdate,
            status_effective_from=status_effective_from,
            valid_until=valid_until,
            plan=plan,
            parent_enrollee_id=parent_enrollee_id,
            parent_relationship=parent_relationship,
            staff_number=staff_number,
            primary_provider_code=primary_provider_code,
            is_floating=is_floating,
            verified_at=verified_at,
            updated_at=updated_at,
        )

        insurance_enrollee.additional_properties = d
        return insurance_enrollee

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
