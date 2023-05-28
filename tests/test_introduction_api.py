# coding: utf-8

from fastapi.testclient import TestClient




def test_start_connection_introduction(client: TestClient):
    """Test case for start_connection_introduction

    Start an introduction between two connections
    """
    params = [("target_connection_id", 'target_connection_id_example'),     ("message", 'message_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/start-introduction".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

