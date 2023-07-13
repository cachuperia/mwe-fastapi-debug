from starlette import status


def test_root_get(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
