from . import client, id_presence, id_employee_bruno


def test_get_presence_by_primary_key():
    response = client.get(f"/presence/{id_presence}/{id_employee_bruno}")
    assert response.status_code == 200


def test_get_all_presence():
    response = client.get("/presence/all")
    assert response.status_code == 200


def test_get_all_presence_with_first_name_last_name():
    response = client.get("/presence/all/first_name/last_name/")
    assert response.status_code == 200


def test_get_presences_by_employee():
    response = client.get(f"/presence/load_employee={id_employee_bruno}")
    assert response.status_code == 200


def test_get_month_year_presences():
    response = client.post("/presence/load")
    assert response.status_code == 422


def test_create_presence():
    response = client.post("/presence/create")
    assert response.status_code == 422


def test_update_presence():
    response = client.post("/presence/update/")
    assert response.status_code == 422


def test_delete_presence():
    response = client.post("/presence/delete/")
    assert response.status_code == 422


def test_insert_update_presence():
    response = client.post("/presence/insertUpdate")
    assert response.status_code == 422


def test_insert_presences():
    response = client.post("/presence/insertPresences")
    assert response.status_code == 422
