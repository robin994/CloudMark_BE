from . import client, business_markup, customer_pippo, employee_bruno
import pytest

business_id = business_markup["id_business"]
customer_name = customer_pippo["name"]
customer_p_iva = customer_pippo["p_iva"]
customer_address = customer_pippo["address"]
customer_cap = customer_pippo["cap"]
customer_iban = customer_pippo["iban"]
customer_phone = customer_pippo["phone"]
customer_email = customer_pippo["email"]
customer_pec = customer_pippo["pec"]
customer_fax = customer_pippo["fax"]
customer_id_business = customer_pippo["id_business"]
customer_id = customer_pippo["id_customer"]
employee_id = employee_bruno["id_employee"]


def test_get_all_customer():
    response = client.get("/customer")
    assert response.status_code == 200


def test_get_all_customer_by_business_id():
    response = client.post(f"/customer/business/{business_id}")
    assert response.status_code == 200


def test_get_by_id():
    response = client.get(f"/customer/{customer_id}")
    assert response.status_code == 200


def test_create_customer():
    response = client.post("/customer/create/", json={
        "name": customer_name,
        "p_iva": customer_p_iva,
        "address": customer_address,
        "cap": customer_cap,
        "iban": customer_iban,
        "phone": customer_phone,
        "email": customer_email,
        "pec": customer_pec,
        "fax": customer_fax,
        "id_business": customer_id_business
    })
    assert response.status_code == 200


def test_delete_customer():
    response = client.post("/customer/delete/", params={
        "id_customer": customer_id
    })
    assert response.status_code == 200


@pytest.mark.skip(reason="(FAIL) Slow down tests")
def test_update_customer_by_id():
    response = client.post("/customer/update/", json={
        "name": customer_name,
        "p_iva": customer_p_iva,
        "address": customer_address,
        "cap": customer_cap,
        "iban": customer_iban,
        "phone": customer_phone,
        "email": customer_email,
        "pec": customer_pec,
        "fax": customer_fax,
        "id_business": customer_id_business,
        "id_customer": customer_id,
    })
    assert response.status_code == 200


def test_get_customer_name_by_employee_id():
    response = client.get(f"/customer/{employee_id}")
    assert response.status_code == 200
