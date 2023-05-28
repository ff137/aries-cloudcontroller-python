# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.invitation_create_request import InvitationCreateRequest
from aries_cloudcontroller.models.invitation_message import InvitationMessage
from aries_cloudcontroller.models.invitation_record import InvitationRecord
from aries_cloudcontroller.models.oob_record import OobRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseOutOfBandApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseOutOfBandApi.subclasses = BaseOutOfBandApi.subclasses + (cls,)
    def create_oob_invitation(
        self,
        auto_accept: bool,
        multi_use: bool,
        body: InvitationCreateRequest,
    ) -> InvitationRecord:
        ...


    def receive_oob_invitation(
        self,
        alias: str,
        auto_accept: bool,
        mediation_id: str,
        use_existing_connection: bool,
        body: InvitationMessage,
    ) -> OobRecord:
        ...
