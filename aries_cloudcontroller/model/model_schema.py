# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ModelSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ModelSchema - a model defined in OpenAPI
        attr_names: Schema attribute names [Optional].
        id: Schema identifier [Optional].
        name: Schema name [Optional].
        seq_no: Schema sequence number [Optional].
        ver: Node protocol version [Optional].
        version: Schema version [Optional].
    """

    attr_names: Optional[List[str]] = Field(None, alias="attrNames")
    id: Optional[str] = None
    name: Optional[str] = None
    seq_no: Optional[int] = Field(None, alias="seqNo")
    ver: Optional[str] = None
    version: Optional[str] = None

    @validator("id")
    def id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of id does not match regex pattern ('{pattern}')")
        return value

    @validator("seq_no")
    def seq_no_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 1:
            raise ValueError(f"seq_no must be greater than 1, currently {value}")
        return value

    @validator("ver")
    def ver_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of ver does not match regex pattern ('{pattern}')")
        return value

    @validator("version")
    def version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of version does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


ModelSchema.update_forward_refs()
