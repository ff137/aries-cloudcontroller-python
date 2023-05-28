# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_ge_proof_pred import IndyGEProofPred


class IndyGEProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyGEProof - a model defined in OpenAPI

        alpha: The alpha of this IndyGEProof [Optional].
        mj: The mj of this IndyGEProof [Optional].
        predicate: The predicate of this IndyGEProof [Optional].
        r: The r of this IndyGEProof [Optional].
        t: The t of this IndyGEProof [Optional].
        u: The u of this IndyGEProof [Optional].
    """

    alpha: Optional[str] = Field(alias="alpha", default=None)
    mj: Optional[str] = Field(alias="mj", default=None)
    predicate: Optional[IndyGEProofPred] = Field(alias="predicate", default=None)
    r: Optional[Dict[str, str]] = Field(alias="r", default=None)
    t: Optional[Dict[str, str]] = Field(alias="t", default=None)
    u: Optional[Dict[str, str]] = Field(alias="u", default=None)

    @validator("alpha")
    def alpha_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]*$", value)
        return value

    @validator("mj")
    def mj_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]*$", value)
        return value

IndyGEProof.update_forward_refs()
