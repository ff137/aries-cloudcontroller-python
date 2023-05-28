# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SchemaSendResultSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaSendResultSchema - a model defined in OpenAPI

        attr_names: The attr_names of this SchemaSendResultSchema [Optional].
        id: The id of this SchemaSendResultSchema [Optional].
        name: The name of this SchemaSendResultSchema [Optional].
        seq_no: The seq_no of this SchemaSendResultSchema [Optional].
        ver: The ver of this SchemaSendResultSchema [Optional].
        version: The version of this SchemaSendResultSchema [Optional].
    """

    attr_names: Optional[List[str]] = Field(alias="attrNames", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    seq_no: Optional[int] = Field(alias="seqNo", default=None)
    ver: Optional[str] = Field(alias="ver", default=None)
    version: Optional[str] = Field(alias="version", default=None)

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

    @validator("seq_no")
    def seq_no_min(cls, value):
        assert value >= 1
        return value

    @validator("ver")
    def ver_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

    @validator("version")
    def version_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

SchemaSendResultSchema.update_forward_refs()
