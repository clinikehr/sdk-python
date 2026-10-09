from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentCancelRequest")


@_attrs_define
class AppointmentCancelRequest:
    """
    Attributes:
        reason (str | Unset):
        notify_patient (bool | Unset): false only ever DOWNGRADES notification columns — the patient is not emailed
            about the cancellation, and it never re-enables a row already silenced. Default: True.
        run_automations (bool | Unset):  Default: False.
    """

    reason: str | Unset = UNSET
    notify_patient: bool | Unset = True
    run_automations: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        notify_patient = self.notify_patient

        run_automations = self.run_automations

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if notify_patient is not UNSET:
            field_dict["notify_patient"] = notify_patient
        if run_automations is not UNSET:
            field_dict["run_automations"] = run_automations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason", UNSET)

        notify_patient = d.pop("notify_patient", UNSET)

        run_automations = d.pop("run_automations", UNSET)

        appointment_cancel_request = cls(
            reason=reason,
            notify_patient=notify_patient,
            run_automations=run_automations,
        )

        return appointment_cancel_request
