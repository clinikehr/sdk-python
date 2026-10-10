from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insurance_claim import InsuranceClaim


T = TypeVar("T", bound="AdjudicateInsuranceClaimResponse200")


@_attrs_define
class AdjudicateInsuranceClaimResponse200:
    """
    Attributes:
        data (InsuranceClaim): A claim the clinic submitted to an insurer. `status` is the clinic-side lifecycle
            (`submitted`, `approved`, `partially_approved`, `denied`, `partially_paid`, `paid`, ...); `hmo_status` is the
            insurer's verdict (`PENDING`, `APPROVED`, `PARTIALLY_APPROVED`, `REJECTED`). `paid_amount` and
            `written_off_amount` are what the CLINIC has recorded - no API call changes them. `items`, `diagnoses` and
            `documents` are on the single-claim read only. The clinic's notes and internal analysis are never exposed.
        idempotent_replay (bool | Unset): Present and true when this Idempotency-Key was already used and the original
            answer is returned.
    """

    data: InsuranceClaim
    idempotent_replay: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        idempotent_replay = self.idempotent_replay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if idempotent_replay is not UNSET:
            field_dict["idempotent_replay"] = idempotent_replay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insurance_claim import InsuranceClaim  # noqa: PLC0415

        d = dict(src_dict)
        data = InsuranceClaim.from_dict(d.pop("data"))

        idempotent_replay = d.pop("idempotent_replay", UNSET)

        adjudicate_insurance_claim_response_200 = cls(
            data=data,
            idempotent_replay=idempotent_replay,
        )

        adjudicate_insurance_claim_response_200.additional_properties = d
        return adjudicate_insurance_claim_response_200

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
