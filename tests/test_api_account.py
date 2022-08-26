from . import client, id_account


def test_get_all_accounts():
    response = client.get("/account")
    assert response.status_code == 200


def test_get_accounts_by_uuid():
    response = client.get(f"/account/{id_account}")
    assert response.status_code == 200


def test_create_account():
    response = client.post("/account/signin/")
    assert response.status_code == 422


def test_update_account():
    response = client.post("/account/update/")
    assert response.status_code == 422


def test_reset_password():
    response = client.patch("/account/reset_passowrd")
    assert response.status_code == 422


def test_get_session():
    response = client.post("/account/login")
    assert response.status_code == 422


def test_delete_account():
    response = client.post("/account/delete/")
    assert response.status_code == 422


def test_jwt_verify():
    response = client.post("/account/verify_account")
    assert response.status_code == 422
