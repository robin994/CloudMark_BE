from . import client, id_order, id_employee


def test_get_all_orders():
    response = client.get("/orders")
    assert response.status_code == 200


def test_get_order_by_id():
    response = client.get(f"/orders/{id_order}")
    assert response.status_code == 200


def test_create_order():
    response = client.post("/orders/create/")
    assert response.status_code == 422


def test_update_order():
    response = client.post("/orders/update/")
    assert response.status_code == 422


def test_delete_order():
    response = client.post("/orders/delete/")
    assert response.status_code == 422


def test_get_order_by_employee():
    response = client.get(f"/orders/employee/{id_employee}")
    assert response.status_code == 200


def test_get_orders_by_customer_id_and_business_id():
    response = client.post("/orders/customer")
    assert response.status_code == 422


def test_add_employee_into_order():
    response = client.post("/orders/employee/relational")
    assert response.status_code == 422
