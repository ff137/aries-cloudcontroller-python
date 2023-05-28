# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.attribute_mime_types_result import AttributeMimeTypesResult
from aries_cloudcontroller.models.cred_info_list import CredInfoList
from aries_cloudcontroller.models.cred_revoked_result import CredRevokedResult
from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.models.vc_record import VCRecord
from aries_cloudcontroller.models.vc_record_list import VCRecordList
from aries_cloudcontroller.models.w3_c_credentials_list_request import W3CCredentialsListRequest
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseCredentialsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCredentialsApi.subclasses = BaseCredentialsApi.subclasses + (cls,)
    def delete_credential_record(
        self,
        credential_id: str,
    ) -> object:
        ...


    def delete_w3c_credential(
        self,
        credential_id: str,
    ) -> object:
        ...


    def get_credential_mime_types(
        self,
        credential_id: str,
    ) -> AttributeMimeTypesResult:
        ...


    def get_credential_record(
        self,
        credential_id: str,
    ) -> IndyCredInfo:
        ...


    def get_credentials(
        self,
        count: str,
        start: str,
        wql: str,
    ) -> CredInfoList:
        ...


    def get_revocation_status(
        self,
        credential_id: str,
        _from: str,
        to: str,
    ) -> CredRevokedResult:
        ...


    def get_w3c_credential(
        self,
        credential_id: str,
    ) -> VCRecord:
        ...


    def get_w3c_credentials(
        self,
        count: str,
        start: str,
        wql: str,
        body: W3CCredentialsListRequest,
    ) -> VCRecordList:
        ...
