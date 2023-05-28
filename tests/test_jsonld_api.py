# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.sign_request import SignRequest  # noqa: F401
from aries_cloudcontroller.models.sign_response import SignResponse  # noqa: F401
from aries_cloudcontroller.models.verify_request import VerifyRequest  # noqa: F401
from aries_cloudcontroller.models.verify_response import VerifyResponse  # noqa: F401


def test_sign(client: TestClient):
    """Test case for sign

    Sign a JSON-LD structure and return it
    """
    body = {"doc":{"credential":"{}","options":null},"verkey":"verkey"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/jsonld/sign",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_verify(client: TestClient):
    """Test case for verify

    Verify a JSON-LD structure.
    """
    body = {"doc":null,"verkey":"verkey"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/jsonld/verify",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

