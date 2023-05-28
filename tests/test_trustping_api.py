# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.ping_request import PingRequest  # noqa: F401
from aries_cloudcontroller.models.ping_request_response import PingRequestResponse  # noqa: F401


def test_send_ping(client: TestClient):
    """Test case for send_ping

    Send a trust ping to a connection
    """
    body = {"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/send-ping".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

