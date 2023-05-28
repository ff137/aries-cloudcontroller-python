# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.did_create import DIDCreate  # noqa: F401
from aries_cloudcontroller.models.did_endpoint import DIDEndpoint  # noqa: F401
from aries_cloudcontroller.models.did_endpoint_with_type import DIDEndpointWithType  # noqa: F401
from aries_cloudcontroller.models.did_list import DIDList  # noqa: F401
from aries_cloudcontroller.models.did_result import DIDResult  # noqa: F401


def test_create_local_did(client: TestClient):
    """Test case for create_local_did

    Create a local DID
    """
    body = {"method":"sov","seed":"000000000000000000000000Trustee1","options":null}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/did/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_did_endpoint(client: TestClient):
    """Test case for get_did_endpoint

    Query DID endpoint in wallet
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/get-did-endpoint",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dids(client: TestClient):
    """Test case for get_dids

    List wallet DIDs
    """
    params = [("did", 'did_example'),     ("key_type", 'key_type_example'),     ("method", 'method_example'),     ("posture", 'posture_example'),     ("verkey", 'verkey_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/did",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_public_did(client: TestClient):
    """Test case for get_public_did

    Fetch the current public DID
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/wallet/did/public",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_rotate_keypair(client: TestClient):
    """Test case for rotate_keypair

    Rotate keypair for a DID not posted to the ledger
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/wallet/did/local/rotate-keypair",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_did_endpoint(client: TestClient):
    """Test case for set_did_endpoint

    Update endpoint in wallet and on ledger if posted to it
    """
    body = {"endpoint":"https://myhost:8021","endpoint_type":"Endpoint","did":"WgWxqztrNooG92RXvxSTWv"}
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/set-did-endpoint",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_public_did(client: TestClient):
    """Test case for set_public_did

    Assign the current public DID
    """
    params = [("did", 'did_example'),     ("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True),     ("mediation_id", 'mediation_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/wallet/did/public",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

