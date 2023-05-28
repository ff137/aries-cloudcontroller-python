# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.connection_api_base import BaseConnectionApi
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
from aries_cloudcontroller.models.connection_list import ConnectionList
from aries_cloudcontroller.models.connection_metadata import ConnectionMetadata
from aries_cloudcontroller.models.connection_metadata_set_request import ConnectionMetadataSetRequest
from aries_cloudcontroller.models.connection_static_request import ConnectionStaticRequest
from aries_cloudcontroller.models.connection_static_result import ConnectionStaticResult
from aries_cloudcontroller.models.create_invitation_request import CreateInvitationRequest
from aries_cloudcontroller.models.endpoints_result import EndpointsResult
from aries_cloudcontroller.models.invitation_result import InvitationResult
from aries_cloudcontroller.models.receive_invitation_request import ReceiveInvitationRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/connections/{conn_id}/accept-invitation",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["connection"],
    summary="Accept a stored connection invitation",
    response_model_by_alias=True,
)
async def accept_connection_invitation(
    conn_id: str = Path(None, description="Connection identifier"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    my_label: str = Query(None, description="Label for connection"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/connections/{conn_id}/accept-request",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["connection"],
    summary="Accept a stored connection request",
    response_model_by_alias=True,
)
async def accept_connection_request(
    conn_id: str = Path(None, description="Connection identifier"),
    my_endpoint: str = Query(None, description="My URL endpoint", regex=r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/connections/create-invitation",
    responses={
        200: {"model": InvitationResult, "description": ""},
    },
    tags=["connection"],
    summary="Create a new connection invitation",
    response_model_by_alias=True,
)
async def create_connection_invitation(
    alias: str = Query(None, description="Alias"),
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    multi_use: bool = Query(None, description="Create invitation for multiple use (default false)"),
    public: bool = Query(None, description="Create invitation from public DID (default false)"),
    body: CreateInvitationRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> InvitationResult:
    ...


@router.post(
    "/connections/create-static",
    responses={
        200: {"model": ConnectionStaticResult, "description": ""},
    },
    tags=["connection"],
    summary="Create a new static connection",
    response_model_by_alias=True,
)
async def create_static_connection(
    body: ConnectionStaticRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnectionStaticResult:
    ...


@router.delete(
    "/connections/{conn_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["connection"],
    summary="Remove an existing connection record",
    response_model_by_alias=True,
)
async def delete_connection_record(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/connections/{conn_id}/endpoints",
    responses={
        200: {"model": EndpointsResult, "description": ""},
    },
    tags=["connection"],
    summary="Fetch connection remote endpoint",
    response_model_by_alias=True,
)
async def get_connection_endpoint(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> EndpointsResult:
    ...


@router.get(
    "/connections/{conn_id}/metadata",
    responses={
        200: {"model": ConnectionMetadata, "description": ""},
    },
    tags=["connection"],
    summary="Fetch connection metadata",
    response_model_by_alias=True,
)
async def get_connection_metadata(
    conn_id: str = Path(None, description="Connection identifier"),
    key: str = Query(None, description="Key to retrieve."),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnectionMetadata:
    ...


@router.get(
    "/connections/{conn_id}",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["connection"],
    summary="Fetch a single connection record",
    response_model_by_alias=True,
)
async def get_connection_record(
    conn_id: str = Path(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.get(
    "/connections",
    responses={
        200: {"model": ConnectionList, "description": ""},
    },
    tags=["connection"],
    summary="Query agent-to-agent connections",
    response_model_by_alias=True,
)
async def get_matching_connections(
    alias: str = Query(None, description="Alias"),
    connection_protocol: str = Query(None, description="Connection protocol used"),
    invitation_key: str = Query(None, description="invitation key", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"),
    invitation_msg_id: str = Query(None, description="Identifier of the associated Invitation Mesage"),
    my_did: str = Query(None, description="My DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    state: str = Query(None, description="Connection state"),
    their_did: str = Query(None, description="Their DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    their_public_did: str = Query(None, description="Their Public DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    their_role: str = Query(None, description="Their role in the connection protocol"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnectionList:
    ...


@router.post(
    "/connections/receive-invitation",
    responses={
        200: {"model": ConnRecord, "description": ""},
    },
    tags=["connection"],
    summary="Receive a new connection invitation",
    response_model_by_alias=True,
)
async def receive_connection_invitation(
    alias: str = Query(None, description="Alias"),
    auto_accept: bool = Query(None, description="Auto-accept connection (defaults to configuration)"),
    mediation_id: str = Query(None, description="Identifier for active mediation record to be used", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: ReceiveInvitationRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnRecord:
    ...


@router.post(
    "/connections/{conn_id}/metadata",
    responses={
        200: {"model": ConnectionMetadata, "description": ""},
    },
    tags=["connection"],
    summary="Set connection metadata",
    response_model_by_alias=True,
)
async def set_connection_metadata(
    conn_id: str = Path(None, description="Connection identifier"),
    body: ConnectionMetadataSetRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> ConnectionMetadata:
    ...


@router.post(
    "/connections/{conn_id}/establish-inbound/{ref_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["connection"],
    summary="Assign another connection as the inbound connection",
    response_model_by_alias=True,
)
async def set_inbound_connection(
    conn_id: str = Path(None, description="Connection identifier"),
    ref_id: str = Path(None, description="Inbound connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
