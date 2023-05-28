# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.ledger_api_base import BaseLedgerApi
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
from aries_cloudcontroller.models.get_did_endpoint_response import GetDIDEndpointResponse
from aries_cloudcontroller.models.get_did_verkey_response import GetDIDVerkeyResponse
from aries_cloudcontroller.models.get_nym_role_response import GetNymRoleResponse
from aries_cloudcontroller.models.ledger_config_list import LedgerConfigList
from aries_cloudcontroller.models.taa_accept import TAAAccept
from aries_cloudcontroller.models.taa_result import TAAResult
from aries_cloudcontroller.models.txn_or_register_ledger_nym_response import TxnOrRegisterLedgerNymResponse
from aries_cloudcontroller.models.write_ledger_request import WriteLedgerRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/ledger/taa/accept",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["ledger"],
    summary="Accept the transaction author agreement",
    response_model_by_alias=True,
)
async def accept_taa(
    body: TAAAccept = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/ledger/get-nym-role",
    responses={
        200: {"model": GetNymRoleResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the role from the NYM registration of a public DID.",
    response_model_by_alias=True,
)
async def get_did_nym_role(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetNymRoleResponse:
    ...


@router.get(
    "/ledger/did-verkey",
    responses={
        200: {"model": GetDIDVerkeyResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the verkey for a DID from the ledger.",
    response_model_by_alias=True,
)
async def get_did_verkey(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetDIDVerkeyResponse:
    ...


@router.get(
    "/ledger/multiple/config",
    responses={
        200: {"model": LedgerConfigList, "description": ""},
    },
    tags=["ledger"],
    summary="Fetch the multiple ledger configuration currently in use",
    response_model_by_alias=True,
)
async def get_multiple_ledger_config(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> LedgerConfigList:
    ...


@router.get(
    "/ledger/did-endpoint",
    responses={
        200: {"model": GetDIDEndpointResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Get the endpoint for a DID from the ledger.",
    response_model_by_alias=True,
)
async def get_published_did_endpoint(
    did: str = Query(None, description="DID of interest", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    endpoint_type: str = Query(None, description="Endpoint type of interest (default &#39;Endpoint&#39;)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> GetDIDEndpointResponse:
    ...


@router.get(
    "/ledger/taa",
    responses={
        200: {"model": TAAResult, "description": ""},
    },
    tags=["ledger"],
    summary="Fetch the current transaction author agreement, if any",
    response_model_by_alias=True,
)
async def get_taa(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TAAResult:
    ...


@router.get(
    "/ledger/multiple/get-write-ledger",
    responses={
        200: {"model": WriteLedgerRequest, "description": ""},
    },
    tags=["ledger"],
    summary="Fetch the current write ledger",
    response_model_by_alias=True,
)
async def get_write_ledger(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> WriteLedgerRequest:
    ...


@router.post(
    "/ledger/register-nym",
    responses={
        200: {"model": TxnOrRegisterLedgerNymResponse, "description": ""},
    },
    tags=["ledger"],
    summary="Send a NYM registration to the ledger.",
    response_model_by_alias=True,
)
async def register_nym(
    did: str = Query(None, description="DID to register", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    verkey: str = Query(None, description="Verification key", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"),
    alias: str = Query(None, description="Alias"),
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    role: str = Query(None, description="Role"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TxnOrRegisterLedgerNymResponse:
    ...


@router.patch(
    "/ledger/rotate-public-did-keypair",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["ledger"],
    summary="Rotate key pair for public DID.",
    response_model_by_alias=True,
)
async def rotate_public_did_keypair(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
