from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.coverage_subscriber_gender_type_1 import CoverageSubscriberGenderType1
from ..models.coverage_subscriber_gender_type_2_type_1 import CoverageSubscriberGenderType2Type1
from ..models.coverage_subscriber_gender_type_3_type_1 import CoverageSubscriberGenderType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageSubscriber")


@_attrs_define
class CoverageSubscriber:
    """The policy holder. Their address is not exposed.

    Attributes:
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        date_of_birth (datetime.date | None | Unset):
        gender (CoverageSubscriberGenderType1 | CoverageSubscriberGenderType2Type1 | CoverageSubscriberGenderType3Type1
            | None | Unset):
        member_id (None | str | Unset):
    """

    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: (
        CoverageSubscriberGenderType1
        | CoverageSubscriberGenderType2Type1
        | CoverageSubscriberGenderType3Type1
        | None
        | Unset
    ) = UNSET
    member_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        elif isinstance(self.gender, CoverageSubscriberGenderType1):
            gender = self.gender.value
        elif isinstance(self.gender, CoverageSubscriberGenderType2Type1):
            gender = self.gender.value
        elif isinstance(self.gender, CoverageSubscriberGenderType3Type1):
            gender = self.gender.value
        else:
            gender = self.gender

        member_id: None | str | Unset
        if isinstance(self.member_id, Unset):
            member_id = UNSET
        else:
            member_id = self.member_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if member_id is not UNSET:
            field_dict["member_id"] = member_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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
            CoverageSubscriberGenderType1
            | CoverageSubscriberGenderType2Type1
            | CoverageSubscriberGenderType3Type1
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
                gender_type_1 = CoverageSubscriberGenderType1(data)

                return gender_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_2_type_1 = CoverageSubscriberGenderType2Type1(data)

                return gender_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_3_type_1 = CoverageSubscriberGenderType3Type1(data)

                return gender_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CoverageSubscriberGenderType1
                | CoverageSubscriberGenderType2Type1
                | CoverageSubscriberGenderType3Type1
                | None
                | Unset,
                data,
            )

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_member_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_id = _parse_member_id(d.pop("member_id", UNSET))

        coverage_subscriber = cls(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            member_id=member_id,
        )

        coverage_subscriber.additional_properties = d
        return coverage_subscriber

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
