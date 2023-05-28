# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.credential_definition_get_result import CredentialDefinitionGetResult  # noqa: F401
from aries_cloudcontroller.models.credential_definition_send_request import CredentialDefinitionSendRequest  # noqa: F401
from aries_cloudcontroller.models.credential_definitions_created_result import CredentialDefinitionsCreatedResult  # noqa: F401
from aries_cloudcontroller.models.txn_or_credential_definition_send_result import TxnOrCredentialDefinitionSendResult  # noqa: F401


def test_get_created_cred_defs(client: TestClient):
    """Test case for get_created_cred_defs

    Search for matching credential definitions that agent originated
    """
    params = [("cred_def_id", 'cred_def_id_example'),     ("issuer_did", 'issuer_did_example'),     ("schema_id", 'schema_id_example'),     ("schema_issuer_did", 'schema_issuer_did_example'),     ("schema_name", 'schema_name_example'),     ("schema_version", 'schema_version_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential-definitions/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credential_definition(client: TestClient):
    """Test case for get_credential_definition

    Gets a credential definition from the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential-definitions/{cred_def_id}".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_credential_definition(client: TestClient):
    """Test case for publish_credential_definition

    Sends a credential definition to the ledger
    """
    body = {"revocation_registry_size":1000,"support_revocation":1,"schema_id":"WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0","tag":"default"}
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credential-definitions",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_write_credential_definition(client: TestClient):
    """Test case for write_credential_definition

    Writes a credential definition non-secret record to the wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credential-definitions/{cred_def_id}/write_record".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

