# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class RouteRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RouteRecord - a model defined in OpenAPI
        recipient_key: The recipient_key of this RouteRecord.
        connection_id: The connection_id of this RouteRecord [Optional].
        created_at: Time of record creation [Optional].
        record_id: The record_id of this RouteRecord [Optional].
        role: The role of this RouteRecord [Optional].
        state: Current record state [Optional].
        updated_at: Time of last record update [Optional].
        wallet_id: The wallet_id of this RouteRecord [Optional].
    """

    recipient_key: str
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    record_id: Optional[str] = None
    role: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None
    wallet_id: Optional[str] = None

    @validator("created_at")
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


RouteRecord.update_forward_refs()
