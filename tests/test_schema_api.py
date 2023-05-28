# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.schema_get_result import SchemaGetResult  # noqa: F401
from aries_cloudcontroller.models.schema_send_request import SchemaSendRequest  # noqa: F401
from aries_cloudcontroller.models.schemas_created_result import SchemasCreatedResult  # noqa: F401
from aries_cloudcontroller.models.txn_or_schema_send_result import TxnOrSchemaSendResult  # noqa: F401


def test_get_matching_created_schemas(client: TestClient):
    """Test case for get_matching_created_schemas

    Search for matching schema that agent originated
    """
    params = [("schema_id", 'schema_id_example'),     ("schema_issuer_did", 'schema_issuer_did_example'),     ("schema_name", 'schema_name_example'),     ("schema_version", 'schema_version_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/schemas/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_schema(client: TestClient):
    """Test case for get_schema

    Gets a schema from the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/schemas/{schema_id}".format(schema_id='schema_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_schema(client: TestClient):
    """Test case for publish_schema

    Sends a schema to the ledger
    """
    body = {"schema_version":"1.0","attributes":["score","score"],"schema_name":"prefs"}
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/schemas",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_write_schema_record_to_wallet(client: TestClient):
    """Test case for write_schema_record_to_wallet

    Writes a schema non-secret record to the wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/schemas/{schema_id}/write_record".format(schema_id='schema_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

