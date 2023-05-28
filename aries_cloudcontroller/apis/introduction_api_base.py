# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseIntroductionApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIntroductionApi.subclasses = BaseIntroductionApi.subclasses + (cls,)
    def start_connection_introduction(
        self,
        conn_id: str,
        target_connection_id: str,
        message: str,
    ) -> object:
        ...
