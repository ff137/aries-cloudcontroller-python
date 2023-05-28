# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.schema_api_base import BaseSchemaApi
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
from aries_cloudcontroller.models.schema_get_result import SchemaGetResult
from aries_cloudcontroller.models.schema_send_request import SchemaSendRequest
from aries_cloudcontroller.models.schemas_created_result import SchemasCreatedResult
from aries_cloudcontroller.models.txn_or_schema_send_result import TxnOrSchemaSendResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/schemas/created",
    responses={
        200: {"model": SchemasCreatedResult, "description": ""},
    },
    tags=["schema"],
    summary="Search for matching schema that agent originated",
    response_model_by_alias=True,
)
async def get_matching_created_schemas(
    schema_id: str = Query(None, description="Schema identifier", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"),
    schema_issuer_did: str = Query(None, description="Schema issuer DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    schema_name: str = Query(None, description="Schema name"),
    schema_version: str = Query(None, description="Schema version", regex=r"^[0-9.]+$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> SchemasCreatedResult:
    ...


@router.get(
    "/schemas/{schema_id}",
    responses={
        200: {"model": SchemaGetResult, "description": ""},
    },
    tags=["schema"],
    summary="Gets a schema from the ledger",
    response_model_by_alias=True,
)
async def get_schema(
    schema_id: str = Path(None, description="Schema identifier", regex=r"^[1-9][0-9]*|[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> SchemaGetResult:
    ...


@router.post(
    "/schemas",
    responses={
        200: {"model": TxnOrSchemaSendResult, "description": ""},
    },
    tags=["schema"],
    summary="Sends a schema to the ledger",
    response_model_by_alias=True,
)
async def publish_schema(
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    body: SchemaSendRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TxnOrSchemaSendResult:
    ...


@router.post(
    "/schemas/{schema_id}/write_record",
    responses={
        200: {"model": SchemaGetResult, "description": ""},
    },
    tags=["schema"],
    summary="Writes a schema non-secret record to the wallet",
    response_model_by_alias=True,
)
async def write_schema_record_to_wallet(
    schema_id: str = Path(None, description="Schema identifier", regex=r"^[1-9][0-9]*|[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> SchemaGetResult:
    ...
