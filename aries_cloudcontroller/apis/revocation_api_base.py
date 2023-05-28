# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseRevocationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRevocationApi.subclasses = BaseRevocationApi.subclasses + (cls,)
    def clear_pending_revocations(
        self,
        body: ClearPendingRevocationsRequest,
    ) -> PublishRevocations:
        ...


    def create_revocation_registry(
        self,
        body: RevRegCreateRequest,
    ) -> RevRegResult:
        ...


    def delete_tails_file(
        self,
        cred_def_id: str,
        rev_reg_id: str,
    ) -> TailsDeleteResponse:
        ...


    def download_tails_file(
        self,
        rev_reg_id: str,
    ) -> file:
        ...


    def get_active_registry_for_cred_def_id(
        self,
        cred_def_id: str,
    ) -> RevRegResult:
        ...


    def get_created_registries(
        self,
        cred_def_id: str,
        state: str,
    ) -> RevRegsCreated:
        ...


    def get_credential_revocation_record(
        self,
        cred_ex_id: str,
        cred_rev_id: str,
        rev_reg_id: str,
    ) -> CredRevRecordResult:
        ...


    def get_issued_credential_details(
        self,
        rev_reg_id: str,
    ) -> CredRevRecordDetailsResult:
        ...


    def get_issued_credentials_count(
        self,
        rev_reg_id: str,
    ) -> RevRegIssuedResult:
        ...


    def get_published_credential_details(
        self,
        rev_reg_id: str,
    ) -> CredRevIndyRecordsResult:
        ...


    def get_revocation_registry(
        self,
        rev_reg_id: str,
    ) -> RevRegResult:
        ...


    def publish_revocation_registry_definition(
        self,
        rev_reg_id: str,
        conn_id: str,
        create_transaction_for_endorser: bool,
    ) -> TxnOrRevRegResult:
        ...


    def publish_revocation_registry_entry(
        self,
        rev_reg_id: str,
        conn_id: str,
        create_transaction_for_endorser: bool,
    ) -> RevRegResult:
        ...


    def publish_revocations(
        self,
        body: PublishRevocations,
    ) -> TxnOrPublishRevocationsResult:
        ...


    def revoke_issued_credential(
        self,
        body: RevokeRequest,
    ) -> object:
        ...


    def set_revocation_registry_state(
        self,
        rev_reg_id: str,
        state: str,
    ) -> RevRegResult:
        ...


    def update_revocation_entry_state(
        self,
        rev_reg_id: str,
        apply_ledger_update: bool,
    ) -> RevRegWalletUpdatedResult:
        ...


    def update_revocation_registry(
        self,
        rev_reg_id: str,
        body: RevRegUpdateTailsFileUri,
    ) -> RevRegResult:
        ...


    def upload_tails_file(
        self,
        rev_reg_id: str,
    ) -> object:
        ...
