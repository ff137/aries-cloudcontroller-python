# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.wallet_api_base import BaseWalletApi
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
from aries_cloudcontroller.models.did_create import DIDCreate
from aries_cloudcontroller.models.did_endpoint import DIDEndpoint
from aries_cloudcontroller.models.did_endpoint_with_type import DIDEndpointWithType
from aries_cloudcontroller.models.did_list import DIDList
from aries_cloudcontroller.models.did_result import DIDResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/wallet/did/create",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Create a local DID",
    response_model_by_alias=True,
)
async def create_local_did(
    body: DIDCreate = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...


@router.get(
    "/wallet/get-did-endpoint",
    responses={
        200: {"model": DIDEndpoint, "description": ""},
    },
    tags=["wallet"],
    summary="Query DID endpoint in wallet",
    response_model_by_alias=True,
)
async def get_did_endpoint(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDEndpoint:
    ...


@router.get(
    "/wallet/did",
    responses={
        200: {"model": DIDList, "description": ""},
    },
    tags=["wallet"],
    summary="List wallet DIDs",
    response_model_by_alias=True,
)
async def get_dids(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+&#x3D;[a-zA-Z0-9_.:%-]*)*)(\\/[^#?]*)?([?][^#]*)?(\#.*)?$$"),
    key_type: str = Query(None, description="Key type to query for."),
    method: str = Query(None, description="DID method to query for. e.g. sov to only fetch indy/sov DIDs"),
    posture: str = Query(None, description="Whether DID is current public DID, posted to ledger but current public DID, or local to the wallet"),
    verkey: str = Query(None, description="Verification key of interest", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDList:
    ...


@router.get(
    "/wallet/did/public",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Fetch the current public DID",
    response_model_by_alias=True,
)
async def get_public_did(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...


@router.patch(
    "/wallet/did/local/rotate-keypair",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["wallet"],
    summary="Rotate keypair for a DID not posted to the ledger",
    response_model_by_alias=True,
)
async def rotate_keypair(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/wallet/set-did-endpoint",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["wallet"],
    summary="Update endpoint in wallet and on ledger if posted to it",
    response_model_by_alias=True,
)
async def set_did_endpoint(
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    body: DIDEndpointWithType = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/wallet/did/public",
    responses={
        200: {"model": DIDResult, "description": ""},
    },
    tags=["wallet"],
    summary="Assign the current public DID",
    response_model_by_alias=True,
)
async def set_public_did(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    mediation_id: str = Query(None, description="Mediation identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> DIDResult:
    ...
