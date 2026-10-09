from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.medication_statement import MedicationStatement


T = TypeVar("T", bound="GetMedicationStatementResponse200")


@_attrs_define
class GetMedicationStatementResponse200:
    """
    Attributes:
        data (MedicationStatement): A reported medicine - the patient (or a connected app) says they take it. It is NOT
            a prescription and nothing is dispensed from it. The exposed-field allow-list, field by field. `review_status`
            says where the record stands: `confirmed` is on the clinic's chart; `pending` is an outside submission still
            waiting for a clinician (`verification_status: unconfirmed`); `rejected` and `withdrawn` are this key's own
            submissions that did not become chart truth. A statement with a recognised RxNorm code is used by the clinic's
            pharmacy interaction checks while it is `active`; a free-text or `local` one is listed there as not checked.
    """

    data: MedicationStatement
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medication_statement import MedicationStatement  # noqa: PLC0415

        d = dict(src_dict)
        data = MedicationStatement.from_dict(d.pop("data"))

        get_medication_statement_response_200 = cls(
            data=data,
        )

        get_medication_statement_response_200.additional_properties = d
        return get_medication_statement_response_200

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
