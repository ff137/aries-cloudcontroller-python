# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.didx_request import DIDXRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseDidExchangeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDidExchangeApi.subclasses = BaseDidExchangeApi.subclasses + (cls,)
    def accept_didex_invitation(
        self,
        conn_id: str,
        my_endpoint: str,
        my_label: str,
    ) -> ConnRecord:
        ...


    def accept_didex_request(
        self,
        conn_id: str,
        mediation_id: str,
        my_endpoint: str,
    ) -> ConnRecord:
        ...


    def create_didex_request(
        self,
        their_public_did: str,
        alias: str,
        mediation_id: str,
        my_endpoint: str,
        my_label: str,
        use_public_did: bool,
    ) -> ConnRecord:
        ...


    def receive_didex_request(
        self,
        alias: str,
        auto_accept: bool,
        mediation_id: str,
        my_endpoint: str,
        body: DIDXRequest,
    ) -> ConnRecord:
        ...
