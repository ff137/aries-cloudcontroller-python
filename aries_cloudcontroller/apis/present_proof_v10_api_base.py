# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.indy_cred_precis import IndyCredPrecis
from aries_cloudcontroller.models.indy_pres_spec import IndyPresSpec
from aries_cloudcontroller.models.v10_presentation_create_request_request import V10PresentationCreateRequestRequest
from aries_cloudcontroller.models.v10_presentation_exchange import V10PresentationExchange
from aries_cloudcontroller.models.v10_presentation_exchange_list import V10PresentationExchangeList
from aries_cloudcontroller.models.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
from aries_cloudcontroller.models.v10_presentation_proposal_request import V10PresentationProposalRequest
from aries_cloudcontroller.models.v10_presentation_send_request_request import V10PresentationSendRequestRequest
from aries_cloudcontroller.models.v10_presentation_send_request_to_proposal import V10PresentationSendRequestToProposal
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BasePresentProofV10Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePresentProofV10Api.subclasses = BasePresentProofV10Api.subclasses + (cls,)
    def create_free_proof_request(
        self,
        body: V10PresentationCreateRequestRequest,
    ) -> V10PresentationExchange:
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
    ) -> V10PresentationExchangeList:
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
    ) -> V10PresentationExchange:
        ...


    def report_pres_ex_problem(
        self,
        pres_ex_id: str,
        body: V10PresentationProblemReportRequest,
    ) -> object:
        ...


    def send_free_presentation_request(
        self,
        body: V10PresentationSendRequestRequest,
    ) -> V10PresentationExchange:
        ...


    def send_presentation_proposal(
        self,
        body: V10PresentationProposalRequest,
    ) -> V10PresentationExchange:
        ...


    def send_proof_presentation(
        self,
        pres_ex_id: str,
        body: IndyPresSpec,
    ) -> V10PresentationExchange:
        ...


    def send_proof_presentation_request(
        self,
        pres_ex_id: str,
        body: V10PresentationSendRequestToProposal,
    ) -> V10PresentationExchange:
        ...


    def verify_received_presentation(
        self,
        pres_ex_id: str,
    ) -> V10PresentationExchange:
        ...
