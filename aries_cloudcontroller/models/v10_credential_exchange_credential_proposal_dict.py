# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.credential_preview import CredentialPreview


class V10CredentialExchangeCredentialProposalDict(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialExchangeCredentialProposalDict - a model defined in OpenAPI

        id: The id of this V10CredentialExchangeCredentialProposalDict [Optional].
        type: The type of this V10CredentialExchangeCredentialProposalDict [Optional].
        comment: The comment of this V10CredentialExchangeCredentialProposalDict [Optional].
        cred_def_id: The cred_def_id of this V10CredentialExchangeCredentialProposalDict [Optional].
        credential_proposal: The credential_proposal of this V10CredentialExchangeCredentialProposalDict [Optional].
        issuer_did: The issuer_did of this V10CredentialExchangeCredentialProposalDict [Optional].
        schema_id: The schema_id of this V10CredentialExchangeCredentialProposalDict [Optional].
        schema_issuer_did: The schema_issuer_did of this V10CredentialExchangeCredentialProposalDict [Optional].
        schema_name: The schema_name of this V10CredentialExchangeCredentialProposalDict [Optional].
        schema_version: The schema_version of this V10CredentialExchangeCredentialProposalDict [Optional].
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    cred_def_id: Optional[str] = Field(alias="cred_def_id", default=None)
    credential_proposal: Optional[CredentialPreview] = Field(alias="credential_proposal", default=None)
    issuer_did: Optional[str] = Field(alias="issuer_did", default=None)
    schema_id: Optional[str] = Field(alias="schema_id", default=None)
    schema_issuer_did: Optional[str] = Field(alias="schema_issuer_did", default=None)
    schema_name: Optional[str] = Field(alias="schema_name", default=None)
    schema_version: Optional[str] = Field(alias="schema_version", default=None)

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$", value)
        return value

    @validator("issuer_did")
    def issuer_did_pattern(cls, value):
        assert value is not None and re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$", value)
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

    @validator("schema_issuer_did")
    def schema_issuer_did_pattern(cls, value):
        assert value is not None and re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$", value)
        return value

    @validator("schema_version")
    def schema_version_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

V10CredentialExchangeCredentialProposalDict.update_forward_refs()
