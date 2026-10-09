from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.patient_import_request_format import PatientImportRequestFormat

if TYPE_CHECKING:
    from ..models.patient_import_request_data_type_0_item import PatientImportRequestDataType0Item
    from ..models.patient_import_request_data_type_2 import PatientImportRequestDataType2


T = TypeVar("T", bound="PatientImportRequest")


@_attrs_define
class PatientImportRequest:
    """
    Attributes:
        format_ (PatientImportRequestFormat): How `data` is written.
        data (list[PatientImportRequestDataType0Item] | PatientImportRequestDataType2 | str): `json_array` — an array of
            patient objects in the same shape as `createPatient` (a row that carries `allergies`, `current_medications` or
            `chronic_conditions` is rejected by name like any other invalid row). `ndjson` — one string, a patient object
            per line. `fhir_bundle` — a FHIR Bundle whose entries include Patient resources (other resource types are
            ignored). At most 100 rows.
    """

    format_: PatientImportRequestFormat
    data: list[PatientImportRequestDataType0Item] | PatientImportRequestDataType2 | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.patient_import_request_data_type_2 import PatientImportRequestDataType2  # noqa: PLC0415

        format_ = self.format_.value

        data: dict[str, Any] | list[dict[str, Any]] | str
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        elif isinstance(self.data, PatientImportRequestDataType2):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "format": format_,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patient_import_request_data_type_0_item import PatientImportRequestDataType0Item  # noqa: PLC0415
        from ..models.patient_import_request_data_type_2 import PatientImportRequestDataType2  # noqa: PLC0415

        d = dict(src_dict)
        format_ = PatientImportRequestFormat(d.pop("format"))

        def _parse_data(data: object) -> list[PatientImportRequestDataType0Item] | PatientImportRequestDataType2 | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = PatientImportRequestDataType0Item.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = PatientImportRequestDataType2.from_dict(data)

                return data_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PatientImportRequestDataType0Item] | PatientImportRequestDataType2 | str, data)

        data = _parse_data(d.pop("data"))

        patient_import_request = cls(
            format_=format_,
            data=data,
        )

        return patient_import_request
