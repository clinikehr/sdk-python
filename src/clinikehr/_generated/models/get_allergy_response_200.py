from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.allergy import Allergy


T = TypeVar("T", bound="GetAllergyResponse200")


@_attrs_define
class GetAllergyResponse200:
    """
    Attributes:
        data (Allergy): An allergy or intolerance - the exposed-field allow-list, field by field. `review_status` says
            where the record stands: `confirmed` is on the clinic's chart (clinic truth); `pending` is an outside submission
            still waiting for a clinician (`verification_status: unconfirmed`); `rejected` and `withdrawn` are this key's
            own submissions that did not become chart truth. `entry` is `structured` for a detailed allergy record and
            `legacy_text` for an allergy that is only a name on the clinic's simple allergy list: it has `id: null`, no
            detail, and cannot be fetched or changed by id. An empty list does NOT mean "no known allergies".
    """

    data: Allergy
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
        from ..models.allergy import Allergy  # noqa: PLC0415

        d = dict(src_dict)
        data = Allergy.from_dict(d.pop("data"))

        get_allergy_response_200 = cls(
            data=data,
        )

        get_allergy_response_200.additional_properties = d
        return get_allergy_response_200

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
