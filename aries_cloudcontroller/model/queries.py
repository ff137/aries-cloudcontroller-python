# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.query_item import QueryItem


class Queries(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Queries - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        queries: The queries of this Queries [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    queries: Optional[List[QueryItem]] = None

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        queries: Optional[List[QueryItem]] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            queries=queries,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


Queries.update_forward_refs()
