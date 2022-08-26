from . import client


def test_get_all_employee_by_customers_rate():
    response = client.get("/order/employee/rate/")
    assert response.status_code == 200


def test_get_all_employee_by_customers_rate_post():
    response = client.post("/order/employee/rate/")
    assert response.status_code == 422


def test_create_new_order_employee():
    response = client.post("/order/employee/create/")
    assert response.status_code == 422


def test_delete_order_employee():
    response = client.post("/order/employee/delete/")
    assert response.status_code == 422


def test_update_order_employee():
    response = client.post("/order/employee/delete/")
    assert response.status_code == 422
