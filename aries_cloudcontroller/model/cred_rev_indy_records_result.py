# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CredRevIndyRecordsResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredRevIndyRecordsResult - a model defined in OpenAPI
        rev_reg_delta: Indy revocation registry delta [Optional].
    """

    rev_reg_delta: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        *,
        rev_reg_delta: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            rev_reg_delta=rev_reg_delta,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


CredRevIndyRecordsResult.update_forward_refs()
