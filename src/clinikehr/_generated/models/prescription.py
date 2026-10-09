from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prescription_source import PrescriptionSource
from ..models.prescription_status import PrescriptionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prescription_medication import PrescriptionMedication


T = TypeVar("T", bound="Prescription")


@_attrs_define
class Prescription:
    """A prescription, read only and deliberately minimal: the drug, the dose, the frequency, the status and when it was
    written. Nothing about dispensing, payment, scheduling, the prescriber or notes ever leaves the clinic. There is no
    way to create or change a prescription through the API. `source` is `eprescribe` for a prescription sent through the
    clinic's e-prescribing connection and `clinic` otherwise. `status: unknown` appears only on an `eprescribe`
    prescription whose status the e-prescribing service reports in a form the platform does not recognise.

        Attributes:
            id (UUID):
            patient_id (UUID):
            medication (PrescriptionMedication):
            status (PrescriptionStatus):
            source (PrescriptionSource):
            dosage (None | str | Unset):
            frequency (None | str | Unset):
            prescribed_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    patient_id: UUID
    medication: PrescriptionMedication
    status: PrescriptionStatus
    source: PrescriptionSource
    dosage: None | str | Unset = UNSET
    frequency: None | str | Unset = UNSET
    prescribed_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        patient_id = str(self.patient_id)

        medication = self.medication.to_dict()

        status = self.status.value

        source = self.source.value

        dosage: None | str | Unset
        if isinstance(self.dosage, Unset):
            dosage = UNSET
        else:
            dosage = self.dosage

        frequency: None | str | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        prescribed_at: None | str | Unset
        if isinstance(self.prescribed_at, Unset):
            prescribed_at = UNSET
        elif isinstance(self.prescribed_at, datetime.datetime):
            prescribed_at = self.prescribed_at.isoformat()
        else:
            prescribed_at = self.prescribed_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "medication": medication,
                "status": status,
                "source": source,
            }
        )
        if dosage is not UNSET:
            field_dict["dosage"] = dosage
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if prescribed_at is not UNSET:
            field_dict["prescribed_at"] = prescribed_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prescription_medication import PrescriptionMedication  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        medication = PrescriptionMedication.from_dict(d.pop("medication"))

        status = PrescriptionStatus(d.pop("status"))

        source = PrescriptionSource(d.pop("source"))

        def _parse_dosage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dosage = _parse_dosage(d.pop("dosage", UNSET))

        def _parse_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_prescribed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prescribed_at_type_0 = datetime.datetime.fromisoformat(data)

                return prescribed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        prescribed_at = _parse_prescribed_at(d.pop("prescribed_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        prescription = cls(
            id=id,
            patient_id=patient_id,
            medication=medication,
            status=status,
            source=source,
            dosage=dosage,
            frequency=frequency,
            prescribed_at=prescribed_at,
            updated_at=updated_at,
        )

        prescription.additional_properties = d
        return prescription

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
