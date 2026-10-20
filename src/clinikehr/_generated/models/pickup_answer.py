from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pickup_answer_answer import PickupAnswerAnswer

T = TypeVar("T", bound="PickupAnswer")


@_attrs_define
class PickupAnswer:
    """
    Attributes:
        id (str):
        text_shown (str): The exact wording shown when the answer was given.
        answer (PickupAnswerAnswer):
    """

    id: str
    text_shown: str
    answer: PickupAnswerAnswer
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text_shown = self.text_shown

        answer = self.answer.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text_shown": text_shown,
                "answer": answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        text_shown = d.pop("text_shown")

        answer = PickupAnswerAnswer(d.pop("answer"))

        pickup_answer = cls(
            id=id,
            text_shown=text_shown,
            answer=answer,
        )

        pickup_answer.additional_properties = d
        return pickup_answer

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
