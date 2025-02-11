# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.menu_option import MenuOption


class Menu(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Menu - a model defined in OpenAPI
        options: List of menu options.
        id: Message identifier [Optional].
        type: Message type [Optional].
        description: Introductory text for the menu [Optional].
        errormsg: An optional error message to display in menu header [Optional].
        title: Menu title [Optional].
    """

    options: List[MenuOption]
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    description: Optional[str] = None
    errormsg: Optional[str] = None
    title: Optional[str] = None

    class Config:
        allow_population_by_field_name = True


Menu.update_forward_refs()
