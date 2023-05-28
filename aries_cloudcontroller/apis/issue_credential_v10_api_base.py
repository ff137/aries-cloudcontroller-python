# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseIssueCredentialV10Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIssueCredentialV10Api.subclasses = BaseIssueCredentialV10Api.subclasses + (cls,)
    def create_credential_record(
        self,
        body: V10CredentialCreate,
    ) -> V10CredentialExchange:
        ...


    def create_free_credential_offer(
        self,
        body: V10CredentialConnFreeOfferRequest,
    ) -> V10CredentialExchange:
        ...


    def delete_cred_ex_record(
        self,
        cred_ex_id: str,
    ) -> object:
        ...


    def get_cred_ex_record(
        self,
        cred_ex_id: str,
    ) -> V10CredentialExchange:
        ...


    def get_matching_cred_ex_records(
        self,
        connection_id: str,
        role: str,
        state: str,
        thread_id: str,
    ) -> V10CredentialExchangeListResult:
        ...


    def issue_credential_to_holder(
        self,
        cred_ex_id: str,
        body: V10CredentialIssueRequest,
    ) -> V10CredentialExchange:
        ...


    def report_cred_ex_problem(
        self,
        cred_ex_id: str,
        body: V10CredentialProblemReportRequest,
    ) -> object:
        ...


    def send_credential_offer(
        self,
        cred_ex_id: str,
        body: V10CredentialBoundOfferRequest,
    ) -> V10CredentialExchange:
        ...


    def send_credential_request(
        self,
        cred_ex_id: str,
    ) -> V10CredentialExchange:
        ...


    def send_free_credential(
        self,
        body: V10CredentialProposalRequestMand,
    ) -> V10CredentialExchange:
        ...


    def send_free_credential_offer(
        self,
        body: V10CredentialFreeOfferRequest,
    ) -> V10CredentialExchange:
        ...


    def send_free_credential_proposal(
        self,
        body: V10CredentialProposalRequestOpt,
    ) -> V10CredentialExchange:
        ...


    def store_received_credential(
        self,
        cred_ex_id: str,
        body: V10CredentialStoreRequest,
    ) -> V10CredentialExchange:
        ...
