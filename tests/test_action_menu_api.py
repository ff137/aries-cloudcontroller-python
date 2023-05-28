# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.action_menu_fetch_result import ActionMenuFetchResult  # noqa: F401
from aries_cloudcontroller.models.perform_request import PerformRequest  # noqa: F401
from aries_cloudcontroller.models.send_menu import SendMenu  # noqa: F401


def test_close_menu_by_conn_id(client: TestClient):
    """Test case for close_menu_by_conn_id

    Close the active menu associated with a connection
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/close".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fetch_menu_by_conn_id(client: TestClient):
    """Test case for fetch_menu_by_conn_id

    Fetch the active menu
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/fetch".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_perform_action_by_conn_id(client: TestClient):
    """Test case for perform_action_by_conn_id

    Perform an action associated with the active menu
    """
    body = {"name":"Query","params":{"key":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/perform".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_request_menu_by_conn_id(client: TestClient):
    """Test case for request_menu_by_conn_id

    Request the active menu
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/request".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_menu_to_conn_id(client: TestClient):
    """Test case for send_menu_to_conn_id

    Send an action menu to a connection
    """
    body = {"menu":null}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/action-menu/{conn_id}/send-menu".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

