# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyGEProofPred(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyGEProofPred - a model defined in OpenAPI
        attr_name: Attribute name, indy-canonicalized [Optional].
        p_type: Predicate type [Optional].
        value: Predicate threshold value [Optional].
    """

    attr_name: Optional[str] = None
    p_type: Optional[Literal["LT", "LE", "GE", "GT"]] = None
    value: Optional[int] = None

    class Config:
        allow_population_by_field_name = True


IndyGEProofPred.update_forward_refs()
