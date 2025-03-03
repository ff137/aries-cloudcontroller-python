# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.connection_invitation import ConnectionInvitation


class InvitationResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InvitationResult - a model defined in OpenAPI
        connection_id: Connection identifier [Optional].
        invitation: The invitation of this InvitationResult [Optional].
        invitation_url: Invitation URL [Optional].
    """

    connection_id: Optional[str] = None
    invitation: Optional[ConnectionInvitation] = None
    invitation_url: Optional[str] = None

    class Config:
        allow_population_by_field_name = True


InvitationResult.update_forward_refs()
