# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.get_did_endpoint_response import GetDIDEndpointResponse  # noqa: F401
from aries_cloudcontroller.models.get_did_verkey_response import GetDIDVerkeyResponse  # noqa: F401
from aries_cloudcontroller.models.get_nym_role_response import GetNymRoleResponse  # noqa: F401
from aries_cloudcontroller.models.ledger_config_list import LedgerConfigList  # noqa: F401
from aries_cloudcontroller.models.taa_accept import TAAAccept  # noqa: F401
from aries_cloudcontroller.models.taa_result import TAAResult  # noqa: F401
from aries_cloudcontroller.models.txn_or_register_ledger_nym_response import TxnOrRegisterLedgerNymResponse  # noqa: F401
from aries_cloudcontroller.models.write_ledger_request import WriteLedgerRequest  # noqa: F401


def test_accept_taa(client: TestClient):
    """Test case for accept_taa

    Accept the transaction author agreement
    """
    body = {"text":"text","mechanism":"mechanism","version":"version"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/ledger/taa/accept",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_did_nym_role(client: TestClient):
    """Test case for get_did_nym_role

    Get the role from the NYM registration of a public DID.
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/get-nym-role",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_did_verkey(client: TestClient):
    """Test case for get_did_verkey

    Get the verkey for a DID from the ledger.
    """
    params = [("did", 'did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/did-verkey",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_multiple_ledger_config(client: TestClient):
    """Test case for get_multiple_ledger_config

    Fetch the multiple ledger configuration currently in use
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/multiple/config",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_published_did_endpoint(client: TestClient):
    """Test case for get_published_did_endpoint

    Get the endpoint for a DID from the ledger.
    """
    params = [("did", 'did_example'),     ("endpoint_type", 'endpoint_type_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/did-endpoint",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_taa(client: TestClient):
    """Test case for get_taa

    Fetch the current transaction author agreement, if any
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/taa",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_write_ledger(client: TestClient):
    """Test case for get_write_ledger

    Fetch the current write ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/ledger/multiple/get-write-ledger",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_register_nym(client: TestClient):
    """Test case for register_nym

    Send a NYM registration to the ledger.
    """
    params = [("did", 'did_example'),     ("verkey", 'verkey_example'),     ("alias", 'alias_example'),     ("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True),     ("role", 'role_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/ledger/register-nym",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_rotate_public_did_keypair(client: TestClient):
    """Test case for rotate_public_did_keypair

    Rotate key pair for public DID.
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/ledger/rotate-public-did-keypair",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

