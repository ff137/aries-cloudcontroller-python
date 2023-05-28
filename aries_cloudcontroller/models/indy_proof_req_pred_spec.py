# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_proof_req_pred_spec_non_revoked import IndyProofReqPredSpecNonRevoked


class IndyProofReqPredSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofReqPredSpec - a model defined in OpenAPI

        name: The name of this IndyProofReqPredSpec.
        non_revoked: The non_revoked of this IndyProofReqPredSpec [Optional].
        p_type: The p_type of this IndyProofReqPredSpec.
        p_value: The p_value of this IndyProofReqPredSpec.
        restrictions: The restrictions of this IndyProofReqPredSpec [Optional].
    """

    name: str = Field(alias="name")
    non_revoked: Optional[IndyProofReqPredSpecNonRevoked] = Field(alias="non_revoked", default=None)
    p_type: str = Field(alias="p_type")
    p_value: int = Field(alias="p_value")
    restrictions: Optional[List[Dict[str, str]]] = Field(alias="restrictions", default=None)

IndyProofReqPredSpec.update_forward_refs()
