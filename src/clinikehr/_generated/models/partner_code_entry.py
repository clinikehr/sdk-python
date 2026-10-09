from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partner_code_entry_state import PartnerCodeEntryState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerCodeEntry")


@_attrs_define
class PartnerCodeEntry:
    """
    Attributes:
        id (UUID):
        state (PartnerCodeEntryState):
        code (None | str | Unset):
        barcode (None | str | Unset):
        nafdac_no (None | str | Unset):
        ndc (None | str | Unset):
        rxcui (None | str | Unset):
        name (None | str | Unset):
        strength (None | str | Unset):
        form (None | str | Unset):
        pack_size (None | str | Unset):
        resolved_medicine_index_id (None | Unset | UUID):
        candidate_medicine_index_ids (list[UUID] | Unset):
        review_reason (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    state: PartnerCodeEntryState
    code: None | str | Unset = UNSET
    barcode: None | str | Unset = UNSET
    nafdac_no: None | str | Unset = UNSET
    ndc: None | str | Unset = UNSET
    rxcui: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    strength: None | str | Unset = UNSET
    form: None | str | Unset = UNSET
    pack_size: None | str | Unset = UNSET
    resolved_medicine_index_id: None | Unset | UUID = UNSET
    candidate_medicine_index_ids: list[UUID] | Unset = UNSET
    review_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        state = self.state.value

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        nafdac_no: None | str | Unset
        if isinstance(self.nafdac_no, Unset):
            nafdac_no = UNSET
        else:
            nafdac_no = self.nafdac_no

        ndc: None | str | Unset
        if isinstance(self.ndc, Unset):
            ndc = UNSET
        else:
            ndc = self.ndc

        rxcui: None | str | Unset
        if isinstance(self.rxcui, Unset):
            rxcui = UNSET
        else:
            rxcui = self.rxcui

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        strength: None | str | Unset
        if isinstance(self.strength, Unset):
            strength = UNSET
        else:
            strength = self.strength

        form: None | str | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        else:
            form = self.form

        pack_size: None | str | Unset
        if isinstance(self.pack_size, Unset):
            pack_size = UNSET
        else:
            pack_size = self.pack_size

        resolved_medicine_index_id: None | str | Unset
        if isinstance(self.resolved_medicine_index_id, Unset):
            resolved_medicine_index_id = UNSET
        elif isinstance(self.resolved_medicine_index_id, UUID):
            resolved_medicine_index_id = str(self.resolved_medicine_index_id)
        else:
            resolved_medicine_index_id = self.resolved_medicine_index_id

        candidate_medicine_index_ids: list[str] | Unset = UNSET
        if not isinstance(self.candidate_medicine_index_ids, Unset):
            candidate_medicine_index_ids = []
            for candidate_medicine_index_ids_item_data in self.candidate_medicine_index_ids:
                candidate_medicine_index_ids_item = str(candidate_medicine_index_ids_item_data)
                candidate_medicine_index_ids.append(candidate_medicine_index_ids_item)

        review_reason: None | str | Unset
        if isinstance(self.review_reason, Unset):
            review_reason = UNSET
        else:
            review_reason = self.review_reason

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "state": state,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if nafdac_no is not UNSET:
            field_dict["nafdac_no"] = nafdac_no
        if ndc is not UNSET:
            field_dict["ndc"] = ndc
        if rxcui is not UNSET:
            field_dict["rxcui"] = rxcui
        if name is not UNSET:
            field_dict["name"] = name
        if strength is not UNSET:
            field_dict["strength"] = strength
        if form is not UNSET:
            field_dict["form"] = form
        if pack_size is not UNSET:
            field_dict["pack_size"] = pack_size
        if resolved_medicine_index_id is not UNSET:
            field_dict["resolved_medicine_index_id"] = resolved_medicine_index_id
        if candidate_medicine_index_ids is not UNSET:
            field_dict["candidate_medicine_index_ids"] = candidate_medicine_index_ids
        if review_reason is not UNSET:
            field_dict["review_reason"] = review_reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        state = PartnerCodeEntryState(d.pop("state"))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))

        def _parse_nafdac_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nafdac_no = _parse_nafdac_no(d.pop("nafdac_no", UNSET))

        def _parse_ndc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ndc = _parse_ndc(d.pop("ndc", UNSET))

        def _parse_rxcui(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rxcui = _parse_rxcui(d.pop("rxcui", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_strength(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strength = _parse_strength(d.pop("strength", UNSET))

        def _parse_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        def _parse_pack_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pack_size = _parse_pack_size(d.pop("pack_size", UNSET))

        def _parse_resolved_medicine_index_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_medicine_index_id_type_0 = UUID(data)

                return resolved_medicine_index_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resolved_medicine_index_id = _parse_resolved_medicine_index_id(d.pop("resolved_medicine_index_id", UNSET))

        _candidate_medicine_index_ids = d.pop("candidate_medicine_index_ids", UNSET)
        candidate_medicine_index_ids: list[UUID] | Unset = UNSET
        if _candidate_medicine_index_ids is not UNSET:
            candidate_medicine_index_ids = []
            for candidate_medicine_index_ids_item_data in _candidate_medicine_index_ids:
                candidate_medicine_index_ids_item = UUID(candidate_medicine_index_ids_item_data)

                candidate_medicine_index_ids.append(candidate_medicine_index_ids_item)

        def _parse_review_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_reason = _parse_review_reason(d.pop("review_reason", UNSET))

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

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        partner_code_entry = cls(
            id=id,
            state=state,
            code=code,
            barcode=barcode,
            nafdac_no=nafdac_no,
            ndc=ndc,
            rxcui=rxcui,
            name=name,
            strength=strength,
            form=form,
            pack_size=pack_size,
            resolved_medicine_index_id=resolved_medicine_index_id,
            candidate_medicine_index_ids=candidate_medicine_index_ids,
            review_reason=review_reason,
            created_at=created_at,
            updated_at=updated_at,
        )

        partner_code_entry.additional_properties = d
        return partner_code_entry

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
