# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.issue_credential_v20_api_base import BaseIssueCredentialV20Api
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
from aries_cloudcontroller.models.v20_cred_bound_offer_request import V20CredBoundOfferRequest
from aries_cloudcontroller.models.v20_cred_ex_free import V20CredExFree
from aries_cloudcontroller.models.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.models.v20_cred_ex_record_detail import V20CredExRecordDetail
from aries_cloudcontroller.models.v20_cred_ex_record_list_result import V20CredExRecordListResult
from aries_cloudcontroller.models.v20_cred_issue_problem_report_request import V20CredIssueProblemReportRequest
from aries_cloudcontroller.models.v20_cred_issue_request import V20CredIssueRequest
from aries_cloudcontroller.models.v20_cred_offer_conn_free_request import V20CredOfferConnFreeRequest
from aries_cloudcontroller.models.v20_cred_offer_request import V20CredOfferRequest
from aries_cloudcontroller.models.v20_cred_request_free import V20CredRequestFree
from aries_cloudcontroller.models.v20_cred_request_request import V20CredRequestRequest
from aries_cloudcontroller.models.v20_cred_store_request import V20CredStoreRequest
from aries_cloudcontroller.models.v20_issue_cred_schema_core import V20IssueCredSchemaCore
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/issue-credential-2.0/create",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Create a credential record without sending (generally for use with Out-Of-Band)",
    response_model_by_alias=True,
)
async def create_credential_record(
    body: V20IssueCredSchemaCore = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/create-offer",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Create a credential offer, independent of any proposal or connection",
    response_model_by_alias=True,
)
async def create_free_credential_offer(
    body: V20CredOfferConnFreeRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.delete(
    "/issue-credential-2.0/records/{cred_ex_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Remove an existing credential exchange record",
    response_model_by_alias=True,
)
async def delete_cred_ex_record(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/issue-credential-2.0/records/{cred_ex_id}",
    responses={
        200: {"model": V20CredExRecordDetail, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Fetch a single credential exchange record",
    response_model_by_alias=True,
)
async def get_cred_ex_record(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecordDetail:
    ...


@router.get(
    "/issue-credential-2.0/records",
    responses={
        200: {"model": V20CredExRecordListResult, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Fetch all credential exchange records",
    response_model_by_alias=True,
)
async def get_matching_cred_ex_records(
    connection_id: str = Query(None, description="Connection identifier"),
    role: str = Query(None, description="Role assigned in credential exchange"),
    state: str = Query(None, description="Credential exchange state"),
    thread_id: str = Query(None, description="Thread identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecordListResult:
    ...


@router.post(
    "/issue-credential-2.0/records/{cred_ex_id}/issue",
    responses={
        200: {"model": V20CredExRecordDetail, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send holder a credential",
    response_model_by_alias=True,
)
async def issue_credential_to_holder(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20CredIssueRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecordDetail:
    ...


@router.post(
    "/issue-credential-2.0/records/{cred_ex_id}/problem-report",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send a problem report for credential exchange",
    response_model_by_alias=True,
)
async def report_cred_ex_problem(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20CredIssueProblemReportRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/issue-credential-2.0/records/{cred_ex_id}/send-offer",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send holder a credential offer in reference to a proposal with preview",
    response_model_by_alias=True,
)
async def send_credential_offer(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20CredBoundOfferRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/records/{cred_ex_id}/send-request",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send issuer a credential request",
    response_model_by_alias=True,
)
async def send_credential_request(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20CredRequestRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/send",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send holder a credential, automating entire flow",
    response_model_by_alias=True,
)
async def send_free_credential(
    body: V20CredExFree = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/send-offer",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send holder a credential offer, independent of any proposal",
    response_model_by_alias=True,
)
async def send_free_credential_offer(
    body: V20CredOfferRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/send-proposal",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send issuer a credential proposal",
    response_model_by_alias=True,
)
async def send_free_credential_proposal(
    body: V20CredExFree = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/send-request",
    responses={
        200: {"model": V20CredExRecord, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request",
    response_model_by_alias=True,
)
async def send_free_credential_request(
    body: V20CredRequestFree = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecord:
    ...


@router.post(
    "/issue-credential-2.0/records/{cred_ex_id}/store",
    responses={
        200: {"model": V20CredExRecordDetail, "description": ""},
    },
    tags=["issue-credential v2.0"],
    summary="Store a received credential",
    response_model_by_alias=True,
)
async def store_received_credential(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20CredStoreRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20CredExRecordDetail:
    ...
