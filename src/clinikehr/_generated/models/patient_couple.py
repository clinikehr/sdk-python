from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatientCouple")


@_attrs_define
class PatientCouple:
    """Read-only — a couple registration is a separate two-patient transaction this API does not perform.

    Attributes:
        partner_id (None | Unset | UUID):
        responsible_for_billing (bool | None | Unset):
        relationship_status (None | str | Unset):
    """

    partner_id: None | Unset | UUID = UNSET
    responsible_for_billing: bool | None | Unset = UNSET
    relationship_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_id: None | str | Unset
        if isinstance(self.partner_id, Unset):
            partner_id = UNSET
        elif isinstance(self.partner_id, UUID):
            partner_id = str(self.partner_id)
        else:
            partner_id = self.partner_id

        responsible_for_billing: bool | None | Unset
        if isinstance(self.responsible_for_billing, Unset):
            responsible_for_billing = UNSET
        else:
            responsible_for_billing = self.responsible_for_billing

        relationship_status: None | str | Unset
        if isinstance(self.relationship_status, Unset):
            relationship_status = UNSET
        else:
            relationship_status = self.relationship_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partner_id"] = partner_id
        if responsible_for_billing is not UNSET:
            field_dict["responsible_for_billing"] = responsible_for_billing
        if relationship_status is not UNSET:
            field_dict["relationship_status"] = relationship_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_partner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                partner_id_type_0 = UUID(data)

                return partner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        partner_id = _parse_partner_id(d.pop("partner_id", UNSET))

        def _parse_responsible_for_billing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        responsible_for_billing = _parse_responsible_for_billing(d.pop("responsible_for_billing", UNSET))

        def _parse_relationship_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_status = _parse_relationship_status(d.pop("relationship_status", UNSET))

        patient_couple = cls(
            partner_id=partner_id,
            responsible_for_billing=responsible_for_billing,
            relationship_status=relationship_status,
        )

        patient_couple.additional_properties = d
        return patient_couple

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
