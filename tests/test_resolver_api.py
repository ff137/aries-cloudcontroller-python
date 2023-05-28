# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.resolution_result import ResolutionResult  # noqa: F401


def test_get_did_document(client: TestClient):
    """Test case for get_did_document

    Retrieve doc for requested did
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/resolver/resolve/{did}".format(did='did_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

