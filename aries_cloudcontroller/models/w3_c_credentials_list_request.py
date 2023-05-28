# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class W3CCredentialsListRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    W3CCredentialsListRequest - a model defined in OpenAPI

        contexts: The contexts of this W3CCredentialsListRequest [Optional].
        given_id: The given_id of this W3CCredentialsListRequest [Optional].
        issuer_id: The issuer_id of this W3CCredentialsListRequest [Optional].
        max_results: The max_results of this W3CCredentialsListRequest [Optional].
        proof_types: The proof_types of this W3CCredentialsListRequest [Optional].
        schema_ids: The schema_ids of this W3CCredentialsListRequest [Optional].
        subject_ids: The subject_ids of this W3CCredentialsListRequest [Optional].
        tag_query: The tag_query of this W3CCredentialsListRequest [Optional].
        types: The types of this W3CCredentialsListRequest [Optional].
    """

    contexts: Optional[List[str]] = Field(alias="contexts", default=None)
    given_id: Optional[str] = Field(alias="given_id", default=None)
    issuer_id: Optional[str] = Field(alias="issuer_id", default=None)
    max_results: Optional[int] = Field(alias="max_results", default=None)
    proof_types: Optional[List[str]] = Field(alias="proof_types", default=None)
    schema_ids: Optional[List[str]] = Field(alias="schema_ids", default=None)
    subject_ids: Optional[List[str]] = Field(alias="subject_ids", default=None)
    tag_query: Optional[Dict[str, str]] = Field(alias="tag_query", default=None)
    types: Optional[List[str]] = Field(alias="types", default=None)

W3CCredentialsListRequest.update_forward_refs()
