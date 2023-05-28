# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.did_create import DIDCreate
from aries_cloudcontroller.models.did_endpoint import DIDEndpoint
from aries_cloudcontroller.models.did_endpoint_with_type import DIDEndpointWithType
from aries_cloudcontroller.models.did_list import DIDList
from aries_cloudcontroller.models.did_result import DIDResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseWalletApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseWalletApi.subclasses = BaseWalletApi.subclasses + (cls,)
    def create_local_did(
        self,
        body: DIDCreate,
    ) -> DIDResult:
        ...


    def get_did_endpoint(
        self,
        did: str,
    ) -> DIDEndpoint:
        ...


    def get_dids(
        self,
        did: str,
        key_type: str,
        method: str,
        posture: str,
        verkey: str,
    ) -> DIDList:
        ...


    def get_public_did(
        self,
    ) -> DIDResult:
        ...


    def rotate_keypair(
        self,
        did: str,
    ) -> object:
        ...


    def set_did_endpoint(
        self,
        conn_id: str,
        create_transaction_for_endorser: bool,
        body: DIDEndpointWithType,
    ) -> object:
        ...


    def set_public_did(
        self,
        did: str,
        conn_id: str,
        create_transaction_for_endorser: bool,
        mediation_id: str,
    ) -> DIDResult:
        ...
