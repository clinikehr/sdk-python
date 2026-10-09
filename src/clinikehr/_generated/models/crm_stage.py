from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmStage")


@_attrs_define
class CrmStage:
    """
    Attributes:
        id (UUID | Unset):
        name (None | str | Unset):
        sort_order (int | None | Unset):
        is_won (bool | None | Unset):
        is_lost (bool | None | Unset):
        probability (int | None | Unset):
        color (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    is_won: bool | None | Unset = UNSET
    is_lost: bool | None | Unset = UNSET
    probability: int | None | Unset = UNSET
    color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        is_won: bool | None | Unset
        if isinstance(self.is_won, Unset):
            is_won = UNSET
        else:
            is_won = self.is_won

        is_lost: bool | None | Unset
        if isinstance(self.is_lost, Unset):
            is_lost = UNSET
        else:
            is_lost = self.is_lost

        probability: int | None | Unset
        if isinstance(self.probability, Unset):
            probability = UNSET
        else:
            probability = self.probability

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if is_won is not UNSET:
            field_dict["is_won"] = is_won
        if is_lost is not UNSET:
            field_dict["is_lost"] = is_lost
        if probability is not UNSET:
            field_dict["probability"] = probability
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        def _parse_is_won(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_won = _parse_is_won(d.pop("is_won", UNSET))

        def _parse_is_lost(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_lost = _parse_is_lost(d.pop("is_lost", UNSET))

        def _parse_probability(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        probability = _parse_probability(d.pop("probability", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        crm_stage = cls(
            id=id,
            name=name,
            sort_order=sort_order,
            is_won=is_won,
            is_lost=is_lost,
            probability=probability,
            color=color,
        )

        crm_stage.additional_properties = d
        return crm_stage

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
