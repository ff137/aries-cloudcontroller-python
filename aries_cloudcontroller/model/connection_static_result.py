# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.conn_record import ConnRecord


class ConnectionStaticResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ConnectionStaticResult - a model defined in OpenAPI
        my_did: Local DID.
        my_endpoint: My URL endpoint.
        my_verkey: My verification key.
        record: The record of this ConnectionStaticResult.
        their_did: Remote DID.
        their_verkey: Remote verification key.
    """

    my_did: str
    my_endpoint: str
    my_verkey: str
    record: ConnRecord
    their_did: str
    their_verkey: str

    @validator("my_did")
    def my_did_pattern(cls, value):
        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of my_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("my_endpoint")
    def my_endpoint_pattern(cls, value):
        pattern = r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of my_endpoint does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("my_verkey")
    def my_verkey_pattern(cls, value):
        pattern = (
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        )
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of my_verkey does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("their_did")
    def their_did_pattern(cls, value):
        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of their_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("their_verkey")
    def their_verkey_pattern(cls, value):
        pattern = (
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        )
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of their_verkey does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


ConnectionStaticResult.update_forward_refs()
