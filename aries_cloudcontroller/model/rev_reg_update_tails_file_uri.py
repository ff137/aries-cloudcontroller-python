# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class RevRegUpdateTailsFileUri(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegUpdateTailsFileUri - a model defined in OpenAPI
        tails_public_uri: Public URI to the tails file.
    """

    tails_public_uri: str

    def __init__(
        self,
        *,
        tails_public_uri: str,
        **kwargs,
    ):
        super().__init__(
            tails_public_uri=tails_public_uri,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


RevRegUpdateTailsFileUri.update_forward_refs()
