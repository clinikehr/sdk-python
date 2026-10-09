from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.allergy_update_category_item import AllergyUpdateCategoryItem
from ..models.allergy_update_clinical_status import AllergyUpdateClinicalStatus
from ..models.allergy_update_criticality import AllergyUpdateCriticality
from ..models.allergy_update_type import AllergyUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allergy_reaction import AllergyReaction


T = TypeVar("T", bound="AllergyUpdate")


@_attrs_define
class AllergyUpdate:
    """A proposed change to an existing allergy. It becomes a NEW pending submission; the allergy itself does not change
    until a clinician confirms it. The substance can never be changed (a different substance is a new allergy).
    `clinical_status: entered_in_error` proposes retracting the allergy and cannot be combined with other changes.

        Attributes:
            clinical_status (AllergyUpdateClinicalStatus | Unset):
            criticality (AllergyUpdateCriticality | Unset):
            category (list[AllergyUpdateCategoryItem] | Unset):
            type_ (AllergyUpdateType | Unset):
            reactions (list[AllergyReaction] | Unset):
            onset_date (datetime.date | Unset):
            note (str | Unset):
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    clinical_status: AllergyUpdateClinicalStatus | Unset = UNSET
    criticality: AllergyUpdateCriticality | Unset = UNSET
    category: list[AllergyUpdateCategoryItem] | Unset = UNSET
    type_: AllergyUpdateType | Unset = UNSET
    reactions: list[AllergyReaction] | Unset = UNSET
    onset_date: datetime.date | Unset = UNSET
    note: str | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        clinical_status: str | Unset = UNSET
        if not isinstance(self.clinical_status, Unset):
            clinical_status = self.clinical_status.value

        criticality: str | Unset = UNSET
        if not isinstance(self.criticality, Unset):
            criticality = self.criticality.value

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        field_dict.update({})
        if clinical_status is not UNSET:
            field_dict["clinical_status"] = clinical_status
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if category is not UNSET:
            field_dict["category"] = category
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from ..models.allergy_reaction import AllergyReaction  # noqa: PLC0415

        d = dict(src_dict)
        _clinical_status = d.pop("clinical_status", UNSET)
        clinical_status: AllergyUpdateClinicalStatus | Unset
        if isinstance(_clinical_status, Unset):
            clinical_status = UNSET
        else:
            clinical_status = AllergyUpdateClinicalStatus(_clinical_status)

        _criticality = d.pop("criticality", UNSET)
        criticality: AllergyUpdateCriticality | Unset
        if isinstance(_criticality, Unset):
            criticality = UNSET
        else:
            criticality = AllergyUpdateCriticality(_criticality)

        _category = d.pop("category", UNSET)
        category: list[AllergyUpdateCategoryItem] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = AllergyUpdateCategoryItem(category_item_data)

                category.append(category_item)

        _type_ = d.pop("type", UNSET)
        type_: AllergyUpdateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AllergyUpdateType(_type_)

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

        allergy_update = cls(
            clinical_status=clinical_status,
            criticality=criticality,
            category=category,
            type_=type_,
            reactions=reactions,
            onset_date=onset_date,
            note=note,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return allergy_update
