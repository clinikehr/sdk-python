from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.allergy_create_substance_code_system import AllergyCreateSubstanceCodeSystem

T = TypeVar("T", bound="AllergyCreateSubstanceCode")


@_attrs_define
class AllergyCreateSubstanceCode:
    """
    Attributes:
        system (AllergyCreateSubstanceCodeSystem):
        code (str):
    """

    system: AllergyCreateSubstanceCodeSystem
    code: str

    def to_dict(self) -> dict[str, Any]:
        system = self.system.value

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "system": system,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system = AllergyCreateSubstanceCodeSystem(d.pop("system"))

        code = d.pop("code")

        allergy_create_substance_code = cls(
            system=system,
            code=code,
        )

        return allergy_create_substance_code
