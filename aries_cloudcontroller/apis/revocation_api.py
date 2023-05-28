# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.revocation_api_base import BaseRevocationApi
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
from aries_cloudcontroller.models.clear_pending_revocations_request import ClearPendingRevocationsRequest
from aries_cloudcontroller.models.cred_rev_indy_records_result import CredRevIndyRecordsResult
from aries_cloudcontroller.models.cred_rev_record_details_result import CredRevRecordDetailsResult
from aries_cloudcontroller.models.cred_rev_record_result import CredRevRecordResult
from aries_cloudcontroller.models.publish_revocations import PublishRevocations
from aries_cloudcontroller.models.rev_reg_create_request import RevRegCreateRequest
from aries_cloudcontroller.models.rev_reg_issued_result import RevRegIssuedResult
from aries_cloudcontroller.models.rev_reg_result import RevRegResult
from aries_cloudcontroller.models.rev_reg_update_tails_file_uri import RevRegUpdateTailsFileUri
from aries_cloudcontroller.models.rev_reg_wallet_updated_result import RevRegWalletUpdatedResult
from aries_cloudcontroller.models.rev_regs_created import RevRegsCreated
from aries_cloudcontroller.models.revoke_request import RevokeRequest
from aries_cloudcontroller.models.tails_delete_response import TailsDeleteResponse
from aries_cloudcontroller.models.txn_or_publish_revocations_result import TxnOrPublishRevocationsResult
from aries_cloudcontroller.models.txn_or_rev_reg_result import TxnOrRevRegResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/revocation/clear-pending-revocations",
    responses={
        200: {"model": PublishRevocations, "description": ""},
    },
    tags=["revocation"],
    summary="Clear pending revocations",
    response_model_by_alias=True,
)
async def clear_pending_revocations(
    body: ClearPendingRevocationsRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> PublishRevocations:
    ...


@router.post(
    "/revocation/create-registry",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Creates a new revocation registry",
    response_model_by_alias=True,
)
async def create_revocation_registry(
    body: RevRegCreateRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.delete(
    "/revocation/registry/delete-tails-file",
    responses={
        200: {"model": TailsDeleteResponse, "description": ""},
    },
    tags=["revocation"],
    summary="Delete the tail files",
    response_model_by_alias=True,
)
async def delete_tails_file(
    cred_def_id: str = Query(None, description="Credential definition identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    rev_reg_id: str = Query(None, description="Revocation registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TailsDeleteResponse:
    ...


@router.get(
    "/revocation/registry/{rev_reg_id}/tails-file",
    responses={
        200: {"model": file, "description": "tails file"},
    },
    tags=["revocation"],
    summary="Download tails file",
    response_model_by_alias=True,
)
async def download_tails_file(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> file:
    ...


@router.get(
    "/revocation/active-registry/{cred_def_id}",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get current active revocation registry by credential definition id",
    response_model_by_alias=True,
)
async def get_active_registry_for_cred_def_id(
    cred_def_id: str = Path(None, description="Credential definition identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.get(
    "/revocation/registries/created",
    responses={
        200: {"model": RevRegsCreated, "description": ""},
    },
    tags=["revocation"],
    summary="Search for matching revocation registries that current agent created",
    response_model_by_alias=True,
)
async def get_created_registries(
    cred_def_id: str = Query(None, description="Credential definition identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"),
    state: str = Query(None, description="Revocation registry state"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegsCreated:
    ...


@router.get(
    "/revocation/credential-record",
    responses={
        200: {"model": CredRevRecordResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get credential revocation status",
    response_model_by_alias=True,
)
async def get_credential_revocation_record(
    cred_ex_id: str = Query(None, description="Credential exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    cred_rev_id: str = Query(None, description="Credential revocation identifier", regex=r"^[1-9][0-9]*$"),
    rev_reg_id: str = Query(None, description="Revocation registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredRevRecordResult:
    ...


@router.get(
    "/revocation/registry/{rev_reg_id}/issued/details",
    responses={
        200: {"model": CredRevRecordDetailsResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get details of credentials issued against revocation registry",
    response_model_by_alias=True,
)
async def get_issued_credential_details(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredRevRecordDetailsResult:
    ...


@router.get(
    "/revocation/registry/{rev_reg_id}/issued",
    responses={
        200: {"model": RevRegIssuedResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get number of credentials issued against revocation registry",
    response_model_by_alias=True,
)
async def get_issued_credentials_count(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegIssuedResult:
    ...


@router.get(
    "/revocation/registry/{rev_reg_id}/issued/indy_recs",
    responses={
        200: {"model": CredRevIndyRecordsResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get details of revoked credentials from ledger",
    response_model_by_alias=True,
)
async def get_published_credential_details(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> CredRevIndyRecordsResult:
    ...


@router.get(
    "/revocation/registry/{rev_reg_id}",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Get revocation registry by revocation registry id",
    response_model_by_alias=True,
)
async def get_revocation_registry(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.post(
    "/revocation/registry/{rev_reg_id}/definition",
    responses={
        200: {"model": TxnOrRevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Send revocation registry definition to ledger",
    response_model_by_alias=True,
)
async def publish_revocation_registry_definition(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TxnOrRevRegResult:
    ...


@router.post(
    "/revocation/registry/{rev_reg_id}/entry",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Send revocation registry entry to ledger",
    response_model_by_alias=True,
)
async def publish_revocation_registry_entry(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    conn_id: str = Query(None, description="Connection identifier"),
    create_transaction_for_endorser: bool = Query(None, description="Create Transaction For Endorser&#39;s signature"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.post(
    "/revocation/publish-revocations",
    responses={
        200: {"model": TxnOrPublishRevocationsResult, "description": ""},
    },
    tags=["revocation"],
    summary="Publish pending revocations to ledger",
    response_model_by_alias=True,
)
async def publish_revocations(
    body: PublishRevocations = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> TxnOrPublishRevocationsResult:
    ...


@router.post(
    "/revocation/revoke",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["revocation"],
    summary="Revoke an issued credential",
    response_model_by_alias=True,
)
async def revoke_issued_credential(
    body: RevokeRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.patch(
    "/revocation/registry/{rev_reg_id}/set-state",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Set revocation registry state manually",
    response_model_by_alias=True,
)
async def set_revocation_registry_state(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    state: str = Query(None, description="Revocation registry state to set"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.put(
    "/revocation/registry/{rev_reg_id}/fix-revocation-entry-state",
    responses={
        200: {"model": RevRegWalletUpdatedResult, "description": ""},
    },
    tags=["revocation"],
    summary="Fix revocation state in wallet and return number of updated entries",
    response_model_by_alias=True,
)
async def update_revocation_entry_state(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    apply_ledger_update: bool = Query(None, description="Apply updated accumulator transaction to ledger"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegWalletUpdatedResult:
    ...


@router.patch(
    "/revocation/registry/{rev_reg_id}",
    responses={
        200: {"model": RevRegResult, "description": ""},
    },
    tags=["revocation"],
    summary="Update revocation registry with new public URI to its tails file",
    response_model_by_alias=True,
)
async def update_revocation_registry(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    body: RevRegUpdateTailsFileUri = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> RevRegResult:
    ...


@router.put(
    "/revocation/registry/{rev_reg_id}/tails-file",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["revocation"],
    summary="Upload local tails file to server",
    response_model_by_alias=True,
)
async def upload_tails_file(
    rev_reg_id: str = Path(None, description="Revocation Registry identifier", regex=r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...
