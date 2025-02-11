# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class DIFOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIFOptions - a model defined in OpenAPI
        challenge: Challenge protect against replay attack [Optional].
        domain: Domain protect against replay attack [Optional].
    """

    challenge: Optional[str] = None
    domain: Optional[str] = None

    @validator("challenge")
    def challenge_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of challenge does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


DIFOptions.update_forward_refs()
