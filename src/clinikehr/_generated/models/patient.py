from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_blood_type_type_1 import PatientBloodTypeType1
from ..models.patient_blood_type_type_2_type_1 import PatientBloodTypeType2Type1
from ..models.patient_blood_type_type_3_type_1 import PatientBloodTypeType3Type1
from ..models.patient_client_type_type_1 import PatientClientTypeType1
from ..models.patient_client_type_type_2_type_1 import PatientClientTypeType2Type1
from ..models.patient_client_type_type_3_type_1 import PatientClientTypeType3Type1
from ..models.patient_gender_type_1 import PatientGenderType1
from ..models.patient_gender_type_2_type_1 import PatientGenderType2Type1
from ..models.patient_gender_type_3_type_1 import PatientGenderType3Type1
from ..models.patient_genotype_type_1 import PatientGenotypeType1
from ..models.patient_genotype_type_2_type_1 import PatientGenotypeType2Type1
from ..models.patient_genotype_type_3_type_1 import PatientGenotypeType3Type1
from ..models.patient_marital_status_type_1 import PatientMaritalStatusType1
from ..models.patient_marital_status_type_2_type_1 import PatientMaritalStatusType2Type1
from ..models.patient_marital_status_type_3_type_1 import PatientMaritalStatusType3Type1
from ..models.patient_status_type_1 import PatientStatusType1
from ..models.patient_status_type_2_type_1 import PatientStatusType2Type1
from ..models.patient_status_type_3_type_1 import PatientStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employment import Employment
    from ..models.next_of_kin import NextOfKin
    from ..models.patient_billing import PatientBilling
    from ..models.patient_care_providers_item import PatientCareProvidersItem
    from ..models.patient_couple import PatientCouple
    from ..models.patient_email import PatientEmail
    from ..models.patient_guardian import PatientGuardian
    from ..models.patient_insurance_item import PatientInsuranceItem
    from ..models.patient_notification_settings import PatientNotificationSettings
    from ..models.patient_pharmacies_item import PatientPharmaciesItem
    from ..models.patient_phone import PatientPhone


T = TypeVar("T", bound="Patient")


