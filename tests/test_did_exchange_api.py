# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.conn_record import ConnRecord  # noqa: F401
from aries_cloudcontroller.models.didx_request import DIDXRequest  # noqa: F401


def test_accept_didex_invitation(client: TestClient):
    """Test case for accept_didex_invitation

    Accept a stored connection invitation
    """
    params = [("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/{conn_id}/accept-invitation".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_accept_didex_request(client: TestClient):
    """Test case for accept_didex_request

    Accept a stored connection request
    """
    params = [("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/{conn_id}/accept-request".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_didex_request(client: TestClient):
    """Test case for create_didex_request

    Create and send a request against public DID's implicit invitation
    """
    params = [("their_public_did", 'their_public_did_example'),     ("alias", 'alias_example'),     ("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example'),     ("use_public_did", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/create-request",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_receive_didex_request(client: TestClient):
    """Test case for receive_didex_request

    Receive request against public DID's implicit invitation
    """
    body = {"@type":"https://didcomm.org/my-family/1.0/my-message-type","@id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","label":"Request to connect with Bob","did":"WgWxqztrNooG92RXvxSTWv","did_doc~attach":null}
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/didexchange/receive-request",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

