# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.send_message import SendMessage  # noqa: F401


def test_send_message(client: TestClient):
    """Test case for send_message

    Send a basic message to a connection
    """
    body = {"content":"Hello"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/send-message".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

