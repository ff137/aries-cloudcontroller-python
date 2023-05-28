# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.conn_record import ConnRecord  # noqa: F401
from aries_cloudcontroller.models.connection_list import ConnectionList  # noqa: F401
from aries_cloudcontroller.models.connection_metadata import ConnectionMetadata  # noqa: F401
from aries_cloudcontroller.models.connection_metadata_set_request import ConnectionMetadataSetRequest  # noqa: F401
from aries_cloudcontroller.models.connection_static_request import ConnectionStaticRequest  # noqa: F401
from aries_cloudcontroller.models.connection_static_result import ConnectionStaticResult  # noqa: F401
from aries_cloudcontroller.models.create_invitation_request import CreateInvitationRequest  # noqa: F401
from aries_cloudcontroller.models.endpoints_result import EndpointsResult  # noqa: F401
from aries_cloudcontroller.models.invitation_result import InvitationResult  # noqa: F401
from aries_cloudcontroller.models.receive_invitation_request import ReceiveInvitationRequest  # noqa: F401


def test_accept_connection_invitation(client: TestClient):
    """Test case for accept_connection_invitation

    Accept a stored connection invitation
    """
    params = [("mediation_id", 'mediation_id_example'),     ("my_endpoint", 'my_endpoint_example'),     ("my_label", 'my_label_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/accept-invitation".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_accept_connection_request(client: TestClient):
    """Test case for accept_connection_request

    Accept a stored connection request
    """
    params = [("my_endpoint", 'my_endpoint_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/accept-request".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_connection_invitation(client: TestClient):
    """Test case for create_connection_invitation

    Create a new connection invitation
    """
    body = {"recipient_keys":["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV","H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"],"mediation_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","metadata":"{}","service_endpoint":"http://192.168.56.102:8020","my_label":"Bob","routing_keys":["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV","H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"]}
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("multi_use", True),     ("public", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/create-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_static_connection(client: TestClient):
    """Test case for create_static_connection

    Create a new static connection
    """
    body = {"their_endpoint":"https://myhost:8021","their_seed":"their_seed","my_seed":"my_seed","their_verkey":"their_verkey","alias":"alias","my_did":"WgWxqztrNooG92RXvxSTWv","their_did":"WgWxqztrNooG92RXvxSTWv","their_label":"their_label"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/create-static",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_connection_record(client: TestClient):
    """Test case for delete_connection_record

    Remove an existing connection record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/connections/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_connection_endpoint(client: TestClient):
    """Test case for get_connection_endpoint

    Fetch connection remote endpoint
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}/endpoints".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_connection_metadata(client: TestClient):
    """Test case for get_connection_metadata

    Fetch connection metadata
    """
    params = [("key", 'key_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}/metadata".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_connection_record(client: TestClient):
    """Test case for get_connection_record

    Fetch a single connection record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections/{conn_id}".format(conn_id='conn_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_matching_connections(client: TestClient):
    """Test case for get_matching_connections

    Query agent-to-agent connections
    """
    params = [("alias", 'alias_example'),     ("connection_protocol", 'connection_protocol_example'),     ("invitation_key", 'invitation_key_example'),     ("invitation_msg_id", 'invitation_msg_id_example'),     ("my_did", 'my_did_example'),     ("state", 'state_example'),     ("their_did", 'their_did_example'),     ("their_public_did", 'their_public_did_example'),     ("their_role", 'their_role_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/connections",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_receive_connection_invitation(client: TestClient):
    """Test case for receive_connection_invitation

    Receive a new connection invitation
    """
    body = {"recipient_keys":["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV","H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"],"@type":"https://didcomm.org/my-family/1.0/my-message-type","image_url":"http://192.168.56.101/img/logo.jpg","@id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","label":"Bob","routing_keys":["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV","H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"],"service_endpoint":"http://192.168.56.101:8020","did":"WgWxqztrNooG92RXvxSTWv"}
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/receive-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_connection_metadata(client: TestClient):
    """Test case for set_connection_metadata

    Set connection metadata
    """
    body = {"metadata":"{}"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/metadata".format(conn_id='conn_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_inbound_connection(client: TestClient):
    """Test case for set_inbound_connection

    Assign another connection as the inbound connection
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/connections/{conn_id}/establish-inbound/{ref_id}".format(conn_id='conn_id_example', ref_id='ref_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

