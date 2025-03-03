from uplink import (
    Consumer,
    Path,
    Query,
    Body,
    Header,
    get,
    post,
    patch,
    put,
    delete,
    returns,
    json,
)

from typing import Any, Dict, List, Optional, Union  # noqa: F401

from aries_cloudcontroller.uplink_util import bool_query

from aries_cloudcontroller.model.v20_cred_bound_offer_request import (
    V20CredBoundOfferRequest,
)
from aries_cloudcontroller.model.v20_cred_ex_free import V20CredExFree
from aries_cloudcontroller.model.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.model.v20_cred_ex_record_detail import V20CredExRecordDetail
from aries_cloudcontroller.model.v20_cred_ex_record_list_result import (
    V20CredExRecordListResult,
)
from aries_cloudcontroller.model.v20_cred_issue_problem_report_request import (
    V20CredIssueProblemReportRequest,
)
from aries_cloudcontroller.model.v20_cred_issue_request import V20CredIssueRequest
from aries_cloudcontroller.model.v20_cred_offer_conn_free_request import (
    V20CredOfferConnFreeRequest,
)
from aries_cloudcontroller.model.v20_cred_offer_request import V20CredOfferRequest
from aries_cloudcontroller.model.v20_cred_request_free import V20CredRequestFree
from aries_cloudcontroller.model.v20_cred_request_request import V20CredRequestRequest
from aries_cloudcontroller.model.v20_cred_store_request import V20CredStoreRequest
from aries_cloudcontroller.model.v20_issue_cred_schema_core import (
    V20IssueCredSchemaCore,
)


