# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.admin_config import AdminConfig  # noqa: F401
from aries_cloudcontroller.models.admin_modules import AdminModules  # noqa: F401
from aries_cloudcontroller.models.admin_status import AdminStatus  # noqa: F401
from aries_cloudcontroller.models.admin_status_liveliness import AdminStatusLiveliness  # noqa: F401
from aries_cloudcontroller.models.admin_status_readiness import AdminStatusReadiness  # noqa: F401


def test_get_config(client: TestClient):
    """Test case for get_config

    Fetch the server configuration
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/config",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_liveliness(client: TestClient):
    """Test case for get_liveliness

    Liveliness check
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/live",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_loaded_plugins(client: TestClient):
    """Test case for get_loaded_plugins

    Fetch the list of loaded plugins
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/plugins",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_readiness(client: TestClient):
    """Test case for get_readiness

    Readiness check
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status/ready",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_status(client: TestClient):
    """Test case for get_status

    Fetch the server status
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/status",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reset_statistics(client: TestClient):
    """Test case for reset_statistics

    Reset statistics
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/status/reset",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shutdown_server(client: TestClient):
    """Test case for shutdown_server

    Shut down server
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/shutdown",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

