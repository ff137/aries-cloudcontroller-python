# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.indy_cred_precis import IndyCredPrecis
from aries_cloudcontroller.models.v20_pres_create_request_request import V20PresCreateRequestRequest
from aries_cloudcontroller.models.v20_pres_ex_record import V20PresExRecord
from aries_cloudcontroller.models.v20_pres_ex_record_list import V20PresExRecordList
from aries_cloudcontroller.models.v20_pres_problem_report_request import V20PresProblemReportRequest
from aries_cloudcontroller.models.v20_pres_proposal_request import V20PresProposalRequest
from aries_cloudcontroller.models.v20_pres_send_request_request import V20PresSendRequestRequest
from aries_cloudcontroller.models.v20_pres_spec_by_format_request import V20PresSpecByFormatRequest
from aries_cloudcontroller.models.v20_presentation_send_request_to_proposal import V20PresentationSendRequestToProposal
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BasePresentProofV20Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePresentProofV20Api.subclasses = BasePresentProofV20Api.subclasses + (cls,)
    def create_proof_request(
        self,
        body: V20PresCreateRequestRequest,
    ) -> V20PresExRecord:
        ...


    def delete_pres_ex_record(
        self,
        pres_ex_id: str,
    ) -> object:
        ...


    def get_matching_pres_ex_records(
        self,
        connection_id: str,
        role: str,
        state: str,
        thread_id: str,
    ) -> V20PresExRecordList:
        ...


    def get_pres_ex_credentials(
        self,
        pres_ex_id: str,
        count: str,
        extra_query: str,
        referent: str,
        start: str,
    ) -> List[IndyCredPrecis]:
        ...


    def get_pres_ex_record(
        self,
        pres_ex_id: str,
    ) -> V20PresExRecord:
        ...


    def report_pres_ex_problem(
        self,
        pres_ex_id: str,
        body: V20PresProblemReportRequest,
    ) -> object:
        ...


    def send_free_presentation_request(
        self,
        body: V20PresSendRequestRequest,
    ) -> V20PresExRecord:
        ...


    def send_presentation_proposal(
        self,
        body: V20PresProposalRequest,
    ) -> V20PresExRecord:
        ...


    def send_proof_presentation(
        self,
        pres_ex_id: str,
        body: V20PresSpecByFormatRequest,
    ) -> V20PresExRecord:
        ...


    def send_proof_presentation_request(
        self,
        pres_ex_id: str,
        body: V20PresentationSendRequestToProposal,
    ) -> V20PresExRecord:
        ...


    def verify_received_presentation(
        self,
        pres_ex_id: str,
    ) -> V20PresExRecord:
        ...
