# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.introduction_api_base import BaseIntroductionApi
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
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/connections/{conn_id}/start-introduction",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["introduction"],
    summary="Start an introduction between two connections",
    response_model_by_alias=True,
)
async def start_connection_introduction(
    conn_id: str = Path(None, description="Connection identifier"),
    target_connection_id: str = Query(None, description="Target connection identifier"),
    message: str = Query(None, description="Message"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