@_attrs_define
class Patient:
    """
    Attributes:
        id (UUID):
        first_name (str):
        last_name (str):
        mrn (None | str | Unset):
        middle_name (None | str | Unset):
        preferred_name (None | str | Unset):
        title (None | str | Unset):
        suffix (None | str | Unset):
        date_of_birth (datetime.date | None | Unset):
        gender (None | PatientGenderType1 | PatientGenderType2Type1 | PatientGenderType3Type1 | Unset):
        marital_status (None | PatientMaritalStatusType1 | PatientMaritalStatusType2Type1 |
            PatientMaritalStatusType3Type1 | Unset):
        client_type (None | PatientClientTypeType1 | PatientClientTypeType2Type1 | PatientClientTypeType3Type1 | Unset):
        client_status (None | str | Unset):
        is_dependent (bool | Unset):
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
        next_of_kin (NextOfKin | Unset):
        national_id (None | str | Unset):
        preferred_language (None | str | Unset):
        referred_by (None | str | Unset):
        referral_source_id (None | Unset | UUID):
        employment (Employment | Unset):
        is_waitlist (bool | Unset):
        billing (PatientBilling | Unset):
        sponsor_id (None | Unset | UUID):
        allergies (list[str] | Unset):
        medical_history (None | str | Unset):
        current_medications (list[str] | Unset):
        chronic_conditions (list[str] | Unset):
        blood_type (None | PatientBloodTypeType1 | PatientBloodTypeType2Type1 | PatientBloodTypeType3Type1 | Unset):
        genotype (None | PatientGenotypeType1 | PatientGenotypeType2Type1 | PatientGenotypeType3Type1 | Unset):
        family_history (None | str | Unset):
        smoking_status (None | str | Unset):
        alcohol_use (None | str | Unset):
        recreational_drug_use (None | str | Unset):
        physical_activity (None | str | Unset):
        living_arrangement (None | str | Unset):
        has_profile_image (bool | Unset): Read-only. Whether the patient has a profile picture on file. The picture
            itself is not available through the API yet.
        profile_image_path (None | str | Unset): Read-only. Not available through the API yet - this value cannot be
            used to download the picture.
        status (None | PatientStatusType1 | PatientStatusType2Type1 | PatientStatusType3Type1 | Unset):
        is_vip (bool | Unset):
        primary_location_id (None | Unset | UUID):
        portal_access_enabled (bool | None | Unset): Read-only.
        admission_status (None | str | Unset): Read-only, ward-only.
        couple (None | PatientCouple | Unset):
        emails (list[PatientEmail] | Unset): Write REPLACES the whole set.
        phones (list[PatientPhone] | Unset): Write REPLACES the whole set.
        guardians (list[PatientGuardian] | Unset): Write REPLACES the whole set. Only accepted when client_type=minor.
        insurance (list[PatientInsuranceItem] | Unset): Read-only. Own module, own save action — never written here.
        pharmacies (list[PatientPharmaciesItem] | Unset): Read-only. Populated by intake extraction only.
        care_providers (list[PatientCareProvidersItem] | Unset): Read-only. Populated by intake extraction only.
        notification_settings (None | PatientNotificationSettings | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    first_name: str
    last_name: str
    mrn: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: None | PatientGenderType1 | PatientGenderType2Type1 | PatientGenderType3Type1 | Unset = UNSET
    marital_status: (
        None | PatientMaritalStatusType1 | PatientMaritalStatusType2Type1 | PatientMaritalStatusType3Type1 | Unset
    ) = UNSET
    client_type: None | PatientClientTypeType1 | PatientClientTypeType2Type1 | PatientClientTypeType3Type1 | Unset = (
        UNSET
    )
    client_status: None | str | Unset = UNSET
    is_dependent: bool | Unset = UNSET
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
    next_of_kin: NextOfKin | Unset = UNSET
    national_id: None | str | Unset = UNSET
    preferred_language: None | str | Unset = UNSET
    referred_by: None | str | Unset = UNSET
    referral_source_id: None | Unset | UUID = UNSET
    employment: Employment | Unset = UNSET
    is_waitlist: bool | Unset = UNSET
    billing: PatientBilling | Unset = UNSET
    sponsor_id: None | Unset | UUID = UNSET
    allergies: list[str] | Unset = UNSET
    medical_history: None | str | Unset = UNSET
    current_medications: list[str] | Unset = UNSET
    chronic_conditions: list[str] | Unset = UNSET
    blood_type: None | PatientBloodTypeType1 | PatientBloodTypeType2Type1 | PatientBloodTypeType3Type1 | Unset = UNSET
    genotype: None | PatientGenotypeType1 | PatientGenotypeType2Type1 | PatientGenotypeType3Type1 | Unset = UNSET
    family_history: None | str | Unset = UNSET
    smoking_status: None | str | Unset = UNSET
    alcohol_use: None | str | Unset = UNSET
    recreational_drug_use: None | str | Unset = UNSET
    physical_activity: None | str | Unset = UNSET
    living_arrangement: None | str | Unset = UNSET
    has_profile_image: bool | Unset = UNSET
    profile_image_path: None | str | Unset = UNSET
    status: None | PatientStatusType1 | PatientStatusType2Type1 | PatientStatusType3Type1 | Unset = UNSET
    is_vip: bool | Unset = UNSET
    primary_location_id: None | Unset | UUID = UNSET
    portal_access_enabled: bool | None | Unset = UNSET
    admission_status: None | str | Unset = UNSET
    couple: None | PatientCouple | Unset = UNSET
    emails: list[PatientEmail] | Unset = UNSET
    phones: list[PatientPhone] | Unset = UNSET
    guardians: list[PatientGuardian] | Unset = UNSET
    insurance: list[PatientInsuranceItem] | Unset = UNSET
    pharmacies: list[PatientPharmaciesItem] | Unset = UNSET
    care_providers: list[PatientCareProvidersItem] | Unset = UNSET
    notification_settings: None | PatientNotificationSettings | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patient_couple import PatientCouple  # noqa: PLC0415
        from ..models.patient_notification_settings import PatientNotificationSettings  # noqa: PLC0415

        id = str(self.id)

        first_name = self.first_name

        last_name = self.last_name

        mrn: None | str | Unset
        if isinstance(self.mrn, Unset):
            mrn = UNSET
        else:
            mrn = self.mrn

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
        elif isinstance(self.gender, PatientGenderType1):
            gender = self.gender.value
        elif isinstance(self.gender, PatientGenderType2Type1):
            gender = self.gender.value
        elif isinstance(self.gender, PatientGenderType3Type1):
            gender = self.gender.value
        else:
            gender = self.gender

        marital_status: None | str | Unset
        if isinstance(self.marital_status, Unset):
            marital_status = UNSET
        elif isinstance(self.marital_status, PatientMaritalStatusType1):
            marital_status = self.marital_status.value
        elif isinstance(self.marital_status, PatientMaritalStatusType2Type1):
            marital_status = self.marital_status.value
        elif isinstance(self.marital_status, PatientMaritalStatusType3Type1):
            marital_status = self.marital_status.value
        else:
            marital_status = self.marital_status

        client_type: None | str | Unset
        if isinstance(self.client_type, Unset):
            client_type = UNSET
        elif isinstance(self.client_type, PatientClientTypeType1):
            client_type = self.client_type.value
        elif isinstance(self.client_type, PatientClientTypeType2Type1):
            client_type = self.client_type.value
        elif isinstance(self.client_type, PatientClientTypeType3Type1):
            client_type = self.client_type.value
        else:
            client_type = self.client_type

        client_status: None | str | Unset
        if isinstance(self.client_status, Unset):
            client_status = UNSET
        else:
            client_status = self.client_status

        is_dependent = self.is_dependent

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

        next_of_kin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_of_kin, Unset):
            next_of_kin = self.next_of_kin.to_dict()

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

        employment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employment, Unset):
            employment = self.employment.to_dict()

        is_waitlist = self.is_waitlist

        billing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing, Unset):
            billing = self.billing.to_dict()

        sponsor_id: None | str | Unset
        if isinstance(self.sponsor_id, Unset):
            sponsor_id = UNSET
        elif isinstance(self.sponsor_id, UUID):
            sponsor_id = str(self.sponsor_id)
        else:
            sponsor_id = self.sponsor_id

        allergies: list[str] | Unset = UNSET
        if not isinstance(self.allergies, Unset):
            allergies = self.allergies

        medical_history: None | str | Unset
        if isinstance(self.medical_history, Unset):
            medical_history = UNSET
        else:
            medical_history = self.medical_history

        current_medications: list[str] | Unset = UNSET
        if not isinstance(self.current_medications, Unset):
            current_medications = self.current_medications

        chronic_conditions: list[str] | Unset = UNSET
        if not isinstance(self.chronic_conditions, Unset):
            chronic_conditions = self.chronic_conditions

        blood_type: None | str | Unset
        if isinstance(self.blood_type, Unset):
            blood_type = UNSET
        elif isinstance(self.blood_type, PatientBloodTypeType1):
            blood_type = self.blood_type.value
        elif isinstance(self.blood_type, PatientBloodTypeType2Type1):
            blood_type = self.blood_type.value
        elif isinstance(self.blood_type, PatientBloodTypeType3Type1):
            blood_type = self.blood_type.value
        else:
            blood_type = self.blood_type

        genotype: None | str | Unset
        if isinstance(self.genotype, Unset):
            genotype = UNSET
        elif isinstance(self.genotype, PatientGenotypeType1):
            genotype = self.genotype.value
        elif isinstance(self.genotype, PatientGenotypeType2Type1):
            genotype = self.genotype.value
        elif isinstance(self.genotype, PatientGenotypeType3Type1):
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

        has_profile_image = self.has_profile_image

        profile_image_path: None | str | Unset
        if isinstance(self.profile_image_path, Unset):
            profile_image_path = UNSET
        else:
            profile_image_path = self.profile_image_path

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PatientStatusType1):
            status = self.status.value
        elif isinstance(self.status, PatientStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, PatientStatusType3Type1):
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

        portal_access_enabled: bool | None | Unset
        if isinstance(self.portal_access_enabled, Unset):
            portal_access_enabled = UNSET
        else:
            portal_access_enabled = self.portal_access_enabled

        admission_status: None | str | Unset
        if isinstance(self.admission_status, Unset):
            admission_status = UNSET
        else:
            admission_status = self.admission_status

        couple: dict[str, Any] | None | Unset
        if isinstance(self.couple, Unset):
            couple = UNSET
        elif isinstance(self.couple, PatientCouple):
            couple = self.couple.to_dict()
        else:
            couple = self.couple

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

        insurance: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.insurance, Unset):
            insurance = []
            for insurance_item_data in self.insurance:
                insurance_item = insurance_item_data.to_dict()
                insurance.append(insurance_item)

        pharmacies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pharmacies, Unset):
            pharmacies = []
            for pharmacies_item_data in self.pharmacies:
                pharmacies_item = pharmacies_item_data.to_dict()
                pharmacies.append(pharmacies_item)

        care_providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.care_providers, Unset):
            care_providers = []
            for care_providers_item_data in self.care_providers:
                care_providers_item = care_providers_item_data.to_dict()
                care_providers.append(care_providers_item)

        notification_settings: dict[str, Any] | None | Unset
        if isinstance(self.notification_settings, Unset):
            notification_settings = UNSET
        elif isinstance(self.notification_settings, PatientNotificationSettings):
            notification_settings = self.notification_settings.to_dict()
        else:
            notification_settings = self.notification_settings

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
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if mrn is not UNSET:
            field_dict["mrn"] = mrn
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
        if client_type is not UNSET:
            field_dict["client_type"] = client_type
        if client_status is not UNSET:
            field_dict["client_status"] = client_status
        if is_dependent is not UNSET:
            field_dict["is_dependent"] = is_dependent
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
        if is_waitlist is not UNSET:
            field_dict["is_waitlist"] = is_waitlist
        if billing is not UNSET:
            field_dict["billing"] = billing
        if sponsor_id is not UNSET:
            field_dict["sponsor_id"] = sponsor_id
        if allergies is not UNSET:
            field_dict["allergies"] = allergies
        if medical_history is not UNSET:
            field_dict["medical_history"] = medical_history
        if current_medications is not UNSET:
            field_dict["current_medications"] = current_medications
        if chronic_conditions is not UNSET:
            field_dict["chronic_conditions"] = chronic_conditions
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
        if has_profile_image is not UNSET:
            field_dict["has_profile_image"] = has_profile_image
        if profile_image_path is not UNSET:
            field_dict["profile_image_path"] = profile_image_path
        if status is not UNSET:
            field_dict["status"] = status
        if is_vip is not UNSET:
            field_dict["is_vip"] = is_vip
        if primary_location_id is not UNSET:
            field_dict["primary_location_id"] = primary_location_id
        if portal_access_enabled is not UNSET:
            field_dict["portal_access_enabled"] = portal_access_enabled
        if admission_status is not UNSET:
            field_dict["admission_status"] = admission_status
        if couple is not UNSET:
            field_dict["couple"] = couple
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if guardians is not UNSET:
            field_dict["guardians"] = guardians
        if insurance is not UNSET:
            field_dict["insurance"] = insurance
        if pharmacies is not UNSET:
            field_dict["pharmacies"] = pharmacies
        if care_providers is not UNSET:
            field_dict["care_providers"] = care_providers
        if notification_settings is not UNSET:
            field_dict["notification_settings"] = notification_settings
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employment import Employment  # noqa: PLC0415
        from ..models.next_of_kin import NextOfKin  # noqa: PLC0415
        from ..models.patient_billing import PatientBilling  # noqa: PLC0415
        from ..models.patient_care_providers_item import PatientCareProvidersItem  # noqa: PLC0415
        from ..models.patient_couple import PatientCouple  # noqa: PLC0415
        from ..models.patient_email import PatientEmail  # noqa: PLC0415
        from ..models.patient_guardian import PatientGuardian  # noqa: PLC0415
        from ..models.patient_insurance_item import PatientInsuranceItem  # noqa: PLC0415
        from ..models.patient_notification_settings import PatientNotificationSettings  # noqa: PLC0415
        from ..models.patient_pharmacies_item import PatientPharmaciesItem  # noqa: PLC0415
        from ..models.patient_phone import PatientPhone  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        def _parse_mrn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mrn = _parse_mrn(d.pop("mrn", UNSET))

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
        ) -> None | PatientGenderType1 | PatientGenderType2Type1 | PatientGenderType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_1 = PatientGenderType1(data)

                return gender_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_2_type_1 = PatientGenderType2Type1(data)

                return gender_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_3_type_1 = PatientGenderType3Type1(data)

                return gender_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatientGenderType1 | PatientGenderType2Type1 | PatientGenderType3Type1 | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_marital_status(
            data: object,
        ) -> None | PatientMaritalStatusType1 | PatientMaritalStatusType2Type1 | PatientMaritalStatusType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_1 = PatientMaritalStatusType1(data)

                return marital_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_2_type_1 = PatientMaritalStatusType2Type1(data)

                return marital_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marital_status_type_3_type_1 = PatientMaritalStatusType3Type1(data)

                return marital_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientMaritalStatusType1
                | PatientMaritalStatusType2Type1
                | PatientMaritalStatusType3Type1
                | Unset,
                data,
            )

        marital_status = _parse_marital_status(d.pop("marital_status", UNSET))

        def _parse_client_type(
            data: object,
        ) -> None | PatientClientTypeType1 | PatientClientTypeType2Type1 | PatientClientTypeType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_type_type_1 = PatientClientTypeType1(data)

                return client_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_type_type_2_type_1 = PatientClientTypeType2Type1(data)

                return client_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                client_type_type_3_type_1 = PatientClientTypeType3Type1(data)

                return client_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatientClientTypeType1 | PatientClientTypeType2Type1 | PatientClientTypeType3Type1 | Unset, data
            )

        client_type = _parse_client_type(d.pop("client_type", UNSET))

        def _parse_client_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_status = _parse_client_status(d.pop("client_status", UNSET))

        is_dependent = d.pop("is_dependent", UNSET)

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

        _next_of_kin = d.pop("next_of_kin", UNSET)
        next_of_kin: NextOfKin | Unset
        if isinstance(_next_of_kin, Unset):
            next_of_kin = UNSET
        else:
            next_of_kin = NextOfKin.from_dict(_next_of_kin)

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

        _employment = d.pop("employment", UNSET)
        employment: Employment | Unset
        if isinstance(_employment, Unset):
            employment = UNSET
        else:
            employment = Employment.from_dict(_employment)

        is_waitlist = d.pop("is_waitlist", UNSET)

        _billing = d.pop("billing", UNSET)
        billing: PatientBilling | Unset
        if isinstance(_billing, Unset):
            billing = UNSET
        else:
            billing = PatientBilling.from_dict(_billing)

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

        allergies = cast(list[str], d.pop("allergies", UNSET))

        def _parse_medical_history(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        medical_history = _parse_medical_history(d.pop("medical_history", UNSET))

        current_medications = cast(list[str], d.pop("current_medications", UNSET))

        chronic_conditions = cast(list[str], d.pop("chronic_conditions", UNSET))

        def _parse_blood_type(
            data: object,
        ) -> None | PatientBloodTypeType1 | PatientBloodTypeType2Type1 | PatientBloodTypeType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_1 = PatientBloodTypeType1(data)

                return blood_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_2_type_1 = PatientBloodTypeType2Type1(data)

                return blood_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blood_type_type_3_type_1 = PatientBloodTypeType3Type1(data)

                return blood_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatientBloodTypeType1 | PatientBloodTypeType2Type1 | PatientBloodTypeType3Type1 | Unset, data
            )

        blood_type = _parse_blood_type(d.pop("blood_type", UNSET))

        def _parse_genotype(
            data: object,
        ) -> None | PatientGenotypeType1 | PatientGenotypeType2Type1 | PatientGenotypeType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_1 = PatientGenotypeType1(data)

                return genotype_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_2_type_1 = PatientGenotypeType2Type1(data)

                return genotype_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                genotype_type_3_type_1 = PatientGenotypeType3Type1(data)

                return genotype_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatientGenotypeType1 | PatientGenotypeType2Type1 | PatientGenotypeType3Type1 | Unset, data
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

        has_profile_image = d.pop("has_profile_image", UNSET)

        def _parse_profile_image_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_image_path = _parse_profile_image_path(d.pop("profile_image_path", UNSET))

        def _parse_status(
            data: object,
        ) -> None | PatientStatusType1 | PatientStatusType2Type1 | PatientStatusType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = PatientStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = PatientStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = PatientStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatientStatusType1 | PatientStatusType2Type1 | PatientStatusType3Type1 | Unset, data)

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

        def _parse_portal_access_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_access_enabled = _parse_portal_access_enabled(d.pop("portal_access_enabled", UNSET))

        def _parse_admission_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admission_status = _parse_admission_status(d.pop("admission_status", UNSET))

        def _parse_couple(data: object) -> None | PatientCouple | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                couple_type_0 = PatientCouple.from_dict(data)

                return couple_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatientCouple | Unset, data)

        couple = _parse_couple(d.pop("couple", UNSET))

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

        _insurance = d.pop("insurance", UNSET)
        insurance: list[PatientInsuranceItem] | Unset = UNSET
        if _insurance is not UNSET:
            insurance = []
            for insurance_item_data in _insurance:
                insurance_item = PatientInsuranceItem.from_dict(insurance_item_data)

                insurance.append(insurance_item)

        _pharmacies = d.pop("pharmacies", UNSET)
        pharmacies: list[PatientPharmaciesItem] | Unset = UNSET
        if _pharmacies is not UNSET:
            pharmacies = []
            for pharmacies_item_data in _pharmacies:
                pharmacies_item = PatientPharmaciesItem.from_dict(pharmacies_item_data)

                pharmacies.append(pharmacies_item)

        _care_providers = d.pop("care_providers", UNSET)
        care_providers: list[PatientCareProvidersItem] | Unset = UNSET
        if _care_providers is not UNSET:
            care_providers = []
            for care_providers_item_data in _care_providers:
                care_providers_item = PatientCareProvidersItem.from_dict(care_providers_item_data)

                care_providers.append(care_providers_item)

        def _parse_notification_settings(data: object) -> None | PatientNotificationSettings | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                notification_settings_type_0 = PatientNotificationSettings.from_dict(data)

                return notification_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatientNotificationSettings | Unset, data)

        notification_settings = _parse_notification_settings(d.pop("notification_settings", UNSET))

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

        patient = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            mrn=mrn,
            middle_name=middle_name,
            preferred_name=preferred_name,
            title=title,
            suffix=suffix,
            date_of_birth=date_of_birth,
            gender=gender,
            marital_status=marital_status,
            client_type=client_type,
            client_status=client_status,
            is_dependent=is_dependent,
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
            is_waitlist=is_waitlist,
            billing=billing,
            sponsor_id=sponsor_id,
            allergies=allergies,
            medical_history=medical_history,
            current_medications=current_medications,
            chronic_conditions=chronic_conditions,
            blood_type=blood_type,
            genotype=genotype,
            family_history=family_history,
            smoking_status=smoking_status,
            alcohol_use=alcohol_use,
            recreational_drug_use=recreational_drug_use,
            physical_activity=physical_activity,
            living_arrangement=living_arrangement,
            has_profile_image=has_profile_image,
            profile_image_path=profile_image_path,
            status=status,
            is_vip=is_vip,
            primary_location_id=primary_location_id,
            portal_access_enabled=portal_access_enabled,
            admission_status=admission_status,
            couple=couple,
            emails=emails,
            phones=phones,
            guardians=guardians,
            insurance=insurance,
            pharmacies=pharmacies,
            care_providers=care_providers,
            notification_settings=notification_settings,
            created_at=created_at,
            updated_at=updated_at,
        )

        patient.additional_properties = d
        return patient

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
