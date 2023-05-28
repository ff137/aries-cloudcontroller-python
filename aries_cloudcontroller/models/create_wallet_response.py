# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CreateWalletResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateWalletResponse - a model defined in OpenAPI

        created_at: The created_at of this CreateWalletResponse [Optional].
        key_management_mode: The key_management_mode of this CreateWalletResponse.
        settings: The settings of this CreateWalletResponse [Optional].
        state: The state of this CreateWalletResponse [Optional].
        token: The token of this CreateWalletResponse [Optional].
        updated_at: The updated_at of this CreateWalletResponse [Optional].
        wallet_id: The wallet_id of this CreateWalletResponse.
    """

    created_at: Optional[str] = Field(alias="created_at", default=None)
    key_management_mode: str = Field(alias="key_management_mode")
    settings: Optional[Dict[str, Any]] = Field(alias="settings", default=None)
    state: Optional[str] = Field(alias="state", default=None)
    token: Optional[str] = Field(alias="token", default=None)
    updated_at: Optional[str] = Field(alias="updated_at", default=None)
    wallet_id: str = Field(alias="wallet_id")

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

CreateWalletResponse.update_forward_refs()
