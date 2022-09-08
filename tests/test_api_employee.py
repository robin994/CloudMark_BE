from . import client, employee_bruno, account_bruno, business_markup, \
              order_pippo, type_account_admin

employee_first_name = employee_bruno["first_name"]
employee_last_name = employee_bruno["last_name"]
employee_cf = employee_bruno["cf"]
employee_iban = employee_bruno["iban"]
employee_id_contractType = employee_bruno["id_contractType"]
employee_email = employee_bruno["email"]
employee_phoneNumber = employee_bruno["phoneNumber"]
employee_id = employee_bruno["id_employee"]
business_id = business_markup["id_business"]
account_id = account_bruno["id_account"]
order_id = order_pippo["id_order"]
account_type_id = type_account_admin["id_account_type"]


def test_get_all_employees():
    response = client.get("/employee")
    assert response.status_code == 200


def test_get_all_employees_by_empty_key():
    response = client.get("/employee/all")
    assert response.status_code == 200


def test_filter_by_employee():
    response = client.post("/employee/", params={
        "idAzienda": business_id
    }, json={
        "first_name": employee_first_name,
        "last_name": employee_last_name,
        "cf": employee_cf,
        "iban": employee_iban,
        "id_contractType": employee_id_contractType,
        "email": employee_email,
        "phoneNumber": employee_phoneNumber
    })
    assert response.status_code == 200


def test_get_employees_by_last_work():
    response = client.get("/employee/lastwork")
    assert response.status_code == 200


def test_get_employees_by_business():
    response = client.get(f"/employee/business/{business_id}")
    assert response.status_code == 200


def test_get_employees_by_account():
    response = client.get(f"/employee/account/{account_id}")
    assert response.status_code == 200


def test_get_employees_by_id():
    response = client.get(f"/employee/{business_id}")
    assert response.status_code == 200


def test_get_employees_by_id_order():
    response = client.get(f"/employee/order/{order_id}")
    assert response.status_code == 200


def test_create_employee():
    response = client.post("/employee/create/", json={
        "first_name": employee_first_name,
        "last_name": employee_last_name,
        "cf": employee_cf,
        "iban": employee_iban,
        "id_contractType": employee_id_contractType,
        "email": employee_email,
        "phoneNumber": employee_phoneNumber
    })
    assert response.status_code == 200


def test_update_employee_by_id():
    response = client.post("/employee/update/", json={
        "first_name": employee_first_name,
        "last_name": employee_last_name,
        "cf": employee_cf,
        "iban": employee_iban,
        "id_contractType": employee_id_contractType,
        "email": employee_email,
        "phoneNumber": employee_phoneNumber,
        "id_employee": employee_id
    })
    assert response.status_code == 200


def test_delete_employee_by_id():
    response = client.post("/employee/delete/", params={
        "id_employee": employee_id
    })
    assert response.status_code == 200


def test_create_new_account_employee():
    response = client.post("/employee/create/account", json={
        "new_employee": {
            "first_name": employee_first_name,
            "last_name": employee_last_name,
            "cf": employee_cf,
            "iban": employee_iban,
            "id_contractType": employee_id_contractType,
            "email": employee_email,
            "phoneNumber": employee_phoneNumber
        }, 
        "new_account": {
            "user": "pytest",
            "password": "pytest_psw",
            "abilitato": 0,
            "id_tipo_account": account_type_id
        },
        "id_business": business_id,
        "start_date": "2022-09-08",
        "end_date": "2022-12-31",
        "serial_num": 0
    })
    assert response.status_code == 200


def test_show_all_Employees_by_Account_and_Business():
    response = client.get("/all/employees/account/business")
    assert response.status_code == 200


def test_disable_account_by_Employee():
    response = client.get(f"/employee/{employee_id}/disabled")
    assert response.status_code == 200


def test_enable_account_by_employee():
    response = client.get(f"/employee/{employee_id}/enabled")
    assert response.status_code == 200


def test_check_employee_account():
    response = client.post("/employee/checkAccount", json={
        "id_employee": employee_id
    })
    assert response.status_code == 200
    assert response.json == {"ok": "not"} or {"ok": "ok"}


def test_add_employee_to_business():
    response = client.post("/employee/business/relational", json={
        "id_employee": employee_id,
        "id_business": business_id,
        "start_date": "2022-09-08",
        "serial_num": "7357",
        "end_date": "2022-12-31"
    })
    assert response.status_code == 200
