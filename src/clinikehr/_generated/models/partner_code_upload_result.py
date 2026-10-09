from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partner_code_upload_result_state_type_1 import PartnerCodeUploadResultStateType1
from ..models.partner_code_upload_result_state_type_2_type_1 import PartnerCodeUploadResultStateType2Type1
from ..models.partner_code_upload_result_state_type_3_type_1 import PartnerCodeUploadResultStateType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerCodeUploadResult")


@_attrs_define
class PartnerCodeUploadResult:
    """
    Attributes:
        code (str):
        state (None | PartnerCodeUploadResultStateType1 | PartnerCodeUploadResultStateType2Type1 |
            PartnerCodeUploadResultStateType3Type1):
        reason (None | str | Unset):
    """

    code: str
    state: (
        None
        | PartnerCodeUploadResultStateType1
        | PartnerCodeUploadResultStateType2Type1
        | PartnerCodeUploadResultStateType3Type1
    )
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        state: None | str
        if isinstance(self.state, PartnerCodeUploadResultStateType1):
            state = self.state.value
        elif isinstance(self.state, PartnerCodeUploadResultStateType2Type1):
            state = self.state.value
        elif isinstance(self.state, PartnerCodeUploadResultStateType3Type1):
            state = self.state.value
        else:
            state = self.state

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "state": state,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        def _parse_state(
            data: object,
        ) -> (
            None
            | PartnerCodeUploadResultStateType1
            | PartnerCodeUploadResultStateType2Type1
            | PartnerCodeUploadResultStateType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_1 = PartnerCodeUploadResultStateType1(data)

                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_2_type_1 = PartnerCodeUploadResultStateType2Type1(data)

                return state_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_3_type_1 = PartnerCodeUploadResultStateType3Type1(data)

                return state_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PartnerCodeUploadResultStateType1
                | PartnerCodeUploadResultStateType2Type1
                | PartnerCodeUploadResultStateType3Type1,
                data,
            )

        state = _parse_state(d.pop("state"))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        partner_code_upload_result = cls(
            code=code,
            state=state,
            reason=reason,
        )

        partner_code_upload_result.additional_properties = d
        return partner_code_upload_result

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
