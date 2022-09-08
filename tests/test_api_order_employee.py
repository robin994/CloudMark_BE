from . import client, order_employee, business_markup

order_id = order_employee["id_order"]
order_id_employee = order_employee["id_employee"]
order_rate = order_employee["rate"]
business_id = business_markup["id_business"]


def test_get_all_employee_by_customers_rate():
    response = client.get("/order/employee/rate/")
    assert response.status_code == 200


def test_get_all_employee_by_customers_rate_post():
    response = client.post("/order/employee/rate/", json={
        "id_business": business_id
    })
    assert response.status_code == 200


def test_create_new_order_employee():
    response = client.post("/order/employee/create/", json={
        "id_order": order_id,
        "id_employee": order_id_employee,
        "rate": order_rate
    })
    assert response.status_code == 200


def test_delete_order_employee():
    response = client.post("/order/employee/delete/", json={
        "old_order": {
            "id_order": order_id,
            "id_employee": order_id_employee,
            "rate": order_rate
        },
        "new_order": {
            "id_order": order_id + 1,
            "id_employee": order_id_employee,
            "rate": 7357
        }
    })
    assert response.status_code == 200
    
# the slack endpoint is overwritten
# def test_update_order_employee():
#     response = client.post("/order/employee/delete/")
#     assert response.status_code == 422
