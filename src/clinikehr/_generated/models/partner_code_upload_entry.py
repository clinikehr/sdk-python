from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerCodeUploadEntry")


@_attrs_define
class PartnerCodeUploadEntry:
    """
    Attributes:
        code (str):
        barcode (str | Unset):
        nafdac_no (str | Unset):
        ndc (str | Unset):
        rxcui (str | Unset):
        name (str | Unset):
        strength (str | Unset):
        form (str | Unset):
        pack_size (str | Unset):
    """

    code: str
    barcode: str | Unset = UNSET
    nafdac_no: str | Unset = UNSET
    ndc: str | Unset = UNSET
    rxcui: str | Unset = UNSET
    name: str | Unset = UNSET
    strength: str | Unset = UNSET
    form: str | Unset = UNSET
    pack_size: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        barcode = self.barcode

        nafdac_no = self.nafdac_no

        ndc = self.ndc

        rxcui = self.rxcui

        name = self.name

        strength = self.strength

        form = self.form

        pack_size = self.pack_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        barcode = d.pop("barcode", UNSET)

        nafdac_no = d.pop("nafdac_no", UNSET)

        ndc = d.pop("ndc", UNSET)

        rxcui = d.pop("rxcui", UNSET)

        name = d.pop("name", UNSET)

        strength = d.pop("strength", UNSET)

        form = d.pop("form", UNSET)

        pack_size = d.pop("pack_size", UNSET)

        partner_code_upload_entry = cls(
            code=code,
            barcode=barcode,
            nafdac_no=nafdac_no,
            ndc=ndc,
            rxcui=rxcui,
            name=name,
            strength=strength,
            form=form,
            pack_size=pack_size,
        )

        partner_code_upload_entry.additional_properties = d
        return partner_code_upload_entry

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
