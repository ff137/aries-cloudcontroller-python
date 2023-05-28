# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.clear_pending_revocations_request import ClearPendingRevocationsRequest  # noqa: F401
from aries_cloudcontroller.models.cred_rev_indy_records_result import CredRevIndyRecordsResult  # noqa: F401
from aries_cloudcontroller.models.cred_rev_record_details_result import CredRevRecordDetailsResult  # noqa: F401
from aries_cloudcontroller.models.cred_rev_record_result import CredRevRecordResult  # noqa: F401
from aries_cloudcontroller.models.publish_revocations import PublishRevocations  # noqa: F401
from aries_cloudcontroller.models.rev_reg_create_request import RevRegCreateRequest  # noqa: F401
from aries_cloudcontroller.models.rev_reg_issued_result import RevRegIssuedResult  # noqa: F401
from aries_cloudcontroller.models.rev_reg_result import RevRegResult  # noqa: F401
from aries_cloudcontroller.models.rev_reg_update_tails_file_uri import RevRegUpdateTailsFileUri  # noqa: F401
from aries_cloudcontroller.models.rev_reg_wallet_updated_result import RevRegWalletUpdatedResult  # noqa: F401
from aries_cloudcontroller.models.rev_regs_created import RevRegsCreated  # noqa: F401
from aries_cloudcontroller.models.revoke_request import RevokeRequest  # noqa: F401
from aries_cloudcontroller.models.tails_delete_response import TailsDeleteResponse  # noqa: F401
from aries_cloudcontroller.models.txn_or_publish_revocations_result import TxnOrPublishRevocationsResult  # noqa: F401
from aries_cloudcontroller.models.txn_or_rev_reg_result import TxnOrRevRegResult  # noqa: F401


def test_clear_pending_revocations(client: TestClient):
    """Test case for clear_pending_revocations

    Clear pending revocations
    """
    body = {"purge":{"key":["12345","12345"]}}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/clear-pending-revocations",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_revocation_registry(client: TestClient):
    """Test case for create_revocation_registry

    Creates a new revocation registry
    """
    body = {"credential_definition_id":"WgWxqztrNooG92RXvxSTWv:3:CL:20:tag","max_cred_num":1000}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/create-registry",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_tails_file(client: TestClient):
    """Test case for delete_tails_file

    Delete the tail files
    """
    params = [("cred_def_id", 'cred_def_id_example'),     ("rev_reg_id", 'rev_reg_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "DELETE",
        "/revocation/registry/delete-tails-file",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_download_tails_file(client: TestClient):
    """Test case for download_tails_file

    Download tails file
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/tails-file".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_active_registry_for_cred_def_id(client: TestClient):
    """Test case for get_active_registry_for_cred_def_id

    Get current active revocation registry by credential definition id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/active-registry/{cred_def_id}".format(cred_def_id='cred_def_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_created_registries(client: TestClient):
    """Test case for get_created_registries

    Search for matching revocation registries that current agent created
    """
    params = [("cred_def_id", 'cred_def_id_example'),     ("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registries/created",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credential_revocation_record(client: TestClient):
    """Test case for get_credential_revocation_record

    Get credential revocation status
    """
    params = [("cred_ex_id", 'cred_ex_id_example'),     ("cred_rev_id", 'cred_rev_id_example'),     ("rev_reg_id", 'rev_reg_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/credential-record",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_issued_credential_details(client: TestClient):
    """Test case for get_issued_credential_details

    Get details of credentials issued against revocation registry
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/issued/details".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_issued_credentials_count(client: TestClient):
    """Test case for get_issued_credentials_count

    Get number of credentials issued against revocation registry
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/issued".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_published_credential_details(client: TestClient):
    """Test case for get_published_credential_details

    Get details of revoked credentials from ledger
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}/issued/indy_recs".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_revocation_registry(client: TestClient):
    """Test case for get_revocation_registry

    Get revocation registry by revocation registry id
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/revocation/registry/{rev_reg_id}".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_revocation_registry_definition(client: TestClient):
    """Test case for publish_revocation_registry_definition

    Send revocation registry definition to ledger
    """
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/registry/{rev_reg_id}/definition".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_revocation_registry_entry(client: TestClient):
    """Test case for publish_revocation_registry_entry

    Send revocation registry entry to ledger
    """
    params = [("conn_id", 'conn_id_example'),     ("create_transaction_for_endorser", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/registry/{rev_reg_id}/entry".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_publish_revocations(client: TestClient):
    """Test case for publish_revocations

    Publish pending revocations to ledger
    """
    body = {"rrid2crid":{"key":["12345","12345"]}}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/publish-revocations",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_revoke_issued_credential(client: TestClient):
    """Test case for revoke_issued_credential

    Revoke an issued credential
    """
    body = {"cred_rev_id":"12345","thread_id":"thread_id","rev_reg_id":"WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0","connection_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","publish":1,"comment":"comment","notify_version":"v1_0","notify":1,"cred_ex_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/revocation/revoke",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_revocation_registry_state(client: TestClient):
    """Test case for set_revocation_registry_state

    Set revocation registry state manually
    """
    params = [("state", 'state_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/revocation/registry/{rev_reg_id}/set-state".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_revocation_entry_state(client: TestClient):
    """Test case for update_revocation_entry_state

    Fix revocation state in wallet and return number of updated entries
    """
    params = [("apply_ledger_update", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/revocation/registry/{rev_reg_id}/fix-revocation-entry-state".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_revocation_registry(client: TestClient):
    """Test case for update_revocation_registry

    Update revocation registry with new public URI to its tails file
    """
    body = {"tails_public_uri":"http://192.168.56.133:6543/revocation/registry/WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0/tails-file"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PATCH",
        "/revocation/registry/{rev_reg_id}".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_upload_tails_file(client: TestClient):
    """Test case for upload_tails_file

    Upload local tails file to server
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/revocation/registry/{rev_reg_id}/tails-file".format(rev_reg_id='rev_reg_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

