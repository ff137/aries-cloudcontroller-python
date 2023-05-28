# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.trustping_api_base import BaseTrustpingApi
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
from aries_cloudcontroller.models.ping_request import PingRequest
from aries_cloudcontroller.models.ping_request_response import PingRequestResponse
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/connections/{conn_id}/send-ping",
    responses={
        200: {"model": PingRequestResponse, "description": ""},
    },
    tags=["trustping"],
    summary="Send a trust ping to a connection",
    response_model_by_alias=True,
)
async def send_ping(
    conn_id: str = Path(None, description="Connection identifier"),
    body: PingRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> PingRequestResponse:
    ...
