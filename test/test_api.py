from backend.api import app


def test_api_vulnerable():

    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "code": "gets(buffer);"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == "VULNERABLE"


def test_api_safe():

    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "code": "fgets(buffer,sizeof(buffer),stdin);"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == "SAFE"