from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allergy_substance_code import AllergySubstanceCode


T = TypeVar("T", bound="AllergySubstance")


@_attrs_define
class AllergySubstance:
    """
    Attributes:
        text (str):
        code (AllergySubstanceCode | None | Unset):
    """

    text: str
    code: AllergySubstanceCode | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.allergy_substance_code import AllergySubstanceCode  # noqa: PLC0415

        text = self.text

        code: dict[str, Any] | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, AllergySubstanceCode):
            code = self.code.to_dict()
        else:
            code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.allergy_substance_code import AllergySubstanceCode  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        def _parse_code(data: object) -> AllergySubstanceCode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                code_type_0 = AllergySubstanceCode.from_dict(data)

                return code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AllergySubstanceCode | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        allergy_substance = cls(
            text=text,
            code=code,
        )

        allergy_substance.additional_properties = d
        return allergy_substance

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
