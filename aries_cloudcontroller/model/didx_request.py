# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator


class DIDXRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIDXRequest - a model defined in OpenAPI
        label: Label for DID exchange request.
        id: Message identifier [Optional].
        type: Message type [Optional].
        did: DID of exchange [Optional].
        did_docattach: As signed attachment, DID Doc associated with DID [Optional].
        goal: A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message [Optional].
        goal_code: A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message [Optional].
    """

    label: str
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    did: Optional[str] = None
    did_docattach: Optional[AttachDecorator] = Field(None, alias="did_doc~attach")
    goal: Optional[str] = None
    goal_code: Optional[str] = None

    @validator("did")
    def did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of did does not match regex pattern ('{pattern}')")
        return value

    class Config:
        allow_population_by_field_name = True


DIDXRequest.update_forward_refs()
