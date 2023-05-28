# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.connection_list import ConnectionList
from aries_cloudcontroller.models.connection_metadata import ConnectionMetadata
from aries_cloudcontroller.models.connection_metadata_set_request import ConnectionMetadataSetRequest
from aries_cloudcontroller.models.connection_static_request import ConnectionStaticRequest
from aries_cloudcontroller.models.connection_static_result import ConnectionStaticResult
from aries_cloudcontroller.models.create_invitation_request import CreateInvitationRequest
from aries_cloudcontroller.models.endpoints_result import EndpointsResult
from aries_cloudcontroller.models.invitation_result import InvitationResult
from aries_cloudcontroller.models.receive_invitation_request import ReceiveInvitationRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseConnectionApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConnectionApi.subclasses = BaseConnectionApi.subclasses + (cls,)
    def accept_connection_invitation(
        self,
        conn_id: str,
        mediation_id: str,
        my_endpoint: str,
        my_label: str,
    ) -> ConnRecord:
        ...


    def accept_connection_request(
        self,
        conn_id: str,
        my_endpoint: str,
    ) -> ConnRecord:
        ...


    def create_connection_invitation(
        self,
        alias: str,
        auto_accept: bool,
        multi_use: bool,
        public: bool,
        body: CreateInvitationRequest,
    ) -> InvitationResult:
        ...


    def create_static_connection(
        self,
        body: ConnectionStaticRequest,
    ) -> ConnectionStaticResult:
        ...


    def delete_connection_record(
        self,
        conn_id: str,
    ) -> object:
        ...


    def get_connection_endpoint(
        self,
        conn_id: str,
    ) -> EndpointsResult:
        ...


    def get_connection_metadata(
        self,
        conn_id: str,
        key: str,
    ) -> ConnectionMetadata:
        ...


    def get_connection_record(
        self,
        conn_id: str,
    ) -> ConnRecord:
        ...


    def get_matching_connections(
        self,
        alias: str,
        connection_protocol: str,
        invitation_key: str,
        invitation_msg_id: str,
        my_did: str,
        state: str,
        their_did: str,
        their_public_did: str,
        their_role: str,
    ) -> ConnectionList:
        ...


    def receive_connection_invitation(
        self,
        alias: str,
        auto_accept: bool,
        mediation_id: str,
        body: ReceiveInvitationRequest,
    ) -> ConnRecord:
        ...


    def set_connection_metadata(
        self,
        conn_id: str,
        body: ConnectionMetadataSetRequest,
    ) -> ConnectionMetadata:
        ...


    def set_inbound_connection(
        self,
        conn_id: str,
        ref_id: str,
    ) -> object:
        ...
