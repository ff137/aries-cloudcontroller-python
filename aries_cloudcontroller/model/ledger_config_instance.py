# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class LedgerConfigInstance(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LedgerConfigInstance - a model defined in OpenAPI
        genesis_file: genesis_file [Optional].
        genesis_transactions: genesis_transactions [Optional].
        genesis_url: genesis_url [Optional].
        id: ledger_id [Optional].
        is_production: is_production [Optional].
    """

    genesis_file: Optional[str] = None
    genesis_transactions: Optional[str] = None
    genesis_url: Optional[str] = None
    id: Optional[str] = None
    is_production: Optional[bool] = None

    class Config:
        allow_population_by_field_name = True


LedgerConfigInstance.update_forward_refs()
