from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dispensing_medicine import DispensingMedicine


T = TypeVar("T", bound="DispensingHistoryLine")


@_attrs_define
class DispensingHistoryLine:
    """
    Attributes:
        id (UUID):
        medicine (DispensingMedicine):
        quantity (float | None):
        days_supply (int | None | Unset):
        dispensed_at (datetime.datetime | None | Unset):
    """

    id: UUID
    medicine: DispensingMedicine
    quantity: float | None
    days_supply: int | None | Unset = UNSET
    dispensed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        medicine = self.medicine.to_dict()

        quantity: float | None
        quantity = self.quantity

        days_supply: int | None | Unset
        if isinstance(self.days_supply, Unset):
            days_supply = UNSET
        else:
            days_supply = self.days_supply

        dispensed_at: None | str | Unset
        if isinstance(self.dispensed_at, Unset):
            dispensed_at = UNSET
        elif isinstance(self.dispensed_at, datetime.datetime):
            dispensed_at = self.dispensed_at.isoformat()
        else:
            dispensed_at = self.dispensed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "medicine": medicine,
                "quantity": quantity,
            }
        )
        if days_supply is not UNSET:
            field_dict["days_supply"] = days_supply
        if dispensed_at is not UNSET:
            field_dict["dispensed_at"] = dispensed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dispensing_medicine import DispensingMedicine  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        medicine = DispensingMedicine.from_dict(d.pop("medicine"))

        def _parse_quantity(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        quantity = _parse_quantity(d.pop("quantity"))

        def _parse_days_supply(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_supply = _parse_days_supply(d.pop("days_supply", UNSET))

        def _parse_dispensed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispensed_at_type_0 = datetime.datetime.fromisoformat(data)

                return dispensed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dispensed_at = _parse_dispensed_at(d.pop("dispensed_at", UNSET))

        dispensing_history_line = cls(
            id=id,
            medicine=medicine,
            quantity=quantity,
            days_supply=days_supply,
            dispensed_at=dispensed_at,
        )

        dispensing_history_line.additional_properties = d
        return dispensing_history_line

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
