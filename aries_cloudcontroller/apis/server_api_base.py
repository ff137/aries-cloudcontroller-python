# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.admin_config import AdminConfig
from aries_cloudcontroller.models.admin_modules import AdminModules
from aries_cloudcontroller.models.admin_status import AdminStatus
from aries_cloudcontroller.models.admin_status_liveliness import AdminStatusLiveliness
from aries_cloudcontroller.models.admin_status_readiness import AdminStatusReadiness
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseServerApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseServerApi.subclasses = BaseServerApi.subclasses + (cls,)
    def get_config(
        self,
    ) -> AdminConfig:
        ...


    def get_liveliness(
        self,
    ) -> AdminStatusLiveliness:
        ...


    def get_loaded_plugins(
        self,
    ) -> AdminModules:
        ...


    def get_readiness(
        self,
    ) -> AdminStatusReadiness:
        ...


    def get_status(
        self,
    ) -> AdminStatus:
        ...


    def reset_statistics(
        self,
    ) -> object:
        ...


    def shutdown_server(
        self,
    ) -> object:
        ...
