# coding: utf-8

from fastapi.testclient import TestClient


from aries_cloudcontroller.models.invitation_create_request import InvitationCreateRequest  # noqa: F401
from aries_cloudcontroller.models.invitation_message import InvitationMessage  # noqa: F401
from aries_cloudcontroller.models.invitation_record import InvitationRecord  # noqa: F401
from aries_cloudcontroller.models.oob_record import OobRecord  # noqa: F401


def test_create_oob_invitation(client: TestClient):
    """Test case for create_oob_invitation

    Create a new connection invitation
    """
    body = {"mediation_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","metadata":"{}","protocol_version":"1.1","attachments":[{"id":"attachment-0","type":"present-proof"},{"id":"attachment-0","type":"present-proof"}],"use_public_did":0,"alias":"Barry","handshake_protocols":["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0","did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"],"my_label":"Invitation to Barry","accept":["didcomm/aip1","didcomm/aip2;env=rfc19"]}
    params = [("auto_accept", True),     ("multi_use", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/out-of-band/create-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_receive_oob_invitation(client: TestClient):
    """Test case for receive_oob_invitation

    Receive a new connection invitation
    """
    body = {"requests~attach":[{"filename":"IMG1092348.png","lastmod_time":"2021-12-31 23:59:59+00:00","mime_type":"image/png","data":{"sha256":"617a48c7c8afe0521efdc03e5bb0ad9e655893e6b4b51f0e794d70fba132aacb","jws":null,"base64":"ey4uLn0=","json":"{\"sample\": \"content\"}","links":["https://link.to/data","https://link.to/data"]},"description":"view from doorway, facing east, with lights off","@id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","byte_count":1234},{"filename":"IMG1092348.png","lastmod_time":"2021-12-31 23:59:59+00:00","mime_type":"image/png","data":{"sha256":"617a48c7c8afe0521efdc03e5bb0ad9e655893e6b4b51f0e794d70fba132aacb","jws":null,"base64":"ey4uLn0=","json":"{\"sample\": \"content\"}","links":["https://link.to/data","https://link.to/data"]},"description":"view from doorway, facing east, with lights off","@id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","byte_count":1234}],"@type":"https://didcomm.org/my-family/1.0/my-message-type","image_url":"http://192.168.56.101/img/logo.jpg","handshake_protocols":["did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0","did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"],"@id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","label":"Bob","services":[{"did":"WgWxqztrNooG92RXvxSTWv","id":"string","recipient_keys":["did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH"],"routing_keys":["did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH"],"service_endpoint":"http://192.168.56.101:8020","type":"string"},"did:sov:WgWxqztrNooG92RXvxSTWv"],"accept":["didcomm/aip1","didcomm/aip2;env=rfc19"]}
    params = [("alias", 'alias_example'),     ("auto_accept", True),     ("mediation_id", 'mediation_id_example'),     ("use_existing_connection", True)]
    headers = {
        "AuthorizationHeader": "special-key",
    }
    response = client.request(
        "POST",
        "/out-of-band/receive-invitation",
        headers=headers,
        json=body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

