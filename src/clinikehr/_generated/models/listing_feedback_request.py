from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.listing_feedback_request_outcome import ListingFeedbackRequestOutcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0
    from ..models.listing_search_request_item_type_1 import ListingSearchRequestItemType1


T = TypeVar("T", bound="ListingFeedbackRequest")


@_attrs_define
class ListingFeedbackRequest:
    """No user data, ever.

    Attributes:
        item (ListingSearchRequestItemType0 | ListingSearchRequestItemType1): Exactly one of an identifier {system,
            value} or a free-text {q}.
        outcome (ListingFeedbackRequestOutcome):
        clinic_id (None | Unset | UUID):
    """

    item: ListingSearchRequestItemType0 | ListingSearchRequestItemType1
    outcome: ListingFeedbackRequestOutcome
    clinic_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0  # noqa: PLC0415

        item: dict[str, Any]
        if isinstance(self.item, ListingSearchRequestItemType0):
            item = self.item.to_dict()
        else:
            item = self.item.to_dict()

        outcome = self.outcome.value

        clinic_id: None | str | Unset
        if isinstance(self.clinic_id, Unset):
            clinic_id = UNSET
        elif isinstance(self.clinic_id, UUID):
            clinic_id = str(self.clinic_id)
        else:
            clinic_id = self.clinic_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item": item,
                "outcome": outcome,
            }
        )
        if clinic_id is not UNSET:
            field_dict["clinic_id"] = clinic_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_search_request_item_type_0 import ListingSearchRequestItemType0  # noqa: PLC0415
        from ..models.listing_search_request_item_type_1 import ListingSearchRequestItemType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_item(data: object) -> ListingSearchRequestItemType0 | ListingSearchRequestItemType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_listing_search_request_item_type_0 = ListingSearchRequestItemType0.from_dict(data)

                return componentsschemas_listing_search_request_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_listing_search_request_item_type_1 = ListingSearchRequestItemType1.from_dict(data)

            return componentsschemas_listing_search_request_item_type_1

        item = _parse_item(d.pop("item"))

        outcome = ListingFeedbackRequestOutcome(d.pop("outcome"))

        def _parse_clinic_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clinic_id_type_0 = UUID(data)

                return clinic_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clinic_id = _parse_clinic_id(d.pop("clinic_id", UNSET))

        listing_feedback_request = cls(
            item=item,
            outcome=outcome,
            clinic_id=clinic_id,
        )

        return listing_feedback_request
