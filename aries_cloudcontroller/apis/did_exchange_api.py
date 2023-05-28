# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.did_exchange_api_base import BaseDidExchangeApi
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
from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.didx_request import DIDXRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/didexchange/{conn_id}/accept-invitation",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["did-exchange"],
    summary="Accept a stored connection invitation",
    response_model_by_alias=True,
)
async def accept_didex_invitation(
    conn_id: str = Path(None, description="Connection identifier"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    my_label: str = Query(None, description="Label for connection request"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/didexchange/{conn_id}/accept-request",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["did-exchange"],
    summary="Accept a stored connection request",
    response_model_by_alias=True,
)
async def accept_didex_request(
    conn_id: str = Path(None, description="Connection identifier"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/didexchange/create-request",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["did-exchange"],
    summary="Create and send a request against public DID&#39;s implicit invitation",
    response_model_by_alias=True,
)
async def create_didex_request(
    their_public_did: str = Query(None, description="Qualified public DID to which to request connection", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+&#x3D;[a-zA-Z0-9_.:%-]*)*)(\\/[^#?]*)?([?][^#]*)?(\#.*)?$$"),
    alias: str = Query(None, description="Alias for connection"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    my_label: str = Query(None, description="Label for connection request"),
    use_public_did: bool = Query(None, description="Use public DID for this connection"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/didexchange/receive-request",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["did-exchange"],
    summary="Receive request against public DID&#39;s implicit invitation",
    response_model_by_alias=True,
)
async def receive_didex_request(
    alias: str = Query(None, description="Alias for connection"),
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    body: DIDXRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...
