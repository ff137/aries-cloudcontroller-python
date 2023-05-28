# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.discover_features_api_base import BaseDiscoverFeaturesApi
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
from aries_cloudcontroller.models.v10_discovery_exchange_list_result import V10DiscoveryExchangeListResult
from aries_cloudcontroller.models.v10_discovery_record import V10DiscoveryRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/discover-features/records",
    responses={
        200: {"model": V10DiscoveryExchangeListResult, "description": ""},
    },
    tags=["discover-features"],
    summary="Discover Features records",
    response_model_by_alias=True,
)
async def get_v10_feature_records(
    connection_id: str = Query(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10DiscoveryExchangeListResult:
    ...


@router.get(
    "/discover-features/query",
    responses={
        200: {"model": V10DiscoveryRecord, "description": ""},
    },
    tags=["discover-features"],
    summary="Query supported features",
    response_model_by_alias=True,
)
async def get_v10_features_query(
    comment: str = Query(None, description="Comment"),
    connection_id: str = Query(None, description="Connection identifier, if none specified, then the query will provide features for this agent."),
    query: str = Query(None, description="Protocol feature query"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10DiscoveryRecord:
    ...
