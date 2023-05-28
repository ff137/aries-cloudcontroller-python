# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_credential_values_value import IndyCredentialValuesValue


class IndyCredential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredential - a model defined in OpenAPI

        cred_def_id: The cred_def_id of this IndyCredential.
        rev_reg: The rev_reg of this IndyCredential [Optional].
        rev_reg_id: The rev_reg_id of this IndyCredential [Optional].
        schema_id: The schema_id of this IndyCredential.
        signature: The signature of this IndyCredential.
        signature_correctness_proof: The signature_correctness_proof of this IndyCredential.
        values: The values of this IndyCredential.
        witness: The witness of this IndyCredential [Optional].
    """

    cred_def_id: str = Field(alias="cred_def_id")
    rev_reg: Optional[Dict[str, Any]] = Field(alias="rev_reg", default=None)
    rev_reg_id: Optional[str] = Field(alias="rev_reg_id", default=None)
    schema_id: str = Field(alias="schema_id")
    signature: Dict[str, Any] = Field(alias="signature")
    signature_correctness_proof: Dict[str, Any] = Field(alias="signature_correctness_proof")
    values: Dict[str, IndyCredentialValuesValue] = Field(alias="values")
    witness: Optional[Dict[str, Any]] = Field(alias="witness", default=None)

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$", value)
        return value

    @validator("rev_reg_id")
    def rev_reg_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)", value)
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

IndyCredential.update_forward_refs()
