from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_department import ProviderDepartment
    from ..models.provider_license import ProviderLicense
    from ..models.provider_specialty import ProviderSpecialty


T = TypeVar("T", bound="Provider")


@_attrs_define
class Provider:
    """One of the clinic's providers (a clinician), read only — the exposed-field allow-list, field by field. The `id` is
    the id the clinic's clinician pickers use. No email, phone or other staff detail is ever exposed, and there is no
    verified flag: a licence or NPI here is what the clinic holds, not a confirmation that it is current.

        Attributes:
            id (UUID):
            display_name (str):
            role (str): The provider's role in the clinic, for example `doctor`.
            specialties (list[ProviderSpecialty]): Primary first.
            licenses (list[ProviderLicense]):
            title (None | str | Unset):
            department (None | ProviderDepartment | Unset):
            npi (None | str | Unset):
    """

    id: UUID
    display_name: str
    role: str
    specialties: list[ProviderSpecialty]
    licenses: list[ProviderLicense]
    title: None | str | Unset = UNSET
    department: None | ProviderDepartment | Unset = UNSET
    npi: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_department import ProviderDepartment  # noqa: PLC0415

        id = str(self.id)

        display_name = self.display_name

        role = self.role

        specialties = []
        for specialties_item_data in self.specialties:
            specialties_item = specialties_item_data.to_dict()
            specialties.append(specialties_item)

        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()
            licenses.append(licenses_item)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        department: dict[str, Any] | None | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        elif isinstance(self.department, ProviderDepartment):
            department = self.department.to_dict()
        else:
            department = self.department

        npi: None | str | Unset
        if isinstance(self.npi, Unset):
            npi = UNSET
        else:
            npi = self.npi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "role": role,
                "specialties": specialties,
                "licenses": licenses,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if department is not UNSET:
            field_dict["department"] = department
        if npi is not UNSET:
            field_dict["npi"] = npi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_department import ProviderDepartment  # noqa: PLC0415
        from ..models.provider_license import ProviderLicense  # noqa: PLC0415
        from ..models.provider_specialty import ProviderSpecialty  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("display_name")

        role = d.pop("role")

        specialties = []
        _specialties = d.pop("specialties")
        for specialties_item_data in _specialties:
            specialties_item = ProviderSpecialty.from_dict(specialties_item_data)

            specialties.append(specialties_item)

        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = ProviderLicense.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_department(data: object) -> None | ProviderDepartment | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                department_type_0 = ProviderDepartment.from_dict(data)

                return department_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderDepartment | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_npi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        npi = _parse_npi(d.pop("npi", UNSET))

        provider = cls(
            id=id,
            display_name=display_name,
            role=role,
            specialties=specialties,
            licenses=licenses,
            title=title,
            department=department,
            npi=npi,
        )

        provider.additional_properties = d
        return provider

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
