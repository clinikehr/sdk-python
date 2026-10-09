from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_template_field_options_type_1 import NoteTemplateFieldOptionsType1


T = TypeVar("T", bound="NoteTemplateField")


@_attrs_define
class NoteTemplateField:
    """
    Attributes:
        id (str): The exact content key (generateFieldId output).
        order (int | None | Unset):
        title (None | str | Unset):
        type_ (None | str | Unset):
        required (bool | Unset):
        options (list[Any] | None | NoteTemplateFieldOptionsType1 | Unset):
    """

    id: str
    order: int | None | Unset = UNSET
    title: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    required: bool | Unset = UNSET
    options: list[Any] | None | NoteTemplateFieldOptionsType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.note_template_field_options_type_1 import NoteTemplateFieldOptionsType1  # noqa: PLC0415

        id = self.id

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        required = self.required

        options: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options

        elif isinstance(self.options, NoteTemplateFieldOptionsType1):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_template_field_options_type_1 import NoteTemplateFieldOptionsType1  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        required = d.pop("required", UNSET)

        def _parse_options(data: object) -> list[Any] | None | NoteTemplateFieldOptionsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[Any], data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_1 = NoteTemplateFieldOptionsType1.from_dict(data)

                return options_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | NoteTemplateFieldOptionsType1 | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        note_template_field = cls(
            id=id,
            order=order,
            title=title,
            type_=type_,
            required=required,
            options=options,
        )

        note_template_field.additional_properties = d
        return note_template_field

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
