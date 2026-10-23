from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickupLine")


@_attrs_define
class PickupLine:
    """One line of a pickup. `line_id` is the line's own selector and is always set: send it in `line_ids` to hand over
    only this line. Of `prescription_id` / `pos_sale_item_id` exactly one is set: a full-edition in-house pharmacy's
    pickup lines carry `prescription_id` (and then `line_id` equals it); a Pharmacy-edition till sale's pickup lines
    carry `pos_sale_item_id` instead (the sale's own line) and `prescription_id` is null. A till line's `line_id` is NOT
    a prescription id and matches nothing in the prescriptions API.

        Attributes:
            line_id (UUID): The selector for this line: what `line_ids` accepts on the collection request. For a
                prescription line it equals `prescription_id`; for a till line it is the line's own id.
            prescription_id (None | Unset | UUID): The prescription this line hands over; null for a till line.
            pos_sale_item_id (None | Unset | UUID): The till sale's own line; null for a prescription line.
    """

    line_id: UUID
    prescription_id: None | Unset | UUID = UNSET
    pos_sale_item_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_id = str(self.line_id)

        prescription_id: None | str | Unset
        if isinstance(self.prescription_id, Unset):
            prescription_id = UNSET
        elif isinstance(self.prescription_id, UUID):
            prescription_id = str(self.prescription_id)
        else:
            prescription_id = self.prescription_id

        pos_sale_item_id: None | str | Unset
        if isinstance(self.pos_sale_item_id, Unset):
            pos_sale_item_id = UNSET
        elif isinstance(self.pos_sale_item_id, UUID):
            pos_sale_item_id = str(self.pos_sale_item_id)
        else:
            pos_sale_item_id = self.pos_sale_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_id": line_id,
            }
        )
        if prescription_id is not UNSET:
            field_dict["prescription_id"] = prescription_id
        if pos_sale_item_id is not UNSET:
            field_dict["pos_sale_item_id"] = pos_sale_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_id = UUID(d.pop("line_id"))

        def _parse_prescription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prescription_id_type_0 = UUID(data)

                return prescription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        prescription_id = _parse_prescription_id(d.pop("prescription_id", UNSET))

        def _parse_pos_sale_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pos_sale_item_id_type_0 = UUID(data)

                return pos_sale_item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pos_sale_item_id = _parse_pos_sale_item_id(d.pop("pos_sale_item_id", UNSET))

        pickup_line = cls(
            line_id=line_id,
            prescription_id=prescription_id,
            pos_sale_item_id=pos_sale_item_id,
        )

        pickup_line.additional_properties = d
        return pickup_line

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
