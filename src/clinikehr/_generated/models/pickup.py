from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pickup_collected_by_type_1 import PickupCollectedByType1
from ..models.pickup_collected_by_type_2_type_1 import PickupCollectedByType2Type1
from ..models.pickup_collected_by_type_3_type_1 import PickupCollectedByType3Type1
from ..models.pickup_counselling_type_1 import PickupCounsellingType1
from ..models.pickup_counselling_type_2_type_1 import PickupCounsellingType2Type1
from ..models.pickup_counselling_type_3_type_1 import PickupCounsellingType3Type1
from ..models.pickup_status import PickupStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pickup_answer import PickupAnswer
    from ..models.pickup_line import PickupLine


T = TypeVar("T", bound="Pickup")


@_attrs_define
class Pickup:
    """One prescription-pickup handover. Signatures are never returned — `has_signature` only. `agent_name` is never shown
    to an organization connection (only `agent_relationship` is). `pos_sale_id` is set, and `lines` carry
    `pos_sale_item_id` instead of `prescription_id`, for a Pharmacy-edition till sale's pickup; otherwise both are null.

        Attributes:
            id (UUID):
            patient_id (UUID):
            status (PickupStatus):
            collected_by (None | PickupCollectedByType1 | PickupCollectedByType2Type1 | PickupCollectedByType3Type1 |
                Unset):
            agent_name (None | str | Unset): Who collected, when collected_by is agent. Never shown to an organization
                connection — null there even when one was recorded.
            agent_relationship (None | str | Unset):
            counselling (None | PickupCounsellingType1 | PickupCounsellingType2Type1 | PickupCounsellingType3Type1 | Unset):
            answers (list[PickupAnswer] | Unset):
            has_signature (bool | Unset): Whether a signature image is on file. A collected pickup can be unsigned (`false`)
                when the clinic has switched off its Require a signature setting and the handover was sent without one; the
                image itself is never returned either way.
            privacy_acknowledged_version (int | None | Unset):
            lines (list[PickupLine] | Unset):
            outreach_event_id (None | Unset | UUID):
            pos_sale_id (None | Unset | UUID): Set for a Pharmacy-edition till sale's pickup; null for a full-edition in-
                house pharmacy pickup.
            collected_at (datetime.datetime | None | Unset):
            voided_at (datetime.datetime | None | Unset):
            void_reason (None | str | Unset): Present only when voided.
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
    """

    id: UUID
    patient_id: UUID
    status: PickupStatus
    collected_by: None | PickupCollectedByType1 | PickupCollectedByType2Type1 | PickupCollectedByType3Type1 | Unset = (
        UNSET
    )
    agent_name: None | str | Unset = UNSET
    agent_relationship: None | str | Unset = UNSET
    counselling: None | PickupCounsellingType1 | PickupCounsellingType2Type1 | PickupCounsellingType3Type1 | Unset = (
        UNSET
    )
    answers: list[PickupAnswer] | Unset = UNSET
    has_signature: bool | Unset = UNSET
    privacy_acknowledged_version: int | None | Unset = UNSET
    lines: list[PickupLine] | Unset = UNSET
    outreach_event_id: None | Unset | UUID = UNSET
    pos_sale_id: None | Unset | UUID = UNSET
    collected_at: datetime.datetime | None | Unset = UNSET
    voided_at: datetime.datetime | None | Unset = UNSET
    void_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        patient_id = str(self.patient_id)

        status = self.status.value

        collected_by: None | str | Unset
        if isinstance(self.collected_by, Unset):
            collected_by = UNSET
        elif isinstance(self.collected_by, PickupCollectedByType1):
            collected_by = self.collected_by.value
        elif isinstance(self.collected_by, PickupCollectedByType2Type1):
            collected_by = self.collected_by.value
        elif isinstance(self.collected_by, PickupCollectedByType3Type1):
            collected_by = self.collected_by.value
        else:
            collected_by = self.collected_by

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        agent_relationship: None | str | Unset
        if isinstance(self.agent_relationship, Unset):
            agent_relationship = UNSET
        else:
            agent_relationship = self.agent_relationship

        counselling: None | str | Unset
        if isinstance(self.counselling, Unset):
            counselling = UNSET
        elif isinstance(self.counselling, PickupCounsellingType1):
            counselling = self.counselling.value
        elif isinstance(self.counselling, PickupCounsellingType2Type1):
            counselling = self.counselling.value
        elif isinstance(self.counselling, PickupCounsellingType3Type1):
            counselling = self.counselling.value
        else:
            counselling = self.counselling

        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        has_signature = self.has_signature

        privacy_acknowledged_version: int | None | Unset
        if isinstance(self.privacy_acknowledged_version, Unset):
            privacy_acknowledged_version = UNSET
        else:
            privacy_acknowledged_version = self.privacy_acknowledged_version

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        outreach_event_id: None | str | Unset
        if isinstance(self.outreach_event_id, Unset):
            outreach_event_id = UNSET
        elif isinstance(self.outreach_event_id, UUID):
            outreach_event_id = str(self.outreach_event_id)
        else:
            outreach_event_id = self.outreach_event_id

        pos_sale_id: None | str | Unset
        if isinstance(self.pos_sale_id, Unset):
            pos_sale_id = UNSET
        elif isinstance(self.pos_sale_id, UUID):
            pos_sale_id = str(self.pos_sale_id)
        else:
            pos_sale_id = self.pos_sale_id

        collected_at: None | str | Unset
        if isinstance(self.collected_at, Unset):
            collected_at = UNSET
        elif isinstance(self.collected_at, datetime.datetime):
            collected_at = self.collected_at.isoformat()
        else:
            collected_at = self.collected_at

        voided_at: None | str | Unset
        if isinstance(self.voided_at, Unset):
            voided_at = UNSET
        elif isinstance(self.voided_at, datetime.datetime):
            voided_at = self.voided_at.isoformat()
        else:
            voided_at = self.voided_at

        void_reason: None | str | Unset
        if isinstance(self.void_reason, Unset):
            void_reason = UNSET
        else:
            void_reason = self.void_reason

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "patient_id": patient_id,
                "status": status,
            }
        )
        if collected_by is not UNSET:
            field_dict["collected_by"] = collected_by
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if agent_relationship is not UNSET:
            field_dict["agent_relationship"] = agent_relationship
        if counselling is not UNSET:
            field_dict["counselling"] = counselling
        if answers is not UNSET:
            field_dict["answers"] = answers
        if has_signature is not UNSET:
            field_dict["has_signature"] = has_signature
        if privacy_acknowledged_version is not UNSET:
            field_dict["privacy_acknowledged_version"] = privacy_acknowledged_version
        if lines is not UNSET:
            field_dict["lines"] = lines
        if outreach_event_id is not UNSET:
            field_dict["outreach_event_id"] = outreach_event_id
        if pos_sale_id is not UNSET:
            field_dict["pos_sale_id"] = pos_sale_id
        if collected_at is not UNSET:
            field_dict["collected_at"] = collected_at
        if voided_at is not UNSET:
            field_dict["voided_at"] = voided_at
        if void_reason is not UNSET:
            field_dict["void_reason"] = void_reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pickup_answer import PickupAnswer  # noqa: PLC0415
        from ..models.pickup_line import PickupLine  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        patient_id = UUID(d.pop("patient_id"))

        status = PickupStatus(d.pop("status"))

        def _parse_collected_by(
            data: object,
        ) -> None | PickupCollectedByType1 | PickupCollectedByType2Type1 | PickupCollectedByType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collected_by_type_1 = PickupCollectedByType1(data)

                return collected_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collected_by_type_2_type_1 = PickupCollectedByType2Type1(data)

                return collected_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collected_by_type_3_type_1 = PickupCollectedByType3Type1(data)

                return collected_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PickupCollectedByType1 | PickupCollectedByType2Type1 | PickupCollectedByType3Type1 | Unset, data
            )

        collected_by = _parse_collected_by(d.pop("collected_by", UNSET))

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        def _parse_agent_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_relationship = _parse_agent_relationship(d.pop("agent_relationship", UNSET))

        def _parse_counselling(
            data: object,
        ) -> None | PickupCounsellingType1 | PickupCounsellingType2Type1 | PickupCounsellingType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                counselling_type_1 = PickupCounsellingType1(data)

                return counselling_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                counselling_type_2_type_1 = PickupCounsellingType2Type1(data)

                return counselling_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                counselling_type_3_type_1 = PickupCounsellingType3Type1(data)

                return counselling_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PickupCounsellingType1 | PickupCounsellingType2Type1 | PickupCounsellingType3Type1 | Unset, data
            )

        counselling = _parse_counselling(d.pop("counselling", UNSET))

        _answers = d.pop("answers", UNSET)
        answers: list[PickupAnswer] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:
                answers_item = PickupAnswer.from_dict(answers_item_data)

                answers.append(answers_item)

        has_signature = d.pop("has_signature", UNSET)

        def _parse_privacy_acknowledged_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        privacy_acknowledged_version = _parse_privacy_acknowledged_version(d.pop("privacy_acknowledged_version", UNSET))

        _lines = d.pop("lines", UNSET)
        lines: list[PickupLine] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = PickupLine.from_dict(lines_item_data)

                lines.append(lines_item)

        def _parse_outreach_event_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outreach_event_id_type_0 = UUID(data)

                return outreach_event_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        outreach_event_id = _parse_outreach_event_id(d.pop("outreach_event_id", UNSET))

        def _parse_pos_sale_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pos_sale_id_type_0 = UUID(data)

                return pos_sale_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pos_sale_id = _parse_pos_sale_id(d.pop("pos_sale_id", UNSET))

        def _parse_collected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collected_at_type_0 = datetime.datetime.fromisoformat(data)

                return collected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        collected_at = _parse_collected_at(d.pop("collected_at", UNSET))

        def _parse_voided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voided_at_type_0 = datetime.datetime.fromisoformat(data)

                return voided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        voided_at = _parse_voided_at(d.pop("voided_at", UNSET))

        def _parse_void_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        void_reason = _parse_void_reason(d.pop("void_reason", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        pickup = cls(
            id=id,
            patient_id=patient_id,
            status=status,
            collected_by=collected_by,
            agent_name=agent_name,
            agent_relationship=agent_relationship,
            counselling=counselling,
            answers=answers,
            has_signature=has_signature,
            privacy_acknowledged_version=privacy_acknowledged_version,
            lines=lines,
            outreach_event_id=outreach_event_id,
            pos_sale_id=pos_sale_id,
            collected_at=collected_at,
            voided_at=voided_at,
            void_reason=void_reason,
            created_at=created_at,
            updated_at=updated_at,
        )

        pickup.additional_properties = d
        return pickup

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
