# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class TransactionJobs(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TransactionJobs - a model defined in OpenAPI
        transaction_my_job: My transaction related job [Optional].
        transaction_their_job: Their transaction related job [Optional].
    """

    transaction_my_job: Optional[
        Literal["TRANSACTION_AUTHOR", "TRANSACTION_ENDORSER", "reset"]
    ] = None
    transaction_their_job: Optional[
        Literal["TRANSACTION_AUTHOR", "TRANSACTION_ENDORSER", "reset"]
    ] = None

    class Config:
        allow_population_by_field_name = True


TransactionJobs.update_forward_refs()
