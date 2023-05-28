# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.get_did_endpoint_response import GetDIDEndpointResponse
from aries_cloudcontroller.models.get_did_verkey_response import GetDIDVerkeyResponse
from aries_cloudcontroller.models.get_nym_role_response import GetNymRoleResponse
from aries_cloudcontroller.models.ledger_config_list import LedgerConfigList
from aries_cloudcontroller.models.taa_accept import TAAAccept
from aries_cloudcontroller.models.taa_result import TAAResult
from aries_cloudcontroller.models.txn_or_register_ledger_nym_response import TxnOrRegisterLedgerNymResponse
from aries_cloudcontroller.models.write_ledger_request import WriteLedgerRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseLedgerApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLedgerApi.subclasses = BaseLedgerApi.subclasses + (cls,)
    def accept_taa(
        self,
        body: TAAAccept,
    ) -> object:
        ...


    def get_did_nym_role(
        self,
        did: str,
    ) -> GetNymRoleResponse:
        ...


    def get_did_verkey(
        self,
        did: str,
    ) -> GetDIDVerkeyResponse:
        ...


    def get_multiple_ledger_config(
        self,
    ) -> LedgerConfigList:
        ...


    def get_published_did_endpoint(
        self,
        did: str,
        endpoint_type: str,
    ) -> GetDIDEndpointResponse:
        ...


    def get_taa(
        self,
    ) -> TAAResult:
        ...


    def get_write_ledger(
        self,
    ) -> WriteLedgerRequest:
        ...


    def register_nym(
        self,
        did: str,
        verkey: str,
        alias: str,
        conn_id: str,
        create_transaction_for_endorser: bool,
        role: str,
    ) -> TxnOrRegisterLedgerNymResponse:
        ...


    def rotate_public_did_keypair(
        self,
    ) -> object:
        ...
