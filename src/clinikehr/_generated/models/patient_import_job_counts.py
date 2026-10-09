from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatientImportJobCounts")


@_attrs_define
class PatientImportJobCounts:
    """
    Attributes:
        created (int):
        flagged_duplicate (int): Created, and marked as a possible duplicate for staff to review.
        skipped_already_imported (int):
        failed (int):
    """

    created: int
    flagged_duplicate: int
    skipped_already_imported: int
    failed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        flagged_duplicate = self.flagged_duplicate

        skipped_already_imported = self.skipped_already_imported

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "flagged_duplicate": flagged_duplicate,
                "skipped_already_imported": skipped_already_imported,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        flagged_duplicate = d.pop("flagged_duplicate")

        skipped_already_imported = d.pop("skipped_already_imported")

        failed = d.pop("failed")

        patient_import_job_counts = cls(
            created=created,
            flagged_duplicate=flagged_duplicate,
            skipped_already_imported=skipped_already_imported,
            failed=failed,
        )

        patient_import_job_counts.additional_properties = d
        return patient_import_job_counts

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
