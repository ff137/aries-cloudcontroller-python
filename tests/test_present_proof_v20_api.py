# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.indy_cred_precis import IndyCredPrecis  # noqa: F401
from aries_cloudcontroller.models.v20_pres_create_request_request import V20PresCreateRequestRequest  # noqa: F401
from aries_cloudcontroller.models.v20_pres_ex_record import V20PresExRecord  # noqa: F401
from aries_cloudcontroller.models.v20_pres_ex_record_list import V20PresExRecordList  # noqa: F401
from aries_cloudcontroller.models.v20_pres_problem_report_request import V20PresProblemReportRequest  # noqa: F401
from aries_cloudcontroller.models.v20_pres_proposal_request import V20PresProposalRequest  # noqa: F401
from aries_cloudcontroller.models.v20_pres_send_request_request import V20PresSendRequestRequest  # noqa: F401
from aries_cloudcontroller.models.v20_pres_spec_by_format_request import V20PresSpecByFormatRequest  # noqa: F401
from aries_cloudcontroller.models.v20_presentation_send_request_to_proposal import V20PresentationSendRequestToProposal  # noqa: F401


def test_create_proof_request(client: TestClient):
    """Test case for create_proof_request

    Creates a presentation request not bound to any proposal or connection
    """
    body = {"trace":0,"auto_verify":0,"presentation_request":{"dif":null,"indy":null},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/create-request",
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
        "/present-proof-2.0/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
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
        "/present-proof-2.0/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_pres_ex_credentials(client: TestClient):
    """Test case for get_pres_ex_credentials

    Fetch credentials from wallet for presentation request
    """
    params = [("count", 'count_example'),     ("extra_query", 'extra_query_example'),     ("referent", 'referent_example'),     ("start", 'start_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/present-proof-2.0/records/{pres_ex_id}/credentials".format(pres_ex_id='pres_ex_id_example'),
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
        "/present-proof-2.0/records/{pres_ex_id}".format(pres_ex_id='pres_ex_id_example'),
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
        "/present-proof-2.0/records/{pres_ex_id}/problem-report".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_free_presentation_request(client: TestClient):
    """Test case for send_free_presentation_request

    Sends a free presentation request not bound to any proposal
    """
    body = {"trace":0,"auto_verify":0,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","presentation_request":{"dif":null,"indy":null},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/send-request",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_presentation_proposal(client: TestClient):
    """Test case for send_presentation_proposal

    Sends a presentation proposal
    """
    body = {"trace":0,"auto_present":1,"connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","presentation_proposal":{"dif":null,"indy":null},"comment":"comment"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/send-proposal",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_send_proof_presentation(client: TestClient):
    """Test case for send_proof_presentation

    Sends a proof presentation
    """
    body = {"dif":null,"trace":1,"indy":null}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/present-proof-2.0/records/{pres_ex_id}/send-presentation".format(pres_ex_id='pres_ex_id_example'),
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
        "/present-proof-2.0/records/{pres_ex_id}/send-request".format(pres_ex_id='pres_ex_id_example'),
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
        "/present-proof-2.0/records/{pres_ex_id}/verify-presentation".format(pres_ex_id='pres_ex_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

