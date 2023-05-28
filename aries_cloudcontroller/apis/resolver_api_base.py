# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.resolution_result import ResolutionResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseResolverApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseResolverApi.subclasses = BaseResolverApi.subclasses + (cls,)
    def get_did_document(
        self,
        did: str,
    ) -> ResolutionResult:
        ...
