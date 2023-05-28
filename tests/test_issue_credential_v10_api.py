# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.v10_credential_bound_offer_request import V10CredentialBoundOfferRequest  # noqa: F401
from aries_cloudcontroller.models.v10_credential_conn_free_offer_request import V10CredentialConnFreeOfferRequest  # noqa: F401
from aries_cloudcontroller.models.v10_credential_create import V10CredentialCreate  # noqa: F401
from aries_cloudcontroller.models.v10_credential_exchange import V10CredentialExchange  # noqa: F401
from aries_cloudcontroller.models.v10_credential_exchange_list_result import V10CredentialExchangeListResult  # noqa: F401
from aries_cloudcontroller.models.v10_credential_free_offer_request import V10CredentialFreeOfferRequest  # noqa: F401
from aries_cloudcontroller.models.v10_credential_issue_request import V10CredentialIssueRequest  # noqa: F401
from aries_cloudcontroller.models.v10_credential_problem_report_request import V10CredentialProblemReportRequest  # noqa: F401
from aries_cloudcontroller.models.v10_credential_proposal_request_mand import V10CredentialProposalRequestMand  # noqa: F401
from aries_cloudcontroller.models.v10_credential_proposal_request_opt import V10CredentialProposalRequestOpt  # noqa: F401
from aries_cloudcontroller.models.v10_credential_store_request import V10CredentialStoreRequest  # noqa: F401


def test_create_credential_record(client: TestClient):
    """Test case for create_credential_record

    Create a credential record without sending (generally for use with Out-Of-Band)
    """
    body = {"schema_version":"1.0","trace":1,"issuer_did":"WgWxqztrNooG92RXvxSTWv","credential_proposal":{"@type":"issue-credential/1.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","schema_id":"WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0","comment":"comment","schema_issuer_did":"WgWxqztrNooG92RXvxSTWv","schema_name":"preferences","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/create",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_free_credential_offer(client: TestClient):
    """Test case for create_free_credential_offer

    Create a credential offer, independent of any proposal or connection
    """
    body = {"trace":1,"credential_preview":{"@type":"issue-credential/1.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","auto_issue":1,"comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/create-offer",
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
        "/issue-credential/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
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
        "/issue-credential/records/{cred_ex_id}".format(cred_ex_id='cred_ex_id_example'),
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
        "/issue-credential/records",
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
        "/issue-credential/records/{cred_ex_id}/issue".format(cred_ex_id='cred_ex_id_example'),
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
        "/issue-credential/records/{cred_ex_id}/problem-report".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_credential_offer(client: TestClient):
    """Test case for send_credential_offer

    Send holder a credential offer in reference to a proposal with preview
    """
    body = {"counter_proposal":null}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/send-offer".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_credential_request(client: TestClient):
    """Test case for send_credential_request

    Send issuer a credential request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/records/{cred_ex_id}/send-request".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential(client: TestClient):
    """Test case for send_free_credential

    Send holder a credential, automating entire flow
    """
    body = {"schema_version":"1.0","trace":1,"issuer_did":"WgWxqztrNooG92RXvxSTWv","credential_proposal":{"@type":"issue-credential/1.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","schema_id":"WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0","comment":"comment","schema_issuer_did":"WgWxqztrNooG92RXvxSTWv","schema_name":"preferences","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential_offer(client: TestClient):
    """Test case for send_free_credential_offer

    Send holder a credential offer, independent of any proposal
    """
    body = {"trace":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","credential_preview":{"@type":"issue-credential/1.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","auto_issue":1,"comment":"comment","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send-offer",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_credential_proposal(client: TestClient):
    """Test case for send_free_credential_proposal

    Send issuer a credential proposal
    """
    body = {"schema_version":"1.0","trace":1,"issuer_did":"WgWxqztrNooG92RXvxSTWv","credential_proposal":{"@type":"issue-credential/1.0/credential-preview","attributes":[{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","name":"favourite_drink","value":"martini"}]},"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","schema_id":"WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0","comment":"comment","schema_issuer_did":"WgWxqztrNooG92RXvxSTWv","schema_name":"preferences","auto_remove":1}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/issue-credential/send-proposal",
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
        "/issue-credential/records/{cred_ex_id}/store".format(cred_ex_id='cred_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

