from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.pickup_collection_create_collected_by import PickupCollectionCreateCollectedBy
from ..models.pickup_collection_create_counselling import PickupCollectionCreateCounselling
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pickup_answer import PickupAnswer
    from ..models.pickup_collection_create_privacy_ack import PickupCollectionCreatePrivacyAck


T = TypeVar("T", bound="PickupCollectionCreate")


@_attrs_define
class PickupCollectionCreate:
    """A collection, submitted for clinician review — it never writes the pickup directly. `signature_data` is required:
    the clinic's single write path cannot mark a pickup collected without one. Send the image your own kiosk captured.

        Attributes:
            collected_by (PickupCollectionCreateCollectedBy):
            counselling (PickupCollectionCreateCounselling):
            signature_data (str): A PNG data URL, under 64 KB.
            agent_name (str | Unset): Required when collected_by is agent.
            agent_relationship (str | Unset): Required when collected_by is agent.
            answers (list[PickupAnswer] | Unset): Only `id` and `answer` are read back; send the clinic's own question ids.
            line_ids (list[UUID] | Unset): Prescription ids to hand over, for a partial pickup. Omit to hand over every
                line.
            privacy_ack (PickupCollectionCreatePrivacyAck | Unset): Present only when the clinic's privacy notice is due
                (GET the pickup first to check).
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    collected_by: PickupCollectionCreateCollectedBy
    counselling: PickupCollectionCreateCounselling
    signature_data: str
    agent_name: str | Unset = UNSET
    agent_relationship: str | Unset = UNSET
    answers: list[PickupAnswer] | Unset = UNSET
    line_ids: list[UUID] | Unset = UNSET
    privacy_ack: PickupCollectionCreatePrivacyAck | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collected_by = self.collected_by.value

        counselling = self.counselling.value

        signature_data = self.signature_data

        agent_name = self.agent_name

        agent_relationship = self.agent_relationship

        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        line_ids: list[str] | Unset = UNSET
        if not isinstance(self.line_ids, Unset):
            line_ids = []
            for line_ids_item_data in self.line_ids:
                line_ids_item = str(line_ids_item_data)
                line_ids.append(line_ids_item)

        privacy_ack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privacy_ack, Unset):
            privacy_ack = self.privacy_ack.to_dict()

        client_reference = self.client_reference

        origin_assistant_name = self.origin_assistant_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collected_by": collected_by,
                "counselling": counselling,
                "signature_data": signature_data,
            }
        )
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if agent_relationship is not UNSET:
            field_dict["agent_relationship"] = agent_relationship
        if answers is not UNSET:
            field_dict["answers"] = answers
        if line_ids is not UNSET:
            field_dict["line_ids"] = line_ids
        if privacy_ack is not UNSET:
            field_dict["privacy_ack"] = privacy_ack
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if origin_assistant_name is not UNSET:
            field_dict["origin_assistant_name"] = origin_assistant_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pickup_answer import PickupAnswer  # noqa: PLC0415
        from ..models.pickup_collection_create_privacy_ack import PickupCollectionCreatePrivacyAck  # noqa: PLC0415

        d = dict(src_dict)
        collected_by = PickupCollectionCreateCollectedBy(d.pop("collected_by"))

        counselling = PickupCollectionCreateCounselling(d.pop("counselling"))

        signature_data = d.pop("signature_data")

        agent_name = d.pop("agent_name", UNSET)

        agent_relationship = d.pop("agent_relationship", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: list[PickupAnswer] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:
                answers_item = PickupAnswer.from_dict(answers_item_data)

                answers.append(answers_item)

        _line_ids = d.pop("line_ids", UNSET)
        line_ids: list[UUID] | Unset = UNSET
        if _line_ids is not UNSET:
            line_ids = []
            for line_ids_item_data in _line_ids:
                line_ids_item = UUID(line_ids_item_data)

                line_ids.append(line_ids_item)

        _privacy_ack = d.pop("privacy_ack", UNSET)
        privacy_ack: PickupCollectionCreatePrivacyAck | Unset
        if isinstance(_privacy_ack, Unset):
            privacy_ack = UNSET
        else:
            privacy_ack = PickupCollectionCreatePrivacyAck.from_dict(_privacy_ack)

        client_reference = d.pop("client_reference", UNSET)

        origin_assistant_name = d.pop("origin_assistant_name", UNSET)

        pickup_collection_create = cls(
            collected_by=collected_by,
            counselling=counselling,
            signature_data=signature_data,
            agent_name=agent_name,
            agent_relationship=agent_relationship,
            answers=answers,
            line_ids=line_ids,
            privacy_ack=privacy_ack,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return pickup_collection_create
