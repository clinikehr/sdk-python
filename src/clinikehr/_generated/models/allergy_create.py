from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.allergy_create_category_item import AllergyCreateCategoryItem
from ..models.allergy_create_clinical_status import AllergyCreateClinicalStatus
from ..models.allergy_create_criticality import AllergyCreateCriticality
from ..models.allergy_create_type import AllergyCreateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allergy_create_substance import AllergyCreateSubstance
    from ..models.allergy_reaction import AllergyReaction


T = TypeVar("T", bound="AllergyCreate")


@_attrs_define
class AllergyCreate:
    """An outside allergy, or a "no known allergies" statement, submitted for a clinician to confirm. It does not enter the
    chart until then. To record that the patient has no known allergies, send `no_known_allergies: true` INSTEAD of a
    substance (the two cannot be combined); it is also held for a clinician to confirm. Sending `none` or similar as a
    substance is refused. `client_reference` (your own id, up to 200 characters) makes a second submission of the same
    record with different content a `client_reference_conflict`. An allergy the patient already has is not refused: it
    is held for a clinician like any other.

        Attributes:
            patient_id (UUID):
            substance (AllergyCreateSubstance | Unset):
            no_known_allergies (bool | Unset): Record that the patient has no known allergies. Send this INSTEAD of
                `substance`; one of the two is required and they cannot be combined.
            category (list[AllergyCreateCategoryItem] | Unset):
            criticality (AllergyCreateCriticality | Unset):
            type_ (AllergyCreateType | Unset):  Default: AllergyCreateType.ALLERGY.
            clinical_status (AllergyCreateClinicalStatus | Unset):  Default: AllergyCreateClinicalStatus.ACTIVE.
            reactions (list[AllergyReaction] | Unset):
            onset_date (datetime.date | Unset):
            note (str | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    patient_id: UUID
    substance: AllergyCreateSubstance | Unset = UNSET
    no_known_allergies: bool | Unset = UNSET
    category: list[AllergyCreateCategoryItem] | Unset = UNSET
    criticality: AllergyCreateCriticality | Unset = UNSET
    type_: AllergyCreateType | Unset = AllergyCreateType.ALLERGY
    clinical_status: AllergyCreateClinicalStatus | Unset = AllergyCreateClinicalStatus.ACTIVE
    reactions: list[AllergyReaction] | Unset = UNSET
    onset_date: datetime.date | Unset = UNSET
    note: str | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        patient_id = str(self.patient_id)

        substance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.substance, Unset):
            substance = self.substance.to_dict()

        no_known_allergies = self.no_known_allergies

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        criticality: str | Unset = UNSET
        if not isinstance(self.criticality, Unset):
            criticality = self.criticality.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        clinical_status: str | Unset = UNSET
        if not isinstance(self.clinical_status, Unset):
            clinical_status = self.clinical_status.value

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)

        onset_date: str | Unset = UNSET
        if not isinstance(self.onset_date, Unset):
            onset_date = self.onset_date.isoformat()

        note = self.note

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "patient_id": patient_id,
            }
        )
        if substance is not UNSET:
            field_dict["substance"] = substance
        if no_known_allergies is not UNSET:
            field_dict["no_known_allergies"] = no_known_allergies
        if category is not UNSET:
            field_dict["category"] = category
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if type_ is not UNSET:
            field_dict["type"] = type_
        if clinical_status is not UNSET:
            field_dict["clinical_status"] = clinical_status
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if onset_date is not UNSET:
            field_dict["onset_date"] = onset_date
        if note is not UNSET:
            field_dict["note"] = note
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allergy_create_substance import AllergyCreateSubstance  # noqa: PLC0415
        from ..models.allergy_reaction import AllergyReaction  # noqa: PLC0415

        d = dict(src_dict)
        patient_id = UUID(d.pop("patient_id"))

        _substance = d.pop("substance", UNSET)
        substance: AllergyCreateSubstance | Unset
        if isinstance(_substance, Unset):
            substance = UNSET
        else:
            substance = AllergyCreateSubstance.from_dict(_substance)

        no_known_allergies = d.pop("no_known_allergies", UNSET)

        _category = d.pop("category", UNSET)
        category: list[AllergyCreateCategoryItem] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = AllergyCreateCategoryItem(category_item_data)

                category.append(category_item)

        _criticality = d.pop("criticality", UNSET)
        criticality: AllergyCreateCriticality | Unset
        if isinstance(_criticality, Unset):
            criticality = UNSET
        else:
            criticality = AllergyCreateCriticality(_criticality)

        _type_ = d.pop("type", UNSET)
        type_: AllergyCreateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AllergyCreateType(_type_)

        _clinical_status = d.pop("clinical_status", UNSET)
        clinical_status: AllergyCreateClinicalStatus | Unset
        if isinstance(_clinical_status, Unset):
            clinical_status = UNSET
        else:
            clinical_status = AllergyCreateClinicalStatus(_clinical_status)

        _reactions = d.pop("reactions", UNSET)
        reactions: list[AllergyReaction] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = AllergyReaction.from_dict(reactions_item_data)

                reactions.append(reactions_item)

        _onset_date = d.pop("onset_date", UNSET)
        onset_date: datetime.date | Unset
        if isinstance(_onset_date, Unset):
            onset_date = UNSET
        else:
            onset_date = datetime.date.fromisoformat(_onset_date)

        note = d.pop("note", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        allergy_create = cls(
            patient_id=patient_id,
            substance=substance,
            no_known_allergies=no_known_allergies,
            category=category,
            criticality=criticality,
            type_=type_,
            clinical_status=clinical_status,
            reactions=reactions,
            onset_date=onset_date,
            note=note,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return allergy_create
