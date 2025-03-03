# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.signed_doc import SignedDoc


class VerifyRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VerifyRequest - a model defined in OpenAPI
        doc: Signed document.
        verkey: Verkey to use for doc verification [Optional].
    """

    doc: SignedDoc
    verkey: Optional[str] = None

    class Config:
        allow_population_by_field_name = True


VerifyRequest.update_forward_refs()
