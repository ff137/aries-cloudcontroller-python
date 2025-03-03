# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_ex_record_detail import V20CredExRecordDetail


class V20CredExRecordListResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordListResult - a model defined in OpenAPI
        results: Credential exchange records and corresponding detail records [Optional].
    """

    results: Optional[List[V20CredExRecordDetail]] = None

    class Config:
        allow_population_by_field_name = True


V20CredExRecordListResult.update_forward_refs()
