from . import client, id_presence_type


def test_get_all_presence_type():
    response = client.get("/type/presence")
    assert response.status_code == 200


def test_get_presence_type_by_id():
    response = client.get(f"/type/presence/id/{id_presence_type}")
    assert response.status_code == 200


def test_create_presence_type():
    response = client.post("/type/presence/create/")
    assert response.status_code == 422


def test_update_presence_type():
    response = client.patch("/type/presence/update/")
    assert response.status_code == 422


def test_delete_presence_type():
    response = client.post("/type/presence/delete/")
    assert response.status_code == 422
