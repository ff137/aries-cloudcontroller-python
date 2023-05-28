# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.create_wallet_request import CreateWalletRequest  # noqa: F401
from aries_cloudcontroller.models.create_wallet_response import CreateWalletResponse  # noqa: F401
from aries_cloudcontroller.models.create_wallet_token_request import CreateWalletTokenRequest  # noqa: F401
from aries_cloudcontroller.models.create_wallet_token_response import CreateWalletTokenResponse  # noqa: F401
from aries_cloudcontroller.models.remove_wallet_request import RemoveWalletRequest  # noqa: F401
from aries_cloudcontroller.models.update_wallet_request import UpdateWalletRequest  # noqa: F401
from aries_cloudcontroller.models.wallet_list import WalletList  # noqa: F401
from aries_cloudcontroller.models.wallet_record import WalletRecord  # noqa: F401


def test_create_wallet(client: TestClient):
    """Test case for create_wallet

    Create a subwallet
    """
    body = {"wallet_key":"MySecretKey123","image_url":"https://aries.ca/images/sample.png","wallet_webhook_urls":["http://localhost:8022/webhooks","http://localhost:8022/webhooks"],"wallet_key_derivation":"RAW","wallet_name":"MyNewWallet","key_management_mode":"managed","wallet_type":"indy","label":"Alice","wallet_dispatch_type":"default"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_wallet(client: TestClient):
    """Test case for delete_wallet

    Remove a subwallet
    """
    body = {"wallet_key":"MySecretKey123"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet/{wallet_id}/remove".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_auth_token(client: TestClient):
    """Test case for get_auth_token

    Get auth token for a subwallet
    """
    body = {"wallet_key":"MySecretKey123"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/multitenancy/wallet/{wallet_id}/token".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_matching_wallets(client: TestClient):
    """Test case for get_matching_wallets

    Query subwallets
    """
    params = [("wallet_name", 'wallet_name_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/multitenancy/wallets",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_wallet_record(client: TestClient):
    """Test case for get_wallet_record

    Get a single subwallet
    """

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/multitenancy/wallet/{wallet_id}".format(wallet_id='wallet_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_wallet(client: TestClient):
    """Test case for update_wallet

    Update a subwallet
    """
    body = {"image_url":"https://aries.ca/images/sample.png","wallet_webhook_urls":["http://localhost:8022/webhooks","http://localhost:8022/webhooks"],"label":"Alice","wallet_dispatch_type":"default"}

    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "PUT",
        "/multitenancy/wallet/{wallet_id}".format(wallet_id='wallet_id_example'),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

