# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class MediationIdMatchInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationIdMatchInfo - a model defined in OpenAPI
        mediation_id: Mediation record identifier [Optional].
    """

    mediation_id: Optional[str] = None

    def __init__(
        self,
        *,
        mediation_id: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            mediation_id=mediation_id,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


MediationIdMatchInfo.update_forward_refs()
