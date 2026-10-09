from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_billing_group_type_type_1 import PatientBillingGroupTypeType1
from ..models.patient_billing_group_type_type_2_type_1 import PatientBillingGroupTypeType2Type1
from ..models.patient_billing_group_type_type_3_type_1 import PatientBillingGroupTypeType3Type1
from ..models.patient_billing_individual_type_type_1 import PatientBillingIndividualTypeType1
from ..models.patient_billing_individual_type_type_2_type_1 import PatientBillingIndividualTypeType2Type1
from ..models.patient_billing_individual_type_type_3_type_1 import PatientBillingIndividualTypeType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientBilling")


@_attrs_define
class PatientBilling:
    """
    Attributes:
        individual_type (None | PatientBillingIndividualTypeType1 | PatientBillingIndividualTypeType2Type1 |
            PatientBillingIndividualTypeType3Type1 | Unset):
        group_type (None | PatientBillingGroupTypeType1 | PatientBillingGroupTypeType2Type1 |
            PatientBillingGroupTypeType3Type1 | Unset):
    """

    individual_type: (
        None
        | PatientBillingIndividualTypeType1
        | PatientBillingIndividualTypeType2Type1
        | PatientBillingIndividualTypeType3Type1
        | Unset
    ) = UNSET
    group_type: (
        None
        | PatientBillingGroupTypeType1
        | PatientBillingGroupTypeType2Type1
        | PatientBillingGroupTypeType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        individual_type: None | str | Unset
        if isinstance(self.individual_type, Unset):
            individual_type = UNSET
        elif isinstance(self.individual_type, PatientBillingIndividualTypeType1):
            individual_type = self.individual_type.value
        elif isinstance(self.individual_type, PatientBillingIndividualTypeType2Type1):
            individual_type = self.individual_type.value
        elif isinstance(self.individual_type, PatientBillingIndividualTypeType3Type1):
            individual_type = self.individual_type.value
        else:
            individual_type = self.individual_type

        group_type: None | str | Unset
        if isinstance(self.group_type, Unset):
            group_type = UNSET
        elif isinstance(self.group_type, PatientBillingGroupTypeType1):
            group_type = self.group_type.value
        elif isinstance(self.group_type, PatientBillingGroupTypeType2Type1):
            group_type = self.group_type.value
        elif isinstance(self.group_type, PatientBillingGroupTypeType3Type1):
            group_type = self.group_type.value
        else:
            group_type = self.group_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual_type is not UNSET:
            field_dict["individual_type"] = individual_type
        if group_type is not UNSET:
            field_dict["group_type"] = group_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_individual_type(
            data: object,
        ) -> (
            None
            | PatientBillingIndividualTypeType1
            | PatientBillingIndividualTypeType2Type1
            | PatientBillingIndividualTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                individual_type_type_1 = PatientBillingIndividualTypeType1(data)

                return individual_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                individual_type_type_2_type_1 = PatientBillingIndividualTypeType2Type1(data)

                return individual_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                individual_type_type_3_type_1 = PatientBillingIndividualTypeType3Type1(data)

                return individual_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientBillingIndividualTypeType1
                | PatientBillingIndividualTypeType2Type1
                | PatientBillingIndividualTypeType3Type1
                | Unset,
                data,
            )

        individual_type = _parse_individual_type(d.pop("individual_type", UNSET))

        def _parse_group_type(
            data: object,
        ) -> (
            None
            | PatientBillingGroupTypeType1
            | PatientBillingGroupTypeType2Type1
            | PatientBillingGroupTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_type_type_1 = PatientBillingGroupTypeType1(data)

                return group_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_type_type_2_type_1 = PatientBillingGroupTypeType2Type1(data)

                return group_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_type_type_3_type_1 = PatientBillingGroupTypeType3Type1(data)

                return group_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatientBillingGroupTypeType1
                | PatientBillingGroupTypeType2Type1
                | PatientBillingGroupTypeType3Type1
                | Unset,
                data,
            )

        group_type = _parse_group_type(d.pop("group_type", UNSET))

        patient_billing = cls(
            individual_type=individual_type,
            group_type=group_type,
        )

        patient_billing.additional_properties = d
        return patient_billing

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
