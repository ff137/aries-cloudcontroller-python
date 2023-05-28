# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.action_menu_api_base import BaseActionMenuApi
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
from aries_cloudcontroller.models.action_menu_fetch_result import ActionMenuFetchResult
from aries_cloudcontroller.models.perform_request import PerformRequest
from aries_cloudcontroller.models.send_menu import SendMenu
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/action-menu/{conn_id}/close",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["action-menu"],
    summary="Close the active menu associated with a connection",
    response_model_by_alias=True,
)
async def close_menu_by_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/action-menu/{conn_id}/fetch",
    responses={
        200: {"model": ActionMenuFetchResult, "description": ""},
    },
    tags=["action-menu"],
    summary="Fetch the active menu",
    response_model_by_alias=True,
)
async def fetch_menu_by_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ActionMenuFetchResult:
    ...


@router.post(
    "/action-menu/{conn_id}/perform",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["action-menu"],
    summary="Perform an action associated with the active menu",
    response_model_by_alias=True,
)
async def perform_action_by_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    body: PerformRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/action-menu/{conn_id}/request",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["action-menu"],
    summary="Request the active menu",
    response_model_by_alias=True,
)
async def request_menu_by_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/action-menu/{conn_id}/send-menu",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["action-menu"],
    summary="Send an action menu to a connection",
    response_model_by_alias=True,
)
async def send_menu_to_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    body: SendMenu = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
