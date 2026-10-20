from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_stock_batch_row_band_type_1 import ExternalStockBatchRowBandType1
from ..models.external_stock_batch_row_band_type_2_type_1 import ExternalStockBatchRowBandType2Type1
from ..models.external_stock_batch_row_band_type_3_type_1 import ExternalStockBatchRowBandType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier import Identifier


T = TypeVar("T", bound="ExternalStockBatchRow")


@_attrs_define
class ExternalStockBatchRow:
    """One product in a stock report. Send at least one identifier and at least one of `quantity` and `band`. A batch with
    any row that breaks these rules is rejected whole (`rejected_reason: invalid_rows`) and nothing is written.

        Attributes:
            identifiers (list[Identifier]):
            quantity (float | None | Unset):
            band (ExternalStockBatchRowBandType1 | ExternalStockBatchRowBandType2Type1 | ExternalStockBatchRowBandType3Type1
                | None | Unset):
    """

    identifiers: list[Identifier]
    quantity: float | None | Unset = UNSET
    band: (
        ExternalStockBatchRowBandType1
        | ExternalStockBatchRowBandType2Type1
        | ExternalStockBatchRowBandType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.to_dict()
            identifiers.append(identifiers_item)

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        band: None | str | Unset
        if isinstance(self.band, Unset):
            band = UNSET
        elif isinstance(self.band, ExternalStockBatchRowBandType1):
            band = self.band.value
        elif isinstance(self.band, ExternalStockBatchRowBandType2Type1):
            band = self.band.value
        elif isinstance(self.band, ExternalStockBatchRowBandType3Type1):
            band = self.band.value
        else:
            band = self.band

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifiers": identifiers,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if band is not UNSET:
            field_dict["band"] = band

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identifier import Identifier  # noqa: PLC0415

        d = dict(src_dict)
        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = Identifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_band(
            data: object,
        ) -> (
            ExternalStockBatchRowBandType1
            | ExternalStockBatchRowBandType2Type1
            | ExternalStockBatchRowBandType3Type1
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
                band_type_1 = ExternalStockBatchRowBandType1(data)

                return band_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_2_type_1 = ExternalStockBatchRowBandType2Type1(data)

                return band_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                band_type_3_type_1 = ExternalStockBatchRowBandType3Type1(data)

                return band_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ExternalStockBatchRowBandType1
                | ExternalStockBatchRowBandType2Type1
                | ExternalStockBatchRowBandType3Type1
                | None
                | Unset,
                data,
            )

        band = _parse_band(d.pop("band", UNSET))

        external_stock_batch_row = cls(
            identifiers=identifiers,
            quantity=quantity,
            band=band,
        )

        external_stock_batch_row.additional_properties = d
        return external_stock_batch_row

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
