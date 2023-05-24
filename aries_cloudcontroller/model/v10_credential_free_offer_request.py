# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_preview import CredentialPreview


class V10CredentialFreeOfferRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialFreeOfferRequest - a model defined in OpenAPI
        connection_id: Connection identifier.
        cred_def_id: Credential definition identifier.
        credential_preview: The credential_preview of this V10CredentialFreeOfferRequest.
        auto_issue: Whether to respond automatically to credential requests, creating and issuing requested credentials [Optional].
        auto_remove: Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) [Optional].
        comment: Human-readable comment [Optional].
        trace: Record trace information, based on agent configuration [Optional].
    """

    connection_id: str
    cred_def_id: str
    credential_preview: CredentialPreview
    auto_issue: Optional[bool] = None
    auto_remove: Optional[bool] = None
    comment: Optional[str] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        connection_id: str,
        cred_def_id: str,
        credential_preview: CredentialPreview,
        auto_issue: Optional[bool] = None,
        auto_remove: Optional[bool] = None,
        comment: Optional[str] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            auto_issue=auto_issue,
            auto_remove=auto_remove,
            comment=comment,
            connection_id=connection_id,
            cred_def_id=cred_def_id,
            credential_preview=credential_preview,
            trace=trace,
            **kwargs,
        )

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


V10CredentialFreeOfferRequest.update_forward_refs()
