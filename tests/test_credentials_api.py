# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.attribute_mime_types_result import AttributeMimeTypesResult  # noqa: F401
from aries_cloudcontroller.models.cred_info_list import CredInfoList  # noqa: F401
from aries_cloudcontroller.models.cred_revoked_result import CredRevokedResult  # noqa: F401
from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo  # noqa: F401
from aries_cloudcontroller.models.vc_record import VCRecord  # noqa: F401
from aries_cloudcontroller.models.vc_record_list import VCRecordList  # noqa: F401
from aries_cloudcontroller.models.w3_c_credentials_list_request import W3CCredentialsListRequest  # noqa: F401


def test_delete_credential_record(client: TestClient):
    """Test case for delete_credential_record

    Remove credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/credential/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_w3c_credential(client: TestClient):
    """Test case for delete_w3c_credential

    Remove W3C credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/credential/w3c/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credential_mime_types(client: TestClient):
    """Test case for get_credential_mime_types

    Get attribute MIME types from wallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/mime-types/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credential_record(client: TestClient):
    """Test case for get_credential_record

    Fetch credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credentials(client: TestClient):
    """Test case for get_credentials

    Fetch credentials from wallet
    """
    params = [("count", 'count_example'),     ("start", 'start_example'),     ("wql", 'wql_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credentials",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_revocation_status(client: TestClient):
    """Test case for get_revocation_status

    Query credential revocation status by id
    """
    params = [("_from", '_from_example'),     ("to", 'to_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/revoked/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_w3c_credential(client: TestClient):
    """Test case for get_w3c_credential

    Fetch W3C credential from wallet by id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/credential/w3c/{credential_id}".format(credential_id='credential_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_w3c_credentials(client: TestClient):
    """Test case for get_w3c_credentials

    Fetch W3C credentials from wallet
    """
    body = {"issuer_id":"issuer_id","schema_ids":["https://myhost:8021","https://myhost:8021"],"tag_query":{"key":"tag_query"},"types":["https://myhost:8021","https://myhost:8021"],"subject_ids":["subject_ids","subject_ids"],"given_id":"given_id","max_results":0,"proof_types":["Ed25519Signature2018","Ed25519Signature2018"],"contexts":["https://myhost:8021","https://myhost:8021"]}
    params = [("count", 'count_example'),     ("start", 'start_example'),     ("wql", 'wql_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/credentials/w3c",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

