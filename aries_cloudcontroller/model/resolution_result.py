# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ResolutionResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResolutionResult - a model defined in OpenAPI
        did_document: DID Document.
        metadata: Resolution metadata.
    """

    did_document: Dict[str, Any]
    metadata: Dict[str, Any]

    class Config:
        allow_population_by_field_name = True


ResolutionResult.update_forward_refs()
