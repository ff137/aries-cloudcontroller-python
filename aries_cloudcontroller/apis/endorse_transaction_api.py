# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.endorse_transaction_api_base import BaseEndorseTransactionApi
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
from aries_cloudcontroller.models.date import Date
from aries_cloudcontroller.models.endorser_info import EndorserInfo
from aries_cloudcontroller.models.transaction_jobs import TransactionJobs
from aries_cloudcontroller.models.transaction_list import TransactionList
from aries_cloudcontroller.models.transaction_record import TransactionRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/transactions/{tran_id}/cancel",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For Author to cancel a particular transaction request",
    response_model_by_alias=True,
)
async def cancel_transaction_request(
    tran_id: str = Path(None, description="Transaction identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transactions/create-request",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For author to send a transaction request",
    response_model_by_alias=True,
)
async def create_transaction_request(
    tran_id: str = Query(None, description="Transaction identifier"),
    endorser_write_txn: bool = Query(None, description="Endorser will write the transaction after endorsing it"),
    body: Date = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transactions/{tran_id}/endorse",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For Endorser to endorse a particular transaction record",
    response_model_by_alias=True,
)
async def endorse_transaction(
    tran_id: str = Path(None, description="Transaction identifier"),
    endorser_did: str = Query(None, description="Endorser DID"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.get(
    "/transactions",
    responses={
        200: {"model": TransactionList, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="Query transactions",
    response_model_by_alias=True,
)
async def get_transaction_list(
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionList:
    ...


@router.get(
    "/transactions/{tran_id}",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="Fetch a single transaction record",
    response_model_by_alias=True,
)
async def get_transaction_record(
    tran_id: str = Path(None, description="Transaction identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transactions/{tran_id}/write",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For Author / Endorser to write an endorsed transaction to the ledger",
    response_model_by_alias=True,
)
async def publish_endorsed_transaction(
    tran_id: str = Path(None, description="Transaction identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transactions/{tran_id}/refuse",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For Endorser to refuse a particular transaction record",
    response_model_by_alias=True,
)
async def refuse_transaction(
    tran_id: str = Path(None, description="Transaction identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transaction/{tran_id}/resend",
    responses={
        200: {"model": TransactionRecord, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="For Author to resend a particular transaction request",
    response_model_by_alias=True,
)
async def resend_transaction_request(
    tran_id: str = Path(None, description="Transaction identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionRecord:
    ...


@router.post(
    "/transactions/{conn_id}/set-endorser-info",
    responses={
        200: {"model": EndorserInfo, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="Set Endorser Info",
    response_model_by_alias=True,
)
async def set_endorser_info_for_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    endorser_did: str = Query(None, description="Endorser DID"),
    endorser_name: str = Query(None, description="Endorser Name"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> EndorserInfo:
    ...


@router.post(
    "/transactions/{conn_id}/set-endorser-role",
    responses={
        200: {"model": TransactionJobs, "description": ""},
    },
    tags=["endorse-transaction"],
    summary="Set transaction jobs",
    response_model_by_alias=True,
)
async def set_endorser_role_for_conn_id(
    conn_id: str = Path(None, description="Connection identifier"),
    transaction_my_job: str = Query(None, description="Transaction related jobs"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TransactionJobs:
    ...
