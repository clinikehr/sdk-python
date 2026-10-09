from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_update_request_blood_type_type_1 import PatientUpdateRequestBloodTypeType1
from ..models.patient_update_request_blood_type_type_2_type_1 import PatientUpdateRequestBloodTypeType2Type1
from ..models.patient_update_request_blood_type_type_3_type_1 import PatientUpdateRequestBloodTypeType3Type1
from ..models.patient_update_request_client_type import PatientUpdateRequestClientType
from ..models.patient_update_request_gender_type_1 import PatientUpdateRequestGenderType1
from ..models.patient_update_request_gender_type_2_type_1 import PatientUpdateRequestGenderType2Type1
from ..models.patient_update_request_gender_type_3_type_1 import PatientUpdateRequestGenderType3Type1
from ..models.patient_update_request_genotype_type_1 import PatientUpdateRequestGenotypeType1
from ..models.patient_update_request_genotype_type_2_type_1 import PatientUpdateRequestGenotypeType2Type1
from ..models.patient_update_request_genotype_type_3_type_1 import PatientUpdateRequestGenotypeType3Type1
from ..models.patient_update_request_marital_status_type_1 import PatientUpdateRequestMaritalStatusType1
from ..models.patient_update_request_marital_status_type_2_type_1 import PatientUpdateRequestMaritalStatusType2Type1
from ..models.patient_update_request_marital_status_type_3_type_1 import PatientUpdateRequestMaritalStatusType3Type1
from ..models.patient_update_request_status_type_1 import PatientUpdateRequestStatusType1
from ..models.patient_update_request_status_type_2_type_1 import PatientUpdateRequestStatusType2Type1
from ..models.patient_update_request_status_type_3_type_1 import PatientUpdateRequestStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employment import Employment
    from ..models.next_of_kin import NextOfKin
    from ..models.patient_billing import PatientBilling
    from ..models.patient_email import PatientEmail
    from ..models.patient_guardian import PatientGuardian
    from ..models.patient_phone import PatientPhone


T = TypeVar("T", bound="PatientUpdateRequest")


