# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.indy_cred_precis import IndyCredPrecis  # noqa: F401
from aries_cloudcontroller.models.indy_pres_spec import IndyPresSpec  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_create_request_request import V10PresentationCreateRequestRequest  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_exchange import V10PresentationExchange  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_exchange_list import V10PresentationExchangeList  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_problem_report_request import V10PresentationProblemReportRequest  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_proposal_request import V10PresentationProposalRequest  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_send_request_request import V10PresentationSendRequestRequest  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_send_request_to_proposal import V10PresentationSendRequestToProposal  # noqa: F401


def test_create_free_proof_request(client: TestClient):
    """Test case for create_free_proof_request

    Creates a presentation request not bound to any proposal or connection
    """
    body = {"trace":0,"auto_verify":0,"proof_request":{"name":"Proof request","requested_attributes":{"key":{"names":["age","age"],"name":"favouriteDrink","restrictions":[{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"},{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"}],"non_revoked":null}},"non_revoked":null,"nonce":"1","requested_predicates":{"key":{"p_value":0,"name":"index","p_type":">=","restrictions":[{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"},{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"}],"non_revoked":null}},"version":"1.0"},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/create-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_pres_ex_record(client: TestClient):
    """Test case for delete_pres_ex_record

    Remove an existing presentation exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/present-proof/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_matching_pres_ex_records(client: TestClient):
    """Test case for get_matching_pres_ex_records

    Fetch all present-proof exchange records
    """
    params = [("connection_id", 'connection_id_example'),     ("role", 'role_example'),     ("state", 'state_example'),     ("thread_id", 'thread_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_pres_ex_credentials(client: TestClient):
    """Test case for get_pres_ex_credentials

    Fetch credentials for a presentation request from wallet
    """
    params = [("count", 'count_example'),     ("extra_query", 'extra_query_example'),     ("referent", 'referent_example'),     ("start", 'start_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof/records/{pres_ex_id}/credentials".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_pres_ex_record(client: TestClient):
    """Test case for get_pres_ex_record

    Fetch a single presentation exchange record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_pres_ex_problem(client: TestClient):
    """Test case for report_pres_ex_problem

    Send a problem report for presentation exchange
    """
    body = {"description":"description"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/records/{pres_ex_id}/problem-report".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_presentation_request(client: TestClient):
    """Test case for send_free_presentation_request

    Sends a free presentation request not bound to any proposal
    """
    body = {"trace":0,"auto_verify":0,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","proof_request":{"name":"Proof request","requested_attributes":{"key":{"names":["age","age"],"name":"favouriteDrink","restrictions":[{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"},{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"}],"non_revoked":null}},"non_revoked":null,"nonce":"1","requested_predicates":{"key":{"p_value":0,"name":"index","p_type":">=","restrictions":[{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"},{"key":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"}],"non_revoked":null}},"version":"1.0"},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/send-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_presentation_proposal(client: TestClient):
    """Test case for send_presentation_proposal

    Sends a presentation proposal
    """
    body = {"trace":0,"auto_present":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","presentation_proposal":{"predicates":[{"predicate":">=","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","name":"high_score","threshold":0},{"predicate":">=","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","name":"high_score","threshold":0}],"@type":"did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-proof/1.0/presentation-preview","attributes":[{"mime_type":"image/jpeg","referent":"0","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","name":"favourite_drink","value":"martini"},{"mime_type":"image/jpeg","referent":"0","cred_def_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","name":"favourite_drink","value":"martini"}]},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_proof_presentation(client: TestClient):
    """Test case for send_proof_presentation

    Sends a proof presentation
    """
    body = {"trace":0,"requested_attributes":{"key":{"cred_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","revealed":1}},"requested_predicates":{"key":{"cred_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","timestamp":1640995199}},"self_attested_attributes":{"key":"self_attested_value"}}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/records/{pres_ex_id}/send-presentation".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_proof_presentation_request(client: TestClient):
    """Test case for send_proof_presentation_request

    Sends a presentation request in reference to a proposal
    """
    body = {"trace":0,"auto_verify":0}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/records/{pres_ex_id}/send-request".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_verify_received_presentation(client: TestClient):
    """Test case for verify_received_presentation

    Verify a received presentation
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof/records/{pres_ex_id}/verify-presentation".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

