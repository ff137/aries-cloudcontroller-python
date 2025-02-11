# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.cred_attr_spec import CredAttrSpec


class CredentialPreview(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialPreview - a model defined in OpenAPI
        attributes: The attributes of this CredentialPreview.
        type: Message type identifier [Optional].
    """

    attributes: List[CredAttrSpec]
    type: Optional[str] = Field(None, alias="@type")

    class Config:
        allow_population_by_field_name = True


CredentialPreview.update_forward_refs()
