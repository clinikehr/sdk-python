from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.referral import Referral


T = TypeVar("T", bound="GetReferralResponse200")


@_attrs_define
class GetReferralResponse200:
    """
    Attributes:
        data (Referral): A clinical referral: another provider or service asks this clinic to see a patient. It is NOT
            the clinic referral programme (clinic-to-clinic credits for recommending ClinikEHR), the marketing "referred by"
            source on a client, or an antenatal or postnatal referral note. The exposed-field allow-list, field by field.
            `review_status` says where the record stands: `confirmed` is on the clinic's referral list; `pending` is an
            outside submission still waiting for clinic staff; `rejected` and `withdrawn` are this key's own submissions
            that did not become a referral. For a confirmed referral `status` is the clinic's workflow: it lands `received`,
            and only the clinic accepts, declines, schedules, completes or cancels it. A sender can never change `status`,
            `recipient` or `scheduled_appointment_id`. `decision_reason` on a confirmed referral (the clinic's reason for
            declining or cancelling) is shown only to the key or organization that sent it; everyone else sees null.
    """

    data: Referral
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
        from ..models.referral import Referral  # noqa: PLC0415

        d = dict(src_dict)
        data = Referral.from_dict(d.pop("data"))

        get_referral_response_200 = cls(
            data=data,
        )

        get_referral_response_200.additional_properties = d
        return get_referral_response_200

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
