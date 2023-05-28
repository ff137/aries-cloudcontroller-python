# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.mediation_api_base import BaseMediationApi
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
from aries_cloudcontroller.models.admin_mediation_deny import AdminMediationDeny
from aries_cloudcontroller.models.keylist import Keylist
from aries_cloudcontroller.models.keylist_query import KeylistQuery
from aries_cloudcontroller.models.keylist_query_filter_request import KeylistQueryFilterRequest
from aries_cloudcontroller.models.keylist_update import KeylistUpdate
from aries_cloudcontroller.models.keylist_update_request import KeylistUpdateRequest
from aries_cloudcontroller.models.mediation_create_request import MediationCreateRequest
from aries_cloudcontroller.models.mediation_deny import MediationDeny
from aries_cloudcontroller.models.mediation_grant import MediationGrant
from aries_cloudcontroller.models.mediation_id_match_info import MediationIdMatchInfo
from aries_cloudcontroller.models.mediation_list import MediationList
from aries_cloudcontroller.models.mediation_record import MediationRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/mediation/default-mediator",
    responses={
        201: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Clear default mediator",
    response_model_by_alias=True,
)
async def clear_default_mediator(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.delete(
    "/mediation/requests/{mediation_id}",
    responses={
        200: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Delete mediation request by ID",
    response_model_by_alias=True,
)
async def delete_mediation_record(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/requests/{mediation_id}/deny",
    responses={
        201: {"model": MediationDeny, "description": ""},
    },
    tags=["mediation"],
    summary="Deny a stored mediation request",
    response_model_by_alias=True,
)
async def deny_mediation_request(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    body: AdminMediationDeny = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationDeny:
    ...


@router.get(
    "/mediation/default-mediator",
    responses={
        200: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Get default mediator",
    response_model_by_alias=True,
)
async def get_default_mediator(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.get(
    "/mediation/keylists",
    responses={
        200: {"model": Keylist, "description": ""},
    },
    tags=["mediation"],
    summary="Retrieve keylists by connection or role",
    response_model_by_alias=True,
)
async def get_keylists(
    conn_id: str = Query(None, description="Connection identifier (optional)"),
    role: str = Query(&#39;server&#39;, description="Filer on role, &#39;client&#39; for keys         mediated by other agents, &#39;server&#39; for keys         mediated by this agent"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> Keylist:
    ...


@router.get(
    "/mediation/requests",
    responses={
        200: {"model": MediationList, "description": ""},
    },
    tags=["mediation"],
    summary="Query mediation requests, returns list of all mediation records",
    response_model_by_alias=True,
)
async def get_matching_mediation_records(
    conn_id: str = Query(None, description="Connection identifier (optional)"),
    mediator_terms: List[str] = Query(None, description="List of mediator rules for recipient"),
    recipient_terms: List[str] = Query(None, description="List of recipient rules for mediation"),
    state: str = Query(None, description="Mediation state (optional)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationList:
    ...


@router.get(
    "/mediation/requests/{mediation_id}",
    responses={
        200: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Retrieve mediation request record",
    response_model_by_alias=True,
)
async def get_mediation_record(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/requests/{mediation_id}/grant",
    responses={
        201: {"model": MediationGrant, "description": ""},
    },
    tags=["mediation"],
    summary="Grant received mediation",
    response_model_by_alias=True,
)
async def grant_mediation_request(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationGrant:
    ...


@router.post(
    "/mediation/request/{conn_id}",
    responses={
        201: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Request mediation from connection",
    response_model_by_alias=True,
)
async def request_mediation_for_connection(
    conn_id: str = Path(None, description="Connection identifier"),
    body: MediationCreateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/keylists/{mediation_id}/send-keylist-query",
    responses={
        201: {"model": KeylistQuery, "description": ""},
    },
    tags=["mediation"],
    summary="Send keylist query to mediator",
    response_model_by_alias=True,
)
async def send_keylist_query_to_mediator(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    paginate_limit: int = Query(-1, description="limit number of results"),
    paginate_offset: int = Query(0, description="offset to use in pagination"),
    body: KeylistQueryFilterRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> KeylistQuery:
    ...


@router.post(
    "/mediation/keylists/{mediation_id}/send-keylist-update",
    responses={
        201: {"model": KeylistUpdate, "description": ""},
    },
    tags=["mediation"],
    summary="Send keylist update to mediator",
    response_model_by_alias=True,
)
async def send_keylist_update_to_mediator(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    body: KeylistUpdateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> KeylistUpdate:
    ...


@router.put(
    "/mediation/{mediation_id}/default-mediator",
    responses={
        201: {"model": MediationRecord, "description": ""},
    },
    tags=["mediation"],
    summary="Set default mediator",
    response_model_by_alias=True,
)
async def set_default_mediator(
    mediation_id: str = Path(None, description="Mediation record identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> MediationRecord:
    ...


@router.post(
    "/mediation/update-keylist/{conn_id}",
    responses={
        200: {"model": KeylistUpdate, "description": ""},
    },
    tags=["mediation"],
    summary="Update keylist for a connection",
    response_model_by_alias=True,
)
async def update_keylist_for_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    body: MediationIdMatchInfo = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> KeylistUpdate:
    ...
