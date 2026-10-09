from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Payer")


@_attrs_define
class Payer:
    """An insurance payer this clinic has enabled in Settings → Insurance. A coverage can only point at one of these.
    Nothing about the clinic's enrollment or transaction setup is exposed.

        Attributes:
            id (UUID): Use this as `payer_id` when you create a coverage.
            display_name (str):
            primary_payer_id (None | str | Unset): The payer's own identifier in the payer network.
            coverage_types (list[str] | Unset):
            operating_states (list[str] | Unset):
    """

    id: UUID
    display_name: str
    primary_payer_id: None | str | Unset = UNSET
    coverage_types: list[str] | Unset = UNSET
    operating_states: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        display_name = self.display_name

        primary_payer_id: None | str | Unset
        if isinstance(self.primary_payer_id, Unset):
            primary_payer_id = UNSET
        else:
            primary_payer_id = self.primary_payer_id

        coverage_types: list[str] | Unset = UNSET
        if not isinstance(self.coverage_types, Unset):
            coverage_types = self.coverage_types

        operating_states: list[str] | Unset = UNSET
        if not isinstance(self.operating_states, Unset):
            operating_states = self.operating_states

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
            }
        )
        if primary_payer_id is not UNSET:
            field_dict["primary_payer_id"] = primary_payer_id
        if coverage_types is not UNSET:
            field_dict["coverage_types"] = coverage_types
        if operating_states is not UNSET:
            field_dict["operating_states"] = operating_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("display_name")

        def _parse_primary_payer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_payer_id = _parse_primary_payer_id(d.pop("primary_payer_id", UNSET))

        coverage_types = cast(list[str], d.pop("coverage_types", UNSET))

        operating_states = cast(list[str], d.pop("operating_states", UNSET))

        payer = cls(
            id=id,
            display_name=display_name,
            primary_payer_id=primary_payer_id,
            coverage_types=coverage_types,
            operating_states=operating_states,
        )

        payer.additional_properties = d
        return payer

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
