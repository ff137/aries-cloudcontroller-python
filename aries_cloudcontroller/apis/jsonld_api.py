# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.jsonld_api_base import BaseJsonldApi
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
from aries_cloudcontroller.models.sign_request import SignRequest
from aries_cloudcontroller.models.sign_response import SignResponse
from aries_cloudcontroller.models.verify_request import VerifyRequest
from aries_cloudcontroller.models.verify_response import VerifyResponse
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/jsonld/sign",
    responses={
        200: {"model": SignResponse, "description": ""},
    },
    tags=["jsonld"],
    summary="Sign a JSON-LD structure and return it",
    response_model_by_alias=True,
)
async def sign(
    body: SignRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> SignResponse:
    ...


@router.post(
    "/jsonld/verify",
    responses={
        200: {"model": VerifyResponse, "description": ""},
    },
    tags=["jsonld"],
    summary="Verify a JSON-LD structure.",
    response_model_by_alias=True,
)
async def verify(
    body: VerifyRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> VerifyResponse:
    ...
