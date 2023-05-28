# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.send_message import SendMessage
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseBasicmessageApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBasicmessageApi.subclasses = BaseBasicmessageApi.subclasses + (cls,)
    def send_message(
        self,
        conn_id: str,
        body: SendMessage,
    ) -> object:
        ...
