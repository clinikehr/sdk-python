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
    """A collection, submitted for clinician review — it never writes the pickup directly. `signature_data` follows the
    clinic's own **Require a signature at pickup** setting, which the server reads: when the clinic requires a
    signature, a request without one is refused with `400 signature_required`; when the clinic has switched it off,
    `signature_data` may be omitted and the pickup is recorded unsigned (`has_signature: false`). A signature you do
    send is always checked (PNG data URL, under 64 KB). To hand over only some lines, list their `line_id` values in
    `line_ids`; the lines left behind stay on a new awaiting pickup.

        Attributes:
            collected_by (PickupCollectionCreateCollectedBy):
            counselling (PickupCollectionCreateCounselling):
            agent_name (str | Unset): Required when collected_by is agent.
            agent_relationship (str | Unset): Required when collected_by is agent.
            answers (list[PickupAnswer] | Unset): Only `id` and `answer` are read back; send the clinic's own question ids.
            signature_data (str | Unset): A PNG data URL, under 64 KB: the image your own kiosk captured. Required when the
                clinic's Require a signature at pickup setting is on (otherwise `400 signature_required`); optional when it is
                off, in which case the pickup is recorded unsigned. If it is on when a clinician later accepts the request and
                none was sent, the acceptance is refused and the request stays pending for the clinic.
            line_ids (list[UUID] | Unset): The `line_id` of each line to hand over, for a partial pickup, from the pickup's
                `lines`. For a prescription line that is its prescription id, so requests written against earlier versions keep
                working; for a Pharmacy-edition till line it is the line's own id (its `pos_sale_item_id` is not accepted here).
                Every id must be a line of this pickup, otherwise the request is refused with `invalid_request`. Omit to hand
                over every line. At least one when present.
            privacy_ack (PickupCollectionCreatePrivacyAck | Unset): Present only when the clinic's privacy notice is due
                (GET the pickup first to check).
            client_reference (str | Unset):
            origin_assistant_name (str | Unset):
    """

    collected_by: PickupCollectionCreateCollectedBy
    counselling: PickupCollectionCreateCounselling
    agent_name: str | Unset = UNSET
    agent_relationship: str | Unset = UNSET
    answers: list[PickupAnswer] | Unset = UNSET
    signature_data: str | Unset = UNSET
    line_ids: list[UUID] | Unset = UNSET
    privacy_ack: PickupCollectionCreatePrivacyAck | Unset = UNSET
    client_reference: str | Unset = UNSET
    origin_assistant_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collected_by = self.collected_by.value

        counselling = self.counselling.value

        agent_name = self.agent_name

        agent_relationship = self.agent_relationship

        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        signature_data = self.signature_data

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
            }
        )
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if agent_relationship is not UNSET:
            field_dict["agent_relationship"] = agent_relationship
        if answers is not UNSET:
            field_dict["answers"] = answers
        if signature_data is not UNSET:
            field_dict["signature_data"] = signature_data
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

        agent_name = d.pop("agent_name", UNSET)

        agent_relationship = d.pop("agent_relationship", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: list[PickupAnswer] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:
                answers_item = PickupAnswer.from_dict(answers_item_data)

                answers.append(answers_item)

        signature_data = d.pop("signature_data", UNSET)

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
            agent_name=agent_name,
            agent_relationship=agent_relationship,
            answers=answers,
            signature_data=signature_data,
            line_ids=line_ids,
            privacy_ack=privacy_ack,
            client_reference=client_reference,
            origin_assistant_name=origin_assistant_name,
        )

        return pickup_collection_create
