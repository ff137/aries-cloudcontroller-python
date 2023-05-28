# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from aries_cloudcontroller.models.admin_mediation_deny import AdminMediationDeny
from aries_cloudcontroller.models.keylist import Keylist
from aries_cloudcontroller.models.keylist_query import KeylistQuery
from aries_cloudcontroller.models.keylist_query_filter_request import KeylistQueryFilterRequest
from aries_cloudcontroller.models.keylist_update import KeylistUpdate
from aries_cloudcontroller.models.keylist_update_request import KeylistUpdateRequest
from aries_cloudcontroller.models.mediation_create_request import MediationCreateRequest
from aries_cloudcontroller.models.mediation_deny import MediationDeny
from aries_cloudcontroller.models.mediation_grant import MediationGrant
from aries_cloudcontroller.models.mediation_id_match_info import MediationIdMatchInfo
from aries_cloudcontroller.models.mediation_list import MediationList
from aries_cloudcontroller.models.mediation_record import MediationRecord
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

class BaseMediationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMediationApi.subclasses = BaseMediationApi.subclasses + (cls,)
    def clear_default_mediator(
        self,
    ) -> MediationRecord:
        ...


    def delete_mediation_record(
        self,
        mediation_id: str,
    ) -> MediationRecord:
        ...


    def deny_mediation_request(
        self,
        mediation_id: str,
        body: AdminMediationDeny,
    ) -> MediationDeny:
        ...


    def get_default_mediator(
        self,
    ) -> MediationRecord:
        ...


    def get_keylists(
        self,
        conn_id: str,
        role: str,
    ) -> Keylist:
        ...


    def get_matching_mediation_records(
        self,
        conn_id: str,
        mediator_terms: List[str],
        recipient_terms: List[str],
        state: str,
    ) -> MediationList:
        ...


    def get_mediation_record(
        self,
        mediation_id: str,
    ) -> MediationRecord:
        ...


    def grant_mediation_request(
        self,
        mediation_id: str,
    ) -> MediationGrant:
        ...


    def request_mediation_for_connection(
        self,
        conn_id: str,
        body: MediationCreateRequest,
    ) -> MediationRecord:
        ...


    def send_keylist_query_to_mediator(
        self,
        mediation_id: str,
        paginate_limit: int,
        paginate_offset: int,
        body: KeylistQueryFilterRequest,
    ) -> KeylistQuery:
        ...


    def send_keylist_update_to_mediator(
        self,
        mediation_id: str,
        body: KeylistUpdateRequest,
    ) -> KeylistUpdate:
        ...


    def set_default_mediator(
        self,
        mediation_id: str,
    ) -> MediationRecord:
        ...


    def update_keylist_for_conn_id(
        self,
        conn_id: str,
        body: MediationIdMatchInfo,
    ) -> KeylistUpdate:
        ...
