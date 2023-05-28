# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.date import Date
from aries_cloudcontroller.models.endorser_info import EndorserInfo
from aries_cloudcontroller.models.transaction_jobs import TransactionJobs
from aries_cloudcontroller.models.transaction_list import TransactionList
from aries_cloudcontroller.models.transaction_record import TransactionRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseEndorseTransactionApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEndorseTransactionApi.subclasses = BaseEndorseTransactionApi.subclasses + (cls,)
    def cancel_transaction_request(
        self,
        tran_id: str,
    ) -> TransactionRecord:
        ...


    def create_transaction_request(
        self,
        tran_id: str,
        endorser_write_txn: bool,
        body: Date,
    ) -> TransactionRecord:
        ...


    def endorse_transaction(
        self,
        tran_id: str,
        endorser_did: str,
    ) -> TransactionRecord:
        ...


    def get_transaction_list(
        self,
    ) -> TransactionList:
        ...


    def get_transaction_record(
        self,
        tran_id: str,
    ) -> TransactionRecord:
        ...


    def publish_endorsed_transaction(
        self,
        tran_id: str,
    ) -> TransactionRecord:
        ...


    def refuse_transaction(
        self,
        tran_id: str,
    ) -> TransactionRecord:
        ...


    def resend_transaction_request(
        self,
        tran_id: str,
    ) -> TransactionRecord:
        ...


    def set_endorser_info_for_conn_id(
        self,
        conn_id: str,
        endorser_did: str,
        endorser_name: str,
    ) -> EndorserInfo:
        ...


    def set_endorser_role_for_conn_id(
        self,
        conn_id: str,
        transaction_my_job: str,
    ) -> TransactionJobs:
        ...
