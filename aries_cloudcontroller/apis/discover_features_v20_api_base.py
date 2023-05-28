# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.v20_discovery_exchange_list_result import V20DiscoveryExchangeListResult
from aries_cloudcontroller.models.v20_discovery_exchange_result import V20DiscoveryExchangeResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseDiscoverFeaturesV20Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDiscoverFeaturesV20Api.subclasses = BaseDiscoverFeaturesV20Api.subclasses + (cls,)
    def get_v20_feature_records(
        self,
        connection_id: str,
    ) -> V20DiscoveryExchangeListResult:
        ...


    def get_v20_features_queries(
        self,
        connection_id: str,
        query_goal_code: str,
        query_protocol: str,
    ) -> V20DiscoveryExchangeResult:
        ...
