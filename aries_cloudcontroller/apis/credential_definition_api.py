# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.credential_definition_api_base import BaseCredentialDefinitionApi
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
from aries_cloudcontroller.models.credential_definition_get_result import CredentialDefinitionGetResult
from aries_cloudcontroller.models.credential_definition_send_request import CredentialDefinitionSendRequest
from aries_cloudcontroller.models.credential_definitions_created_result import CredentialDefinitionsCreatedResult
from aries_cloudcontroller.models.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/credential-definitions/created",
    responses={
        200: {"model": CredentialDefinitionsCreatedResult, "description": ""},
    },
    tags=["credential-definition"],
    summary="Search for matching credential definitions that agent originated",
    response_model_by_alias=True,
)
async def get_created_cred_defs(
    cred_def_id: str = Query(None, description="Credential definition id", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    issuer_did: str = Query(None, description="Issuer DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    schema_id: str = Query(None, description="Schema identifier", regex=r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"),
    schema_issuer_did: str = Query(None, description="Schema issuer DID", regex=r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"),
    schema_name: str = Query(None, description="Schema name"),
    schema_version: str = Query(None, description="Schema version", regex=r"^[0-9.]+$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredentialDefinitionsCreatedResult:
    ...


@router.get(
    "/credential-definitions/{cred_def_id}",
    responses={
        200: {"model": CredentialDefinitionGetResult, "description": ""},
    },
    tags=["credential-definition"],
    summary="Gets a credential definition from the ledger",
    response_model_by_alias=True,
)
async def get_credential_definition(
    cred_def_id: str = Path(None, description="Credential definition identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredentialDefinitionGetResult:
    ...


@router.post(
    "/credential-definitions",
    responses={
        200: {"model": TxnOrCredentialDefinitionSendResult, "description": ""},
    },
    tags=["credential-definition"],
    summary="Sends a credential definition to the ledger",
    response_model_by_alias=True,
)
async def publish_credential_definition(
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    body: CredentialDefinitionSendRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TxnOrCredentialDefinitionSendResult:
    ...


@router.post(
    "/credential-definitions/{cred_def_id}/write_record",
    responses={
        200: {"model": CredentialDefinitionGetResult, "description": ""},
    },
    tags=["credential-definition"],
    summary="Writes a credential definition non-secret record to the wallet",
    response_model_by_alias=True,
)
async def write_credential_definition(
    cred_def_id: str = Path(None, description="Credential definition identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredentialDefinitionGetResult:
    ...
