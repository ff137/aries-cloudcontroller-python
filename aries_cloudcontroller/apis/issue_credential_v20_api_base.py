# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseIssueCredentialV20Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIssueCredentialV20Api.subclasses = BaseIssueCredentialV20Api.subclasses + (cls,)
    def create_credential_record(
        self,
        body: V20IssueCredSchemaCore,
    ) -> V20CredExRecord:
        ...


    def create_free_credential_offer(
        self,
        body: V20CredOfferConnFreeRequest,
    ) -> V20CredExRecord:
        ...


    def delete_cred_ex_record(
        self,
        cred_ex_id: str,
    ) -> object:
        ...


    def get_cred_ex_record(
        self,
        cred_ex_id: str,
    ) -> V20CredExRecordDetail:
        ...


    def get_matching_cred_ex_records(
        self,
        connection_id: str,
        role: str,
        state: str,
        thread_id: str,
    ) -> V20CredExRecordListResult:
        ...


    def issue_credential_to_holder(
        self,
        cred_ex_id: str,
        body: V20CredIssueRequest,
    ) -> V20CredExRecordDetail:
        ...


    def report_cred_ex_problem(
        self,
        cred_ex_id: str,
        body: V20CredIssueProblemReportRequest,
    ) -> object:
        ...


    def send_credential_offer(
        self,
        cred_ex_id: str,
        body: V20CredBoundOfferRequest,
    ) -> V20CredExRecord:
        ...


    def send_credential_request(
        self,
        cred_ex_id: str,
        body: V20CredRequestRequest,
    ) -> V20CredExRecord:
        ...


    def send_free_credential(
        self,
        body: V20CredExFree,
    ) -> V20CredExRecord:
        ...


    def send_free_credential_offer(
        self,
        body: V20CredOfferRequest,
    ) -> V20CredExRecord:
        ...


    def send_free_credential_proposal(
        self,
        body: V20CredExFree,
    ) -> V20CredExRecord:
        ...


    def send_free_credential_request(
        self,
        body: V20CredRequestFree,
    ) -> V20CredExRecord:
        ...


    def store_received_credential(
        self,
        cred_ex_id: str,
        body: V20CredStoreRequest,
    ) -> V20CredExRecordDetail:
        ...
