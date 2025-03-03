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

from aries_cloudcontroller.model.invitation_create_request import (
    InvitationCreateRequest,
)
from aries_cloudcontroller.model.invitation_message import InvitationMessage
from aries_cloudcontroller.model.invitation_record import InvitationRecord
from aries_cloudcontroller.model.oob_record import OobRecord


class OutOfBandApi(Consumer):
    async def create_invitation(
        self,
        *,
        auto_accept: Optional[bool] = None,
        multi_use: Optional[bool] = None,
        body: Optional[InvitationCreateRequest] = None
    ) -> InvitationRecord:
        """Create a new connection invitation"""
        if not body:
            body = InvitationCreateRequest()
        return await self.__create_invitation(
            auto_accept=bool_query(auto_accept),
            multi_use=bool_query(multi_use),
            body=body,
        )

    async def receive_invitation(
        self,
        *,
        alias: Optional[str] = None,
        auto_accept: Optional[bool] = None,
        mediation_id: Optional[str] = None,
        use_existing_connection: Optional[bool] = None,
        body: Optional[InvitationMessage] = None
    ) -> OobRecord:
        """Receive a new connection invitation"""
        if not body:
            body = InvitationMessage()
        return await self.__receive_invitation(
            alias=alias,
            auto_accept=bool_query(auto_accept),
            mediation_id=mediation_id,
            use_existing_connection=bool_query(use_existing_connection),
            body=body,
        )

    @returns.json
    @json
    @post("/out-of-band/create-invitation")
    def __create_invitation(
        self,
        *,
        auto_accept: Query = None,
        multi_use: Query = None,
        body: Body(type=InvitationCreateRequest) = {}
    ) -> InvitationRecord:
        """Internal uplink method for create_invitation"""

    @returns.json
    @json
    @post("/out-of-band/receive-invitation")
    def __receive_invitation(
        self,
        *,
        alias: Query = None,
        auto_accept: Query = None,
        mediation_id: Query = None,
        use_existing_connection: Query = None,
        body: Body(type=InvitationMessage) = {}
    ) -> OobRecord:
        """Internal uplink method for receive_invitation"""
