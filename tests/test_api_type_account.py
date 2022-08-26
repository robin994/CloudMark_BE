from . import client, id_account_type


def test_get_all_tipo_account():
    response = client.get("/type/account")
    assert response.status_code == 200


def test_get_tipo_account_by_id():
    response = client.post(f"/type/account/{id_account_type}")
    assert response.status_code == 200


def test_create_account_type():
    response = client.post("/type/account/create/")
    assert response.status_code == 422


def test_update_account_type():
    response = client.post("/type/account/update/")
    assert response.status_code == 422


def test_delete_account_type():
    response = client.post("/type/account/delete/")
    assert response.status_code == 422
