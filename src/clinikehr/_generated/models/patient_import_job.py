from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patient_import_job_input_format import PatientImportJobInputFormat
from ..models.patient_import_job_started_by import PatientImportJobStartedBy
from ..models.patient_import_job_status import PatientImportJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patient_import_job_counts import PatientImportJobCounts
    from ..models.patient_import_row_error import PatientImportRowError


T = TypeVar("T", bound="PatientImportJob")


@_attrs_define
class PatientImportJob:
    """
    Attributes:
        id (UUID):
        status (PatientImportJobStatus):
        input_format (PatientImportJobInputFormat):
        row_count (int):
        last_processed_row (int):
        counts (PatientImportJobCounts):
        row_errors (list[PatientImportRowError]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        started_by (PatientImportJobStartedBy | Unset):
        valid_only_run_at (datetime.datetime | None | Unset):
    """

    id: UUID
    status: PatientImportJobStatus
    input_format: PatientImportJobInputFormat
    row_count: int
    last_processed_row: int
    counts: PatientImportJobCounts
    row_errors: list[PatientImportRowError]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    started_by: PatientImportJobStartedBy | Unset = UNSET
    valid_only_run_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        input_format = self.input_format.value

        row_count = self.row_count

        last_processed_row = self.last_processed_row

        counts = self.counts.to_dict()

        row_errors = []
        for row_errors_item_data in self.row_errors:
            row_errors_item = row_errors_item_data.to_dict()
            row_errors.append(row_errors_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        started_by: str | Unset = UNSET
        if not isinstance(self.started_by, Unset):
            started_by = self.started_by.value

        valid_only_run_at: None | str | Unset
        if isinstance(self.valid_only_run_at, Unset):
            valid_only_run_at = UNSET
        elif isinstance(self.valid_only_run_at, datetime.datetime):
            valid_only_run_at = self.valid_only_run_at.isoformat()
        else:
            valid_only_run_at = self.valid_only_run_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "input_format": input_format,
                "row_count": row_count,
                "last_processed_row": last_processed_row,
                "counts": counts,
                "row_errors": row_errors,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if started_by is not UNSET:
            field_dict["started_by"] = started_by
        if valid_only_run_at is not UNSET:
            field_dict["valid_only_run_at"] = valid_only_run_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patient_import_job_counts import PatientImportJobCounts  # noqa: PLC0415
        from ..models.patient_import_row_error import PatientImportRowError  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = PatientImportJobStatus(d.pop("status"))

        input_format = PatientImportJobInputFormat(d.pop("input_format"))

        row_count = d.pop("row_count")

        last_processed_row = d.pop("last_processed_row")

        counts = PatientImportJobCounts.from_dict(d.pop("counts"))

        row_errors = []
        _row_errors = d.pop("row_errors")
        for row_errors_item_data in _row_errors:
            row_errors_item = PatientImportRowError.from_dict(row_errors_item_data)

            row_errors.append(row_errors_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _started_by = d.pop("started_by", UNSET)
        started_by: PatientImportJobStartedBy | Unset
        if isinstance(_started_by, Unset):
            started_by = UNSET
        else:
            started_by = PatientImportJobStartedBy(_started_by)

        def _parse_valid_only_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_only_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return valid_only_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_only_run_at = _parse_valid_only_run_at(d.pop("valid_only_run_at", UNSET))

        patient_import_job = cls(
            id=id,
            status=status,
            input_format=input_format,
            row_count=row_count,
            last_processed_row=last_processed_row,
            counts=counts,
            row_errors=row_errors,
            created_at=created_at,
            updated_at=updated_at,
            started_by=started_by,
            valid_only_run_at=valid_only_run_at,
        )

        patient_import_job.additional_properties = d
        return patient_import_job

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
