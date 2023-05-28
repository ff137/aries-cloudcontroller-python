# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.date import Date  # noqa: F401
from aries_cloudcontroller.models.endorser_info import EndorserInfo  # noqa: F401
from aries_cloudcontroller.models.transaction_jobs import TransactionJobs  # noqa: F401
from aries_cloudcontroller.models.transaction_list import TransactionList  # noqa: F401
from aries_cloudcontroller.models.transaction_record import TransactionRecord  # noqa: F401


def test_cancel_transaction_request(client: TestClient):
    """Test case for cancel_transaction_request

    For Author to cancel a particular transaction request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/cancel".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_transaction_request(client: TestClient):
    """Test case for create_transaction_request

    For author to send a transaction request
    """
    body = {"expires_time":"2021-03-29 05:22:19+00:00"}
    params = [("tran_id", 'tran_id_example'),     ("endorser_write_txn", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/create-request",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_endorse_transaction(client: TestClient):
    """Test case for endorse_transaction

    For Endorser to endorse a particular transaction record
    """
    params = [("endorser_did", 'endorser_did_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/endorse".format(tran_id='tran_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_transaction_list(client: TestClient):
    """Test case for get_transaction_list

    Query transactions
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/transactions",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_transaction_record(client: TestClient):
    """Test case for get_transaction_record

    Fetch a single transaction record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/transactions/{tran_id}".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_endorsed_transaction(client: TestClient):
    """Test case for publish_endorsed_transaction

    For Author / Endorser to write an endorsed transaction to the ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/write".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_refuse_transaction(client: TestClient):
    """Test case for refuse_transaction

    For Endorser to refuse a particular transaction record
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{tran_id}/refuse".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resend_transaction_request(client: TestClient):
    """Test case for resend_transaction_request

    For Author to resend a particular transaction request
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transaction/{tran_id}/resend".format(tran_id='tran_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_endorser_info_for_conn_id(client: TestClient):
    """Test case for set_endorser_info_for_conn_id

    Set Endorser Info
    """
    params = [("endorser_did", 'endorser_did_example'),     ("endorser_name", 'endorser_name_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{conn_id}/set-endorser-info".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_endorser_role_for_conn_id(client: TestClient):
    """Test case for set_endorser_role_for_conn_id

    Set transaction jobs
    """
    params = [("transaction_my_job", 'transaction_my_job_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/transactions/{conn_id}/set-endorser-role".format(conn_id='conn_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

