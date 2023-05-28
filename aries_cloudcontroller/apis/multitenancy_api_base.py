# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.create_wallet_request import CreateWalletRequest
from aries_cloudcontroller.models.create_wallet_response import CreateWalletResponse
from aries_cloudcontroller.models.create_wallet_token_request import CreateWalletTokenRequest
from aries_cloudcontroller.models.create_wallet_token_response import CreateWalletTokenResponse
from aries_cloudcontroller.models.remove_wallet_request import RemoveWalletRequest
from aries_cloudcontroller.models.update_wallet_request import UpdateWalletRequest
from aries_cloudcontroller.models.wallet_list import WalletList
from aries_cloudcontroller.models.wallet_record import WalletRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseMultitenancyApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMultitenancyApi.subclasses = BaseMultitenancyApi.subclasses + (cls,)
    def create_wallet(
        self,
        body: CreateWalletRequest,
    ) -> CreateWalletResponse:
        ...


    def delete_wallet(
        self,
        wallet_id: str,
        body: RemoveWalletRequest,
    ) -> object:
        ...


    def get_auth_token(
        self,
        wallet_id: str,
        body: CreateWalletTokenRequest,
    ) -> CreateWalletTokenResponse:
        ...


    def get_matching_wallets(
        self,
        wallet_name: str,
    ) -> WalletList:
        ...


    def get_wallet_record(
        self,
        wallet_id: str,
    ) -> WalletRecord:
        ...


    def update_wallet(
        self,
        wallet_id: str,
        body: UpdateWalletRequest,
    ) -> WalletRecord:
        ...
