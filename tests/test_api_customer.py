from . import client, id_business, id_customer, id_employee_bruno


def test_get_all_customer():
    response = client.get("/customer")
    assert response.status_code == 200


def test_get_all_customer_by_business_id():
    response = client.post(f"/customer/business/{id_business}")
    assert response.status_code == 200


def test_get_by_id():
    response = client.get(f"/customer/{id_customer}")
    assert response.status_code == 200


def test_create_customer():
    response = client.post("/customer/create/")
    assert response.status_code == 422


def test_delete_customer():
    response = client.post("/customer/delete/")
    assert response.status_code == 422


def test_update_customer_by_id():
    response = client.post("/customer/update/")
    assert response.status_code == 422


def test_get_customer_name_by_employee_id():
    response = client.get(f"/customer/{id_employee_bruno}")
    assert response.status_code == 200
