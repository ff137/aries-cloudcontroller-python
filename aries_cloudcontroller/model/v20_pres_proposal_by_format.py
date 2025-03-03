# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.dif_proof_proposal import DIFProofProposal
from aries_cloudcontroller.model.indy_proof_request import IndyProofRequest


class V20PresProposalByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresProposalByFormat - a model defined in OpenAPI
        dif: Presentation proposal for DIF [Optional].
        indy: Presentation proposal for indy [Optional].
    """

    dif: Optional[DIFProofProposal] = None
    indy: Optional[IndyProofRequest] = None

    class Config:
        allow_population_by_field_name = True


V20PresProposalByFormat.update_forward_refs()
