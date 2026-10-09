from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicationStatementUpdateDosage")


@_attrs_define
class MedicationStatementUpdateDosage:
    """
    Attributes:
        text (str | Unset):
        route (str | Unset):
        frequency (str | Unset):
    """

    text: str | Unset = UNSET
    route: str | Unset = UNSET
    frequency: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        route = self.route

        frequency = self.frequency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if route is not UNSET:
            field_dict["route"] = route
        if frequency is not UNSET:
            field_dict["frequency"] = frequency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text", UNSET)

        route = d.pop("route", UNSET)

        frequency = d.pop("frequency", UNSET)

        medication_statement_update_dosage = cls(
            text=text,
            route=route,
            frequency=frequency,
        )

        return medication_statement_update_dosage
