# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.v10_discovery_exchange_list_result import V10DiscoveryExchangeListResult  # noqa: F401
from aries_cloudcontroller.models.v10_discovery_record import V10DiscoveryRecord  # noqa: F401


def test_get_v10_feature_records(client: TestClient):
    """Test case for get_v10_feature_records

    Discover Features records
    """
    params = [("connection_id", 'connection_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/discover-features/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v10_features_query(client: TestClient):
    """Test case for get_v10_features_query

    Query supported features
    """
    params = [("comment", 'comment_example'),     ("connection_id", 'connection_id_example'),     ("query", 'query_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/discover-features/query",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

