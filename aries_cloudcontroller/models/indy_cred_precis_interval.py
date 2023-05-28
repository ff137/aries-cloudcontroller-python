# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyCredPrecisInterval(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredPrecisInterval - a model defined in OpenAPI

        _from: The _from of this IndyCredPrecisInterval [Optional].
        to: The to of this IndyCredPrecisInterval [Optional].
    """

    _from: Optional[int] = Field(alias="from", default=None)
    to: Optional[int] = Field(alias="to", default=None)

    @validator("_from")
    def _from_max(cls, value):
        assert value <= -1
        return value

    @validator("_from")
    def _from_min(cls, value):
        assert value >= 0
        return value

    @validator("to")
    def to_max(cls, value):
        assert value <= -1
        return value

    @validator("to")
    def to_min(cls, value):
        assert value >= 0
        return value

IndyCredPrecisInterval.update_forward_refs()
