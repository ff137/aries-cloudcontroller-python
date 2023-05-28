# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.ping_request import PingRequest
from aries_cloudcontroller.models.ping_request_response import PingRequestResponse
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseTrustpingApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrustpingApi.subclasses = BaseTrustpingApi.subclasses + (cls,)
    def send_ping(
        self,
        conn_id: str,
        body: PingRequest,
    ) -> PingRequestResponse:
        ...
