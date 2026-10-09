from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dispensing_flag_check_state_type_1 import DispensingFlagCheckStateType1
from ..models.dispensing_flag_check_state_type_2_type_1 import DispensingFlagCheckStateType2Type1
from ..models.dispensing_flag_check_state_type_3_type_1 import DispensingFlagCheckStateType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dispensing_flag_evidence import DispensingFlagEvidence
    from ..models.dispensing_flag_reason import DispensingFlagReason
    from ..models.dispensing_medicine import DispensingMedicine


T = TypeVar("T", bound="DispensingFlag")


@_attrs_define
class DispensingFlag:
    """Never the pharmacy's other customers, never price, never staff identity beyond a role word (this row carries no
    staff column at all). check_state is never no_person/person_not_identified_skipped — those are excluded before this
    row is ever built (the ABSENCE of a check, not a finding).

        Attributes:
            id (UUID):
            patient_id (UUID):
            medicine (DispensingMedicine):
            days_supply (int | None | Unset):
            date (datetime.datetime | None | Unset):
            check_state (DispensingFlagCheckStateType1 | DispensingFlagCheckStateType2Type1 |
                DispensingFlagCheckStateType3Type1 | None | Unset):
            flags (list[str] | Unset):
            evidence (DispensingFlagEvidence | Unset):
            reason (DispensingFlagReason | Unset):
    """

    id: UUID
    patient_id: UUID
    medicine: DispensingMedicine
    days_supply: int | None | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    check_state: (
        DispensingFlagCheckStateType1
        | DispensingFlagCheckStateType2Type1
        | DispensingFlagCheckStateType3Type1
        | None
        | Unset
    ) = UNSET
    flags: list[str] | Unset = UNSET
    evidence: DispensingFlagEvidence | Unset = UNSET
    reason: DispensingFlagReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        patient_id = str(self.patient_id)

        medicine = self.medicine.to_dict()

        days_supply: int | None | Unset
        if isinstance(self.days_supply, Unset):
            days_supply = UNSET
        else:
            days_supply = self.days_supply

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        check_state: None | str | Unset
        if isinstance(self.check_state, Unset):
            check_state = UNSET
        elif isinstance(self.check_state, DispensingFlagCheckStateType1):
            check_state = self.check_state.value
        elif isinstance(self.check_state, DispensingFlagCheckStateType2Type1):
            check_state = self.check_state.value
        elif isinstance(self.check_state, DispensingFlagCheckStateType3Type1):
            check_state = self.check_state.value
        else:
            check_state = self.check_state

        flags: list[str] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags

        evidence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence.to_dict()

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "medicine": medicine,
            }
        )
        if days_supply is not UNSET:
            field_dict["days_supply"] = days_supply
        if date is not UNSET:
            field_dict["date"] = date
        if check_state is not UNSET:
            field_dict["check_state"] = check_state
        if flags is not UNSET:
            field_dict["flags"] = flags
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dispensing_flag_evidence import DispensingFlagEvidence  # noqa: PLC0415
        from ..models.dispensing_flag_reason import DispensingFlagReason  # noqa: PLC0415
        from ..models.dispensing_medicine import DispensingMedicine  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        medicine = DispensingMedicine.from_dict(d.pop("medicine"))

        def _parse_days_supply(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_supply = _parse_days_supply(d.pop("days_supply", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.datetime.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_check_state(
            data: object,
        ) -> (
            DispensingFlagCheckStateType1
            | DispensingFlagCheckStateType2Type1
            | DispensingFlagCheckStateType3Type1
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
                check_state_type_1 = DispensingFlagCheckStateType1(data)

                return check_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_state_type_2_type_1 = DispensingFlagCheckStateType2Type1(data)

                return check_state_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_state_type_3_type_1 = DispensingFlagCheckStateType3Type1(data)

                return check_state_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DispensingFlagCheckStateType1
                | DispensingFlagCheckStateType2Type1
                | DispensingFlagCheckStateType3Type1
                | None
                | Unset,
                data,
            )

        check_state = _parse_check_state(d.pop("check_state", UNSET))

        flags = cast(list[str], d.pop("flags", UNSET))

        _evidence = d.pop("evidence", UNSET)
        evidence: DispensingFlagEvidence | Unset
        if isinstance(_evidence, Unset):
            evidence = UNSET
        else:
            evidence = DispensingFlagEvidence.from_dict(_evidence)

        _reason = d.pop("reason", UNSET)
        reason: DispensingFlagReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = DispensingFlagReason.from_dict(_reason)

        dispensing_flag = cls(
            id=id,
            patient_id=patient_id,
            medicine=medicine,
            days_supply=days_supply,
            date=date,
            check_state=check_state,
            flags=flags,
            evidence=evidence,
            reason=reason,
        )

        dispensing_flag.additional_properties = d
        return dispensing_flag

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
