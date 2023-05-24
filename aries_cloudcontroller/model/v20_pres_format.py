# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20PresFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresFormat - a model defined in OpenAPI
        attach_id: Attachment identifier.
        format: Attachment format specifier.
    """

    attach_id: str
    format: str

    def __init__(
        self,
        *,
        attach_id: str,
        format: str,
        **kwargs,
    ):
        super().__init__(
            attach_id=attach_id,
            format=format,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20PresFormat.update_forward_refs()
