# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.admin_mediation_deny import AdminMediationDeny  # noqa: F401
from aries_cloudcontroller.models.keylist import Keylist  # noqa: F401
from aries_cloudcontroller.models.keylist_query import KeylistQuery  # noqa: F401
from aries_cloudcontroller.models.keylist_query_filter_request import KeylistQueryFilterRequest  # noqa: F401
from aries_cloudcontroller.models.keylist_update import KeylistUpdate  # noqa: F401
from aries_cloudcontroller.models.keylist_update_request import KeylistUpdateRequest  # noqa: F401
from aries_cloudcontroller.models.mediation_create_request import MediationCreateRequest  # noqa: F401
from aries_cloudcontroller.models.mediation_deny import MediationDeny  # noqa: F401
from aries_cloudcontroller.models.mediation_grant import MediationGrant  # noqa: F401
from aries_cloudcontroller.models.mediation_id_match_info import MediationIdMatchInfo  # noqa: F401
from aries_cloudcontroller.models.mediation_list import MediationList  # noqa: F401
from aries_cloudcontroller.models.mediation_record import MediationRecord  # noqa: F401


def test_clear_default_mediator(client: TestClient):
    """Test case for clear_default_mediator

    Clear default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/mediation/default-mediator",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_mediation_record(client: TestClient):
    """Test case for delete_mediation_record

    Delete mediation request by ID
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/mediation/requests/{mediation_id}".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_deny_mediation_request(client: TestClient):
    """Test case for deny_mediation_request

    Deny a stored mediation request
    """
    body = {"mediator_terms":["mediator_terms","mediator_terms"],"recipient_terms":["recipient_terms","recipient_terms"]}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/requests/{mediation_id}/deny".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_default_mediator(client: TestClient):
    """Test case for get_default_mediator

    Get default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/default-mediator",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_keylists(client: TestClient):
    """Test case for get_keylists

    Retrieve keylists by connection or role
    """
    params = [("conn_id", 'conn_id_example'),     ("role", 'server')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/keylists",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_matching_mediation_records(client: TestClient):
    """Test case for get_matching_mediation_records

    Query mediation requests, returns list of all mediation records
    """
    params = [("conn_id", 'conn_id_example'),     ("mediator_terms", ['mediator_terms_example']),     ("recipient_terms", ['recipient_terms_example']),     ("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/requests",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_mediation_record(client: TestClient):
    """Test case for get_mediation_record

    Retrieve mediation request record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/mediation/requests/{mediation_id}".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grant_mediation_request(client: TestClient):
    """Test case for grant_mediation_request

    Grant received mediation
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/requests/{mediation_id}/grant".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_request_mediation_for_connection(client: TestClient):
    """Test case for request_mediation_for_connection

    Request mediation from connection
    """
    body = {"mediator_terms":["mediator_terms","mediator_terms"],"recipient_terms":["recipient_terms","recipient_terms"]}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/request/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_keylist_query_to_mediator(client: TestClient):
    """Test case for send_keylist_query_to_mediator

    Send keylist query to mediator
    """
    body = {"filter":"{}"}
    params = [("paginate_limit", -1),     ("paginate_offset", 0)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/keylists/{mediation_id}/send-keylist-query".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_keylist_update_to_mediator(client: TestClient):
    """Test case for send_keylist_update_to_mediator

    Send keylist update to mediator
    """
    body = {"updates":[{"action":"add","recipient_key":"did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH"},{"action":"add","recipient_key":"did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH"}]}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/keylists/{mediation_id}/send-keylist-update".format(mediation_id='mediation_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_default_mediator(client: TestClient):
    """Test case for set_default_mediator

    Set default mediator
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/mediation/{mediation_id}/default-mediator".format(mediation_id='mediation_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_keylist_for_conn_id(client: TestClient):
    """Test case for update_keylist_for_conn_id

    Update keylist for a connection
    """
    body = {"mediation_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/mediation/update-keylist/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

