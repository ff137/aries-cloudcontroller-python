# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.multitenancy_api_base import BaseMultitenancyApi
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
from aries_cloudcontroller.models.create_wallet_request import CreateWalletRequest
from aries_cloudcontroller.models.create_wallet_response import CreateWalletResponse
from aries_cloudcontroller.models.create_wallet_token_request import CreateWalletTokenRequest
from aries_cloudcontroller.models.create_wallet_token_response import CreateWalletTokenResponse
from aries_cloudcontroller.models.remove_wallet_request import RemoveWalletRequest
from aries_cloudcontroller.models.update_wallet_request import UpdateWalletRequest
from aries_cloudcontroller.models.wallet_list import WalletList
from aries_cloudcontroller.models.wallet_record import WalletRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/multitenancy/wallet",
    responses={
        200: {"model": CreateWalletResponse, "description": ""},
    },
    tags=["multitenancy"],
    summary="Create a subwallet",
    response_model_by_alias=True,
)
async def create_wallet(
    body: CreateWalletRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CreateWalletResponse:
    ...


@router.post(
    "/multitenancy/wallet/{wallet_id}/remove",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["multitenancy"],
    summary="Remove a subwallet",
    response_model_by_alias=True,
)
async def delete_wallet(
    wallet_id: str = Path(None, description="Subwallet identifier"),
    body: RemoveWalletRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/multitenancy/wallet/{wallet_id}/token",
    responses={
        200: {"model": CreateWalletTokenResponse, "description": ""},
    },
    tags=["multitenancy"],
    summary="Get auth token for a subwallet",
    response_model_by_alias=True,
)
async def get_auth_token(
    wallet_id: str = Path(None, description=""),
    body: CreateWalletTokenRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CreateWalletTokenResponse:
    ...


@router.get(
    "/multitenancy/wallets",
    responses={
        200: {"model": WalletList, "description": ""},
    },
    tags=["multitenancy"],
    summary="Query subwallets",
    response_model_by_alias=True,
)
async def get_matching_wallets(
    wallet_name: str = Query(None, description="Wallet name"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> WalletList:
    ...


@router.get(
    "/multitenancy/wallet/{wallet_id}",
    responses={
        200: {"model": WalletRecord, "description": ""},
    },
    tags=["multitenancy"],
    summary="Get a single subwallet",
    response_model_by_alias=True,
)
async def get_wallet_record(
    wallet_id: str = Path(None, description="Subwallet identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> WalletRecord:
    ...


@router.put(
    "/multitenancy/wallet/{wallet_id}",
    responses={
        200: {"model": WalletRecord, "description": ""},
    },
    tags=["multitenancy"],
    summary="Update a subwallet",
    response_model_by_alias=True,
)
async def update_wallet(
    wallet_id: str = Path(None, description="Subwallet identifier"),
    body: UpdateWalletRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> WalletRecord:
    ...
