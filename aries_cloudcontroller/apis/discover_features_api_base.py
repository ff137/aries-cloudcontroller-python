# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.v10_discovery_exchange_list_result import V10DiscoveryExchangeListResult
from aries_cloudcontroller.models.v10_discovery_record import V10DiscoveryRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseDiscoverFeaturesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDiscoverFeaturesApi.subclasses = BaseDiscoverFeaturesApi.subclasses + (cls,)
    def get_v10_feature_records(
        self,
        connection_id: str,
    ) -> V10DiscoveryExchangeListResult:
        ...


    def get_v10_features_query(
        self,
        comment: str,
        connection_id: str,
        query: str,
    ) -> V10DiscoveryRecord:
        ...
