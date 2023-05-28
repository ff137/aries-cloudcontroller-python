# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.sign_request import SignRequest
from aries_cloudcontroller.models.sign_response import SignResponse
from aries_cloudcontroller.models.verify_request import VerifyRequest
from aries_cloudcontroller.models.verify_response import VerifyResponse
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseJsonldApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseJsonldApi.subclasses = BaseJsonldApi.subclasses + (cls,)
    def sign(
        self,
        body: SignRequest,
    ) -> SignResponse:
        ...


    def verify(
        self,
        body: VerifyRequest,
    ) -> VerifyResponse:
        ...
