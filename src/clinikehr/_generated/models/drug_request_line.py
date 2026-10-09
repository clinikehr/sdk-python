from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.drug_request_line_code_system_type_1 import DrugRequestLineCodeSystemType1
from ..models.drug_request_line_code_system_type_2_type_1 import DrugRequestLineCodeSystemType2Type1
from ..models.drug_request_line_code_system_type_3_type_1 import DrugRequestLineCodeSystemType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="DrugRequestLine")


@_attrs_define
class DrugRequestLine:
    """Present ONLY on GET — create/list/cancel/confirm_substitution do not return lines.

    Attributes:
        id (None | Unset | UUID):
        line_no (int | None | Unset):
        code_system (DrugRequestLineCodeSystemType1 | DrugRequestLineCodeSystemType2Type1 |
            DrugRequestLineCodeSystemType3Type1 | None | Unset):
        code_value (None | str | Unset):
        description (None | str | Unset):
        quantity (None | str | Unset):
        directions (None | str | Unset):
        matched_inventory_item_id (None | Unset | UUID):
        matched_medicine_index_id (None | Unset | UUID):
        line_status (None | str | Unset):
        substituted_item_id (None | Unset | UUID):
        substitution_reason (None | str | Unset):
        decline_reason (None | str | Unset):
    """

    id: None | Unset | UUID = UNSET
    line_no: int | None | Unset = UNSET
    code_system: (
        DrugRequestLineCodeSystemType1
        | DrugRequestLineCodeSystemType2Type1
        | DrugRequestLineCodeSystemType3Type1
        | None
        | Unset
    ) = UNSET
    code_value: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    quantity: None | str | Unset = UNSET
    directions: None | str | Unset = UNSET
    matched_inventory_item_id: None | Unset | UUID = UNSET
    matched_medicine_index_id: None | Unset | UUID = UNSET
    line_status: None | str | Unset = UNSET
    substituted_item_id: None | Unset | UUID = UNSET
    substitution_reason: None | str | Unset = UNSET
    decline_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        line_no: int | None | Unset
        if isinstance(self.line_no, Unset):
            line_no = UNSET
        else:
            line_no = self.line_no

        code_system: None | str | Unset
        if isinstance(self.code_system, Unset):
            code_system = UNSET
        elif isinstance(self.code_system, DrugRequestLineCodeSystemType1):
            code_system = self.code_system.value
        elif isinstance(self.code_system, DrugRequestLineCodeSystemType2Type1):
            code_system = self.code_system.value
        elif isinstance(self.code_system, DrugRequestLineCodeSystemType3Type1):
            code_system = self.code_system.value
        else:
            code_system = self.code_system

        code_value: None | str | Unset
        if isinstance(self.code_value, Unset):
            code_value = UNSET
        else:
            code_value = self.code_value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        quantity: None | str | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        directions: None | str | Unset
        if isinstance(self.directions, Unset):
            directions = UNSET
        else:
            directions = self.directions

        matched_inventory_item_id: None | str | Unset
        if isinstance(self.matched_inventory_item_id, Unset):
            matched_inventory_item_id = UNSET
        elif isinstance(self.matched_inventory_item_id, UUID):
            matched_inventory_item_id = str(self.matched_inventory_item_id)
        else:
            matched_inventory_item_id = self.matched_inventory_item_id

        matched_medicine_index_id: None | str | Unset
        if isinstance(self.matched_medicine_index_id, Unset):
            matched_medicine_index_id = UNSET
        elif isinstance(self.matched_medicine_index_id, UUID):
            matched_medicine_index_id = str(self.matched_medicine_index_id)
        else:
            matched_medicine_index_id = self.matched_medicine_index_id

        line_status: None | str | Unset
        if isinstance(self.line_status, Unset):
            line_status = UNSET
        else:
            line_status = self.line_status

        substituted_item_id: None | str | Unset
        if isinstance(self.substituted_item_id, Unset):
            substituted_item_id = UNSET
        elif isinstance(self.substituted_item_id, UUID):
            substituted_item_id = str(self.substituted_item_id)
        else:
            substituted_item_id = self.substituted_item_id

        substitution_reason: None | str | Unset
        if isinstance(self.substitution_reason, Unset):
            substitution_reason = UNSET
        else:
            substitution_reason = self.substitution_reason

        decline_reason: None | str | Unset
        if isinstance(self.decline_reason, Unset):
            decline_reason = UNSET
        else:
            decline_reason = self.decline_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if line_no is not UNSET:
            field_dict["line_no"] = line_no
        if code_system is not UNSET:
            field_dict["code_system"] = code_system
        if code_value is not UNSET:
            field_dict["code_value"] = code_value
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if directions is not UNSET:
            field_dict["directions"] = directions
        if matched_inventory_item_id is not UNSET:
            field_dict["matched_inventory_item_id"] = matched_inventory_item_id
        if matched_medicine_index_id is not UNSET:
            field_dict["matched_medicine_index_id"] = matched_medicine_index_id
        if line_status is not UNSET:
            field_dict["line_status"] = line_status
        if substituted_item_id is not UNSET:
            field_dict["substituted_item_id"] = substituted_item_id
        if substitution_reason is not UNSET:
            field_dict["substitution_reason"] = substitution_reason
        if decline_reason is not UNSET:
            field_dict["decline_reason"] = decline_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_line_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_no = _parse_line_no(d.pop("line_no", UNSET))

        def _parse_code_system(
            data: object,
        ) -> (
            DrugRequestLineCodeSystemType1
            | DrugRequestLineCodeSystemType2Type1
            | DrugRequestLineCodeSystemType3Type1
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
                code_system_type_1 = DrugRequestLineCodeSystemType1(data)

                return code_system_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                code_system_type_2_type_1 = DrugRequestLineCodeSystemType2Type1(data)

                return code_system_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                code_system_type_3_type_1 = DrugRequestLineCodeSystemType3Type1(data)

                return code_system_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DrugRequestLineCodeSystemType1
                | DrugRequestLineCodeSystemType2Type1
                | DrugRequestLineCodeSystemType3Type1
                | None
                | Unset,
                data,
            )

        code_system = _parse_code_system(d.pop("code_system", UNSET))

        def _parse_code_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_value = _parse_code_value(d.pop("code_value", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_quantity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_directions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directions = _parse_directions(d.pop("directions", UNSET))

        def _parse_matched_inventory_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                matched_inventory_item_id_type_0 = UUID(data)

                return matched_inventory_item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        matched_inventory_item_id = _parse_matched_inventory_item_id(d.pop("matched_inventory_item_id", UNSET))

        def _parse_matched_medicine_index_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                matched_medicine_index_id_type_0 = UUID(data)

                return matched_medicine_index_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        matched_medicine_index_id = _parse_matched_medicine_index_id(d.pop("matched_medicine_index_id", UNSET))

        def _parse_line_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line_status = _parse_line_status(d.pop("line_status", UNSET))

        def _parse_substituted_item_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                substituted_item_id_type_0 = UUID(data)

                return substituted_item_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        substituted_item_id = _parse_substituted_item_id(d.pop("substituted_item_id", UNSET))

        def _parse_substitution_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        substitution_reason = _parse_substitution_reason(d.pop("substitution_reason", UNSET))

        def _parse_decline_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decline_reason = _parse_decline_reason(d.pop("decline_reason", UNSET))

        drug_request_line = cls(
            id=id,
            line_no=line_no,
            code_system=code_system,
            code_value=code_value,
            description=description,
            quantity=quantity,
            directions=directions,
            matched_inventory_item_id=matched_inventory_item_id,
            matched_medicine_index_id=matched_medicine_index_id,
            line_status=line_status,
            substituted_item_id=substituted_item_id,
            substitution_reason=substitution_reason,
            decline_reason=decline_reason,
        )

        drug_request_line.additional_properties = d
        return drug_request_line

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
