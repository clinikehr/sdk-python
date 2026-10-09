from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dispensing_flag_reason_code_type_1 import DispensingFlagReasonCodeType1
from ..models.dispensing_flag_reason_code_type_2_type_1 import DispensingFlagReasonCodeType2Type1
from ..models.dispensing_flag_reason_code_type_3_type_1 import DispensingFlagReasonCodeType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="DispensingFlagReason")


@_attrs_define
class DispensingFlagReason:
    """
    Attributes:
        code (DispensingFlagReasonCodeType1 | DispensingFlagReasonCodeType2Type1 | DispensingFlagReasonCodeType3Type1 |
            None | Unset):
        text (None | str | Unset):
    """

    code: (
        DispensingFlagReasonCodeType1
        | DispensingFlagReasonCodeType2Type1
        | DispensingFlagReasonCodeType3Type1
        | None
        | Unset
    ) = UNSET
    text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, DispensingFlagReasonCodeType1):
            code = self.code.value
        elif isinstance(self.code, DispensingFlagReasonCodeType2Type1):
            code = self.code.value
        elif isinstance(self.code, DispensingFlagReasonCodeType3Type1):
            code = self.code.value
        else:
            code = self.code

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_code(
            data: object,
        ) -> (
            DispensingFlagReasonCodeType1
            | DispensingFlagReasonCodeType2Type1
            | DispensingFlagReasonCodeType3Type1
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
                code_type_1 = DispensingFlagReasonCodeType1(data)

                return code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                code_type_2_type_1 = DispensingFlagReasonCodeType2Type1(data)

                return code_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                code_type_3_type_1 = DispensingFlagReasonCodeType3Type1(data)

                return code_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DispensingFlagReasonCodeType1
                | DispensingFlagReasonCodeType2Type1
                | DispensingFlagReasonCodeType3Type1
                | None
                | Unset,
                data,
            )

        code = _parse_code(d.pop("code", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        dispensing_flag_reason = cls(
            code=code,
            text=text,
        )

        dispensing_flag_reason.additional_properties = d
        return dispensing_flag_reason

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
