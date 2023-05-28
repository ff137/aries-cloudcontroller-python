# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.credential_definition_get_result import CredentialDefinitionGetResult
from aries_cloudcontroller.models.credential_definition_send_request import CredentialDefinitionSendRequest
from aries_cloudcontroller.models.credential_definitions_created_result import CredentialDefinitionsCreatedResult
from aries_cloudcontroller.models.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseCredentialDefinitionApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCredentialDefinitionApi.subclasses = BaseCredentialDefinitionApi.subclasses + (cls,)
    def get_created_cred_defs(
        self,
        cred_def_id: str,
        issuer_did: str,
        schema_id: str,
        schema_issuer_did: str,
        schema_name: str,
        schema_version: str,
    ) -> CredentialDefinitionsCreatedResult:
        ...


    def get_credential_definition(
        self,
        cred_def_id: str,
    ) -> CredentialDefinitionGetResult:
        ...


    def publish_credential_definition(
        self,
        conn_id: str,
        create_transaction_for_endorser: bool,
        body: CredentialDefinitionSendRequest,
    ) -> TxnOrCredentialDefinitionSendResult:
        ...


    def write_credential_definition(
        self,
        cred_def_id: str,
    ) -> CredentialDefinitionGetResult:
        ...
