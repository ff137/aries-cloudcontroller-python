# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_requested_creds_requested_attr import (
    IndyRequestedCredsRequestedAttr,
)
from aries_cloudcontroller.model.indy_requested_creds_requested_pred import (
    IndyRequestedCredsRequestedPred,
)


class IndyPresSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPresSpec - a model defined in OpenAPI
        requested_attributes: Nested object mapping proof request attribute referents to requested-attribute specifiers.
        requested_predicates: Nested object mapping proof request predicate referents to requested-predicate specifiers.
        self_attested_attributes: Self-attested attributes to build into proof.
        trace: Whether to trace event (default false) [Optional].
    """

    requested_attributes: Dict[str, IndyRequestedCredsRequestedAttr]
    requested_predicates: Dict[str, IndyRequestedCredsRequestedPred]
    self_attested_attributes: Dict[str, str]
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        requested_attributes: Dict[str, IndyRequestedCredsRequestedAttr],
        requested_predicates: Dict[str, IndyRequestedCredsRequestedPred],
        self_attested_attributes: Dict[str, str],
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            requested_attributes=requested_attributes,
            requested_predicates=requested_predicates,
            self_attested_attributes=self_attested_attributes,
            trace=trace,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


IndyPresSpec.update_forward_refs()
