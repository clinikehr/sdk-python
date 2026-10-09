from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.allergy_reaction_severity_type_1 import AllergyReactionSeverityType1
from ..models.allergy_reaction_severity_type_2_type_1 import AllergyReactionSeverityType2Type1
from ..models.allergy_reaction_severity_type_3_type_1 import AllergyReactionSeverityType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="AllergyReaction")


@_attrs_define
class AllergyReaction:
    """One reaction. `manifestation` lists what happened, in the clinic's or sender's own words.

    Attributes:
        manifestation (list[str]):
        severity (AllergyReactionSeverityType1 | AllergyReactionSeverityType2Type1 | AllergyReactionSeverityType3Type1 |
            None | Unset):
        description (None | str | Unset):
    """

    manifestation: list[str]
    severity: (
        AllergyReactionSeverityType1
        | AllergyReactionSeverityType2Type1
        | AllergyReactionSeverityType3Type1
        | None
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        manifestation = self.manifestation

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        elif isinstance(self.severity, AllergyReactionSeverityType1):
            severity = self.severity.value
        elif isinstance(self.severity, AllergyReactionSeverityType2Type1):
            severity = self.severity.value
        elif isinstance(self.severity, AllergyReactionSeverityType3Type1):
            severity = self.severity.value
        else:
            severity = self.severity

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "manifestation": manifestation,
            }
        )
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manifestation = cast(list[str], d.pop("manifestation"))

        def _parse_severity(
            data: object,
        ) -> (
            AllergyReactionSeverityType1
            | AllergyReactionSeverityType2Type1
            | AllergyReactionSeverityType3Type1
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
                severity_type_1 = AllergyReactionSeverityType1(data)

                return severity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                severity_type_2_type_1 = AllergyReactionSeverityType2Type1(data)

                return severity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                severity_type_3_type_1 = AllergyReactionSeverityType3Type1(data)

                return severity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AllergyReactionSeverityType1
                | AllergyReactionSeverityType2Type1
                | AllergyReactionSeverityType3Type1
                | None
                | Unset,
                data,
            )

        severity = _parse_severity(d.pop("severity", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        allergy_reaction = cls(
            manifestation=manifestation,
            severity=severity,
            description=description,
        )

        return allergy_reaction