class IssueCredentialV20Api(Consumer):
    async def create_credential(
        self, *, body: Optional[V20IssueCredSchemaCore] = None
    ) -> V20CredExRecord:
        """Create a credential record without sending (generally for use with Out-Of-Band)"""
        if not body:
            body = V20IssueCredSchemaCore()
        return await self.__create_credential(
            body=body,
        )

    async def delete_record(self, *, cred_ex_id: str) -> Dict[str, Any]:
        """Remove an existing credential exchange record"""
        return await self.__delete_record(
            cred_ex_id=cred_ex_id,
        )

    async def get_record(self, *, cred_ex_id: str) -> V20CredExRecordDetail:
        """Fetch a single credential exchange record"""
        return await self.__get_record(
            cred_ex_id=cred_ex_id,
        )

    async def get_records(
        self,
        *,
        connection_id: Optional[str] = None,
        role: Optional[str] = None,
        state: Optional[str] = None,
        thread_id: Optional[str] = None
    ) -> V20CredExRecordListResult:
        """Fetch all credential exchange records"""
        return await self.__get_records(
            connection_id=connection_id,
            role=role,
            state=state,
            thread_id=thread_id,
        )

    async def issue_credential(
        self, *, cred_ex_id: str, body: Optional[V20CredIssueRequest] = None
    ) -> V20CredExRecordDetail:
        """Send holder a credential"""
        if not body:
            body = V20CredIssueRequest()
        return await self.__issue_credential(
            cred_ex_id=cred_ex_id,
            body=body,
        )

    async def issue_credential20_create_offer_post(
        self, *, body: Optional[V20CredOfferConnFreeRequest] = None
    ) -> V20CredExRecord:
        """Create a credential offer, independent of any proposal or connection"""
        if not body:
            body = V20CredOfferConnFreeRequest()
        return await self.__issue_credential20_create_offer_post(
            body=body,
        )

    async def issue_credential_automated(
        self, *, body: Optional[V20CredExFree] = None
    ) -> V20CredExRecord:
        """Send holder a credential, automating entire flow"""
        if not body:
            body = V20CredExFree()
        return await self.__issue_credential_automated(
            body=body,
        )

    async def report_problem(
        self,
        *,
        cred_ex_id: str,
        body: Optional[V20CredIssueProblemReportRequest] = None
    ) -> Dict[str, Any]:
        """Send a problem report for credential exchange"""
        if not body:
            body = V20CredIssueProblemReportRequest()
        return await self.__report_problem(
            cred_ex_id=cred_ex_id,
            body=body,
        )

    async def send_offer(
        self, *, cred_ex_id: str, body: Optional[V20CredBoundOfferRequest] = None
    ) -> V20CredExRecord:
        """Send holder a credential offer in reference to a proposal with preview"""
        if not body:
            body = V20CredBoundOfferRequest()
        return await self.__send_offer(
            cred_ex_id=cred_ex_id,
            body=body,
        )

    async def send_offer_free(
        self, *, body: Optional[V20CredOfferRequest] = None
    ) -> V20CredExRecord:
        """Send holder a credential offer, independent of any proposal"""
        if not body:
            body = V20CredOfferRequest()
        return await self.__send_offer_free(
            body=body,
        )

    async def send_proposal(
        self, *, body: Optional[V20CredExFree] = None
    ) -> V20CredExRecord:
        """Send issuer a credential proposal"""
        if not body:
            body = V20CredExFree()
        return await self.__send_proposal(
            body=body,
        )

    async def send_request(
        self, *, cred_ex_id: str, body: Optional[V20CredRequestRequest] = None
    ) -> V20CredExRecord:
        """Send issuer a credential request"""
        if not body:
            body = V20CredRequestRequest()
        return await self.__send_request(
            cred_ex_id=cred_ex_id,
            body=body,
        )

    async def send_request_free(
        self, *, body: Optional[V20CredRequestFree] = None
    ) -> V20CredExRecord:
        """Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request"""
        if not body:
            body = V20CredRequestFree()
        return await self.__send_request_free(
            body=body,
        )

    async def store_credential(
        self, *, cred_ex_id: str, body: Optional[V20CredStoreRequest] = None
    ) -> V20CredExRecordDetail:
        """Store a received credential"""
        if not body:
            body = V20CredStoreRequest()
        return await self.__store_credential(
            cred_ex_id=cred_ex_id,
            body=body,
        )

    @returns.json
    @json
    @post("/issue-credential-2.0/create")
    def __create_credential(
        self, *, body: Body(type=V20IssueCredSchemaCore) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for create_credential"""

    @returns.json
    @delete("/issue-credential-2.0/records/{cred_ex_id}")
    def __delete_record(self, *, cred_ex_id: str) -> Dict[str, Any]:
        """Internal uplink method for delete_record"""

    @returns.json
    @get("/issue-credential-2.0/records/{cred_ex_id}")
    def __get_record(self, *, cred_ex_id: str) -> V20CredExRecordDetail:
        """Internal uplink method for get_record"""

    @returns.json
    @get("/issue-credential-2.0/records")
    def __get_records(
        self,
        *,
        connection_id: Query = None,
        role: Query = None,
        state: Query = None,
        thread_id: Query = None
    ) -> V20CredExRecordListResult:
        """Internal uplink method for get_records"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/issue")
    def __issue_credential(
        self, *, cred_ex_id: str, body: Body(type=V20CredIssueRequest) = {}
    ) -> V20CredExRecordDetail:
        """Internal uplink method for issue_credential"""

    @returns.json
    @json
    @post("/issue-credential-2.0/create-offer")
    def __issue_credential20_create_offer_post(
        self, *, body: Body(type=V20CredOfferConnFreeRequest) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for issue_credential20_create_offer_post"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send")
    def __issue_credential_automated(
        self, *, body: Body(type=V20CredExFree) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for issue_credential_automated"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/problem-report")
    def __report_problem(
        self, *, cred_ex_id: str, body: Body(type=V20CredIssueProblemReportRequest) = {}
    ) -> Dict[str, Any]:
        """Internal uplink method for report_problem"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/send-offer")
    def __send_offer(
        self, *, cred_ex_id: str, body: Body(type=V20CredBoundOfferRequest) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for send_offer"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-offer")
    def __send_offer_free(
        self, *, body: Body(type=V20CredOfferRequest) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for send_offer_free"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-proposal")
    def __send_proposal(
        self, *, body: Body(type=V20CredExFree) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for send_proposal"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/send-request")
    def __send_request(
        self, *, cred_ex_id: str, body: Body(type=V20CredRequestRequest) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for send_request"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-request")
    def __send_request_free(
        self, *, body: Body(type=V20CredRequestFree) = {}
    ) -> V20CredExRecord:
        """Internal uplink method for send_request_free"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/store")
    def __store_credential(
        self, *, cred_ex_id: str, body: Body(type=V20CredStoreRequest) = {}
    ) -> V20CredExRecordDetail:
        """Internal uplink method for store_credential"""
