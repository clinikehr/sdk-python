from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allergy_create_substance_code import AllergyCreateSubstanceCode


T = TypeVar("T", bound="AllergyCreateSubstance")


@_attrs_define
class AllergyCreateSubstance:
    """
    Attributes:
        text (str):
        code (AllergyCreateSubstanceCode | Unset):
    """

    text: str
    code: AllergyCreateSubstanceCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allergy_create_substance_code import AllergyCreateSubstanceCode  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        _code = d.pop("code", UNSET)
        code: AllergyCreateSubstanceCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = AllergyCreateSubstanceCode.from_dict(_code)

        allergy_create_substance = cls(
            text=text,
            code=code,
        )

        return allergy_create_substance
