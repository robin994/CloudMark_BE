from . import client, id_account, id_business, id_order, id_employee


def test_get_all_employees():
    response = client.get("/employee")
    assert response.status_code == 200


def test_get_all_employees_by_empty_key():
    response = client.get("/employee/all")
    assert response.status_code == 200


def test_filter_by_employee():
    response = client.post("/employee/")
    assert response.status_code == 422


def test_get_employees_by_last_work():
    response = client.get("/employee/lastwork")
    assert response.status_code == 200


def test_get_employees_by_business():
    response = client.get(f"/employee/business/{id_business}")
    assert response.status_code == 200


def test_get_employees_by_account():
    response = client.get(f"/employee/account/{id_account}")
    assert response.status_code == 200


def test_get_employees_by_id():
    response = client.get(f"/employee/{id_business}")
    assert response.status_code == 200


def test_get_employees_by_id_order():
    response = client.get(f"/employee/order/{id_order}")
    assert response.status_code == 200


def test_create_employee():
    response = client.post("/employee/create/")
    assert response.status_code == 422


def test_update_employee_by_id():
    response = client.post("/employee/update/")
    assert response.status_code == 422


def test_delete_employee_by_id():
    response = client.post("/employee/delete/")
    assert response.status_code == 422


def test_create_new_account_employee():
    response = client.post("/employee/create/account")
    assert response.status_code == 422


def test_show_all_Employees_by_Account_and_Business():
    response = client.get("/all/employees/account/business")
    assert response.status_code == 200


def test_disable_account_by_Employee():
    response = client.get(f"/employee/{id_employee}/disabled")
    assert response.status_code == 200


def test_enable_account_by_employee():
    response = client.get(f"/employee/{id_employee}/enabled")
    assert response.status_code == 200


def test_check_employee_account():
    response = client.post("/employee/checkAccount")
    assert response.status_code == 422


def test_add_employee_to_business():
    response = client.post("/employee/business/relational")
    assert response.status_code == 422
