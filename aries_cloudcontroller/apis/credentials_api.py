# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.credentials_api_base import BaseCredentialsApi
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
from aries_cloudcontroller.models.attribute_mime_types_result import AttributeMimeTypesResult
from aries_cloudcontroller.models.cred_info_list import CredInfoList
from aries_cloudcontroller.models.cred_revoked_result import CredRevokedResult
from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.models.vc_record import VCRecord
from aries_cloudcontroller.models.vc_record_list import VCRecordList
from aries_cloudcontroller.models.w3_c_credentials_list_request import W3CCredentialsListRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/credential/{credential_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["credentials"],
    summary="Remove credential from wallet by id",
    response_model_by_alias=True,
)
async def delete_credential_record(
    credential_id: str = Path(None, description="Credential identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.delete(
    "/credential/w3c/{credential_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["credentials"],
    summary="Remove W3C credential from wallet by id",
    response_model_by_alias=True,
)
async def delete_w3c_credential(
    credential_id: str = Path(None, description="Credential identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/credential/mime-types/{credential_id}",
    responses={
        200: {"model": AttributeMimeTypesResult, "description": ""},
    },
    tags=["credentials"],
    summary="Get attribute MIME types from wallet",
    response_model_by_alias=True,
)
async def get_credential_mime_types(
    credential_id: str = Path(None, description="Credential identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> AttributeMimeTypesResult:
    ...


@router.get(
    "/credential/{credential_id}",
    responses={
        200: {"model": IndyCredInfo, "description": ""},
    },
    tags=["credentials"],
    summary="Fetch credential from wallet by id",
    response_model_by_alias=True,
)
async def get_credential_record(
    credential_id: str = Path(None, description="Credential identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> IndyCredInfo:
    ...


@router.get(
    "/credentials",
    responses={
        200: {"model": CredInfoList, "description": ""},
    },
    tags=["credentials"],
    summary="Fetch credentials from wallet",
    response_model_by_alias=True,
)
async def get_credentials(
    count: str = Query(None, description="Maximum number to retrieve", regex=r"^[1-9][0-9]*$"),
    start: str = Query(None, description="Start index", regex=r"^[0-9]*$"),
    wql: str = Query(None, description="(JSON) WQL query", regex=r"^{.*}$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredInfoList:
    ...


@router.get(
    "/credential/revoked/{credential_id}",
    responses={
        200: {"model": CredRevokedResult, "description": ""},
    },
    tags=["credentials"],
    summary="Query credential revocation status by id",
    response_model_by_alias=True,
)
async def get_revocation_status(
    credential_id: str = Path(None, description="Credential identifier"),
    _from: str = Query(None, description="Earliest epoch of revocation status interval of interest", regex=r"^[0-9]*$"),
    to: str = Query(None, description="Latest epoch of revocation status interval of interest", regex=r"^[0-9]*$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredRevokedResult:
    ...


@router.get(
    "/credential/w3c/{credential_id}",
    responses={
        200: {"model": VCRecord, "description": ""},
    },
    tags=["credentials"],
    summary="Fetch W3C credential from wallet by id",
    response_model_by_alias=True,
)
async def get_w3c_credential(
    credential_id: str = Path(None, description="Credential identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> VCRecord:
    ...


@router.post(
    "/credentials/w3c",
    responses={
        200: {"model": VCRecordList, "description": ""},
    },
    tags=["credentials"],
    summary="Fetch W3C credentials from wallet",
    response_model_by_alias=True,
)
async def get_w3c_credentials(
    count: str = Query(None, description="Maximum number to retrieve", regex=r"^[1-9][0-9]*$"),
    start: str = Query(None, description="Start index", regex=r"^[0-9]*$"),
    wql: str = Query(None, description="(JSON) WQL query", regex=r"^{.*}$"),
    body: W3CCredentialsListRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> VCRecordList:
    ...
