# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.out_of_band_api_base import BaseOutOfBandApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from aries_cloudcontroller.models.extra_models import TokenModel  # noqa: F401
from aries_cloudcontroller.models.invitation_create_request import InvitationCreateRequest
from aries_cloudcontroller.models.invitation_message import InvitationMessage
from aries_cloudcontroller.models.invitation_record import InvitationRecord
from aries_cloudcontroller.models.oob_record import OobRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/out-of-band/create-invitation",
    responses={
        200: {"model": InvitationRecord, "description": ""},
    },
    tags=["out-of-band"],
    summary="Create a new connection invitation",
    response_model_by_alias=True,
)
async def create_oob_invitation(
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    multi_use: bool = Query(None, description="Create invitation for multiple use (default false)"),
    body: InvitationCreateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> InvitationRecord:
    ...


@router.post(
    "/out-of-band/receive-invitation",
    responses={
        200: {"model": OobRecord, "description": ""},
    },
    tags=["out-of-band"],
    summary="Receive a new connection invitation",
    response_model_by_alias=True,
)
async def receive_oob_invitation(
    alias: str = Query(None, description="Alias for connection"),
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    use_existing_connection: bool = Query(None, description="Use an existing connection, if possible"),
    body: InvitationMessage = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> OobRecord:
    ...
