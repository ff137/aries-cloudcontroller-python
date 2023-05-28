# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.schema_get_result import SchemaGetResult
from aries_cloudcontroller.models.schema_send_request import SchemaSendRequest
from aries_cloudcontroller.models.schemas_created_result import SchemasCreatedResult
from aries_cloudcontroller.models.txn_or_schema_send_result import TxnOrSchemaSendResult
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseSchemaApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSchemaApi.subclasses = BaseSchemaApi.subclasses + (cls,)
    def get_matching_created_schemas(
        self,
        schema_id: str,
        schema_issuer_did: str,
        schema_name: str,
        schema_version: str,
    ) -> SchemasCreatedResult:
        ...


    def get_schema(
        self,
        schema_id: str,
    ) -> SchemaGetResult:
        ...


    def publish_schema(
        self,
        conn_id: str,
        create_transaction_for_endorser: bool,
        body: SchemaSendRequest,
    ) -> TxnOrSchemaSendResult:
        ...


    def write_schema_record_to_wallet(
        self,
        schema_id: str,
    ) -> SchemaGetResult:
        ...
