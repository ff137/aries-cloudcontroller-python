# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.menu_json import MenuJson


class SendMenu(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SendMenu - a model defined in OpenAPI
        menu: Menu to send to connection.
    """

    menu: MenuJson

    class Config:
        allow_population_by_field_name = True


SendMenu.update_forward_refs()
