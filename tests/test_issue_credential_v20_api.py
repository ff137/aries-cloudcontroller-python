# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.v20_cred_bound_offer_request import V20CredBoundOfferRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_ex_free import V20CredExFree  # noqa: F401
from aries_cloudcontroller.models.v20_cred_ex_record import V20CredExRecord  # noqa: F401
from aries_cloudcontroller.models.v20_cred_ex_record_detail import V20CredExRecordDetail  # noqa: F401
from aries_cloudcontroller.models.v20_cred_ex_record_list_result import V20CredExRecordListResult  # noqa: F401
from aries_cloudcontroller.models.v20_cred_issue_problem_report_request import V20CredIssueProblemReportRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_issue_request import V20CredIssueRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_offer_conn_free_request import V20CredOfferConnFreeRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_offer_request import V20CredOfferRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_request_free import V20CredRequestFree  # noqa: F401
from aries_cloudcontroller.models.v20_cred_request_request import V20CredRequestRequest  # noqa: F401
from aries_cloudcontroller.models.v20_cred_store_request import V20CredStoreRequest  # noqa: F401
from aries_cloudcontroller.models.v20_issue_cred_schema_core import V20IssueCredSchemaCore  # noqa: F401


def test_create_credential_record(client: TestClient):
    """Test case for create_credential_record

    Create a credential record without sending (generally for use with Out-Of-Band)
    """
    body = {"filter":null,"trace":1,"credential_preview":{"@type":"issue-credential/2.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_free_credential_offer(client: TestClient):
    """Test case for create_free_credential_offer

    Create a credential offer, independent of any proposal or connection
    """
    body = {"filter":null,"trace":1,"credential_preview":{"@type":"issue-credential/2.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"auto_issue":1,"comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/create-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_cred_ex_record(client: TestClient):
    """Test case for delete_cred_ex_record

    Remove an existing credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/issue-credential-2.0/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_cred_ex_record(client: TestClient):
    """Test case for get_cred_ex_record

    Fetch a single credential exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential-2.0/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_matching_cred_ex_records(client: TestClient):
    """Test case for get_matching_cred_ex_records

    Fetch all credential exchange records
    """
    params = [("connection_id", 'connection_id_example'),     ("role", 'role_example'),     ("state", 'state_example'),     ("thread_id", 'thread_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/issue-credential-2.0/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_issue_credential_to_holder(client: TestClient):
    """Test case for issue_credential_to_holder

    Send holder a credential
    """
    body = {"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/issue".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_cred_ex_problem(client: TestClient):
    """Test case for report_cred_ex_problem

    Send a problem report for credential exchange
    """
    body = {"description":"description"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/problem-report".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_credential_offer(client: TestClient):
    """Test case for send_credential_offer

    Send holder a credential offer in reference to a proposal with preview
    """
    body = {"filter":null,"counter_preview":null}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/send-offer".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_credential_request(client: TestClient):
    """Test case for send_credential_request

    Send issuer a credential request
    """
    body = {"holder_did":"did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/send-request".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential(client: TestClient):
    """Test case for send_free_credential

    Send holder a credential, automating entire flow
    """
    body = {"filter":null,"trace":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","credential_preview":{"@type":"issue-credential/2.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"verification_method":"verification_method","comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential_offer(client: TestClient):
    """Test case for send_free_credential_offer

    Send holder a credential offer, independent of any proposal
    """
    body = {"filter":null,"trace":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","credential_preview":{"@type":"issue-credential/2.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"auto_issue":1,"comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential_proposal(client: TestClient):
    """Test case for send_free_credential_proposal

    Send issuer a credential proposal
    """
    body = {"filter":null,"trace":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","credential_preview":{"@type":"issue-credential/2.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"verification_method":"verification_method","comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential_request(client: TestClient):
    """Test case for send_free_credential_request

    Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request
    """
    body = {"filter":null,"holder_did":"did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs","trace":0,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/send-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_store_received_credential(client: TestClient):
    """Test case for store_received_credential

    Store a received credential
    """
    body = {"credential_id":"credential_id"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential-2.0/records/{cred_ex_id}/store".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

