# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.issue_credential_v10_api_base import BaseIssueCredentialV10Api
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
from aries_cloudcontroller.models.v10_credential_bound_offer_request import V10CredentialBoundOfferRequest
from aries_cloudcontroller.models.v10_credential_conn_free_offer_request import V10CredentialConnFreeOfferRequest
from aries_cloudcontroller.models.v10_credential_create import V10CredentialCreate
from aries_cloudcontroller.models.v10_credential_exchange import V10CredentialExchange
from aries_cloudcontroller.models.v10_credential_exchange_list_result import V10CredentialExchangeListResult
from aries_cloudcontroller.models.v10_credential_free_offer_request import V10CredentialFreeOfferRequest
from aries_cloudcontroller.models.v10_credential_issue_request import V10CredentialIssueRequest
from aries_cloudcontroller.models.v10_credential_problem_report_request import V10CredentialProblemReportRequest
from aries_cloudcontroller.models.v10_credential_proposal_request_mand import V10CredentialProposalRequestMand
from aries_cloudcontroller.models.v10_credential_proposal_request_opt import V10CredentialProposalRequestOpt
from aries_cloudcontroller.models.v10_credential_store_request import V10CredentialStoreRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/issue-credential/create",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Create a credential record without sending (generally for use with Out-Of-Band)",
    response_model_by_alias=True,
)
async def create_credential_record(
    body: V10CredentialCreate = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/create-offer",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Create a credential offer, independent of any proposal or connection",
    response_model_by_alias=True,
)
async def create_free_credential_offer(
    body: V10CredentialConnFreeOfferRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.delete(
    "/issue-credential/records/{cred_ex_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["issue-credential v1.0"],
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
    "/issue-credential/records/{cred_ex_id}",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Fetch a single credential exchange record",
    response_model_by_alias=True,
)
async def get_cred_ex_record(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.get(
    "/issue-credential/records",
    responses={
        200: {"model": V10CredentialExchangeListResult, "description": ""},
    },
    tags=["issue-credential v1.0"],
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
) -> V10CredentialExchangeListResult:
    ...


@router.post(
    "/issue-credential/records/{cred_ex_id}/issue",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send holder a credential",
    response_model_by_alias=True,
)
async def issue_credential_to_holder(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V10CredentialIssueRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/records/{cred_ex_id}/problem-report",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send a problem report for credential exchange",
    response_model_by_alias=True,
)
async def report_cred_ex_problem(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V10CredentialProblemReportRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/issue-credential/records/{cred_ex_id}/send-offer",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send holder a credential offer in reference to a proposal with preview",
    response_model_by_alias=True,
)
async def send_credential_offer(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V10CredentialBoundOfferRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/records/{cred_ex_id}/send-request",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send issuer a credential request",
    response_model_by_alias=True,
)
async def send_credential_request(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/send",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send holder a credential, automating entire flow",
    response_model_by_alias=True,
)
async def send_free_credential(
    body: V10CredentialProposalRequestMand = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/send-offer",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send holder a credential offer, independent of any proposal",
    response_model_by_alias=True,
)
async def send_free_credential_offer(
    body: V10CredentialFreeOfferRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/send-proposal",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Send issuer a credential proposal",
    response_model_by_alias=True,
)
async def send_free_credential_proposal(
    body: V10CredentialProposalRequestOpt = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...


@router.post(
    "/issue-credential/records/{cred_ex_id}/store",
    responses={
        200: {"model": V10CredentialExchange, "description": ""},
    },
    tags=["issue-credential v1.0"],
    summary="Store a received credential",
    response_model_by_alias=True,
)
async def store_received_credential(
    cred_ex_id: str = Path(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V10CredentialStoreRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V10CredentialExchange:
    ...