@_attrs_define
class PatientUpdateRequest:
    """A key ABSENT from the body leaves that field unchanged; a key present with JSON null clears it where the column
    allows null, refused (naming the field) where it does not (first_name/last_name can never be cleared). Nested
    objects (next_of_kin/employment/billing) replace as a whole when present. Arrays (emails/phones/guardians) replace
    the set when present. `allergies`, `current_medications` and `chronic_conditions` cannot be changed here: they are
    refused by name. Use `createAllergy` / `updateAllergy` and `createCondition` / `updateCondition`, which a clinician
    confirms. They are still returned when you read a patient.

        Attributes:
            first_name (str | Unset):
            last_name (str | Unset):
            middle_name (None | str | Unset):
            preferred_name (None | str | Unset):
            title (None | str | Unset):
            suffix (None | str | Unset):
            client_type (PatientUpdateRequestClientType | Unset): Never couple.
            date_of_birth (datetime.date | None | Unset):
            gender (None | PatientUpdateRequestGenderType1 | PatientUpdateRequestGenderType2Type1 |
                PatientUpdateRequestGenderType3Type1 | Unset):
            marital_status (None | PatientUpdateRequestMaritalStatusType1 | PatientUpdateRequestMaritalStatusType2Type1 |
                PatientUpdateRequestMaritalStatusType3Type1 | Unset):
            email (None | str | Unset):
            phone (None | str | Unset):
            secondary_phone (None | str | Unset):
            country (None | str | Unset):
            nationality (None | str | Unset):
            occupation (None | str | Unset):
            residential_address (None | str | Unset):
            work_address (None | str | Unset):
            city (None | str | Unset):
            state (None | str | Unset):
            zip_ (None | str | Unset):
            next_of_kin (NextOfKin | None | Unset):
            national_id (None | str | Unset):
            preferred_language (None | str | Unset):
            referred_by (None | str | Unset):
            referral_source_id (None | Unset | UUID):
            employment (Employment | None | Unset):
            is_dependent (bool | Unset):
            is_waitlist (bool | Unset):
            sponsor_id (None | Unset | UUID):
            billing (None | PatientBilling | Unset):
            medical_history (None | str | Unset):
            blood_type (None | PatientUpdateRequestBloodTypeType1 | PatientUpdateRequestBloodTypeType2Type1 |
                PatientUpdateRequestBloodTypeType3Type1 | Unset):
            genotype (None | PatientUpdateRequestGenotypeType1 | PatientUpdateRequestGenotypeType2Type1 |
                PatientUpdateRequestGenotypeType3Type1 | Unset):
            family_history (None | str | Unset):
            smoking_status (None | str | Unset):
            alcohol_use (None | str | Unset):
            recreational_drug_use (None | str | Unset):
            physical_activity (None | str | Unset):
            living_arrangement (None | str | Unset):
            status (None | PatientUpdateRequestStatusType1 | PatientUpdateRequestStatusType2Type1 |
                PatientUpdateRequestStatusType3Type1 | Unset):
            is_vip (bool | Unset):
            primary_location_id (None | Unset | UUID):
            emails (list[PatientEmail] | Unset):
            phones (list[PatientPhone] | Unset):
            guardians (list[PatientGuardian] | Unset):
    """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET
    client_type: PatientUpdateRequestClientType | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: (
        None
        | PatientUpdateRequestGenderType1
        | PatientUpdateRequestGenderType2Type1
        | PatientUpdateRequestGenderType3Type1
        | Unset
    ) = UNSET
    marital_status: (
        None
        | PatientUpdateRequestMaritalStatusType1
        | PatientUpdateRequestMaritalStatusType2Type1
        | PatientUpdateRequestMaritalStatusType3Type1
        | Unset
    ) = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    secondary_phone: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    nationality: None | str | Unset = UNSET
    occupation: None | str | Unset = UNSET
    residential_address: None | str | Unset = UNSET
    work_address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    zip_: None | str | Unset = UNSET
    next_of_kin: NextOfKin | None | Unset = UNSET
    national_id: None | str | Unset = UNSET
    preferred_language: None | str | Unset = UNSET
    referred_by: None | str | Unset = UNSET
    referral_source_id: None | Unset | UUID = UNSET
    employment: Employment | None | Unset = UNSET
    is_dependent: bool | Unset = UNSET
    is_waitlist: bool | Unset = UNSET
    sponsor_id: None | Unset | UUID = UNSET
    billing: None | PatientBilling | Unset = UNSET
    medical_history: None | str | Unset = UNSET
    blood_type: (
        None
        | PatientUpdateRequestBloodTypeType1
        | PatientUpdateRequestBloodTypeType2Type1
        | PatientUpdateRequestBloodTypeType3Type1
        | Unset
    ) = UNSET
    genotype: (
        None
        | PatientUpdateRequestGenotypeType1
        | PatientUpdateRequestGenotypeType2Type1
        | PatientUpdateRequestGenotypeType3Type1
        | Unset
    ) = UNSET
    family_history: None | str | Unset = UNSET
    smoking_status: None | str | Unset = UNSET
    alcohol_use: None | str | Unset = UNSET
    recreational_drug_use: None | str | Unset = UNSET
    physical_activity: None | str | Unset = UNSET
    living_arrangement: None | str | Unset = UNSET
    status: (
        None
        | PatientUpdateRequestStatusType1
        | PatientUpdateRequestStatusType2Type1
        | PatientUpdateRequestStatusType3Type1
        | Unset
    ) = UNSET
    is_vip: bool | Unset = UNSET
    primary_location_id: None | Unset | UUID = UNSET
    emails: list[PatientEmail] | Unset = UNSET
    phones: list[PatientPhone] | Unset = UNSET
    guardians: list[PatientGuardian] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employment import Employment  # noqa: PLC0415
        from ..models.next_of_kin import NextOfKin  # noqa: PLC0415
        from ..models.patient_billing import PatientBilling  # noqa: PLC0415

        first_name = self.first_name

        last_name = self.last_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        client_type: str | Unset = UNSET
        if not isinstance(self.client_type, Unset):
            client_type = self.client_type.value

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        elif isinstance(self.gender, PatientUpdateRequestGenderType1):
            gender = self.gender.value
        elif isinstance(self.gender, PatientUpdateRequestGenderType2Type1):
            gender = self.gender.value
        elif isinstance(self.gender, PatientUpdateRequestGenderType3Type1):
            gender = self.gender.value
        else:
            gender = self.gender

        marital_status: None | str | Unset
        if isinstance(self.marital_status, Unset):
            marital_status = UNSET
        elif isinstance(self.marital_status, PatientUpdateRequestMaritalStatusType1):
            marital_status = self.marital_status.value
        elif isinstance(self.marital_status, PatientUpdateRequestMaritalStatusType2Type1):
            marital_status = self.marital_status.value
        elif isinstance(self.marital_status, PatientUpdateRequestMaritalStatusType3Type1):
            marital_status = self.marital_status.value
        else:
            marital_status = self.marital_status

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

        secondary_phone: None | str | Unset
        if isinstance(self.secondary_phone, Unset):
            secondary_phone = UNSET
        else:
            secondary_phone = self.secondary_phone

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        nationality: None | str | Unset
        if isinstance(self.nationality, Unset):
            nationality = UNSET
        else:
            nationality = self.nationality

        occupation: None | str | Unset
        if isinstance(self.occupation, Unset):
            occupation = UNSET
        else:
            occupation = self.occupation

        residential_address: None | str | Unset
        if isinstance(self.residential_address, Unset):
            residential_address = UNSET
        else:
            residential_address = self.residential_address

        work_address: None | str | Unset
        if isinstance(self.work_address, Unset):
            work_address = UNSET
        else:
            work_address = self.work_address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        zip_: None | str | Unset
        if isinstance(self.zip_, Unset):
            zip_ = UNSET
        else:
            zip_ = self.zip_

        next_of_kin: dict[str, Any] | None | Unset
        if isinstance(self.next_of_kin, Unset):
            next_of_kin = UNSET
        elif isinstance(self.next_of_kin, NextOfKin):
            next_of_kin = self.next_of_kin.to_dict()
        else:
            next_of_kin = self.next_of_kin

        national_id: None | str | Unset
        if isinstance(self.national_id, Unset):
            national_id = UNSET
        else:
            national_id = self.national_id

        preferred_language: None | str | Unset
        if isinstance(self.preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = self.preferred_language

        referred_by: None | str | Unset
        if isinstance(self.referred_by, Unset):
            referred_by = UNSET
        else:
            referred_by = self.referred_by

        referral_source_id: None | str | Unset
        if isinstance(self.referral_source_id, Unset):
            referral_source_id = UNSET
        elif isinstance(self.referral_source_id, UUID):
            referral_source_id = str(self.referral_source_id)
        else:
            referral_source_id = self.referral_source_id

        employment: dict[str, Any] | None | Unset
        if isinstance(self.employment, Unset):
            employment = UNSET
        elif isinstance(self.employment, Employment):
            employment = self.employment.to_dict()
        else:
            employment = self.employment

        is_dependent = self.is_dependent

        is_waitlist = self.is_waitlist

        sponsor_id: None | str | Unset
        if isinstance(self.sponsor_id, Unset):
            sponsor_id = UNSET
        elif isinstance(self.sponsor_id, UUID):
            sponsor_id = str(self.sponsor_id)
        else:
            sponsor_id = self.sponsor_id

        billing: dict[str, Any] | None | Unset
        if isinstance(self.billing, Unset):
            billing = UNSET
        elif isinstance(self.billing, PatientBilling):
            billing = self.billing.to_dict()
        else:
            billing = self.billing

        medical_history: None | str | Unset
        if isinstance(self.medical_history, Unset):
            medical_history = UNSET
        else:
            medical_history = self.medical_history

        blood_type: None | str | Unset
        if isinstance(self.blood_type, Unset):
            blood_type = UNSET
        elif isinstance(self.blood_type, PatientUpdateRequestBloodTypeType1):
            blood_type = self.blood_type.value
        elif isinstance(self.blood_type, PatientUpdateRequestBloodTypeType2Type1):
            blood_type = self.blood_type.value
        elif isinstance(self.blood_type, PatientUpdateRequestBloodTypeType3Type1):
            blood_type = self.blood_type.value
        else:
            blood_type = self.blood_type

        genotype: None | str | Unset
        if isinstance(self.genotype, Unset):
            genotype = UNSET
        elif isinstance(self.genotype, PatientUpdateRequestGenotypeType1):
            genotype = self.genotype.value
        elif isinstance(self.genotype, PatientUpdateRequestGenotypeType2Type1):
            genotype = self.genotype.value
        elif isinstance(self.genotype, PatientUpdateRequestGenotypeType3Type1):
            genotype = self.genotype.value
        else:
            genotype = self.genotype

        family_history: None | str | Unset
        if isinstance(self.family_history, Unset):
            family_history = UNSET
        else:
            family_history = self.family_history

        smoking_status: None | str | Unset
        if isinstance(self.smoking_status, Unset):
            smoking_status = UNSET
        else:
            smoking_status = self.smoking_status

        alcohol_use: None | str | Unset
        if isinstance(self.alcohol_use, Unset):
            alcohol_use = UNSET
        else:
            alcohol_use = self.alcohol_use

        recreational_drug_use: None | str | Unset
        if isinstance(self.recreational_drug_use, Unset):
            recreational_drug_use = UNSET
        else:
            recreational_drug_use = self.recreational_drug_use

        physical_activity: None | str | Unset
        if isinstance(self.physical_activity, Unset):
            physical_activity = UNSET
        else:
            physical_activity = self.physical_activity

        living_arrangement: None | str | Unset
        if isinstance(self.living_arrangement, Unset):
            living_arrangement = UNSET
        else:
            living_arrangement = self.living_arrangement

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PatientUpdateRequestStatusType1):
            status = self.status.value
        elif isinstance(self.status, PatientUpdateRequestStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, PatientUpdateRequestStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        is_vip = self.is_vip

        primary_location_id: None | str | Unset
        if isinstance(self.primary_location_id, Unset):
            primary_location_id = UNSET
        elif isinstance(self.primary_location_id, UUID):
            primary_location_id = str(self.primary_location_id)
        else:
            primary_location_id = self.primary_location_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if title is not UNSET:
            field_dict["title"] = title
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if client_type is not UNSET:
            field_dict["client_type"] = client_type
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
        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        _client_type = d.pop("client_type", UNSET)
        client_type: PatientUpdateRequestClientType | Unset
        if isinstance(_client_type, Unset):
            client_type = UNSET
        else:
            client_type = PatientUpdateRequestClientType(_client_type)

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = datetime.date.fromisoformat(data)

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_gender(
            data: object,
        ) -> (
            None
            | PatientUpdateRequestGenderType1
            | PatientUpdateRequestGenderType2Type1
            | PatientUpdateRequestGenderType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_1 = PatientUpdateRequestGenderType1(data)

                return gender_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_2_type_1 = PatientUpdateRequestGenderType2Type1(data)

                return gender_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_3_type_1 = PatientUpdateRequestGenderType3Type1(data)

                return gender_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientUpdateRequestGenderType1
                | PatientUpdateRequestGenderType2Type1
                | PatientUpdateRequestGenderType3Type1
                | Unset,
                data,
            )

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_marital_status(
            data: object,
        ) -> (
            None
            | PatientUpdateRequestMaritalStatusType1
            | PatientUpdateRequestMaritalStatusType2Type1
            | PatientUpdateRequestMaritalStatusType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_1 = PatientUpdateRequestMaritalStatusType1(data)

                return marital_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_2_type_1 = PatientUpdateRequestMaritalStatusType2Type1(data)

                return marital_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_3_type_1 = PatientUpdateRequestMaritalStatusType3Type1(data)

                return marital_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientUpdateRequestMaritalStatusType1
                | PatientUpdateRequestMaritalStatusType2Type1
                | PatientUpdateRequestMaritalStatusType3Type1
                | Unset,
                data,
            )

        marital_status = _parse_marital_status(d.pop("marital_status", UNSET))

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

        def _parse_secondary_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secondary_phone = _parse_secondary_phone(d.pop("secondary_phone", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_nationality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nationality = _parse_nationality(d.pop("nationality", UNSET))

        def _parse_occupation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupation = _parse_occupation(d.pop("occupation", UNSET))

        def _parse_residential_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        residential_address = _parse_residential_address(d.pop("residential_address", UNSET))

        def _parse_work_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_address = _parse_work_address(d.pop("work_address", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_zip_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_ = _parse_zip_(d.pop("zip", UNSET))

        def _parse_next_of_kin(data: object) -> NextOfKin | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_of_kin_type_0 = NextOfKin.from_dict(data)

                return next_of_kin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NextOfKin | None | Unset, data)

        next_of_kin = _parse_next_of_kin(d.pop("next_of_kin", UNSET))

        def _parse_national_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        national_id = _parse_national_id(d.pop("national_id", UNSET))

        def _parse_preferred_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_language = _parse_preferred_language(d.pop("preferred_language", UNSET))

        def _parse_referred_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referred_by = _parse_referred_by(d.pop("referred_by", UNSET))

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

        def _parse_employment(data: object) -> Employment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employment_type_0 = Employment.from_dict(data)

                return employment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Employment | None | Unset, data)

        employment = _parse_employment(d.pop("employment", UNSET))

        is_dependent = d.pop("is_dependent", UNSET)

        is_waitlist = d.pop("is_waitlist", UNSET)

        def _parse_sponsor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sponsor_id_type_0 = UUID(data)

                return sponsor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sponsor_id = _parse_sponsor_id(d.pop("sponsor_id", UNSET))

        def _parse_billing(data: object) -> None | PatientBilling | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_type_0 = PatientBilling.from_dict(data)

                return billing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatientBilling | Unset, data)

        billing = _parse_billing(d.pop("billing", UNSET))

        def _parse_medical_history(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medical_history = _parse_medical_history(d.pop("medical_history", UNSET))

        def _parse_blood_type(
            data: object,
        ) -> (
            None
            | PatientUpdateRequestBloodTypeType1
            | PatientUpdateRequestBloodTypeType2Type1
            | PatientUpdateRequestBloodTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_1 = PatientUpdateRequestBloodTypeType1(data)

                return blood_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_2_type_1 = PatientUpdateRequestBloodTypeType2Type1(data)

                return blood_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_3_type_1 = PatientUpdateRequestBloodTypeType3Type1(data)

                return blood_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientUpdateRequestBloodTypeType1
                | PatientUpdateRequestBloodTypeType2Type1
                | PatientUpdateRequestBloodTypeType3Type1
                | Unset,
                data,
            )

        blood_type = _parse_blood_type(d.pop("blood_type", UNSET))

        def _parse_genotype(
            data: object,
        ) -> (
            None
            | PatientUpdateRequestGenotypeType1
            | PatientUpdateRequestGenotypeType2Type1
            | PatientUpdateRequestGenotypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_1 = PatientUpdateRequestGenotypeType1(data)

                return genotype_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_2_type_1 = PatientUpdateRequestGenotypeType2Type1(data)

                return genotype_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_3_type_1 = PatientUpdateRequestGenotypeType3Type1(data)

                return genotype_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientUpdateRequestGenotypeType1
                | PatientUpdateRequestGenotypeType2Type1
                | PatientUpdateRequestGenotypeType3Type1
                | Unset,
                data,
            )

        genotype = _parse_genotype(d.pop("genotype", UNSET))

        def _parse_family_history(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_history = _parse_family_history(d.pop("family_history", UNSET))

        def _parse_smoking_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        smoking_status = _parse_smoking_status(d.pop("smoking_status", UNSET))

        def _parse_alcohol_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alcohol_use = _parse_alcohol_use(d.pop("alcohol_use", UNSET))

        def _parse_recreational_drug_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recreational_drug_use = _parse_recreational_drug_use(d.pop("recreational_drug_use", UNSET))

        def _parse_physical_activity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        physical_activity = _parse_physical_activity(d.pop("physical_activity", UNSET))

        def _parse_living_arrangement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        living_arrangement = _parse_living_arrangement(d.pop("living_arrangement", UNSET))

        def _parse_status(
            data: object,
        ) -> (
            None
            | PatientUpdateRequestStatusType1
            | PatientUpdateRequestStatusType2Type1
            | PatientUpdateRequestStatusType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = PatientUpdateRequestStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = PatientUpdateRequestStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = PatientUpdateRequestStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientUpdateRequestStatusType1
                | PatientUpdateRequestStatusType2Type1
                | PatientUpdateRequestStatusType3Type1
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        is_vip = d.pop("is_vip", UNSET)

        def _parse_primary_location_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_location_id_type_0 = UUID(data)

                return primary_location_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_location_id = _parse_primary_location_id(d.pop("primary_location_id", UNSET))

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

        patient_update_request = cls(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            preferred_name=preferred_name,
            title=title,
            suffix=suffix,
            client_type=client_type,
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
        )

        patient_update_request.additional_properties = d
        return patient_update_request

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
