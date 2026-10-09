from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medication_code import MedicationCode


T = TypeVar("T", bound="MedicationStatementMedication")


@_attrs_define
class MedicationStatementMedication:
    """
    Attributes:
        text (str): The medicine as the patient or the sender states it.
        code (MedicationCode | None | Unset):
    """

    text: str
    code: MedicationCode | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.medication_code import MedicationCode  # noqa: PLC0415

        text = self.text

        code: dict[str, Any] | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, MedicationCode):
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
        from ..models.medication_code import MedicationCode  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        def _parse_code(data: object) -> MedicationCode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                code_type_0 = MedicationCode.from_dict(data)

                return code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MedicationCode | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        medication_statement_medication = cls(
            text=text,
            code=code,
        )

        medication_statement_medication.additional_properties = d
        return medication_statement_medication

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
