# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_pres_format import V20PresFormat


class V20PresExRecordPres(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresExRecordPres - a model defined in OpenAPI

        id: The id of this V20PresExRecordPres [Optional].
        type: The type of this V20PresExRecordPres [Optional].
        comment: The comment of this V20PresExRecordPres [Optional].
        formats: The formats of this V20PresExRecordPres.
        presentationsattach: The presentationsattach of this V20PresExRecordPres.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    formats: List[V20PresFormat] = Field(alias="formats")
    presentationsattach: List[AttachDecorator] = Field(alias="presentations~attach")

V20PresExRecordPres.update_forward_refs()
