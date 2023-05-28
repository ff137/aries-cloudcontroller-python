# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.action_menu_fetch_result import ActionMenuFetchResult
from aries_cloudcontroller.models.perform_request import PerformRequest
from aries_cloudcontroller.models.send_menu import SendMenu
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseActionMenuApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseActionMenuApi.subclasses = BaseActionMenuApi.subclasses + (cls,)
    def close_menu_by_conn_id(
        self,
        conn_id: str,
    ) -> object:
        ...


    def fetch_menu_by_conn_id(
        self,
        conn_id: str,
    ) -> ActionMenuFetchResult:
        ...


    def perform_action_by_conn_id(
        self,
        conn_id: str,
        body: PerformRequest,
    ) -> object:
        ...


    def request_menu_by_conn_id(
        self,
        conn_id: str,
    ) -> object:
        ...


    def send_menu_to_conn_id(
        self,
        conn_id: str,
        body: SendMenu,
    ) -> object:
        ...
