from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_create_request_blood_type import PatientCreateRequestBloodType
from ..models.patient_create_request_client_type import PatientCreateRequestClientType
from ..models.patient_create_request_gender import PatientCreateRequestGender
from ..models.patient_create_request_genotype import PatientCreateRequestGenotype
from ..models.patient_create_request_marital_status import PatientCreateRequestMaritalStatus
from ..models.patient_create_request_status import PatientCreateRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employment import Employment
    from ..models.next_of_kin import NextOfKin
    from ..models.patient_billing import PatientBilling
    from ..models.patient_email import PatientEmail
    from ..models.patient_guardian import PatientGuardian
    from ..models.patient_phone import PatientPhone


T = TypeVar("T", bound="PatientCreateRequest")


@_attrs_define
class PatientCreateRequest:
    """Unknown top-level fields, and every named read-only field (mrn, portal_access_enabled, admission_status,
    client_status, insurance, pharmacies, care_providers, couple, profile_image, notification_settings — the last
    refused with the distinct code notification_settings_not_writable), are refused BY NAME, never silently dropped —
    enforced by the database, not this schema. `allergies`, `current_medications` and `chronic_conditions` are not
    accepted here either: they are the clinic's reviewed clinical record, so they are refused by name. Send allergies to
    `createAllergy` and conditions to `createCondition`; each is held for a clinician to confirm. They are still
    returned when you read a patient.

        Attributes:
            first_name (str):
            last_name (str):
            client_type (PatientCreateRequestClientType):
            middle_name (str | Unset):
            preferred_name (str | Unset):
            title (str | Unset):
            suffix (str | Unset):
            date_of_birth (datetime.date | Unset):
            gender (PatientCreateRequestGender | Unset):
            marital_status (PatientCreateRequestMaritalStatus | Unset):
            email (str | Unset):
            phone (str | Unset):
            secondary_phone (str | Unset):
            country (str | Unset):
            nationality (str | Unset):
            occupation (str | Unset):
            residential_address (str | Unset):
            work_address (str | Unset):
            city (str | Unset):
            state (str | Unset):
            zip_ (str | Unset):
            next_of_kin (NextOfKin | Unset):
            national_id (str | Unset):
            preferred_language (str | Unset):
            referred_by (str | Unset):
            referral_source_id (UUID | Unset):
            employment (Employment | Unset):
            is_dependent (bool | Unset):
            is_waitlist (bool | Unset):
            sponsor_id (UUID | Unset):
            billing (PatientBilling | Unset):
            medical_history (str | Unset):
            blood_type (PatientCreateRequestBloodType | Unset):
            genotype (PatientCreateRequestGenotype | Unset):
            family_history (str | Unset):
            smoking_status (str | Unset):
            alcohol_use (str | Unset):
            recreational_drug_use (str | Unset):
            physical_activity (str | Unset):
            living_arrangement (str | Unset):
            status (PatientCreateRequestStatus | Unset):
            is_vip (bool | Unset):
            primary_location_id (UUID | Unset):
            emails (list[PatientEmail] | Unset):
            phones (list[PatientPhone] | Unset):
            guardians (list[PatientGuardian] | Unset):
            run_automations (bool | Unset): Default false suppresses the patient.created Agent Studio dispatch. Default:
                False.
    """

    first_name: str
    last_name: str
    client_type: PatientCreateRequestClientType
    middle_name: str | Unset = UNSET
    preferred_name: str | Unset = UNSET
    title: str | Unset = UNSET
    suffix: str | Unset = UNSET
    date_of_birth: datetime.date | Unset = UNSET
    gender: PatientCreateRequestGender | Unset = UNSET
    marital_status: PatientCreateRequestMaritalStatus | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    secondary_phone: str | Unset = UNSET
    country: str | Unset = UNSET
    nationality: str | Unset = UNSET
    occupation: str | Unset = UNSET
    residential_address: str | Unset = UNSET
    work_address: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    zip_: str | Unset = UNSET
    next_of_kin: NextOfKin | Unset = UNSET
    national_id: str | Unset = UNSET
    preferred_language: str | Unset = UNSET
    referred_by: str | Unset = UNSET
    referral_source_id: UUID | Unset = UNSET
    employment: Employment | Unset = UNSET
    is_dependent: bool | Unset = UNSET
    is_waitlist: bool | Unset = UNSET
    sponsor_id: UUID | Unset = UNSET
    billing: PatientBilling | Unset = UNSET
    medical_history: str | Unset = UNSET
    blood_type: PatientCreateRequestBloodType | Unset = UNSET
    genotype: PatientCreateRequestGenotype | Unset = UNSET
    family_history: str | Unset = UNSET
    smoking_status: str | Unset = UNSET
    alcohol_use: str | Unset = UNSET
    recreational_drug_use: str | Unset = UNSET
    physical_activity: str | Unset = UNSET
    living_arrangement: str | Unset = UNSET
    status: PatientCreateRequestStatus | Unset = UNSET
    is_vip: bool | Unset = UNSET
    primary_location_id: UUID | Unset = UNSET
    emails: list[PatientEmail] | Unset = UNSET
    phones: list[PatientPhone] | Unset = UNSET
    guardians: list[PatientGuardian] | Unset = UNSET
    run_automations: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        client_type = self.client_type.value

        middle_name = self.middle_name

        preferred_name = self.preferred_name

        title = self.title

        suffix = self.suffix

        date_of_birth: str | Unset = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        marital_status: str | Unset = UNSET
        if not isinstance(self.marital_status, Unset):
            marital_status = self.marital_status.value

        email = self.email

        phone = self.phone

        secondary_phone = self.secondary_phone

        country = self.country

        nationality = self.nationality

        occupation = self.occupation

        residential_address = self.residential_address

        work_address = self.work_address

        city = self.city

        state = self.state

        zip_ = self.zip_

        next_of_kin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_of_kin, Unset):
            next_of_kin = self.next_of_kin.to_dict()

        national_id = self.national_id

        preferred_language = self.preferred_language

        referred_by = self.referred_by

        referral_source_id: str | Unset = UNSET
        if not isinstance(self.referral_source_id, Unset):
            referral_source_id = str(self.referral_source_id)

        employment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employment, Unset):
            employment = self.employment.to_dict()

        is_dependent = self.is_dependent

        is_waitlist = self.is_waitlist

        sponsor_id: str | Unset = UNSET
        if not isinstance(self.sponsor_id, Unset):
            sponsor_id = str(self.sponsor_id)

        billing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing, Unset):
            billing = self.billing.to_dict()

        medical_history = self.medical_history

        blood_type: str | Unset = UNSET
        if not isinstance(self.blood_type, Unset):
            blood_type = self.blood_type.value

        genotype: str | Unset = UNSET
        if not isinstance(self.genotype, Unset):
            genotype = self.genotype.value

        family_history = self.family_history

        smoking_status = self.smoking_status

        alcohol_use = self.alcohol_use

        recreational_drug_use = self.recreational_drug_use

        physical_activity = self.physical_activity

        living_arrangement = self.living_arrangement

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_vip = self.is_vip

        primary_location_id: str | Unset = UNSET
        if not isinstance(self.primary_location_id, Unset):
            primary_location_id = str(self.primary_location_id)

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        phones: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        guardians: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.guardians, Unset):
            guardians = []
            for guardians_item_data in self.guardians:
                guardians_item = guardians_item_data.to_dict()
                guardians.append(guardians_item)

        run_automations = self.run_automations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "client_type": client_type,
            }
        )
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if title is not UNSET:
            field_dict["title"] = title
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if marital_status is not UNSET:
            field_dict["marital_status"] = marital_status
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if secondary_phone is not UNSET:
            field_dict["secondary_phone"] = secondary_phone
        if country is not UNSET:
            field_dict["country"] = country
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if residential_address is not UNSET:
            field_dict["residential_address"] = residential_address
        if work_address is not UNSET:
            field_dict["work_address"] = work_address
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if next_of_kin is not UNSET:
            field_dict["next_of_kin"] = next_of_kin
        if national_id is not UNSET:
            field_dict["national_id"] = national_id
        if preferred_language is not UNSET:
            field_dict["preferred_language"] = preferred_language
        if referred_by is not UNSET:
            field_dict["referred_by"] = referred_by
        if referral_source_id is not UNSET:
            field_dict["referral_source_id"] = referral_source_id
        if employment is not UNSET:
            field_dict["employment"] = employment
        if is_dependent is not UNSET:
            field_dict["is_dependent"] = is_dependent
        if is_waitlist is not UNSET:
            field_dict["is_waitlist"] = is_waitlist
        if sponsor_id is not UNSET:
            field_dict["sponsor_id"] = sponsor_id
        if billing is not UNSET:
            field_dict["billing"] = billing
        if medical_history is not UNSET:
            field_dict["medical_history"] = medical_history
        if blood_type is not UNSET:
            field_dict["blood_type"] = blood_type
        if genotype is not UNSET:
            field_dict["genotype"] = genotype
        if family_history is not UNSET:
            field_dict["family_history"] = family_history
        if smoking_status is not UNSET:
            field_dict["smoking_status"] = smoking_status
        if alcohol_use is not UNSET:
            field_dict["alcohol_use"] = alcohol_use
        if recreational_drug_use is not UNSET:
            field_dict["recreational_drug_use"] = recreational_drug_use
        if physical_activity is not UNSET:
            field_dict["physical_activity"] = physical_activity
        if living_arrangement is not UNSET:
            field_dict["living_arrangement"] = living_arrangement
        if status is not UNSET:
            field_dict["status"] = status
        if is_vip is not UNSET:
            field_dict["is_vip"] = is_vip
        if primary_location_id is not UNSET:
            field_dict["primary_location_id"] = primary_location_id
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if guardians is not UNSET:
            field_dict["guardians"] = guardians
        if run_automations is not UNSET:
            field_dict["run_automations"] = run_automations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employment import Employment  # noqa: PLC0415
        from ..models.next_of_kin import NextOfKin  # noqa: PLC0415
        from ..models.patient_billing import PatientBilling  # noqa: PLC0415
        from ..models.patient_email import PatientEmail  # noqa: PLC0415
        from ..models.patient_guardian import PatientGuardian  # noqa: PLC0415
        from ..models.patient_phone import PatientPhone  # noqa: PLC0415

        d = dict(src_dict)
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        client_type = PatientCreateRequestClientType(d.pop("client_type"))

        middle_name = d.pop("middle_name", UNSET)

        preferred_name = d.pop("preferred_name", UNSET)

        title = d.pop("title", UNSET)

        suffix = d.pop("suffix", UNSET)

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: datetime.date | Unset
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = datetime.date.fromisoformat(_date_of_birth)

        _gender = d.pop("gender", UNSET)
        gender: PatientCreateRequestGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = PatientCreateRequestGender(_gender)

        _marital_status = d.pop("marital_status", UNSET)
        marital_status: PatientCreateRequestMaritalStatus | Unset
        if isinstance(_marital_status, Unset):
            marital_status = UNSET
        else:
            marital_status = PatientCreateRequestMaritalStatus(_marital_status)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        secondary_phone = d.pop("secondary_phone", UNSET)

        country = d.pop("country", UNSET)

        nationality = d.pop("nationality", UNSET)

        occupation = d.pop("occupation", UNSET)

        residential_address = d.pop("residential_address", UNSET)

        work_address = d.pop("work_address", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_ = d.pop("zip", UNSET)

        _next_of_kin = d.pop("next_of_kin", UNSET)
        next_of_kin: NextOfKin | Unset
        if isinstance(_next_of_kin, Unset):
            next_of_kin = UNSET
        else:
            next_of_kin = NextOfKin.from_dict(_next_of_kin)

        national_id = d.pop("national_id", UNSET)

        preferred_language = d.pop("preferred_language", UNSET)

        referred_by = d.pop("referred_by", UNSET)

        _referral_source_id = d.pop("referral_source_id", UNSET)
        referral_source_id: UUID | Unset
        if isinstance(_referral_source_id, Unset):
            referral_source_id = UNSET
        else:
            referral_source_id = UUID(_referral_source_id)

        _employment = d.pop("employment", UNSET)
        employment: Employment | Unset
        if isinstance(_employment, Unset):
            employment = UNSET
        else:
            employment = Employment.from_dict(_employment)

        is_dependent = d.pop("is_dependent", UNSET)

        is_waitlist = d.pop("is_waitlist", UNSET)

        _sponsor_id = d.pop("sponsor_id", UNSET)
        sponsor_id: UUID | Unset
        if isinstance(_sponsor_id, Unset):
            sponsor_id = UNSET
        else:
            sponsor_id = UUID(_sponsor_id)

        _billing = d.pop("billing", UNSET)
        billing: PatientBilling | Unset
        if isinstance(_billing, Unset):
            billing = UNSET
        else:
            billing = PatientBilling.from_dict(_billing)

        medical_history = d.pop("medical_history", UNSET)

        _blood_type = d.pop("blood_type", UNSET)
        blood_type: PatientCreateRequestBloodType | Unset
        if isinstance(_blood_type, Unset):
            blood_type = UNSET
        else:
            blood_type = PatientCreateRequestBloodType(_blood_type)

        _genotype = d.pop("genotype", UNSET)
        genotype: PatientCreateRequestGenotype | Unset
        if isinstance(_genotype, Unset):
            genotype = UNSET
        else:
            genotype = PatientCreateRequestGenotype(_genotype)

        family_history = d.pop("family_history", UNSET)

        smoking_status = d.pop("smoking_status", UNSET)

        alcohol_use = d.pop("alcohol_use", UNSET)

        recreational_drug_use = d.pop("recreational_drug_use", UNSET)

        physical_activity = d.pop("physical_activity", UNSET)

        living_arrangement = d.pop("living_arrangement", UNSET)

        _status = d.pop("status", UNSET)
        status: PatientCreateRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatientCreateRequestStatus(_status)

        is_vip = d.pop("is_vip", UNSET)

        _primary_location_id = d.pop("primary_location_id", UNSET)
        primary_location_id: UUID | Unset
        if isinstance(_primary_location_id, Unset):
            primary_location_id = UNSET
        else:
            primary_location_id = UUID(_primary_location_id)

        _emails = d.pop("emails", UNSET)
        emails: list[PatientEmail] | Unset = UNSET
        if _emails is not UNSET:
            emails = []
            for emails_item_data in _emails:
                emails_item = PatientEmail.from_dict(emails_item_data)

                emails.append(emails_item)

        _phones = d.pop("phones", UNSET)
        phones: list[PatientPhone] | Unset = UNSET
        if _phones is not UNSET:
            phones = []
            for phones_item_data in _phones:
                phones_item = PatientPhone.from_dict(phones_item_data)

                phones.append(phones_item)

        _guardians = d.pop("guardians", UNSET)
        guardians: list[PatientGuardian] | Unset = UNSET
        if _guardians is not UNSET:
            guardians = []
            for guardians_item_data in _guardians:
                guardians_item = PatientGuardian.from_dict(guardians_item_data)

                guardians.append(guardians_item)

        run_automations = d.pop("run_automations", UNSET)

        patient_create_request = cls(
            first_name=first_name,
            last_name=last_name,
            client_type=client_type,
            middle_name=middle_name,
            preferred_name=preferred_name,
            title=title,
            suffix=suffix,
            date_of_birth=date_of_birth,
            gender=gender,
            marital_status=marital_status,
            email=email,
            phone=phone,
            secondary_phone=secondary_phone,
            country=country,
            nationality=nationality,
            occupation=occupation,
            residential_address=residential_address,
            work_address=work_address,
            city=city,
            state=state,
            zip_=zip_,
            next_of_kin=next_of_kin,
            national_id=national_id,
            preferred_language=preferred_language,
            referred_by=referred_by,
            referral_source_id=referral_source_id,
            employment=employment,
            is_dependent=is_dependent,
            is_waitlist=is_waitlist,
            sponsor_id=sponsor_id,
            billing=billing,
            medical_history=medical_history,
            blood_type=blood_type,
            genotype=genotype,
            family_history=family_history,
            smoking_status=smoking_status,
            alcohol_use=alcohol_use,
            recreational_drug_use=recreational_drug_use,
            physical_activity=physical_activity,
            living_arrangement=living_arrangement,
            status=status,
            is_vip=is_vip,
            primary_location_id=primary_location_id,
            emails=emails,
            phones=phones,
            guardians=guardians,
            run_automations=run_automations,
        )

        patient_create_request.additional_properties = d
        return patient_create_request

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
