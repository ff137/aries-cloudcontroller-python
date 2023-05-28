# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.server_api_base import BaseServerApi
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
from aries_cloudcontroller.models.admin_config import AdminConfig
from aries_cloudcontroller.models.admin_modules import AdminModules
from aries_cloudcontroller.models.admin_status import AdminStatus
from aries_cloudcontroller.models.admin_status_liveliness import AdminStatusLiveliness
from aries_cloudcontroller.models.admin_status_readiness import AdminStatusReadiness
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/status/config",
    responses={
        200: {"model": AdminConfig, "description": ""},
    },
    tags=["server"],
    summary="Fetch the server configuration",
    response_model_by_alias=True,
)
async def get_config(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminConfig:
    ...


@router.get(
    "/status/live",
    responses={
        200: {"model": AdminStatusLiveliness, "description": ""},
    },
    tags=["server"],
    summary="Liveliness check",
    response_model_by_alias=True,
)
async def get_liveliness(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatusLiveliness:
    ...


@router.get(
    "/plugins",
    responses={
        200: {"model": AdminModules, "description": ""},
    },
    tags=["server"],
    summary="Fetch the list of loaded plugins",
    response_model_by_alias=True,
)
async def get_loaded_plugins(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminModules:
    ...


@router.get(
    "/status/ready",
    responses={
        200: {"model": AdminStatusReadiness, "description": ""},
    },
    tags=["server"],
    summary="Readiness check",
    response_model_by_alias=True,
)
async def get_readiness(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatusReadiness:
    ...


@router.get(
    "/status",
    responses={
        200: {"model": AdminStatus, "description": ""},
    },
    tags=["server"],
    summary="Fetch the server status",
    response_model_by_alias=True,
)
async def get_status(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AdminStatus:
    ...


@router.post(
    "/status/reset",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["server"],
    summary="Reset statistics",
    response_model_by_alias=True,
)
async def reset_statistics(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/shutdown",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["server"],
    summary="Shut down server",
    response_model_by_alias=True,
)
async def shutdown_server(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
