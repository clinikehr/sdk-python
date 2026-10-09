from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_duplicate_flag_status import PatientDuplicateFlagStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientDuplicateFlag")


@_attrs_define
class PatientDuplicateFlag:
    """
    Attributes:
        id (UUID):
        clinic_patient_id (UUID):
        candidate_clinic_patient_id (UUID):
        status (PatientDuplicateFlagStatus):
        similarity (float | None | Unset):
        source (None | str | Unset):
        decided_by_staff_id (None | Unset | UUID):
        decided_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    clinic_patient_id: UUID
    candidate_clinic_patient_id: UUID
    status: PatientDuplicateFlagStatus
    similarity: float | None | Unset = UNSET
    source: None | str | Unset = UNSET
    decided_by_staff_id: None | Unset | UUID = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        clinic_patient_id = str(self.clinic_patient_id)

        candidate_clinic_patient_id = str(self.candidate_clinic_patient_id)

        status = self.status.value

        similarity: float | None | Unset
        if isinstance(self.similarity, Unset):
            similarity = UNSET
        else:
            similarity = self.similarity

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        decided_by_staff_id: None | str | Unset
        if isinstance(self.decided_by_staff_id, Unset):
            decided_by_staff_id = UNSET
        elif isinstance(self.decided_by_staff_id, UUID):
            decided_by_staff_id = str(self.decided_by_staff_id)
        else:
            decided_by_staff_id = self.decided_by_staff_id

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clinic_patient_id": clinic_patient_id,
                "candidate_clinic_patient_id": candidate_clinic_patient_id,
                "status": status,
            }
        )
        if similarity is not UNSET:
            field_dict["similarity"] = similarity
        if source is not UNSET:
            field_dict["source"] = source
        if decided_by_staff_id is not UNSET:
            field_dict["decided_by_staff_id"] = decided_by_staff_id
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        clinic_patient_id = UUID(d.pop("clinic_patient_id"))

        candidate_clinic_patient_id = UUID(d.pop("candidate_clinic_patient_id"))

        status = PatientDuplicateFlagStatus(d.pop("status"))

        def _parse_similarity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        similarity = _parse_similarity(d.pop("similarity", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_decided_by_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_by_staff_id_type_0 = UUID(data)

                return decided_by_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        decided_by_staff_id = _parse_decided_by_staff_id(d.pop("decided_by_staff_id", UNSET))

        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)

                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decided_at", UNSET))

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

        patient_duplicate_flag = cls(
            id=id,
            clinic_patient_id=clinic_patient_id,
            candidate_clinic_patient_id=candidate_clinic_patient_id,
            status=status,
            similarity=similarity,
            source=source,
            decided_by_staff_id=decided_by_staff_id,
            decided_at=decided_at,
            created_at=created_at,
        )

        patient_duplicate_flag.additional_properties = d
        return patient_duplicate_flag

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
