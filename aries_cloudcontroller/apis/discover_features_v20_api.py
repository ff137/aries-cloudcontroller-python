# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.discover_features_v20_api_base import BaseDiscoverFeaturesV20Api
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
from aries_cloudcontroller.models.v20_discovery_exchange_list_result import V20DiscoveryExchangeListResult
from aries_cloudcontroller.models.v20_discovery_exchange_result import V20DiscoveryExchangeResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/discover-features-2.0/records",
    responses={
        200: {"model": V20DiscoveryExchangeListResult, "description": ""},
    },
    tags=["discover-features v2.0"],
    summary="Discover Features v2.0 records",
    response_model_by_alias=True,
)
async def get_v20_feature_records(
    connection_id: str = Query(None, description="Connection identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20DiscoveryExchangeListResult:
    ...


@router.get(
    "/discover-features-2.0/queries",
    responses={
        200: {"model": V20DiscoveryExchangeResult, "description": ""},
    },
    tags=["discover-features v2.0"],
    summary="Query supported features",
    response_model_by_alias=True,
)
async def get_v20_features_queries(
    connection_id: str = Query(None, description="Connection identifier, if none specified, then the query will provide features for this agent."),
    query_goal_code: str = Query(None, description="Goal-code feature-type query"),
    query_protocol: str = Query(None, description="Protocol feature-type query"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20DiscoveryExchangeResult:
    ...
