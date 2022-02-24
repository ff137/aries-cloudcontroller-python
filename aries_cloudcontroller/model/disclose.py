# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.protocol_descriptor import ProtocolDescriptor


class Disclose(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Disclose - a model defined in OpenAPI
        protocols: List of protocol descriptors.
        id: Message identifier [Optional].
        type: Message type [Optional].
    """

    protocols: List[ProtocolDescriptor]
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")

    def __init__(
        self,
        *,
        protocols: List[ProtocolDescriptor] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            protocols=protocols,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


Disclose.update_forward_refs()
