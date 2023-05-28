# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.v20_discovery_exchange_list_result import V20DiscoveryExchangeListResult  # noqa: F401
from aries_cloudcontroller.models.v20_discovery_exchange_result import V20DiscoveryExchangeResult  # noqa: F401


def test_get_v20_feature_records(client: TestClient):
    """Test case for get_v20_feature_records

    Discover Features v2.0 records
    """
    params = [("connection_id", 'connection_id_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/discover-features-2.0/records",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v20_features_queries(client: TestClient):
    """Test case for get_v20_features_queries

    Query supported features
    """
    params = [("connection_id", 'connection_id_example'),     ("query_goal_code", 'query_goal_code_example'),     ("query_protocol", 'query_protocol_example')]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "GET",
        "/discover-features-2.0/queries",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

